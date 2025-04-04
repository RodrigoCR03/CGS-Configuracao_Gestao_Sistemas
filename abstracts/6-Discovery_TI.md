# Discovery em Gestão de TI – Resumo Atualizado

Este documento aborda a importância e as metodologias da descoberta (discovery) numa infraestrutura de TI. A descoberta consiste em identificar, mapear e monitorizar ativos (hardware, software, usuários, dispositivos de rede, etc.) para garantir a segurança, eficiência operacional, conformidade e planeamento estratégico. Além disso, o processo é contínuo, sendo essencial tanto em ambientes Greenfield (novos) quanto em Brownfield (existentes), para detectar e corrigir problemas que possam surgir, como conflitos de rede ou configurações inadequadas.

---

## 1. Introdução e Motivação

- **Propósito da Descoberta**:  
  A descoberta permite criar um inventário detalhado e atualizado dos ativos, essencial para:
  - Gerir e planear atualizações de hardware e software.
  - Detectar falhas e problemas de configuração (por exemplo, conflitos de DHCP ou problemas com gateways).
  - Assegurar a conformidade com normas de segurança e licenciamento.
  - Apoiar a resolução de problemas e auditorias.

- **Exemplo Prático**:  
  Um caso mencionado envolve um Access Point (AP) adquirido, por exemplo, na Worten, que internamente possui um servidor de DHCP com funções de NAT. Este equipamento, quando ligado numa rede sem a devida configuração (como na situação em que o default gateway mudou), provocou conflitos de tráfego e falhas na comunicação de parte dos utilizadores, evidenciando a necessidade de discovery contínuo para identificar “equipamentos estranhos” ou mal configurados.

---

## 2. Metodologias e Ferramentas de Discovery

### 2.1 Agentes e Monitorização Ativa

- **Instalação de Agentes**:  
  Em PCs e servidores, instalam-se softwares (como o GLPI) que recolhem informações sobre hardware, software, configurações e tráfego, integrando-se com sistemas de ticketing (TTS) para facilitar diagnósticos.
  
- **Verificação de Software**:  
  Métodos não intrusivos – como consulta a registos do sistema, verificação de diretórios (/Programs), execução de comandos (top ou ps) e análise dos nomes dos executáveis – ajudam a identificar quais programas estão instalados.

### 2.2 Escaneamento e Descoberta Ativa de Rede

- **NMAP e Escaneamento de Portas**:  
  Realiza varreduras nos IPs e portas conhecidas (well-known ports) para identificar aplicações em execução, mesmo quando firewalls bloqueiam pings.

- **Traceroute/ICNP**:  
  Utilizado para mapear os caminhos percorridos pelos pacotes entre os dispositivos, ajudando a construir um grafo da rede e identificar possíveis gargalos ou pontos de falha.

### 2.3 Inspeção de Tráfego e Monitorização Passiva

- **Análise de Pacotes**:  
  O exame do tráfego de rede – incluindo endereços MAC de origem e destino, TTL (Time To Live) e outros parâmetros – permite identificar se os pacotes estão a transitar dentro da mesma rede ou a partir de redes externas.  
  - **TTL**: É um campo que indica o número de saltos (routers) que um pacote pode percorrer antes de ser descartado. Se o TTL não decresce, pode indicar que o tráfego está a ser gerido dentro da mesma rede.

### 2.4 Protocolos e Descoberta de Equipamentos

- **LLDP/CDP (Link Layer Discovery Protocol/ Cisco Discovery Protocol)**:  
  São protocolos que permitem aos dispositivos de rede anunciar a sua identidade, capacidades e vizinhança. Esses protocolos ajudam a identificar:
  - Switches e outros dispositivos conectados.
  - Impressoras, VOIP e outros equipamentos que possam estar ligados na rede.
  - **Explicação do LLDP**: Este protocolo envia periodicamente mensagens contendo informações como o MAC address e TLVs (Type Length Value), possibilitando a construção de um mapa físico e lógico da rede.

- **SNMP/MIB**:  
  Através do Simple Network Management Protocol e da Management Information Base, é possível recolher informações detalhadas sobre os dispositivos e seus vizinhos, contribuindo para a montagem de um grafo completo da rede.

---

## 3. Componentes do Inventário e Objetivos da Descoberta

### 3.1 Hardware

- **Objetivos**:
  - Registrar a idade e expectativas de vida dos equipamentos.
  - Planejar a substituição ou manutenção preventiva.
  - Identificar “hardware fantasma” – ativos registrados mas não efetivamente em uso.
  
- **Contexto Prático**:  
  Problemas como a alteração do default gateway num servidor de armazenamento (stor) evidenciam a importância de ter um inventário preciso e atualizado para reconfigurar a rede sem interrupções. Durante a mudança, por exemplo, ambos os gateways precisam estar ativos até que o lease time do DHCP seja renovado em todos os dispositivos.

### 3.2 Software

- **Objetivos**:
  - Verificar versões e atualizações, garantindo a segurança e a compatibilidade.
  - Gerir licenças e identificar software não autorizado que possa representar riscos ou violações legais.

### 3.3 Utilizadores e Gestão de Acessos

- **Objetivos**:
  - Monitorizar a movimentação dos utilizadores (entradas e saídas).
  - Garantir a revogação de permissões de utilizadores que deixam a organização, prevenindo riscos de segurança.

### 3.4 Questões Legais e de Inventário

- **Inventário e Auditoria**:  
  Manter um registro detalhado de todos os ativos facilita auditorias, garante conformidade com normas legais e auxilia na tomada de decisões estratégicas.

---

## 4. Desafios e Considerações Práticas

- **Descoberta Contínua**:  
  Embora a descoberta possa ser inicialmente efetuada durante a montagem do sistema, ela deve ser um processo permanente, dada a dinâmica das redes (adicionamento, remoção ou alteração de dispositivos).

- **Problemas de Configuração e Conectividade**:  
  Exemplos práticos, como o conflito de DHCP de um AP mal configurado, mostram a importância de manter uma monitorização constante para identificar dispositivos “fora do padrão” ou que possam causar interferências.

- **Equilíbrio entre Gestão e Privacidade**:  
  É necessário encontrar um equilíbrio entre recolher informações suficientes para a gestão e respeitar a privacidade dos utilizadores. Este ponto pode exigir políticas internas e discussões éticas aprofundadas.

- **Interoperabilidade dos Métodos**:  
  Combinar abordagens ativas (escaneamento, agentes) e passivas (inspeção de tráfego, análise de logs de protocolos) enriquece o mapeamento e permite uma visão mais completa da rede.

---

## 5. Considerações Técnicas e Dúvidas Frequentes

Durante o processo de discovery, surgem questões que merecem esclarecimento:

- **O que é um Access Point comprado na Worten?**  
  Geralmente, refere-se a dispositivos de rede de menor custo, adquiridos em lojas de retalho como a Worten, que podem ter funcionalidades limitadas ou configurações padrão que não se enquadram perfeitamente em ambientes empresariais.

- **O que é TTL?**  
  O TTL (Time To Live) é um campo nos pacotes de rede que indica o número máximo de saltos (routers) que o pacote pode atravessar antes de ser descartado. Serve para evitar loops infinitos e para determinar se um pacote vem de fora ou de dentro da rede local.

- **O que é ICNP?**  
  Embora menos comum, o termo ICNP pode referir-se a ferramentas ou métodos de mapeamento de caminhos na rede, semelhantes ao traceroute, que ajudam a identificar a rota seguida pelos pacotes.

- **Mapeamento de Métodos**:  
  Cada método de discovery oferece diferentes níveis de informação:
  - **Agentes**: Detalhes internos dos PCs, como software instalado e configurações.
  - **Escaneamento de Portas e NMAP**: Identificação de serviços e aplicações em execução.
  - **Inspeção de Tráfego**: Verificação do comportamento dos pacotes (TTL, MACs) para inferir topologia e identificar anomalias.
  - **Protocolos (LLDP, CDP, SNMP)**: Construção do grafo físico e lógico da rede.

- **Explicação Detalhada do LLDP**:  
  O LLDP (Link Layer Discovery Protocol) permite que os dispositivos de rede anunciem a sua identidade e capacidades para os dispositivos vizinhos através de mensagens periódicas contendo TLVs. Estas informações incluem o identificador do dispositivo, o número de portas, capacidades e outras características, permitindo a construção automática de um mapa detalhado da rede, facilitando o diagnóstico e a gestão dos ativos.

---

## 6. Conclusão

A descoberta em gestão de TI é uma prática indispensável para manter a integridade, segurança e eficiência das infraestruturas de rede. Ao integrar métodos ativos e passivos, utilizar agentes e protocolos como LLDP/CDP e SNMP, e manter um inventário atualizado de hardware, software e utilizadores, é possível antecipar problemas, realizar manutenções preventivas e assegurar a conformidade com políticas internas e legais. A descoberta contínua também possibilita a identificação de dispositivos não autorizados ou mal configurados, garantindo uma rede robusta e preparada para os desafios dinâmicos do ambiente corporativo.

---

Este resumo integra não só a estrutura original, mas também casos práticos, detalhes técnicos (como problemas com DHCP e gateways), metodologias diversas e esclarecimentos sobre termos e dúvidas frequentes. Assim, serve como um guia completo para administradores de TI e estudantes que buscam compreender e aplicar o processo de discovery numa rede moderna.
