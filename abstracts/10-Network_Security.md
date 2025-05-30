# Fundamentos de Segurança de Sistemas de Informação

Este é sobre segurança em sistemas de redes, com ênfase em conceitos práticos e exemplos relacionados com autenticação, controlo de acesso, não-repúdio e disponibilidade de serviços e dados. Não se trata de um curso intensivo de segurança em TI, mas sim de uma introdução a aspectos-chave, destinada a fornecer uma base compreensível. A autoria é atribuída a "Cus - Hiso Mirumta" (provavelmente um erro de OCR para "Curso - Hiso Miranda"). Abaixo está o resumo detalhado de cada secção.

---

## Os Pilares da Segurança (FCAP**S**)

A segurança da informação assenta em cinco pilares fundamentais que garantem a proteção completa dos sistemas e dados organizacionais.

### Autenticação - Verificar "Quem És"

A autenticação constitui a primeira linha de defesa, estabelecendo a identidade dos utilizadores. Para implementar uma autenticação robusta, deve considerar-se a autenticação de dois factores (2FA), que adiciona uma camada extra de segurança sem complicar desnecessariamente os processos. A Chave Móvel Digital representa uma solução nacional eficaz, enquanto o Single Sign-On (SSO) permite que os utilizadores acedam a múltiplos sistemas com uma única credencial, reduzindo a fadiga de passwords e melhorando a experiência do utilizador.

O SSO funciona através de um servidor de autenticação centralizado que gere credenciais partilhadas entre diferentes aplicações. Isto significa que, uma vez autenticado, o utilizador pode aceder a todos os sistemas autorizados sem necessidade de novas autenticações. Complementarmente, a Autenticação de Múltiplos Factores (MFA) fortalece ainda mais este processo, exigindo pelo menos dois elementos diferentes para verificar a identidade.

### Confidencialidade - Proteger "O Quê"

A confidencialidade garante que apenas pessoas autorizadas acedem à informação. Este pilar encontra-se intimamente ligado ao Regulamento Geral sobre a Proteção de Dados (RGPD), que estabelece as regras legais para o tratamento de dados pessoais.

A criptografia constitui a ferramenta fundamental para garantir confidencialidade. As chaves privadas e públicas permitem cifrar informação de forma que apenas o destinatário autorizado a possa decifrar. Os certificados digitais complementam este sistema, fornecendo uma forma de verificar a autenticidade das chaves públicas.

As partições cifradas representam uma medida de proteção adicional, disponível tanto em sistemas Linux como Windows. Esta tecnologia garante que, mesmo com acesso físico ao disco, os dados permanecem inacessíveis sem as credenciais adequadas. Em cenários de alto risco, podem implementar-se "botões de autodestruição" através de daemons que contactam servidores centrais, permitindo o apagamento remoto de dados sensíveis quando necessário.

### Integridade - Garantir "Como Está"

A integridade assegura que os dados não foram alterados de forma não autorizada. Os backups constituem o mecanismo fundamental para manter a integridade, permitindo restaurar sistemas e dados para estados anteriores conhecidos e confiáveis.

Os backups servem dois propósitos essenciais: repor sistemas escolhendo pontos específicos no tempo para restauro, e manter um histórico que pode ser crucial para auditoria e conformidade legal. Esta funcionalidade de arquivo histórico revela-se particularmente importante para efeitos contabilísticos e de compliance.

Existem três tipos principais de backup, cada um com as suas vantagens específicas. O backup completo (Full) copia todo o disco, oferecendo simplicidade máxima na recuperação. O backup diferencial (Diff) compara o estado atual com o último backup completo, guardando apenas as diferenças, permitindo estratégias como backups completos mensais combinados com diferenciais diários. O backup incremental guarda apenas as informações novas relativamente ao último backup, independentemente do seu tipo, optimizando o espaço de armazenamento.

Em termos de facilidade de recuperação, a hierarquia é clara: Full > Diferencial > Incremental. Quanto mais simples o tipo de backup, mais rápida e directa é a recuperação.

Contudo, os backups enfrentam desafios legais significativos, particularmente com o direito ao esquecimento do RGPD. As organizações são obrigadas a apagar informações pessoais a pedido, mas isto torna-se impraticável com backups históricos de 20+ anos armazenados em fitas magnéticas.

### Não Repúdio - Provar "Quando e Por Quem"

O não repúdio garante que as acções realizadas não podem ser negadas posteriormente. Isto consegue-se principalmente através da manutenção de logs detalhados, que requerem espaço de armazenamento significativo e podem ser enviados para sistemas SIEM (Security Information and Event Management) para análise.

Para que os logs tenham validade jurídica, é fundamental garantir a sua integridade. Tecnologias como blockchain podem ser utilizadas para criar registos imutáveis que comprovem que os logs não foram alterados após a sua criação.

O objectivo é duplo: conseguir provar que os utilizadores realizaram actividades inadequadas quando necessário, e manter um registo completo de quem fez o quê e quando, para efeitos de auditoria e investigação.

### Disponibilidade - Garantir "Quando Precisas"

A disponibilidade assegura que os sistemas e dados estão acessíveis quando necessário. Este pilar conecta-se directamente com os conceitos de RPO (Recovery Point Objective) e RTO (Recovery Time Objective).

O RPO define qual o tempo do backup mais recente, ou seja, quantos dados podem ser perdidos em caso de falha. O RTO especifica quanto tempo é necessário para restaurar o sistema a partir dos backups. Estes dois indicadores são cruciais para definir estratégias de backup e recuperação adequadas às necessidades do negócio.

## Estratégias de Proteção e Governança

### Políticas de Segurança

As políticas constituem ferramentas fundamentais para impor regras de segurança de forma consistente. Servem como referência que remove a responsabilidade das equipas de suporte de primeira linha, transferindo-a para os administradores. Isto inclui considerações sobre legislação aplicável e conformidade com o RGPD.

### Auditoria e Avaliação

A auditoria de segurança pode ser realizada através de várias abordagens complementares. O pentesting envolve contratar empresas especializadas para tentar comprometer a segurança organizacional, permitindo identificar e corrigir vulnerabilidades antes que sejam exploradas maliciosamente.

O GVM (provavelmente Greenbone Vulnerability Management) compara descobertas sobre a rede com bases de dados de vulnerabilidades conhecidas (CVE - Common Vulnerabilities and Exposures), gerando relatórios detalhados sobre potenciais riscos.

As checklists proporcionam uma abordagem sistemática, definindo verificações regulares que devem ser realizadas para manter os níveis de segurança adequados.

Os serviços de rating agregam informação sobre organizações através de vários meios, oferecendo avaliações de segurança sem necessidade de pentesting directo. Estas empresas podem alertar para vulnerabilidades e permitir que as organizações paguem para incluir os seus ratings em listas públicas.

## Desafios e Considerações Práticas

### Resistência dos Utilizadores

Qualquer mecanismo de segurança encontra resistência natural dos utilizadores, que o percepcionam como um obstáculo que complica e atrasa o seu trabalho. Isto leva frequentemente a comportamentos de contorno, como utilizar post-its para passwords ou gravar credenciais no browser, comprometendo a segurança pretendida.

### Tecnologias Emergentes e Ameaças

A cloud computing introduz novos riscos, como a capacidade dos atacantes cifrarem dados rapidamente através de ransomware. Contudo, surgem também novas protecções, como tecnologias "write once" que permitem apenas escrita, tornando o apagamento um processo demorado que não pode ser realizado apenas com credenciais de root.

### Air Gap e Isolamento

O air gap pode ser implementado não apenas fisicamente, mas também através de software. Isto envolve agentes que activam aleatoriamente as placas de rede para realizar backups, desligando-as de seguida. Estes sistemas não permitem SSH ou outros acessos remotos, requerendo intervenção física para manutenção.

### Automatização de Backups

Existem sistemas robotizados de gestão de fitas magnéticas que utilizam braços mecânicos para gerir automaticamente quando e onde as fitas são escritas, optimizando o processo de backup para grandes volumes de dados.

Este resumo integra todos os conceitos dos seus apontamentos numa estrutura coerente que facilita a compreensão das inter-relações entre os diferentes aspectos da segurança da informação. Cada elemento contribui para um sistema de segurança robusto que protege adequadamente os activos informacionais organizacionais.

---

## Página 2: Introdução à Rede e Segurança
- **Título**: The Cube Network Systems Applications
- **Conteúdo**: Introduz a temática geral da apresentação, que abrange sistemas de redes, aplicações e segurança. É uma página inicial que define o contexto, sugerindo que os tópicos seguintes serão explorados em profundidade.

---

## Página 3: Atividades de Segurança
- **Título**: Security Activities
- **Conteúdo**:
  - **Autenticação**: Verificar a identidade de utilizadores ou dispositivos.
  - **Confidencialidade**: Garantir que apenas pessoas autorizadas acedam aos dados.
  - **Integridade**: Assegurar que os dados não são alterados de forma não autorizada.
  - **Não-repúdio**: Garantir que uma ação ou transação não pode ser negada por quem a realizou.
  - **Disponibilidade**: Manter os serviços e dados acessíveis quando necessários (nota: "Availability" aparece duplicado, possivelmente um erro).
- **Explicação**: Esta página lista os pilares fundamentais da segurança em TI, explicando brevemente o que cada um significa. São os objetivos principais que qualquer sistema seguro deve alcançar.

---

## Página 4: Segurança como um Compromisso
- **Título**: Security as a Compromise
- **Conteúdo**:
  - **Corrida entre segurança e hackers**: Há uma competição constante entre os responsáveis pela segurança e os atacantes.
  - **Compromisso entre usabilidade e segurança**: Maior segurança pode reduzir a facilidade de uso. O sistema mais seguro seria um que estivesse desconectado da rede, mas isso não é prático.
- **Explicação**: Introduz a ideia de que a segurança não é absoluta e exige equilíbrio. Por exemplo, um sistema offline é impenetrável, mas inútil para a maioria dos fins práticos.

---

## Página 5: Exemplos Práticos de Segurança
- **Título**: Examples
- **Conteúdo**:
  - **VPN**: Usada para aceder a serviços de forma segura.
  - **Bloqueio de portas a endereços MAC**: Limita o acesso à rede com base em identificadores de hardware.
  - **Expiração/restrições de palavras-passe**: Obriga a troca regular e a complexidade das palavras-passe.
  - **Bloqueio automático do computador**: Após um período de inatividade, o sistema bloqueia-se.
  - **Armazenamento encriptado**: Dados pessoais são guardados de forma cifrada.
  - **Impacto do antivírus no desempenho**: Pode tornar o sistema mais lento.
  - **Autenticação de dois fatores (2FA)**: Mais segura, mas pode ser lenta ou difícil de usar.
- **Explicação**: Esta secção fornece exemplos concretos de medidas de segurança e os seus efeitos no dia a dia, destacando o compromisso entre segurança e conveniência.

---

## Página 6: Objetivo da Lição
- **Título**: This Lesson
- **Conteúdo**:
  - Não é um curso intensivo de segurança em TI.
  - Foco em aspectos práticos:
    - Autenticação
    - Controlo de Acesso
    - Não-repúdio
    - Disponibilidade de Serviços e Dados
- **Explicação**: Define o âmbito da apresentação, esclarecendo que o objetivo é abordar tópicos específicos de forma prática, em vez de cobrir toda a segurança em TI.

---

## Página 7: Autenticação de Hardware - Porquê?
- **Título**: Hardware Authentication - Why?
- **Conteúdo**:
  - **Riscos de dispositivos na rede**:
    - **ARP poisoning**: Ataque que falsifica endereços na rede.
    - **Network snooping**: Interceção de dados na rede.
    - **Servidores DHCP falsos**: Podem redirecionar o tráfego.
    - **Falsificação de endereços MAC**: Embora usados para identificação, podem ser manipulados.
- **Explicação**: Explica a necessidade de autenticação de hardware devido aos riscos que dispositivos não autorizados representam numa rede.

---

## Página 8: Autenticação de Hardware - Como?
- **Título**: Hardware Authentication - How?
- **Conteúdo**:
  - **Protocolo 802.1x**:
    - Usado para autenticação de utilizadores e dispositivos.
    - Opera na camada de ligação (link layer).
    - Popular em redes Wi-Fi, menos em redes com cabo.
  - **Tarefa de casa**: Ler sobre o protocolo 802.1x e entender os papéis dos participantes (ex.: cliente, autenticador, servidor de autenticação).
- **Explicação**: Detalha o uso do 802.1x como solução para autenticação segura, destacando a sua aplicação prática e incentivando estudo adicional.

---

## Página 10: Abordagens ao Controlo de Acesso
- **Título**: Approaches
- **Conteúdo**:
  - **Pergunta central**: "Onde está a lista de quem pode fazer o quê?"
  - **Listas de Controlo de Acesso (ACL)**:
    - A lista está no recurso.
    - **Lista branca**: Acesso negado por padrão, exceto aos permitidos.
    - **Lista negra**: Acesso permitido por padrão, exceto aos bloqueados.
  - **Capacidades**: A lista está com o utilizador (ex.: permissões associadas ao utilizador).
- **Explicação**: Compara dois métodos de controlo de acesso, mostrando como a localização da "lista de permissões" define a abordagem de segurança.

---

## Página 32: Software de Backups
- **Título**: Backup: Software
- **Conteúdo**:
  - **Funções do software de backup**:
    - Agenda os backups.
    - Coordena a suspensão/retoma de serviços.
    - Integra-se com hipervisores de máquinas virtuais (VM) e armazenamento.
    - Gere o processo de staging (preparação de dados).
    - Controla robots (dispositivos automatizados de backup).
    - Permite recuperar ficheiros individuais.
- **Explicação**: Descreve o papel do software na gestão de backups, destacando a sua importância na coordenação e recuperação de dados.

---

## Página 33: Observações Finais sobre Backups (Parte 1)
- **Título**: Backups: Final Remarks
- **Conteúdo**:
  - **Preservação das fitas**:
    - Longe do público (segurança).
    - Proteção de dados.
    - Fora do centro de dados original.
    - Condições adequadas (humidade, campos magnéticos).
- **Explicação**: Aborda a necessidade de proteger fisicamente os backups, enfatizando a sua localização e condições de armazenamento.

---

## Página 34: Observações Finais sobre Backups (Parte 2)
- **Título**: Backups: Final Remarks
- **Conteúdo**:
  - **Falhas das fitas**: Podem falhar quando mais necessárias.
  - **Solução**: Testar amostras aleatórias regularmente.
- **Explicação**: Alerta para a possibilidade de falhas e sugere uma prática de verificação para garantir a fiabilidade.

---

## Página 35: Observações Finais sobre Backups (Parte 3)
- **Título**: Backups: Final Remarks
- **Conteúdo**:
  - **Preservar histórico**:
    - Problemas podem ser detetados após vários backups.
    - Manter backups históricos.
- **Explicação**: Recomenda guardar backups antigos para permitir a recuperação de dados em caso de problemas descobertos tardiamente.

---

## Páginas Omitidas ou incompletas
- **Páginas 1, 9, 11, 31, 36, 37**: Contêm tabelas ou texto incompleto, possivelmente devido a falhas de OCR ou formatação. Não fornecem informação substancial além de títulos repetidos ou fragmentos.
- **Nota**: Algumas páginas parecem ser placeholders ou slides de transição sem conteúdo relevante.

---

## Conclusão
A apresentação foca-se em conceitos práticos de segurança em redes, abordando:
1. **Autenticação**: Com destaque para o protocolo 802.1x e a necessidade de verificar dispositivos.
2. **Controlo de Acesso**: Comparando ACL e capacidades.
3. **Não-repúdio**: Garantir a responsabilidade por ações (embora menos detalhado).
4. **Disponibilidade**: Enfatizando backups e a sua gestão.

Os exemplos práticos (VPN, 2FA, etc.) e as observações sobre backups reforçam a aplicação real destes conceitos. A lição sublinha que a segurança é um equilíbrio entre proteção e usabilidade, com soluções como o 802.1x e backups bem geridos a serem fundamentais.

---
