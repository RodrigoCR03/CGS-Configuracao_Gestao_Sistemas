# IT Management Concepts (t030-slides)

O documento aborda os conceitos fundamentais da gestão de IT, estruturando o conteúdo em diversas secções que cobrem desde a definição e perspetivas sobre a administração de IT até à organização da equipa e às ferramentas de suporte. Abaixo, encontra-se um resumo detalhado de cada secção, atualizado com a nova informação.

---

## 1. Introdução e Agenda

- **Título:** IT Management Concepts  
- **Objetivos da Aula:**
  - O que é administração de IT?
  - O ciclo de vida da infraestrutura de IT.
  - O ciclo de vida da gestão de IT.
  - Organização da equipa de IT.

Esta secção serve de ponto de partida para compreender a abrangência do tema, apresentando a estrutura do documento e os principais tópicos que serão explorados.

---

## 2. Perspetivas sobre a Gestão de IT

Foram apresentadas três definições que refletem diferentes perspetivas:

- **Perspetiva 1 (Saydam, 1996):**  
  A gestão de IT é descrita como a *implantação, integração e coordenação* dos componentes (hardware, software e recursos humanos) para monitorizar, configurar e controlar a rede, garantindo um desempenho operacional em tempo real e níveis de QoS aceitáveis, com um custo razoável.

- **Perspetiva 2 (Verma, 2009):**  
  Considera a gestão de IT como o ramo da ciência da computação que se ocupa das técnicas que asseguram o funcionamento impecável dos sistemas de computador.

- **Perspetiva 3 (Veríssimo, 2001):**  
  Define a gestão de IT em termos das funções de *planeamento, supervisão e controlo* que asseguram a prestação de um serviço adequado, conforme as expectativas dos utilizadores.

---

## 3. Objetivos da Gestão de IT

- **Satisfação dos Utilizadores:**  
  Medida através do desempenho e disponibilidade dos serviços, embora por vezes estes aspetos possam ser confundidos.

- **Custo:**  
  Existe sempre um equilíbrio a ser alcançado entre o custo e a qualidade do serviço prestado.

---

## 4. O Ciclo de Vida do Sistema de IT

O documento apresenta o ciclo de vida dos sistemas de IT, dividido em várias fases, agora enriquecido com detalhes sobre requisitos, estratégias e operação:

### 4.1 Planeamento

- **Definição de Necessidades:**  
  - Estabelecimento dos objetivos do sistema.
  - Definição do orçamento (investimento inicial e despesas mensais).
  - Identificação das entidades responsáveis pela construção e gestão do sistema.

- **Requisitos:**  
  - **Funcionais:** Relativos às funcionalidades do programa, ou seja, aquilo que o sistema deve fazer.  
  - **Não-Funcionais:**  
    - **Dimensionamento de Hardware:** Escolha adequada de servidores e componentes.  
    - **Ambientais:** Evitar locais perigosos (ex.: não profanar estátuas, evitar favelas ou zonas de risco).  
    - **Legais:** Conformidade com regulamentos como o RGPD para proteção de dados dos utilizadores.  
    - **Energia:** Consumo e abastecimento (ex.: fontes redundantes).  
    - **Controlo de Acesso:** Garantir segurança física e lógica.  
    - **Conectividade:** Acesso a fibra ótica ou outras infraestruturas de rede.  
    - **Performance:** Largura de banda, replicação, tolerância a falhas.  
    - **Gestão e Segurança:** Requisitos como autenticação de dois fatores (2FA) para administradores.  
    - **Custos:** Gestão de custos operacionais e de implementação.

- **Design do Sistema:**  
  - Definição da conectividade, aplicações e hardware.  
  - Dimensionamento do sistema (tipo e configuração).  
  - Planeamento da gestão, infraestrutura e definição de estratégias e políticas:  
    - Exemplo de política: Servidores com redundância (fontes de alimentação, placas de rede) e mecanismos para detetar avarias.  
  - **Infraestrutura Física vs. Cloud:**  
    - **Vantagens da Cloud:** Escalabilidade, baixo custo inicial, alta customização, sem necessidade de espaço físico ou técnicos locais.  
    - **Desvantagens da Cloud:** Dependência de fornecedores, custos elevados ao mudar devido a APIs proprietárias.  
    - **Alternativas:** Uso de clouds híbridas.  
  - **Exemplo:** O datacenter da FCUL é um *brownfield*, ou seja, uma instalação existente que está a ser adaptada.

### 4.2 Implementação

- **Construção Física:**  
  - Instalação em datacenters, cabeamento e infraestrutura física.

- **Aquisição e Instalação:**  
  - Compra e instalação de hardware.  
  - Estabelecimento de contratos e realização de testes.

- **Garantia dos Requisitos:**  
  - Assegurar que os requisitos de performance e as estratégias definidas sejam cumpridos através de políticas específicas.  
  - **Nota:** A instalação segue o plano à risca para garantir que tudo corra bem.

### 4.3 Operação

- **Prestação de Serviços:**  
  - A fase onde o sistema está em funcionamento e os serviços são fornecidos, sendo a mais longa do ciclo de vida do datacenter.

- **Monitorização e Gestão:**  
  - A equipa atua para garantir que os serviços cumpram as expectativas e para responder a eventos ou anomalias.  
  - **Reconfiguração:** Inclui adicionar hardware (ex.: cabos a switches), atualizar endereços IP, adicionar utilizadores, etc.  
  - **Ferramentas:** Uso do *Ticket Troubling Service (TTS)* para gestão de tickets, semelhante a sistemas de helpdesk.

### 4.4 Atualização (Update)

- **Natureza:**  
  - Procedimento planeado, não apenas manutenção regular.

- **Motivações:**  
  - Baixo desempenho.  
  - Atualização tecnológica.  
  - Redução de custos operacionais.  
  - Alterações organizacionais (fusões, novos negócios).

### 4.5 Terminação

- **Procedimentos:**  
  - Transferência de dados e eliminação correta do hardware.

- **Considerações:**  
  - Restrições de segurança e confidencialidade.  
  - Conformidade com normas ambientais (ex.: reciclagem).  
  - Observância da legislação aplicável.

---

## 5. Organização e Estrutura da Equipa de Gestão de IT

- **Divisão da Equipa:**  
  - **Linhas de Suporte:**  
    - **1ª Linha:** Suporte inicial (ex.: "call center"), faz triagem e resolve a maioria dos casos simples (ex.: reiniciar routers). Escalona casos complexos.  
    - **2ª Linha:** Mais especializada, com permissões alargadas. Trabalha para capacitar a 1ª linha (ex.: via FAQs, guiões ou ferramentas de diagnóstico) e reduz a sua própria carga.  
    - **3ª Linha:** Altamente especializada (ex.: administradores de sistemas), lida com problemas complexos.  
  - **Interdependências:**  
    - Redes (L1 e L2), sistemas (L3+), aplicações (transversal).  
    - Segurança é uma preocupação transversal (ex.: certificados em aplicações, firewalls em redes, autenticação em sistemas).

- **Papéis e Responsabilidades:**  
  - **Técnico/Technical Manager:** Define estratégias a nível de redes.  
  - **CTO:** Implementa políticas, alinhado com a 2ª linha.  
  - **Suporte (Utilizador):** Resposta imediata a eventos operacionais.  
  - **Coordenador Técnico:** Faz a ponte entre IT e compras, elaborando cadernos de encargos.

- **Adaptação da Estrutura:**  
  - Depende da especialização dos membros, do negócio, do tamanho da equipa e da complexidade da infraestrutura.  
  - Comunicação entre áreas (sistemas, redes, aplicações) é essencial devido à interdependência.

---

## 6. O Ciclo de Vida da Gestão

- **Processos Chave:**  
  - Monitorização constante do sistema.  
  - Processamento de eventos e supervisão do estado dos sistemas.  
  - Tomada de decisões para reconfiguração conforme os eventos.

- **Decisões Baseadas em:**  
  - **Estratégia**  
  - **Política**  
  - **Táticas**

---

## 7. Decisões na Gestão de IT

As decisões são fundamentadas em três níveis:

### 7.1 Estratégia
- **Caracterização:**  
  - Visão a longo prazo com incerteza, revista ocasionalmente.  
  - Inicia-se no planeamento.  
- **Exemplo:** Todos os utilizadores devem ser identificados para evitar roubo de identidade.

### 7.2 Política
- **Caracterização:**  
  - Regras gerais que implementam a estratégia, definidas no planeamento.  
- **Exemplo:** Senhas com mínimo de 8 caracteres, alteradas a cada 90 dias; administradores usam 2FA.

### 7.3 Táticas
- **Caracterização:**  
  - Ações imediatas derivadas da política, focadas em eventos inesperados.  
- **Exemplo:** Configurar o Active Directory para regras de senhas e gerir expirações.

---

## 8. Ferramentas de Suporte à Gestão de IT

- **8.1 Ticket Trouble Service (TTS):**  
  - **Funções:**  
    - Gestão de tickets/incidentes, com integração de e-mail para respostas, atribuições e histórico.  
    - Geração de estatísticas e registo de problemas.  
  - **Exemplos:** OTRS, GLPI.

- **8.2 Monitoring Framework:**  
  - **Funções:**  
    - Recolha contínua de dados do sistema.  
    - Visão global do estado do sistema e alertas para problemas.  
    - Integração com dados da equipa.  
  - **Exemplos:** Nagios, Zabbix.

- **8.3 Knowledge Base (KB):**  
  - **Funções:**  
    - Plataforma tipo wiki para armazenar conhecimento da equipa (ex.: mapa da rede, passwords de root, configurações de aplicações/redes).  
    - Essencial para resiliência organizacional face a saídas de pessoal.  
    - Suporta resolução de tickets e diagnóstico.

---

## 9. Conclusão

- **Resumo Final:**  
  - Os sistemas de IT têm um ciclo de vida (nascimento, operação, término), e a gestão eficaz depende de procedimentos claros, equipas bem organizadas e ferramentas adequadas.  
  - Diretrizes e papéis definidos poupam tempo, evitam erros e protegem a equipa.

---

## Fontes e Links de Referência

- **OTRS:** [https://otrs.com/](https://otrs.com/)  
- **GLPI:** [https://glpi-project.org/](https://glpi-project.org/)  
- **Nagios:** [https://www.nagios.com](https://www.nagios.com)  
- **Zabbix:** [https://www.zabbix.com/](https://www.zabbix.com/)
