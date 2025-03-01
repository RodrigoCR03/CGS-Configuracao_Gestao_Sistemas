# How the Internet Works (t020-slides)

---

## TCP/IP
### Pilha TCP/IP
- **Camadas e Protocolos**:
  1. **Aplicação**: Protocolos como HTTP, DNS, FTP (ex.: Browser, cliente de email, etc.).
  2. **Transporte**: TCP, UDP, RTP – determinam a confiabilidade e a velocidade na transmissão.
  3. **Rede**: IP, ARP – responsáveis pelo endereçamento e mapeamento de endereços MAC.
  4. **Link**: Ethernet, ATM – definem como os dados são transmitidos através dos meios de rede.
  5. **Física**: Meios físicos como cobre, fibra ótica e rádio.

### Visão de Hardware e Roteamento
- **Dispositivos Associados**:
  - **Camada de Aplicação**: Computadores, gateways, firewalls.
  - **Camadas Inferiores**: Roteadores, switches, hubs/repetidores.
- **Exemplo de Fluxo**:
  - Browser (Aplicação) → TCP/UDP (Transporte) → IP (Rede) → Ethernet (Link) → Meio físico (Cobre/Fibra/Rádio).
- **Roteamento na Pilha**:
  - Associação de protocolos a cada camada: aplicações (Browser, Email, FTP), transporte (definição de portas, TCP para confiabilidade e UDP para velocidade), rede (endereçamento IP e ARP) e link/física (Ethernet com EtherType).

---

## LAN (Local Area Network)
### Características e Funcionamento
- **Escopo**:
  - Redes locais, como em escritórios ou residências.
- **Dispositivos e Protocolos**:
  - Uso de switches, hubs, NAT e firewalls.
  - Protocolos típicos: Ethernet, ARP, IP.
- **Exemplo de Topologia**:

> D1 - D2 - D3 conectados a Sw1 - Sw2 - Sw3, com NAT (R), Firewall (Fw) e roteadores (R).

### Desafios na LAN
- Gerenciamento de múltiplos protocolos numa única rede.
- Diagnóstico de problemas como colisões, falhas de NAT ou conflitos de endereçamento.

---

## WAN (Wide Area Network)
### Características
- **Escopo**:
- Redes de longa distância, incluindo a Internet.
- **Dispositivos**:
- Roteadores interconectados para estender a comunicação através de diversas redes.
- **Sistemas Autônomos (AS)**:
- Redes geridas por uma única entidade, com vários roteadores interligados.
### Protocolos Específicos
- **BGP (Border Gateway Protocol)**: Fundamental para o roteamento entre sistemas autônomos.
- Outros protocolos envolvidos: IP, TCP/UDP e protocolos de encapsulamento (ex.: MPLS).

---

## DNS (Domain Name System)
- **Função**:
- Traduzir nomes de domínio (ex.: www.exemplo.com) em endereços IP.
- **Principais Tipos de Registros**:
- **A**: Associa nomes a endereços IPv4.
- **AAAA**: Associa nomes a endereços IPv6.
- **CNAME**: Define um alias para outro domínio.
- **MX**: Especifica os servidores responsáveis pelo correio eletrónico.
- **NS**: Indica os servidores de nomes autoritativos.
- **SOA**: Contém informações essenciais sobre a zona DNS.

---

## Atribuição de Endereços IP
- **Transmissão de Dados**: Dados circulam como sinais elétricos em cabos de cobre ou pulsos de luz em fibras óticas, formando pacotes com metadados (emissor, receptor, protocolo) e carga útil (ex.: texto de um e-mail). Esses pacotes atravessam redes locais e globais para alcançar o destino.
- **Hierarquia de Rede**: Os pacotes seguem camadas do modelo TCP/IP: Ethernet (Link Layer) → IP (Network Layer) → TCP (Transport Layer). Cada camada adiciona ou remove cabeçalhos. Por exemplo, Ethernet define origem/destino físico, IP roteia entre redes, e TCP assegura entrega confiável. Bits de controle (ex.: flags de roteamento) são descartados ao subir, deixando apenas os dados úteis.
- **Análise de Pacotes**: Ferramentas como TCPdump e Wireshark capturam pacotes, exibindo origem, destino e protocolo. Porém, simplificam a saída, omitindo detalhes como flags TCP ou opções IP (ex.: TTL), que são cruciais para análises completas exigidas em estudos técnicos.
- **Métodos de Atribuição de IP**:
  - **Manual**: IPs fixos são configurados em ficheiros locais (ex.: /etc/network/interfaces no Linux). É trabalhoso e propenso a conflitos em redes grandes, sendo inviável para uso dinâmico.
  - **DHCP (Dynamic Host Configuration Protocol)**:
    - **Funcionamento**: Opera na camada de aplicação, gerenciando uma pool de IPs (ex.: 192.168.1.100–192.168.1.200). Atribui IPs automaticamente a dispositivos que entram na rede.
    - **Passos**:  
      1. *Discover*: Cliente envia um broadcast (sem IP atribuído) para localizar um servidor DHCP.  
      2. *Offer*: Servidor responde com um IP disponível.  
      3. *Request*: Cliente aceita formalmente o IP.  
      4. *Acknowledge*: Servidor confirma a alocação.  
      5. *Renovação*: Cliente renova o IP periodicamente (ex.: a cada 6000 segundos), evitando conflitos.  
    - **Detalhes**: Usa um *nonce* (número único) no *Discover* para identificar o cliente em broadcast. Se a pool esgotar, novos dispositivos aguardam até um IP ser liberado.
- **Endereço Mágico**: 255.255.255.255 (32 bits a 1) é um broadcast local, enviando pacotes a todos os dispositivos da LAN. Não atravessa roteadores, limitando-se à rede local.
- **Rede Local**: Poderia operar só com endereços MAC (Ethernet), mas IPs são preferidos por oferecerem hierarquia e escalabilidade.

## Gestão de Endereços MAC
- **Formato**: Endereços MAC têm 6 bytes (48 bits), escritos como 00:1A:2B:3C:4D:5E (hexadecimal). São únicos por interface de rede e operam na Link Layer (camada 2 do modelo OSI).
- **Função**: Identificam dispositivos fisicamente. Os primeiros 3 bytes (OUI - Organizationally Unique Identifier) indicam o fabricante (ex.: 00:16:17 para Apple), enquanto os últimos diferenciam unidades específicas. Ferramentas como Wireshark convertem esses bytes em nomes por praticidade.
- **Particularidades**:  
  - **Telemóveis**: Geram MACs aleatórios periodicamente (MAC randomization) para evitar rastreamento em redes Wi-Fi públicas.  
  - **Máquinas Virtuais (VMs)**: Usam OUIs reservados (ex.: 00:50:56 para VMware), permitindo identificar que o dispositivo é virtual.
- **Broadcast**: ff:ff:ff:ff:ff:ff (48 bits a 1) envia pacotes a todos os dispositivos conectados na LAN. Usado em protocolos como ARP ou DHCP para descoberta inicial.
- **Switches**: Encaminham pacotes com base em tabelas MAC (MAC Address Table), associando endereços a portas físicas. Loops entre switches geram *broadcast storms* (crescimento exponencial de pacotes), mas protocolos como Spanning Tree (STP) eliminam loops, mantendo redundância útil.

## DHCP e Lease Time
- **Tabela do Servidor**: O servidor DHCP mantém uma tabela: MAC | IP | Lease Time. Exemplo: "00:1A:2B:3C:4D:5E | 192.168.1.101 | 6000s". Registra alocações temporárias.
- **Lease Time**: Define o tempo de validade do IP (ex.: 6000 segundos). Se o cliente não renova (ex.: desligou-se), o IP retorna à pool, permitindo reciclagem em redes com IPs limitados.

## Comunicação Local vs. Externa
- **Redes Locais**: IPs da mesma rede compartilham um prefixo (ex.: 192.168.1.x). A máscara de rede determina essa divisão.
- **Máscaras de Rede**: Especificam quais bits do IP identificam a rede e quais os dispositivos. Ex.: 192.168.0.0/16 (máscara 255.255.0.0) fixa os primeiros 16 bits (192.168), permitindo 65.536 IPs (0.0 a 255.255). Um PC usa a máscara para decidir se um IP está na LAN (comunicação direta via MAC) ou fora (envio ao gateway). Ex.: 192.168.1.10/24 e 192.168.1.20/24 estão na mesma rede; 192.168.2.10/24 requer roteamento.
- **Placa de Rede**: IPs são associados a interfaces (ex.: Ethernet, Wi-Fi). Um PC com duas placas (ex.: 192.168.1.10 e 10.0.0.5) tem dois IPs distintos.

## Acesso à Internet
- **DNS (Domain Name System)**:
  - **Função**: Traduz nomes de domínio (ex.: google.com) em IPs (ex.: 142.250.190.14), necessário antes de conexões TCP.
  - **Cache Local**: Armazena respostas recentes (ex.: no Windows, veja com "ipconfig /displaydns") para evitar consultas repetidas ao servidor DNS.
  - **Processo de Resolução**:  
    1. O DNS local não encontra o IP.  
    2. Consulta um dos 13 *root servers* (endereços fixos, como 198.41.0.4), que indicam o servidor do TLD (ex.: .com).  
    3. Segue a hierarquia (ex.: .com → google.com) até obter o IP.  
    - **Registros**:  
      - A: Nome → IPv4 (ex.: google.com → 142.250.190.14).  
      - AAAA: Nome → IPv6 (ex.: google.com → 2001:4860:4860::8888).  
      - MX: Nome → Servidor de e-mail.  
      - CNAME: Nome → Outro nome (alias).  
      - NS: Nome → Servidor DNS responsável.  
    - **Recursividade**: Pode ser feita pelo DNS local (recursivo) ou iterativamente pelo PC (consultando cada nível).
- **Pacote Exemplo (Aceder google.com)**:
  - **ETH**: MAC Origem (PC), MAC Destino (descoberto via ARP, ex.: roteador).
  - **IP**: IP Origem (ex.: 192.168.1.10), IP Destino (DNS inicialmente, depois Google).
  - **UDP/DNS**: Consulta "google.com".
- **ARP (Address Resolution Protocol)**:
  - **Função**: Descobre o MAC associado a um IP na LAN. Ex.: "Quem tem 192.168.1.1?".
  - **Operações**:  
    - *Query*: Broadcast perguntando o MAC de um IP.  
    - *Response*: Resposta com o MAC correspondente (ex.: 00:1A:2B:3C:4D:5E).  
  - Executado apenas localmente, não na Internet.
- **Default Gateway**: É o roteador da LAN (ex.: 192.168.1.1) que encaminha pacotes para fora. Quando o destino não está na rede local (determinado pela máscara), o PC envia o pacote ao gateway, que decide o próximo salto com base em tabelas de roteamento. Ex.: Para acessar 8.8.8.8, o pacote vai ao gateway, que o envia à Internet.
- **Encaminhamento Externo**:  
  - Exemplo (acesso ao Google):  
    - MAC Destino = MAC do Gateway.  
    - MAC Origem = MAC do PC.  
    - IP Origem = 192.168.1.10.  
    - IP Destino = 142.250.190.14 (Google).  
  - O gateway reencaminha, ajustando cabeçalhos conforme necessário.

## Conceitos Adicionais
- **Bidirecionalidade**: Ethernet moderna (ex.: Cat5e) é full-duplex, permitindo envio e receção simultâneos, unlike redes antigas half-duplex.
- **Broadcast Inicial**: Ao ligar, um PC envia um broadcast (ex.: DHCP Discover) para integrar-se à LAN.
- **Link Layer**: Camada 2 (modelo OSI), gerencia comunicação física entre dispositivos na mesma rede. Protocolos como Ethernet (c cobre/fibra) ou PPP (point-to-point) definem framing, endereçamento (MAC) e detecção de erros (ex.: CRC). Em dados móveis, substitui Ethernet por 4G/5G, mas mantém IP acima.
- **IPv4 vs. IPv6**:  
  - **IPv4**: 32 bits (ex.: 192.168.1.1), ~4,3 bilhões de endereços. Esgotado, usa NAT para contornar limitações.  
  - **IPv6**: 128 bits (ex.: 2001:0db8::1), ~340 undecilhões de endereços. Elimina NAT, suporta mais dispositivos e tem cabeçalhos simplificados. Exemplo prático: IPv4 é suficiente para LANs pequenas; IPv6 é essencial para IoT e redes globais.
- **Dados Móveis**: Alteram a Link Layer (ex.: Ethernet → 5G), mas mantêm IP/TCP nas camadas superiores.

---

## Desafios e Complexidade
### Problemas Comuns
- Falhas em camadas específicas (por exemplo, problemas na camada física ou de roteamento).
- Configurações incorretas em dispositivos como firewalls e NAT.
- Latência e perda de pacotes em ambientes WAN.
### Estratégias para Mitigação
- **Diagnóstico**: Identificar a camada problemática (do físico à aplicação).
- **Políticas e Padrões**: Estabelecer normas de segurança e procedimentos de roteamento.
- **Ferramentas**: Uso de analisadores de protocolos (por exemplo, Wireshark) para monitorização e troubleshooting.

---

## Conclusão (Wrap Up)
- **Principais Lições**:
- A rede é um sistema complexo, composto por múltiplas camadas e protocolos interdependentes.
- O domínio desses conceitos permite a identificação de problemas e a otimização do desempenho das redes.
- Estratégias claras e políticas bem definidas são essenciais para a implementação de redes robustas e seguras.
- **Aplicações Práticas**:
- Configuração e manutenção de redes LAN e WAN.
- Resolução de problemas relacionados com DNS, roteamento e segurança de rede.
- Gestão eficaz de Sistemas Autônomos (AS) e implementação de políticas de segurança.

---

**Fontes e Links de Referência:**

- Documento original: *How the Internet Works* – Hugo Miranda (2021). (PDF disponibilizado localmente: `t020-slides.pdf`)
- [Wikipedia – TCP/IP](https://pt.wikipedia.org/wiki/Conjunto_de_protocolos_TCP/IP)
- [Wikipedia – LAN](https://pt.wikipedia.org/wiki/Rede_de_%C3%A1rea_local)
- [Wikipedia – WAN](https://pt.wikipedia.org/wiki/Rede_de_%C3%A1rea_alta)
- [Wikipedia – DNS](https://pt.wikipedia.org/wiki/Sistema_de_Nomes_de_Dom%C3%ADnio)
