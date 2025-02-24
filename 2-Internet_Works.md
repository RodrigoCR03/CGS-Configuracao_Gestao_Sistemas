# How the Internet Works (t020-slides)

## Estrutura do Documento
1. **Introdução**
2. **TCP/IP**
3. **LAN (Local Area Network)**
4. **WAN (Wide Area Network)**
5. **DNS (Domain Name System)**
6. **Desafios e Complexidade**
7. **Conclusão (Wrap Up)**

---

## 1. Introdução
- **Objetivos da Aula**:
  - Revisar os conceitos básicos de TCP/IP, LAN, WAN e alguns protocolos essenciais.
  - Compreender a complexidade das redes e identificar pontos onde podem ocorrer falhas.
  - Facilitar o estudo de casos práticos e a realização de diagnósticos de problemas na rede.
- **Contexto**:
  - Apresentação geral sobre a importância de conhecer cada camada da rede para a correta implementação e resolução de problemas.

---

## 2. TCP/IP
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

## 3. LAN (Local Area Network)
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

## 4. WAN (Wide Area Network)
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

## 5. DNS (Domain Name System)
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

## 6. Desafios e Complexidade
### Problemas Comuns
- Falhas em camadas específicas (por exemplo, problemas na camada física ou de roteamento).
- Configurações incorretas em dispositivos como firewalls e NAT.
- Latência e perda de pacotes em ambientes WAN.
### Estratégias para Mitigação
- **Diagnóstico**: Identificar a camada problemática (do físico à aplicação).
- **Políticas e Padrões**: Estabelecer normas de segurança e procedimentos de roteamento.
- **Ferramentas**: Uso de analisadores de protocolos (por exemplo, Wireshark) para monitorização e troubleshooting.

---

## 7. Conclusão (Wrap Up)
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
