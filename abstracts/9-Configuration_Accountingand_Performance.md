# FCAPS - Configuração

## 1. Introdução à Configuração em FCAPS

No modelo FCAPS (Fault, Configuration, Accounting, Performance, Security), a **Configuração** representa um aspeto fundamental da gestão de sistemas. É importante compreender que a configuração vai muito além da simples alteração de parâmetros nas definições ou num ficheiro de texto. Trata-se de um processo estruturado que envolve múltiplos componentes e considerações.

## 2. Gestão de Valores de Configuração

### 2.1 Configuração Integrada

Um dos princípios fundamentais na gestão de configuração é a necessidade de configurar não apenas o programa principal, mas também todas as suas dependências. Esta abordagem previne problemas como o caso mencionado nas notas, onde uma aplicação deixou de funcionar porque o MySQL foi atualizado em produção, mas não em desenvolvimento.

### 2.2 Descoberta de Configurações

Antes de iniciar o processo de configuração propriamente dito, é essencial realizar a **Descoberta** das configurações existentes. Este passo requer:

- Agentes especializados que convertam informações de diferentes fontes para um formato padrão
- Mecanismos para recolher configurações de equipamentos heterogéneos
- Ferramentas para análise e utilização posterior destas configurações

## 3. CMDB (Configuration Management Database)

A CMDB é uma base de dados centralizada que armazena informações sobre todos os componentes de um sistema de informação.

### 3.1 Métodos de Recolha de Configurações

- **Para equipamentos de rede (Switches):** Utilização do protocolo **SNMP** (Simple Network Management Protocol)
  - Uso da operação **GetNext()** para recolha iterativa de configurações
  - Processo: Inicia-se com GetNext(1), utiliza-se o OID devolvido para fazer GetNext novamente, e assim sucessivamente
  - Cada operação GetNext devolve um par (OID+1, Value)

- **Para serviços como o Apache:** Utilização de ficheiros de configuração em texto
  - Não é possível utilizar SNMP, o que contribui para a heterogeneidade da base de dados

### 3.2 Estrutura da CMDB

A CMDB deve armazenar, para cada configuração:
- Nome do parâmetro
- Valor do parâmetro
- Histórico completo de alterações (quem alterou e quando)

### 3.3 Gestão de Dependências

A gestão de dependências representa um dos maiores desafios na CMDB devido à sua complexidade:

- **Hierarquia de dependências:** Cada componente pode depender de outros que, por sua vez, têm as suas próprias dependências
- **Dependências de versões:** Aplicações podem depender de versões específicas de outros componentes
- **Dependências entre plugins:** Plugins podem depender uns dos outros
- **Dependências técnicas:** Entre plugins e linguagens de programação
- **Diversidade de componentes:** Para além de aplicações, existem firewalls, proxies, load balancers, servidores e outros equipamentos
- **Heterogeneidade:** Existem muitos tipos diferentes de dependências

### 3.4 Benefícios da CMDB

- **Integração entre departamentos:** Funciona como uma base de dados transversal a toda a organização
- **Validação:** Permite validar ficheiros de configuração por comparação com versões guardadas
- **Análise "What If":** Possibilita a análise de impacto antes de implementar alterações
- **Migrações:** Facilita processos de migração de sistemas
- **Clonagem de configurações:** Permite replicar configurações entre sistemas similares

## 4. Scripts e Workflows

A automatização através de scripts e workflows é essencial para uma gestão de configuração eficiente.

### 4.1 Exemplo: Script para Criação de Conta

Um script pode automatizar tarefas como:
- Definição de login e endereços
- Criação de área de utilizador
- Criação de mailbox
- Criação de área no Cirrus
- Registo no Census
- Outras tarefas necessárias

### 4.2 Vantagens da Automatização

- **Redução de trabalho manual:** Diminui o esforço necessário para realizar tarefas repetitivas
- **Minimização de erros:** Reduz a probabilidade de erros humanos
- **Normalização:** Garante que os processos são executados sempre da mesma forma
- **Troubleshooting simplificado:** Facilita a identificação e resolução de problemas
- **Alterações em massa:** Permite implementar alterações em múltiplos sistemas de forma consistente

## 5. Gestão de Políticas e Configurações

### 5.1 Active Directory (Microsoft)

O Active Directory (AD) é uma solução da Microsoft para gestão de políticas que:
- Trata todos os elementos como objetos
- Permite criar grupos de objetos
- Possibilita a atribuição de regras a grupos específicos
- Oferece excelentes capacidades para gestão de políticas
- Utiliza o protocolo LDAP para comunicação
- Tem como desvantagem ser limitado ao ambiente Windows

### 5.2 Ferramentas para Gestão de Políticas em Equipamentos

#### 5.2.1 Puppet/Chef
- **Abordagem declarativa:** Especifica o estado final desejado para os equipamentos
- O sistema determina automaticamente como atingir esse estado

#### 5.2.2 Ansible
- Estabelece ligações SSH para os equipamentos alvo
- Aplica configurações diretamente através dessas ligações

### 5.3 Fwbuilder

- Ferramenta para criação de configurações abstratas de firewalls
- Interface gráfica com funcionalidades de arrastar e soltar (drag and drop)
- Converte configurações para formatos específicos de diferentes marcas de firewalls

### 5.4 FOG (Free Open Ghost)

Sistema de clonagem e gestão de imagens para computadores em rede, frequentemente utilizado em conjunto com PXE.

## 6. Gestão de Atualizações (Patch Management)

A gestão de atualizações é um processo crítico que deve balancear a necessidade de manter os sistemas atualizados com a estabilidade operacional.

### 6.1 Princípios Básicos
- **Estabilidade:** "Se está a funcionar, não mexer" é um princípio importante
- **Atualização seletiva:** Nem todas as atualizações devem ser implementadas imediatamente

### 6.2 Processo de Gestão de Atualizações

#### 6.2.1 Descoberta
- Identificação da disponibilidade de atualizações
- Atualmente facilitado por notificações automáticas dos próprios sistemas

#### 6.2.2 Avaliação
A decisão de implementar uma atualização deve considerar:

- **Segurança**
  - Geralmente prioritárias, mas deve-se avaliar:
  - A relevância da vulnerabilidade no contexto específico
  - O potencial para introdução de novos erros

- **Custos**
  - Tempo de inatividade (downtime)
  - Recursos humanos necessários
  - Potencial necessidade de atualização de hardware
  - Aumento de requisitos de processamento ou memória

- **Compatibilidade**
  - Impacto nas dependências existentes
  - Necessidade de testes abrangentes antes da implementação em produção

#### 6.2.3 Testes
- Utilização de servidores virtuais para replicar o ambiente de produção
- Implementação da atualização no ambiente de teste
- Execução de um plano de testes estruturado
- Avaliação da ordem correta para implementação das atualizações

#### 6.2.4 Instalação
- Implementação das atualizações aprovadas
- Possibilidade de adiar ou rejeitar atualizações com base nos resultados dos testes

## 7. PXE (Preboot Execution Environment)

O PXE é uma tecnologia que permite o arranque de computadores através da rede.

### 7.1 Funcionamento
- É uma funcionalidade incorporada nas placas de rede modernas
- Apresenta-se à BIOS como uma alternativa de arranque ao disco ou pen drive
- Permite carregar o sistema operativo através da rede

### 7.2 Processo de Arranque PXE
1. O computador envia um pedido DHCP, solicitando um sistema operativo
2. O pedido propaga-se por broadcast até alcançar o servidor FOG
3. O servidor, que mantém uma base de dados de endereços MAC dos computadores, responde com:
   - Um endereço IP (resposta DHCP normal)
   - Um "nextserver" e um "filename" (para acesso TFTP)
4. O computador utiliza estas informações para descarregar a imagem do sistema operativo
5. A imagem é escrita no disco local para servir como sistema operativo

### 7.3 Aplicação Prática (Exemplo FCUL)
- Aquisição de 25 computadores idênticos (24 + 1 reserva)
- O computador reserva é configurado com todas as aplicações e definições necessárias
- Os restantes 24 computadores, quando arrancam por PXE, recebem a imagem do computador configurado
- Após a configuração inicial, apenas são instaladas as diferenças (diffs) e não a imagem completa
- Um agente instalado nos computadores gere estas atualizações incrementais

## 8. Wake on LAN

O Wake on LAN é uma tecnologia que permite ligar remotamente um computador.

### 8.1 Funcionamento
- A placa de rede permanece parcialmente ativa mesmo quando o computador está desligado
- Ao receber um pacote especial (Magic Packet), a placa inicia o processo de arranque do computador
- Esta funcionalidade pode ser combinada com PXE para automatizar completamente o processo de arranque e configuração

### 8.2 Aplicações
- Manutenção remota fora do horário de expediente
- Implementação automatizada de atualizações
- Preparação de salas de computadores para utilização

---

# FCAPS: Accounting e Performance

## 1. Accounting (Contabilização)

**Objetivo:** Registar e atribuir o consumo de recursos (rede, CPU, aplicações, licenças) aos utilizadores ou grupos, suportando cobranças internas ou análise de custos.

### 1.1. Funcionalidades principais

* **Medição de recursos**

  * Impressões de cada utilizador ou departamento.
  * Utilização de licenças de software (licenciamento por utilizador, por instância).
  * Tráfego de rede por VLAN, interface ou aplicação.

* **Modelos de billing**

  * Antigos: tarifação por volume ou tempo de uso.
  * Modernos: licenciamento por subscrição, modelos SaaS, billing baseado em contêineres ou instâncias efémeras (cloud).

* **Integração com Performance**

  * Só avaliando o uso real de recursos é possível decidir se é necessário aumentar capacidade ou otimizar configuração para atingir SLAs de desempenho.

### 1.2. Técnicas de monitorização

| Nível          | Ferramentas / Protocolos                     | Descrição                                                           |
| -------------- | -------------------------------------------- | ------------------------------------------------------------------- |
| **Rede**       | SNMP/MIB, port mirroring, NetFlow/IPFIX      | Coleta estatísticas de interfaces, fluxos; espelhamento de pacotes. |
| **Sistema**    | Ping, agentes (ex.: Telegraf, Zabbix agents) | Verificação de disponibilidade e métricas de CPU, memória.          |
| **Aplicações** | Logs, proxies, agentes, NetFlow              | Registo de transações, tempos de resposta, fluxos de dados.         |

---

## 2. Performance

### 2.1. Métricas essenciais

* **Utilização (%)**
  Percentagem de recurso em uso (CPU, memória, rede). Ex.: ideal \~40% para headroom.

* **Workload**
  Número de pedidos (requests) chega a um componente por segundo.

* **Throughput**
  Número de pedidos que o componente consegue efetivamente processar por segundo.

  * Nota: se o workload aumenta demasiado, pode ocorrer *thrashing* (troca excessiva entre RAM e disco), reduzindo o throughput.

* **Loss Rate**
  Percentagem ou número de pedidos sem resposta (perdas, timeouts).

* **Capacity**
  Máximo throughput alcançável pelo sistema sob condições ideais.

### 2.2. Picos de utilização

* **Ocasionais**
  Imprevisíveis (ex.: trânsito extra por evento súbito).

* **Sazonais**
  Previsíveis (ex.: tráfego elevado em horas de ponta diárias, campanhas de marketing).

  * **Soluções:**

    * Modelos híbridos (cloud + on‑premise) com auto‑scaling.
    * Uso de CDN para cache de conteúdo estático e mitigação de DDoS, aproximando o cliente de servidores de borda que espelham apenas os conteúdos mais acedidos.

### 2.3. Fatores de crescimento de carga

* Aumento natural do número de utilizadores.
* Complexidade crescente do software em novas versões (novas funcionalidades, mais dados em memória).

### 2.4. Memória virtual: SWAP e *thrashing*

* **SWAP files**
  Espaço em disco reservado para estender a RAM. Quando a RAM enche, páginas ativas são movidas para SWAP.

* **Thrashing**
  Situação em que a troca constante (swap in/out) consome CPU e I/O, degradando severamente o desempenho.

---

## 3. Detecção de Problemas de Performance

* **Feedback dos utilizadores**
  Queixas directas de lentidão ou falhas.

* **Thresholds**
  Alertas configurados quando métricas (e.g., CPU > 90%) ultrapassam limites.

  * Desafio: definir níveis sensíveis o suficiente para detectar problemas reais sem gerar *falsos-positivos*.

* **Detecção de anomalias estatísticas**
  Complemento aos thresholds, identificando valores fora de padrões esperados.

  * Ex.: assumir distribuição normal (μ, σ) e sinalizar além de ±3σ como possível anomalia.

> **Importante:** a deteção raramente é *boolean*; thresholds isolados podem falhar. Ideal combinar múltiplas fontes e métodos.

---

## 4. Resolução de Incidentes de Performance

| Tipo de Causa              | Ação de Correção                                                  |
| -------------------------- | ----------------------------------------------------------------- |
| **Configuração**           | Rever parâmetros (buffers, timeouts, limites de conexão).         |
| **Bugs de Software**       | Identificar e aplicar *patches* ou versões corrigidas.            |
| **Limitações de Hardware** | Upgrade de CPU, memória, discos mais rápidos (SSD/NVMe).          |
| **Crescimento de Carga**   | Escalar horizontal (mais instâncias) ou vertical (mais recursos). |

---

## 5. Visualização de Métricas

* **Velocímetro (gauge)**
  Exibe valor atual vs. intervalo esperado (e.g., CPU, latência).

* **Nível (barra/retângulo)**
  Percentagem de utilização (e.g., uso de disco, memória).

* **Gráficos de séries temporais**
  Exibem histórico e tendências ao longo do tempo (ideal para análise de picos e sazonalidade).

---

## 6. Principais Dúvidas e Esclarecimentos

1. **Como a CDN mitiga picos e DDoS?**

   * **Cache distribuído:** réplica de conteúdo estático em servidores de borda próximos do utilizador, reduzindo carga no servidor de origem e latência.
   * **Proteção DDoS:** tráfego malicioso é absorvido e filtrado nas camadas de borda do provedor CDN.

2. **Diferença entre Throughput e Capacity**

   * **Throughput:** taxa real de processamento (pedidos/s), sujeita a variações por carga e configurações.
   * **Capacity:** máximo teórico ou mensurável (pedidos/s) que o sistema pode suportar sob condições ideais.

3. **SWAP files vs. Thrashing**

   * **SWAP files:** recurso de extensão de memória em disco.
   * **Thrashing:** estado de elevada atividade de swap, degradando o desempenho global.

---

# Análise das Métricas e Resiliência no Dimensionamento de Sistemas

Analisei o documento de slides completo sobre dimensionamento de sistemas. O material aborda conceitos fundamentais para entender o desempenho de sistemas, modelar componentes e analisar métricas de performance e resiliência. Vou apresentar uma síntese organizada do conteúdo.

## Motivação para Dimensionamento de Sistemas

O dimensionamento visa responder perguntas críticas como:
- Por que o sistema está (ou estará) lento?
- Quais são os gargalos?
- O sistema suportará carga adicional?
- Quantas réplicas são necessárias?
- Como a carga flui entre componentes?
- Qual carga esperar?

## Passos para Entender o Desempenho

1. Criar um modelo dividindo o sistema em componentes
2. Preencher com métricas de desempenho (estimativas, valores observados, dados de fornecedores)
3. Analisar o modelo (simulação ou análise matemática)
4. Ajustar o modelo e repetir o processo

## Métricas Principais

### 1. Workload (Carga de trabalho)
- **Definição**: Quantidade de trabalho por unidade de tempo
- **Unidade**: trabalho/tempo (ex: pacotes/s)
- **Observação**: A carga pode diferir entre componentes (ex: 1 requisição HTTP pode gerar múltiplos pacotes IP)

### 2. Capacity (Capacidade)
- **Definição**: Throughput máximo possível do componente
- **Unidade**: trabalho/tempo

### 3. Response Time (Tempo de resposta)
- **Definição**: Tempo necessário para o componente responder a uma requisição
- **Unidade**: tempo
- **Observação**: Não é constante, depende do tipo de requisição

### 4. Loss Rate (Taxa de perda)
- **Definição**: Fração de requisições sem resposta ou com resposta errônea
- **Unidade**: %

### 5. Throughput (Taxa de transferência)
- **Definição**: Quantidade de trabalho por unidade de tempo que recebe resposta normal
- **Unidade**: trabalho/tempo

### 6. Utilization (Utilização)
- **Definição**: Fração de tempo em que o componente está ocupado
- **Unidade**: %
- **Regra prática**: Visar 30% de utilização

## Leis Fundamentais

### 1. Lei da Utilização
- A utilização média de qualquer componente é o throughput do sistema multiplicado pelo tempo de serviço de cada requisição naquele componente
- **Fórmula**: Utilização = throughput × (tempo/réplicas)

### 2. Lei de Little
- O número médio de requisições pendentes em qualquer sistema é igual à taxa média de chegada multiplicada pelo tempo médio gasto pela requisição no sistema
- **Fórmula**: clientes = throughput × tempo_resposta

### 3. Lei do Fluxo Forçado
- O throughput em diferentes componentes é proporcional ao número de vezes que cada componente precisa lidar com cada requisição
- Se o throughput de um componente x é Tx e o throughput do sistema S é Ts, cada requisição visita Tx/Ty o componente

## Dimensionamento e Distribuição

### Regra dos 3-σ
- A maioria dos valores em qualquer distribuição com média m e desvio padrão σ está dentro do intervalo [m-3σ, m+3σ]
- Usada para evitar filas e dimensionar recursos apropriadamente

### Teoria das Filas de Espera
- Lida com chegadas não uniformes de requisições
- Distribuições populares: Determinística, Geral, Poisson

### Notação de Filas (A/B/C)
- A: distribuição de entrada
- B: distribuição de serviço
- C: número de réplicas
- Distribuições típicas: M (Poisson), D (Determinística), G (Geral)

### Aplicações (M/M/1 e M/D/1)
- Para M/M/1 (quando ρ < 1):
  - Atraso médio: 1/μ(1-ρ)
  - Requisições pendentes: ρ/(1-ρ)
- Para M/D/1 (quando ρ < 1):
  - Atraso médio: 1/2(μ-λ) + 1/2μ
  - Requisições pendentes: 1 + ρ²/2(1-ρ)

## Resiliência

### Métricas de Resiliência
- **MTBF** (Mean Time Between Failures): Tempo previsto entre falhas
- **N 9's**: Proporção de tempo em que o sistema está disponível
  - 99,999% (5 noves): 5,26 minutos indisponível por ano
  - 99,99% (4 noves): 52 minutos indisponível por ano

### Modelos de Resiliência

#### 1. Serial (Componentes em série)
- Sistema funciona se TODOS os componentes funcionarem
- Probabilidade = Pp × Pq (onde Pp e Pq são probabilidades dos componentes p e q estarem corretos)
- Alternativa: 1 - [(1-Pp) × (1-Pq)]

#### 2. Paralelo (Componentes em paralelo)
- Sistema funciona se PELO MENOS UM componente funcionar
- Probabilidade = 1 - [(1-Pp) × (1-Pq)]
- Alternativa: (Pp × Pq) + [Pp × (1-Pq)] + [(1-Pp) × Pq]

#### 3. Blocos
- Tratar cada bloco separadamente e compor blocos em série
- Sistemas em paralelo são mais resilientes que sistemas em série

## Relações entre Métricas

É fundamental entender como as métricas se relacionam:
- Quando a utilização se aproxima da capacidade, o tempo de resposta aumenta drasticamente
- Aumentar a utilização pode ser feito reduzindo o throughput, diminuindo o tempo de processamento ou aumentando o número de réplicas
- A resiliência depende da arquitetura do sistema (serial vs. paralelo)

Esta análise abrange as métricas essenciais e conceitos de resiliência apresentados no documento, proporcionando uma base para dimensionar sistemas eficientemente.
