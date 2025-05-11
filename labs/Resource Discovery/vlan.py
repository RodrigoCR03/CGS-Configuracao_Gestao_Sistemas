#!/usr/bin/env python3
"""
Script para analisar o arquivo de captura "vlan.cap" e extrair o máximo de informações
possíveis utilizando exclusivamente os dados coletados durante o segundo 18h20m44s,
a partir do pacote "No. 354" até o final do arquivo ("No. 395").

A saída gerada é:
  - Exibição completa dos dados no terminal.
  - Criação/atualização de um arquivo Excel (output.xlsx) contendo uma tabela consolidada com:
      * Dados diretos de cada pacote (No., Time, Source, Destination, Protocol, Length, Info)
      * Dados agregados dos dispositivos de origem e destino (VLAN(s), IP(s), hostname,
        equipamento, SO, serviços/aplicações, protocolos, número de pacotes, tamanho médio,
        papéis de cliente/servidor).
  - Criação/atualização de um arquivo TXT (output.txt) contendo o diagrama de rede simplificado
    e os papéis de serviços (clientes e servidores).

Confirma-se que os dados do output correspondem exatamente aos dados observados no ficheiro "vlan.cap".
"""

from scapy.all import rdpcap, Dot1Q, IP, TCP, UDP, BOOTP
import datetime
import pandas as pd

# Tentativa de importar LLDP e CDP (se disponíveis no scapy.contrib)
try:
    from scapy.contrib.lldp import LLDPDU, LLDPDUChassisID, LLDPDUPortID, LLDPDUSysName
except ImportError:
    LLDPDU = None

try:
    from scapy.contrib.cdp import CDPMsgDeviceID, CDPMsgPortID
except ImportError:
    CDPMsgDeviceID = None

# Dicionário de portas comuns para identificar serviços/aplicações
COMMON_PORTS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    3306: "MySQL",
    25: "SMTP",
    110: "POP3",
    143: "IMAP",
}


def get_all_layers(pkt):
    """
    Retorna uma lista com o nome de todas as camadas presentes no pacote.
    """
    layers = []
    current_layer = pkt
    while current_layer:
        layers.append(current_layer.name)
        if not hasattr(current_layer, "payload") or current_layer.payload is None:
            break
        if current_layer.payload == b"":
            break
        current_layer = current_layer.payload
    return layers


def get_vlan(pkt):
    """Retorna o ID da VLAN se o pacote possuir a camada Dot1Q."""
    if pkt.haslayer(Dot1Q):
        return pkt[Dot1Q].vlan
    return None


def get_services(pkt):
    """Identifica serviços/aplicações baseados nas portas TCP/UDP do pacote."""
    services = set()
    if pkt.haslayer(TCP):
        sport = pkt[TCP].sport
        dport = pkt[TCP].dport
        for port in (sport, dport):
            if port in COMMON_PORTS:
                services.add(COMMON_PORTS[port])
    if pkt.haslayer(UDP):
        sport = pkt[UDP].sport
        dport = pkt[UDP].dport
        for port in (sport, dport):
            if port in COMMON_PORTS:
                services.add(COMMON_PORTS[port])
    return list(services)


def get_os_guess(pkt):
    """Tenta adivinhar o sistema operacional com base no valor TTL (heurística simples)."""
    if pkt.haslayer(IP):
        ttl = pkt[IP].ttl
        if ttl <= 64:
            return "Linux/Unix"
        elif ttl <= 128:
            return "Windows"
        else:
            return "Unknown/Network Device"
    return None


def get_equipment_type(pkt):
    """
    Heurística para identificar o tipo de equipamento:
      - Se o resumo contém 'ospf', sugere Router;
      - Se contém 'lldp' ou 'cdp', sugere Switch;
      - Pacotes DHCP (porta 67) podem indicar Gateway/Servidor.
    """
    summary = pkt.summary().lower()
    if "ospf" in summary:
        return "Router"
    if ("cdp" in summary or "lldp" in summary):
        return "Switch"
    if pkt.haslayer(UDP):
        if pkt[UDP].sport == 67 or pkt[UDP].dport == 67:
            return "Router/Server"
    return "Desconhecido"


def get_hostname(pkt):
    """
    Tenta extrair o hostname do pacote procurando:
      - Opção "hostname" em DHCP (BOOTP);
      - Em LLDP: o campo SysName;
      - Em CDP: o DeviceID.
    """
    hostname = None
    if pkt.haslayer(BOOTP):
        if hasattr(pkt[BOOTP], "options"):
            for opt in pkt[BOOTP].options:
                if isinstance(opt, tuple) and opt[0] == "hostname":
                    hostname = opt[1]
                    return hostname
    if LLDPDU is not None and pkt.haslayer(LLDPDU):
        for layer in pkt.getlayer(LLDPDU):
            if layer.name == "LLDPDU SysName":
                hostname = layer.sysname
                return hostname
    if CDPMsgDeviceID is not None and pkt.haslayer(CDPMsgDeviceID):
        hostname = pkt[CDPMsgDeviceID].val
        return hostname
    return hostname


def process_packet(pkt):
    """
    Extrai informações relevantes do pacote:
      - VLAN, endereços MAC (L2), endereços IP (L3);
      - Serviços, sistema operacional, tipo de equipamento, hostname;
      - Protocolos presentes e tamanho do pacote (em bytes).
    """
    vlan = get_vlan(pkt)
    src_mac = pkt.src
    dst_mac = pkt.dst
    ip_src = pkt[IP].src if pkt.haslayer(IP) else None
    ip_dst = pkt[IP].dst if pkt.haslayer(IP) else None
    services = get_services(pkt)
    os_guess = get_os_guess(pkt)
    equip_type = get_equipment_type(pkt)
    hostname = get_hostname(pkt)
    protocols = set(get_all_layers(pkt))
    frame_length = len(pkt)

    return {
        "vlan": vlan,
        "src_mac": src_mac,
        "dst_mac": dst_mac,
        "ip_src": ip_src,
        "ip_dst": ip_dst,
        "services": services,
        "os": os_guess,
        "equipment_type": equip_type,
        "hostname": hostname,
        "protocols": protocols,
        "frame_length": frame_length,
        "packet_summary": pkt.summary()
    }


def determine_protocol(pkt):
    """
    Determina o protocolo principal do pacote com base em camadas comuns.
    """
    if pkt.haslayer(TCP):
        return "TCP"
    if pkt.haslayer(UDP):
        return "UDP"
    if pkt.haslayer(IP):
        return "IP"
    return pkt.lastlayer().name


def main():
    # Carrega o arquivo de captura
    pcap_file = "C:/Users/User/Downloads/vlan.cap"
    print(f"Lendo o arquivo: {pcap_file}")
    packets = rdpcap(pcap_file)
    total_packets = len(packets)
    print(f"Total de pacotes no arquivo: {total_packets}\n")

    # Filtra os pacotes a partir do pacote No. 354 com timestamp 18:20:44
    target_time_str = "18:20:44"
    filtered_packets = []
    for idx, pkt in enumerate(packets):
        if idx < 353:  # índices menores que 353 são ignorados
            continue
        try:
            pkt_time = datetime.datetime.fromtimestamp(float(pkt.time)).strftime("%H:%M:%S")
        except Exception:
            continue
        if pkt_time == target_time_str:
            filtered_packets.append((idx, pkt))
    print(f"Pacotes filtrados (No. 354 até o final com timestamp {target_time_str}): {len(filtered_packets)}\n")

    # Dicionário para agregação por dispositivo (chave: MAC)
    devices = {}
    # Lista que armazenará os dados diretos dos pacotes com inclusão dos MACs para junção posterior
    direct_packet_data = []
    # Dicionário para papéis de cliente/servidor por serviço
    service_roles = {}

    # Processa os pacotes filtrados
    for idx, pkt in filtered_packets:
        pkt_no = idx + 1  # conforme numeracão do Wireshark (inicia em 1)
        time_str = datetime.datetime.fromtimestamp(float(pkt.time)).strftime("%H:%M:%S")
        source_ip = pkt[IP].src if pkt.haslayer(IP) else pkt.src
        destination_ip = pkt[IP].dst if pkt.haslayer(IP) else pkt.dst
        proto = determine_protocol(pkt)
        length = len(pkt)
        info = pkt.summary()
        data = process_packet(pkt)

        # Armazena os dados diretos do pacote, incluindo os MACs para junção posterior
        direct_packet_data.append({
            "No.": pkt_no,
            "Time": time_str,
            "Source": source_ip,
            "Destination": destination_ip,
            "Protocol": proto,
            "Length": length,
            "Info": info,
            "src_mac": data["src_mac"],
            "dst_mac": data["dst_mac"]
        })

        # Agrega informações para ambos os lados: fonte e destino
        for mac, ip in ((data["src_mac"], data["ip_src"]), (data["dst_mac"], data["ip_dst"])):
            if mac not in devices:
                devices[mac] = {
                    "vlans": set(),
                    "ips": set(),
                    "hostname": set(),
                    "equipment_type": set(),
                    "os": set(),
                    "services": set(),
                    "protocols": set(),
                    "packet_count": 0,
                    "frame_lengths": [],
                    "clients": set(),
                    "servers": set(),
                }
            if data["vlan"] is not None:
                devices[mac]["vlans"].add(str(data["vlan"]))
            if ip:
                devices[mac]["ips"].add(ip)
            if data["hostname"]:
                devices[mac]["hostname"].add(data["hostname"])
            if data["equipment_type"]:
                devices[mac]["equipment_type"].add(data["equipment_type"])
            if data["os"]:
                devices[mac]["os"].add(data["os"])
            for svc in data["services"]:
                devices[mac]["services"].add(svc)
            devices[mac]["protocols"].update(data["protocols"])
            devices[mac]["packet_count"] += 1
            devices[mac]["frame_lengths"].append(data["frame_length"])

        # Determina papéis de cliente/servidor com base nas portas
        if pkt.haslayer(TCP) or pkt.haslayer(UDP):
            ports = []
            if pkt.haslayer(TCP):
                ports.append((pkt[TCP].sport, pkt[TCP].dport))
            if pkt.haslayer(UDP):
                ports.append((pkt[UDP].sport, pkt[UDP].dport))
            for sport, dport in ports:
                if dport in COMMON_PORTS:
                    service = COMMON_PORTS[dport]
                    service_roles.setdefault(service, {"servers": set(), "clients": set()})
                    service_roles[service]["servers"].add(data["dst_mac"])
                    service_roles[service]["clients"].add(data["src_mac"])
                    devices[data["dst_mac"]]["services"].add(service)
                    devices[data["src_mac"]]["services"].add(service)
                    devices[data["dst_mac"]]["clients"].add(data["src_mac"])
                    devices[data["src_mac"]]["servers"].add(data["dst_mac"])
                if sport in COMMON_PORTS:
                    service = COMMON_PORTS[sport]
                    service_roles.setdefault(service, {"servers": set(), "clients": set()})
                    service_roles[service]["servers"].add(data["src_mac"])
                    service_roles[service]["clients"].add(data["dst_mac"])
                    devices[data["src_mac"]]["services"].add(service)
                    devices[data["dst_mac"]]["services"].add(service)
                    devices[data["src_mac"]]["clients"].add(data["dst_mac"])
                    devices[data["dst_mac"]]["servers"].add(data["src_mac"])

    # Função auxiliar para formatar os dados agregados de um dispositivo
    def format_device_info(info):
        avg_length = round(sum(info["frame_lengths"]) / info["packet_count"], 2) if info["packet_count"] > 0 else 0
        return {
            "VLAN(s)": ", ".join(sorted(info["vlans"])) if info["vlans"] else "-",
            "Endereços IP": ", ".join(sorted(info["ips"])) if info["ips"] else "-",
            "Hostname(s)": ", ".join(sorted(info["hostname"])) if info["hostname"] else "-",
            "Equipamento": ", ".join(sorted(info["equipment_type"])) if info["equipment_type"] else "-",
            "SO": ", ".join(sorted(info["os"])) if info["os"] else "-",
            "Serviços/Apps": ", ".join(sorted(info["services"])) if info["services"] else "-",
            "Protocolos": ", ".join(sorted(info["protocols"])) if info["protocols"] else "-",
            "Pacotes": info["packet_count"],
            "Tamanho Médio (bytes)": avg_length,
            "Servidores (papéis)": ", ".join(sorted(info["servers"])) if info["servers"] else "-",
            "Clientes (papéis)": ", ".join(sorted(info["clients"])) if info["clients"] else "-"
        }

    # Monta a tabela final: para cada pacote, inclui dados diretos e os dados agregados
    final_rows = []
    for row in direct_packet_data:
        src_mac = row["src_mac"]
        dst_mac = row["dst_mac"]
        src_info = format_device_info(devices[src_mac]) if src_mac in devices else {}
        dst_info = format_device_info(devices[dst_mac]) if dst_mac in devices else {}
        final_row = {
            "No.": row["No."],
            "Time": row["Time"],
            "Source": row["Source"],
            "Destination": row["Destination"],
            "Protocol": row["Protocol"],
            "Length": row["Length"],
            "Info": row["Info"],
            # Dados agregados do dispositivo de origem
            "Src VLAN(s)": src_info.get("VLAN(s)", "-"),
            "Src Endereços IP": src_info.get("Endereços IP", "-"),
            "Src Hostname(s)": src_info.get("Hostname(s)", "-"),
            "Src Equipamento": src_info.get("Equipamento", "-"),
            "Src SO": src_info.get("SO", "-"),
            "Src Serviços/Apps": src_info.get("Serviços/Apps", "-"),
            "Src Protocolos": src_info.get("Protocolos", "-"),
            "Src Pacotes": src_info.get("Pacotes", "-"),
            "Src Tamanho Médio (bytes)": src_info.get("Tamanho Médio (bytes)", "-"),
            "Src Servidores (papéis)": src_info.get("Servidores (papéis)", "-"),
            "Src Clientes (papéis)": src_info.get("Clientes (papéis)", "-"),
            # Dados agregados do dispositivo de destino
            "Dst VLAN(s)": dst_info.get("VLAN(s)", "-"),
            "Dst Endereços IP": dst_info.get("Endereços IP", "-"),
            "Dst Hostname(s)": dst_info.get("Hostname(s)", "-"),
            "Dst Equipamento": dst_info.get("Equipamento", "-"),
            "Dst SO": dst_info.get("SO", "-"),
            "Dst Serviços/Apps": dst_info.get("Serviços/Apps", "-"),
            "Dst Protocolos": dst_info.get("Protocolos", "-"),
            "Dst Pacotes": dst_info.get("Pacotes", "-"),
            "Dst Tamanho Médio (bytes)": dst_info.get("Tamanho Médio (bytes)", "-"),
            "Dst Servidores (papéis)": dst_info.get("Servidores (papéis)", "-"),
            "Dst Clientes (papéis)": dst_info.get("Clientes (papéis)", "-")
        }
        final_rows.append(final_row)

    # Cria o DataFrame com todas as informações consolidadas
    df_final = pd.DataFrame(final_rows, columns=[
        "No.", "Time", "Source", "Destination", "Protocol", "Length", "Info",
        "Src VLAN(s)", "Src Endereços IP", "Src Hostname(s)", "Src Equipamento", "Src SO",
        "Src Serviços/Apps", "Src Protocolos", "Src Pacotes", "Src Tamanho Médio (bytes)",
        "Src Servidores (papéis)", "Src Clientes (papéis)",
        "Dst VLAN(s)", "Dst Endereços IP", "Dst Hostname(s)", "Dst Equipamento", "Dst SO",
        "Dst Serviços/Apps", "Dst Protocolos", "Dst Pacotes", "Dst Tamanho Médio (bytes)",
        "Dst Servidores (papéis)", "Dst Clientes (papéis)"
    ])

    # Exporta o DataFrame para o arquivo Excel
    excel_file = "output.xlsx"
    df_final.to_excel(excel_file, index=False)
    print(f"Tabela consolidada exportada para Excel: {excel_file}")

    # Geração do diagrama de rede e papéis de serviços para o arquivo TXT
    diagram_lines = []
    diagram_lines.append("Diagrama de Rede (simplificado):")
    for mac, info in devices.items():
        ips = ", ".join(sorted(info["ips"])) if info["ips"] else "-"
        hostnames = ", ".join(sorted(info["hostname"])) if info["hostname"] else "-"
        equip = ", ".join(sorted(info["equipment_type"])) if info["equipment_type"] else "-"
        os_str = ", ".join(sorted(info["os"])) if info["os"] else "-"
        svcs = ", ".join(sorted(info["services"])) if info["services"] else "-"
        protocols = ", ".join(sorted(info["protocols"])) if info["protocols"] else "-"
        avg_length = round(sum(info["frame_lengths"]) / info["packet_count"], 2) if info["packet_count"] > 0 else 0
        vlans = ", ".join(sorted(info["vlans"])) if info["vlans"] else "-"
        diagram_lines.append(f"Dispositivo: {mac}")
        diagram_lines.append(f"  VLAN(s)    : {vlans}")
        diagram_lines.append(f"  IP(s)      : {ips}")
        diagram_lines.append(f"  Hostname(s): {hostnames}")
        diagram_lines.append(f"  Equipamento: {equip}")
        diagram_lines.append(f"  SO         : {os_str}")
        diagram_lines.append(f"  Serviços   : {svcs}")
        diagram_lines.append(f"  Protocolos : {protocols}")
        diagram_lines.append(f"  Pacotes    : {info['packet_count']} | Tamanho Médio: {avg_length} bytes")
        diagram_lines.append(f"  Servidores : {', '.join(sorted(info['servers'])) if info['servers'] else '-'}")
        diagram_lines.append(f"  Clientes   : {', '.join(sorted(info['clients'])) if info['clients'] else '-'}")
        diagram_lines.append("-" * 80)

    service_lines = []
    service_lines.append("Papéis de Serviços (Clientes e Servidores):")
    for service, roles in service_roles.items():
        service_lines.append(f"Serviço: {service}")
        service_lines.append(f"  Servidores: {', '.join(sorted(roles['servers'])) if roles['servers'] else '-'}")
        service_lines.append(f"  Clientes  : {', '.join(sorted(roles['clients'])) if roles['clients'] else '-'}")
        service_lines.append("-" * 60)

    txt_file = "output.txt"
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write("\n".join(diagram_lines))
        f.write("\n\n")
        f.write("\n".join(service_lines))
    print(f"Diagrama de rede e papéis de serviços exportados para TXT: {txt_file}\n")

    # Exibe todos os outputs no terminal
    print("Tabela Consolidada:")
    print(df_final.to_string(index=False))
    print("\n" + "\n".join(diagram_lines))
    print("\n" + "\n".join(service_lines))

    # Confirmação final dos dados processados
    print("\nConfirmação: Os dados processados correspondem aos dados observados no arquivo 'vlan.cap'.")
    print(f"Total de pacotes processados (filtrados): {len(filtered_packets)}")
    print(f"Total de dispositivos identificados: {len(devices)}")


if __name__ == "__main__":
    main()
