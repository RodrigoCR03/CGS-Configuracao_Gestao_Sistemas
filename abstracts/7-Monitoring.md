# Monitorização

Este resumo está organizado os conceitos relacionados com sistemas de monitorização, processamento de eventos, gestão de dados e balanceamento de carga em bases de dados. O objetivo é apresentar uma visão consolidada, abordando tanto os pontos teóricos como práticos, incluindo exemplos de ferramentas (como Zenoss e Nagios) e detalhes sobre a recolha, pré-processamento, armazenamento e pós-processamento de dados.

---

## 1. Visão Geral do Sistema ("The Big Picture")
### Descrição
O sistema descrito é um framework adaptativo para monitorização e gestão de eventos, com foco em infraestruturas de TI, redes ou sistemas distribuídos. A sua arquitetura permite:
- **Processamento de eventos**: Tratamento de dados em tempo real ou em lotes.
- **Supervisão de estado**: Monitorização contínua do funcionamento dos componentes.
- **Decisões de reconfiguração**: Ajustes dinâmicos com base em condições ou falhas detectadas.
- **Monitorização centralizada**: Recolha de eventos que desencadeiam ações ou alertas.

### Fluxo Operacional
O sistema opera num ciclo contínuo:
1. **Eventos** são gerados por dispositivos, agentes ou aplicações.
2. **Monitorização** recolhe e analisa esses eventos.
3. **Supervisão de estado** verifica a integridade do sistema.
4. **Reconfiguração** ajusta parâmetros ou recursos conforme necessário.

Este ciclo é típico de sistemas de gestão de redes (ex.: Zenoss, Nagios) e garante resiliência e eficiência.

---

## 2. Recolha de Dados
### Objetivo
A recolha de dados é o primeiro passo na monitorização, mas deve ser seletiva para evitar sobrecarga. A escolha dos indicadores é crítica, pois a quantidade de dados pode escalar rapidamente.

### Indicadores Comuns
- **Keep-alives**: Pings periódicos para verificar se um dispositivo está ativo.
- **Validade de certificados**: Monitorização de certificados SSL/TLS em websites hospedados.
- **Outros**: Estado de hardware, uso de CPU, memória, disco, tráfego de rede, etc.

### Tipos de Agentes
Os agentes de monitorização podem ser:
- **Passivos**:
  - Respondem apenas quando solicitados pelo servidor.
  - Requerem duas mensagens (pedido + resposta), consumindo mais largura de banda.
  - Podem usar **SNMP Traps** (triggers) para enviar mensagens automáticas quando um atributo (identificado por um OID) muda.
- **Ativos**:
  - Enviando dados periodicamente sem solicitação.
  - Para evitar sobrecarga síncrona, os intervalos de envio não devem ser fixos (ex.: T segundos). Em vez disso, usam intervalos aleatórios (ex.: ]0,2T]) e podem aumentar para ]0,3T] se o servidor estiver sobrecarregado.

### Tipos de Dados Recolhidos
- **Booleanos**: Ex.: ligado/desligado.
- **Numéricos**: Ex.: temperaturas, percentagens de uso.
- **Datas/Horas**: Ex.: timestamps de eventos.
- **Erros**: Ex.: falhas de conexão.
- **Configurações**: Ex.: tabelas de rotas em roteadores.

### Papel dos Agentes
- Os agentes recolhem dados brutos, mas não os interpretam. A análise (ex.: determinar se um valor é problemático) é feita pelo servidor central (monitorizador).
- Dados passam por três fases: **pré-processamento**, **armazenamento** e **pós-processamento**. Em alguns casos, o agente pode realizar o pré-processamento localmente.

### Segurança dos Agentes Passivos
- **Desafios**:
  - Requerem portas abertas para pedidos, aumentando a superfície de ataque.
  - Exigem autenticação robusta para milhares de agentes, o que é complexo.
  - Vulneráveis a ataques de negação de serviço (DoS).
- **Métodos de Autenticação**:
  - **Password única**: Simples, mas arriscada (ex.: se comprometida, afeta todos os agentes).
  - **Template de password**: Baseado em características do agente (ex.: IP, nome). Vulnerável a tentativas de adivinhação.
  - **Password Manager**: Seguro, mas depende de conectividade para validar credenciais, o que pode falhar em cenários sem rede.
- **Mitigação**:
  - Autenticação forte é essencial para limitar riscos de DoS ou acesso não autorizado.

### Outras Estratégias de Monitorização
- **Pings**:
  - Configuráveis por omissão em servidores, mas podem ser desativados na firewall ou configurações.
  - Úteis, mas limitados (ex.: hardware ativo, mas software em falha).
- **Proxies transparentes**:
  - Registam tráfego entre cliente e servidor, medindo tempos de resposta.
  - Introduzem pequena latência.
- **Scripts**:
  - Ex.: Verificar espaço em disco usando linguagens como **sed**, **awk** ou expressões regulares.
- **SNMP/SNMP Traps**:
  - Permitem monitorização detalhada e alertas automáticos.
- **Queries falsas**:
  - Simulações de pedidos para testar respostas do sistema.
  - Ex.: Usar contas falsas para verificar o comportamento de uma aplicação.
  - Cuidado com falsos positivos (ex.: ping responde, mas serviço está inativo).
- **Tickets de utilizadores**:
  - Feedback humano sobre problemas.
- **Logs**:
  - Análise de registos para detetar anomalias.
- **Traceroute**:
  - Verifica mudanças em rotas de rede.
- **Clientes de routing**:
  - Relacionados com tabelas de rotas, mas não fazem roteamento diretamente (detalhe pouco claro, possivelmente software de monitorização de rotas).
- **Inspeção de tráfego**:
  - Análise de pacotes para identificar padrões ou anomalias.

### Boas Práticas
- **Discrição**: A monitorização deve consumir poucos recursos para não sobrecarregar os serviços.
- **Escalonamento**: Evitar picos de tráfego, distribuindo pedidos ao longo do tempo.

---

## 3. Pré-processamento
### Objetivo
Preparar os dados brutos para armazenamento e análise, garantindo consistência e eficiência.

### Etapas
1. **Limpeza de Dados**:
   - **Partição em tokens**: Dividir dados em unidades menores (ex.: separar campos de um log).
   - **Validação**:
     - Verificar valores individuais (ex.: temperatura de 9000ºC é inválida).
     - Validar conjuntos de dados para consistência.
2. **Conversão de Dados**:
   - Uniformizar unidades (ex.: ºC para ºF).
   - Ajustar fusos horários e formatos de data/hora.
3. **Redução de Dados**:
   - **Compressão**: Usar algoritmos para reduzir tamanho.
   - **Digests/sumários**: Resumir informações (ex.: média diária).
   - **Thresholding**: Registar apenas exceções (ex.: valores fora do normal).
   - **Eliminar duplicados**: Remover entradas redundantes.
   - **Registar início/fim**: Para eventos prolongados.
   - **Agregação**: Calcular médias, medianas, máximo, mínimo ou desvios padrão (com cuidado para não perder detalhes críticos).

---

## 4. Armazenamento de Dados
### Desafios
Com grandes volumes de dados, as bases de dados podem sofrer degradação de desempenho. Estratégias específicas são necessárias para escalabilidade e eficiência.

### Técnicas de Armazenamento
1. **Particionamento**:
   - Dividir dados entre vários servidores com base numa função de hash (ex.: ID do componente).
   - Para leitura, a hash determina em qual base de dados procurar.
2. **Round-Robin Databases (RRD)**:
   - Otimizadas para séries temporais.
   - Usam listas circulares: quando cheias, os dados mais antigos são sobrescritos.
   - Comuns em ferramentas como Zenoss para monitorização de desempenho.
3. **Rolling Databases**:
   - Bases de dados escaláveis geridas por software que simula uma única base de dados.
   - Quando uma instância enche, uma nova é adicionada (ex.: novo servidor SQL para dados recentes).
   - O gestor coordena queries entre instâncias.
4. **Bases de Dados Hierárquicas**:
   - Organizam dados em níveis (ex.: dados brutos, agregações, sumários).
   - Facilitam análises em diferentes granularidades.
   - Exemplo: resumos diários derivados de dados horários.
5. **Replicação**:
   - **Mestre-Escravo**:
     - Uma base de dados mestre gere escritas e propaga mudanças para réplicas.
     - Réplicas são usadas para leituras, aliviando a carga do mestre.
   - **Balanceamento de carga**: Um load balancer distribui pedidos de leitura entre réplicas.
   - Garante tolerância a falhas e consistência (todas as réplicas em acordo).

### Balanceamento de Carga em Bases de Dados
- **Distribuição de dados**: Dividir dados entre várias instâncias para reduzir carga.
- **Replicação apenas de leitura**: Criar cópias para leituras, preservando o mestre para escritas.
- **Buffers circulares**: Ideais para dados com validade limitada (ex.: métricas de desempenho).
- **RRD e Rolling Databases**: Substituem dados antigos por novos, mantendo eficiência.
- **Hierarquias**: Organizam dados para acesso rápido a agregações.

### Descoberta (Discovery)
- O armazenamento pode revelar dispositivos ou componentes desconhecidos (ex.: novos servidores numa rede).
- Ferramentas como Nagios usam descoberta para mapear infraestruturas automaticamente.

---

## 5. Pós-processamento
### Objetivo
Transformar dados armazenados em informação útil para utilizadores finais, geralmente através de interfaces gráficas ou alertas.

### Componentes
- **Visualizações**:
  - Gráficos, velocímetros, tabelas, mapas de calor, relatórios.
  - Ex.: Painéis de controlo em Zenoss ou Nagios.
- **Alertas**:
  - Notificações sobre eventos críticos (ex.: servidor offline, disco cheio).
  - Configuráveis com base em limiares ou regras.
- **Interatividade**:
  - Botões de ação (ex.: reiniciar serviço), filtros, exportação de dados.

### Importância
- O pós-processamento é onde o valor da monitorização se concretiza, pois traduz dados técnicos em decisões acionáveis.
- Alertas são especialmente críticos, sendo uma funcionalidade de alto custo em ferramentas comerciais.

---

## 6. Ferramentas de Monitorização
### Zenoss
- **Descrição**: Plataforma open-source para monitorização de redes, servidores e aplicações.
- **Funcionalidades**:
  - Detecção de eventos, alertas, visualização de métricas.
  - Suporta RRD para séries temporais e gestão eficiente de dados.
- **Exemplo**: O documento menciona uma captura de ecrã do Zenoss, provavelmente mostrando um painel com métricas ou alertas.

### Nagios
- **Descrição**: Ferramenta de monitorização amplamente usada para infraestruturas de TI.
- **Funcionalidades**:
  - Monitorização de hosts, serviços e redes.
  - Suporta agentes ativos e passivos, SNMP, scripts personalizados.
  - Configuração via templates, host groups, service groups e admin groups para escalabilidade.
- **Projeto Sugerido**:
  - Explorar Nagios, reutilizando templates para evitar configurações manuais.
  - Escrever scripts para agentes (ex.: verificar espaço em disco).
  - Consultar **exchange.nagios.com** para plugins e recursos adicionais.

---

## 7. Questões Técnicas
### SNMP Traps
- **Explicação**: São mensagens assíncronas enviadas por agentes SNMP quando um evento específico ocorre (ex.: mudança de estado, erro). Funcionam como triggers configurados para monitorizar atributos (OIDs) e notificar o servidor sem polling constante.
- **Exemplo**: Um roteador envia uma trap quando a utilização da CPU excede 90%.

### Queries Falsas
- **Explicação**: Pedidos simulados para testar a disponibilidade ou comportamento de um serviço. Ex.: Enviar um pedido HTTP a uma aplicação para verificar se responde corretamente.
- **Cuidados**:
  - Evitar falsos positivos (ex.: hardware responde a ping, mas aplicação está inativa).
  - Usar contas de teste para simulações realistas.

### Clientes de Routing
- **Explicação**: Termo ambíguo, mas provavelmente refere-se a software que monitoriza ou interage com tabelas de rotas sem realizar roteamento diretamente. Ex.: Ferramentas que analisam rotas BGP ou OSPF para detetar mudanças.
- **Contexto**: Usado em monitorização de redes para identificar falhas ou alterações de topologia.

### Bases de Dados Hierárquicas
- **Explicação**: Bases de dados que organizam dados em níveis ou camadas, como uma árvore. Cada nível agrega ou resume os dados do nível inferior.
- **Exemplo**:
  - Nível 1: Dados brutos (ex.: leituras de CPU por segundo).
  - Nível 2: Médias horárias.
  - Nível 3: Resumos diários.
- **Uso**: Facilitam análises rápidas e reduzem a carga em queries complexas.

### CRONs
- **Explicação**: CRON é um utilitário em sistemas Unix/Linux para agendar tarefas recorrentes. Usa expressões (ex.: `0 0 * * *` para executar diariamente à meia-noite) para automatizar scripts ou comandos.
- **Exemplo**: Configurar um script de monitorização para correr a cada 5 minutos (`*/5 * * * *`).
- **Relevância**: Usado em agentes ativos para enviar dados em intervalos programados.

---

## 8. Interpretação Geral
### Objetivo do Documento
O documento é uma apresentação técnica que explora:
- **Teoria**: Conceitos de monitorização, gestão de eventos e balanceamento de carga.
- **Prática**: Implementações em ferramentas como Zenoss e Nagios.
- **Desafios**: Segurança, escalabilidade, eficiência na gestão de grandes volumes de dados.

### Público-Alvo
- Profissionais de TI, administradores de sistemas, engenheiros de redes.
- Estudantes ou formadores interessados em monitorização e DevOps.

### Limitações
- Erros de OCR dificultam a leitura de algumas páginas, especialmente diagramas ou tabelas.
- O documento original provavelmente inclui elementos visuais (ex.: capturas de ecrã, fluxogramas) que complementam o texto.

---

## 9. Conclusão
O sistema descrito é um framework robusto para monitorização e gestão de infraestruturas, com ênfase em:
- **Recolha seletiva** de dados para evitar sobrecarga.
- **Processamento eficiente** (pré e pós) para garantir consistência e utilidade.
- **Armazenamento escalável** usando técnicas como RRD, rolling databases e replicação.
- **Ferramentas práticas** como Zenoss e Nagios para implementar essas ideias.
- **Segurança e discrição** para minimizar impacto nos recursos.

Os conceitos abordados são fundamentais em DevOps, administração de sistemas e gestão de redes, com aplicações em cenários reais como data centers, cloud computing e IoT. Para aprofundar, recomenda-se explorar o Nagios (usando templates e plugins de **exchange.nagios.com**) e analisar o Zenoss para visualizações práticas. O acesso ao documento original em formato visual seria ideal para clarificar detalhes obscurecidos pelo OCR.
