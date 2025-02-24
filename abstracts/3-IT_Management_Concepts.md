# IT Management Concepts (t030-slides)

O documento aborda os conceitos fundamentais da gestão de IT, estruturando o conteúdo em diversas secções que cobrem desde a definição e perspetivas sobre a administração de IT até à organização da equipa e às ferramentas de suporte. Abaixo, encontra-se um resumo detalhado de cada secção.

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

O documento apresenta o ciclo de vida dos sistemas de IT, dividido em várias fases:

- **Planeamento:**  
  - **Definição de Necessidades:**  
    - Estabelecimento dos objectivos do sistema.
    - Definição do orçamento (investimento inicial e despesas mensais).
    - Identificação das entidades responsáveis pela construção e gestão do sistema.
  
  - **Requisitos:**
    - **Funcionais vs. Não-Funcionais:**
      - **Performance:** Ex.: largura de banda, replicação.
      - **Ambientais:** Localizações geográficas, infraestruturas físicas.
      - **Custos:** Custos operacionais.
      - **Gestão e Segurança:** Considerações de gestão e requisitos de segurança.
      - **Aspectos Legais:** Cumprimento das normas e legislações.

  - **Design do Sistema:**
    - Definição da conectividade, aplicações e hardware.
    - Dimensionamento do sistema (tipo e configuração).
    - Planeamento da gestão, infraestrutura e definição de estratégias.

- **Implementação:**
  - **Construção Física:**  
    - Instalação em data centers, cabeamento e infraestrutura física.
  
  - **Aquisição e Instalação:**
    - Compra e instalação de hardware.
    - Estabelecimento de contratos e realização de testes.
  
  - **Garantia dos Requisitos:**  
    - Assegurar que os requisitos de performance e as estratégias definidas sejam cumpridos através de políticas específicas.

- **Operação:**
  - **Prestação de Serviços:**  
    - A fase onde o sistema está em funcionamento e os serviços são efetivamente fornecidos.
  
  - **Monitorização e Gestão:**
    - A equipa de gestão atua para garantir que os serviços prestados cumpram as expectativas e para responder a quaisquer eventos ou anomalias.

- **Atualização (Update):**
  - **Natureza:**  
    - Não se trata de manutenção regular, mas de um procedimento planeado.
  
  - **Motivações:**
    - Baixo desempenho.
    - Atualização tecnológica.
    - Redução dos custos operacionais.
    - Alterações organizacionais (fusões, novos negócios).

- **Terminação:**
  - **Procedimentos:**
    - Não se limita ao encerramento, mas inclui a transferência de dados e a eliminação correta do hardware.
  
  - **Considerações:**
    - Restrições de segurança e confidencialidade.
    - Conformidade com normas ambientais (ex.: reciclagem).
    - Observância da legislação aplicável.

---

## 5. Organização e Estrutura da Equipa de Gestão de IT

- **Divisão da Equipa:**
  - **Linhas de Suporte:**  
    - 1ª linha, 2ª linha e 3ª linha, organizadas conforme a complexidade e a área de especialização (ex.: Redes, Sistemas, Segurança).

- **Papéis e Responsabilidades:**
  - **Técnico/Technical Manager:**  
    - Atua na definição de estratégias a nível de redes.
  
  - **CTO:**  
    - Foca na implementação das políticas, correspondendo à 2ª linha de suporte.
  
  - **Suporte (Utilizador):**  
    - Responsável pelas táticas, ou seja, pela resposta imediata a problemas e eventos operacionais.

- **Adaptação da Estrutura:**
  - As fronteiras e a organização dependem da especialização dos membros, do negócio, do número de membros e da complexidade da infraestrutura e dos serviços.

---

## 6. O Ciclo de Vida da Gestão

Este ciclo enfoca a monitorização e as ações corretivas contínuas:

- **Processos Chave:**
  - Monitorização constante do sistema.
  - Processamento de eventos e supervisão do estado dos sistemas.
  - Tomada de decisões para reconfiguração conforme os eventos detectados.

- **Decisões Baseadas em:**
  - **Estratégia**
  - **Política**
  - **Táticas**

---

## 7. Decisões na Gestão de IT

As decisões são fundamentadas em três níveis:

### 7.1 Estratégia
- **Caracterização:**
  - Visão a longo prazo com elevado grau de incerteza.
  - Reflete a visão dos decisores e é revista ocasionalmente quando as condições mudam.
  - Inicia-se na fase de planeamento.
  
- **Exemplo de Estratégia:**
  - Todos os utilizadores do sistema devem ser identificados de forma a dificultar o roubo de identidade.

### 7.2 Política
- **Caracterização:**
  - Regras gerais que implementam a estratégia.
  - Devem ser estabelecidas já no planeamento.
  
- **Exemplo de Política:**
  - As senhas devem ter, no mínimo, 8 caracteres e ser alteradas a cada 90 dias, com evidência da alteração efetuada pelo utilizador.

### 7.3 Táticas
- **Caracterização:**
  - Ações imediatas e práticas derivadas da política.
  - Focam na resposta a eventos inesperados durante a operação.
  
- **Exemplo de Tática:**
  - Configurar o Active Directory para aplicar as regras de senhas e definir procedimentos para senhas expiradas, especialmente para utilizadores no estrangeiro.

---

## 8. Ferramentas de Suporte à Gestão de IT

O documento destaca diversas ferramentas que facilitam a gestão, a comunicação e a monitorização dos sistemas:

### 8.1 Ticket Trouble Service (TTS)
- **Funções:**
  - Recolha de "tickets" ou incidentes criados pelos utilizadores.
  - Integração com sistemas de e-mail para:
    - Responder aos utilizadores.
    - Atribuir tickets a membros ou grupos.
    - Registar notas e manter um histórico permanente.
  - Geração de estatísticas e histórico dos problemas.

- **Exemplos:**
  - [OTRS](https://otrs.com/)
  - [GLPI](https://glpi-project.org/)

### 8.2 Monitoring Framework
- **Funções:**
  - Recolha contínua de informações do sistema.
  - Fornecimento de uma visão global e consistente da situação do sistema.
  - Emissão de alertas à equipa sempre que são detectados problemas.
  - Integração com informações recolhidas pela própria equipa.

- **Exemplos:**
  - [Nagios](https://www.nagios.com)
  - [Zabbix](https://www.zabbix.com/)

### 8.3 Knowledge Base
- **Funções:**
  - Plataforma de estilo wiki para armazenamento e consulta de informação.
  - Registo histórico das ações realizadas e dos motivos por detrás das decisões.
  - Suporte na resolução de problemas através de diagnósticos e pesquisa histórica.

---

## 9. Conclusão

- **Resumo Final:**
  - Os sistemas de IT nascem, vivem e terminam, e a sua gestão é um processo dinâmico e complexo.
  - Uma gestão eficaz depende da implementação de procedimentos bem definidos, de uma equipa diversificada e de ferramentas que facilitam a monitorização e a comunicação.
  - Estabelecer diretrizes claras e papéis bem definidos na equipa é essencial para poupar tempo, evitar erros e proteger os membros envolvidos no processo.

---

## Fontes e Links de Referência

- **OTRS:** [https://otrs.com/](https://otrs.com/)  
- **GLPI:** [https://glpi-project.org/](https://glpi-project.org/)  
- **Nagios:** [https://www.nagios.com](https://www.nagios.com)  
- **Zabbix:** [https://www.zabbix.com/](https://www.zabbix.com/)
