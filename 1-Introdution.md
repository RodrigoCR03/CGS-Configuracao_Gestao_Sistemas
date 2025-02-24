#  Introdução de CGS
- Sigla: **FCAPS** -> Todos os processo de administração de Tecnologia de Informação.
  
# Criterios de Avaliação
- Mini Testes: 40% (- 2 notas + baixas);
- 4 Trabalhos Individuais: 20% (- 1 Trabalho);
- 3 Aulas online (Lessons): 5% (1 nota 20v);
- Wiki/KB: 35% (2 notas + altas). -> Desenvolver ao longo do semestre.

Ferramenta de analise de plagio: "TermiTin".

# Sistema de Virtualização
**!IMPORTANTE:** NAS, SAN, STORAGE, VLAN.

A virtualização é uma tecnologia essencial na administração de sistemas de TI, permitindo a execução de múltiplas máquinas virtuais (VMs) numa única máquina física, otimizando o uso de recursos e aumentando a flexibilidade na gestão de infraestruturas. Para compreender este conceito, é necessário conhecer os componentes fundamentais e as tecnologias associadas: **Hypervisors**, **VLANs**, **Storages**, **NAS**, **SAN** e **LUNs**.

---

## Hypervisor

O **Hypervisor** é o componente central da virtualização, responsável pela gestão das máquinas virtuais (VMs) que operam sobre o hardware físico. Existem dois tipos principais:
- **Type 1 (Bare-metal)**: Executam diretamente sobre o hardware físico, proporcionando maior desempenho e segurança.  
  *Exemplos: VMware ESXi, Microsoft Hyper-V, XenServer.* 
- **Type 2 (Hosted)**: Executam sobre um sistema operativo host, oferecendo maior flexibilidade e facilidade de uso.  
  *Exemplos: VMware Workstation, Oracle VirtualBox.*

**Funções do Hypervisor:**

- Gestão de recursos de hardware (CPU, memória, armazenamento e rede) entre as VMs.
- Isolamento e segurança entre as VMs.
- Monitorização e distribuição de carga (load balancing) para otimização de desempenho.
- Migração de VMs entre hosts físicos para manutenção ou em caso de falhas, minimizando o downtime.

**CPU para Virtualização:**

- Processadores **Xeon** (da Intel) são amplamente utilizados em servidores físicos para virtualização devido à sua elevada capacidade de processamento e ao suporte a tecnologias como Intel VT-x.
- As **vCPUs** (Virtual CPUs) correspondem ao mapeamento lógico das CPUs físicas, atribuídas às VMs conforme necessário.

---

## User Interfaces e Gestão Centralizada

Em ambientes virtualizados complexos, utilizam-se plataformas de gestão e monitorização, tais como o **CloudStack**:

- **CloudStack**: Interface gráfica que permite visualizar e gerir todos os Hypervisors na infraestrutura.
- Facilita a distribuição automática de VMs em caso de falhas (failover) em servidores físicos, aumentando a resiliência do sistema.

---

## VLAN (Virtual Local Area Network)

Com a virtualização dos servidores, torna-se necessário virtualizar também a rede. As **VLANs** permitem:
- **Segregação lógica** do tráfego de rede, aumentando a segurança e a eficiência na utilização da largura de banda.
- Comunicação segura e eficiente entre VMs na mesma máquina física ou em diferentes hosts.

**Protocolo 802.1Q:**

- É o protocolo padrão para *VLAN tagging*, que adiciona um cabeçalho extra aos pacotes de rede, incluindo o identificador da VLAN.
- Garante que o tráfego é corretamente encaminhado entre VMs pertencentes à mesma VLAN, mesmo que estas se encontrem em servidores físicos distintos.

---

## Switches e Gestão de Tráfego

Os **Switches** utilizados em ambientes virtualizados suportam o protocolo **802.1Q**, permitindo:

- Configuração de VLANs em portas específicas, assegurando que apenas o tráfego autorizado circula em cada segmento.
- Exemplo típico: *Switches com 48 portas*, cada uma com **1 Gbps** de largura de banda, totalizando **48 Gbps** para o processamento de dados.

---

## Storage

Em ambientes virtualizados, o armazenamento centralizado é crítico para:
- Garantir alta disponibilidade e redundância.
- Facilitar a migração de VMs entre diferentes hosts físicos.

**Características:**

- Constituído por uma máquina física com um **sistema operativo próprio** dedicado à gestão de armazenamento.
- Contém centenas ou milhares de **discos rígidos**, organizados e geridos por controladores redundantes, assegurando tolerância a falhas.

**Tipos de Storage:**

- **NAS (Network Attached Storage):**
  - Funciona como um sistema de ficheiros acessível pela rede.
  - Utiliza protocolos como **CIFS (Common Internet File System)** e **NFS (Network File System)** para operações de leitura e escrita.
  - Ideal para partilha de ficheiros em redes locais.

- **SAN (Storage Area Network):**
  - Rede dedicada exclusivamente ao armazenamento de dados.
  - Proporciona elevada flexibilidade e desempenho na gestão de armazenamento.
  - Utiliza o protocolo **Fibre Channel** (normalmente com **10 Gbps** de largura de banda) para comunicação de alta velocidade entre servidores e storage.

---

## LUNs (Logical Unit Numbers)

- As **LUNs** representam unidades lógicas de armazenamento dentro da infraestrutura SAN.
- Cada LUN é configurada como um disco virtual, que pode ser atribuído a um servidor ou a uma VM, permitindo a separação lógica dos dados.
- A gestão das LUNs é efetuada pelo administrador, podendo estas ser acessadas tanto via NAS como via SAN.

---

## Tiering

- **Tiering** é uma funcionalidade avançada de gestão de armazenamento, que consiste na organização dos dados em diferentes camadas (tiers) conforme a frequência de acesso e a importância dos mesmos.
- Dados mais frequentemente acedidos (*hot data*) são armazenados em discos de alta velocidade (por exemplo, SSDs), enquanto dados menos críticos (*cold data*) ficam em discos de menor custo (HDDs).
- Esta técnica otimiza tanto o desempenho como os custos operacionais.

---

## Conectividade e Protocolos de Comunicação

Para garantir um elevado desempenho e disponibilidade, recomenda-se:
- O uso de, no mínimo, **4 placas de rede** em paralelo, permitindo a distribuição do tráfego e redundância em caso de falhas.
- **Protocolo iSCSI (Internet Small Computer Systems Interface):**
  - Utilizado para a comunicação entre servidores e storage através de redes IP.
  - Permite o acesso a LUNs localizadas em storages remotos como se fossem discos locais.
