# Arquitetura e Planeamento de Datacenters

## Introdução
O planeamento e montagem de um datacenter é um processo complexo que requer atenção meticulosa a diversos aspetos técnicos, desde a disposição física dos equipamentos até sistemas de refrigeração e segurança.

## Padronização Física dos Equipamentos

### Racks e Servidores
- **Largura Padronizada**: Independentemente da marca, as racks seguem medidas standard.
- **Altura em Rack Units (U)**: 
  - Cada unidade (U) corresponde a 4.5 cm
  - A altura dos servidores e racks é sempre múltipla de U
  - Não existem meios U's, apenas unidades inteiras

### Instalação e Manutenção
- Servidores são instalados diretamente nas racks através de parafusos
- Utilizam calhas deslizantes que permitem manutenção fácil, similar a gavetas
- Alguns servidores são "hot-swappable", permitindo substituição de componentes sem interromper o funcionamento

## Energia e Redundância

### Alimentação Elétrica
- Servidores não ligam diretamente à parede
- Conectam-se às fichas especializadas da rack
- Cada rack possui duas filas de fichas com circuitos elétricos distintos
- Múltiplas racks podem ter até 10 circuitos diferentes

### Sistemas de Backup
- Ligação a Unidades de Alimentação Ininterrupta (UPS)
- Gerador de emergência para falhas de energia
- Duas fontes de alimentação por servidor para redundância

## Infraestrutura de Refrigeração

### Gestão Térmica
- **Corredores de Ar**:
  - Separação entre corredores de ar frio e quente
  - Ar frio entra pela frente dos servidores, sai por trás
  - Servidores posicionados costas com costas e frente com frente

### Técnicas de Arrefecimento
- **Inrows**: Equipamentos que capturam ar quente e injetam ar frio
- Métodos de transferência de calor:
  1. Sistemas de água por tubagens subterrâneas
  2. Expansão Direta (usando gás, similar a frigoríficos)
  3. Freecooling em dias mais frios (usando ar exterior)

### Otimização Térmica
- Placeholders em espaços livres das racks para controlo de fluxo de ar
- Switches orientados para compatibilidade térmica
- Grelhas de controlo de pressão e extração de ar

## Segurança e Acessos

### Controlo de Acesso
- Sistemas rigorosos de entrada e monitorização
- Restrição de movimento dentro do datacenter

### Proteção contra Incêndios
- Sistema de deteção com dupla tecnologia
- Ativação de extintores apenas após confirmação de dois sensores diferentes
- Controlo cuidadoso da pressão durante libertação de gases

## Infraestrutura de Rede

### Sistemas KVM
- Switches que permitem controlo de múltiplas máquinas
- Acesso através de um único ecrã, rato e teclado
- Rede paralela semelhante a ethernet

## Planeamento Prévio
- Elaboração detalhada de planta antes da construção
- Consideração de:
  - Disposição elétrica
  - Fluxos de ar
  - Routing de cabos
  - Posicionamento de equipamentos

## Conclusão
A montagem de um datacenter é um processo de engenharia complexo que requer planeamento meticuloso, considerando aspetos de hardware, energia, refrigeração, segurança e eficiência operacional.
