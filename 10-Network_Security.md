# Network Security

Este é sobre segurança em sistemas de redes, com ênfase em conceitos práticos e exemplos relacionados com autenticação, controlo de acesso, não-repúdio e disponibilidade de serviços e dados. Não se trata de um curso intensivo de segurança em TI, mas sim de uma introdução a aspectos-chave, destinada a fornecer uma base compreensível. A autoria é atribuída a "Cus - Hiso Mirumta" (provavelmente um erro de OCR para "Curso - Hiso Miranda"). Abaixo está o resumo detalhado de cada secção.

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
