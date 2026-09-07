# Notas Técnicas — SCADA/ICS

## 1. Infraestrutura crítica e OT/IT

Infraestrutura crítica reúne sistemas e ativos cuja interrupção ou destruição pode causar impacto relevante sobre segurança nacional, saúde pública ou segurança econômica. O material destaca energia elétrica, água e saneamento, gás e petróleo, transporte, saúde, telecomunicações, financeiro e governo.

A convergência OT/IT reduziu o isolamento histórico dos ambientes industriais. OT prioriza disponibilidade e segurança física; IT tradicionalmente prioriza confidencialidade e integridade. Essa diferença de prioridades é central para a análise de risco.

## 2. Purdue Reference Model

O modelo apresentado organiza a planta em níveis:

- **Nível 0:** processo físico — sensores e atuadores;
- **Nível 1:** controle básico — RTUs, PLCs e IEDs;
- **Nível 2:** supervisório — SCADA, HMI e OPC Server;
- **Nível 3:** operações de site — Historian, MES, KPIs, manutenção e serviços de transição;
- **Níveis 4–5:** rede corporativa e internet.

A DMZ e a segmentação entre IT e OT são apresentadas como elementos importantes de contenção.

## 3. RTU

A Remote Terminal Unit coleta dados físicos, transmite informações ao SCADA e recebe comandos capazes de acionar atuadores. O material usa como exemplo uma RTU simulada comunicando DNP3 via TCP/20000.

## 4. DNP3

O DNP3 é apresentado como protocolo amplamente utilizado em energia elétrica, água e saneamento e oil & gas. A documentação do módulo destaca que implementações de DNP3 base podem não utilizar autenticação criptográfica.

Principais grupos abordados:

| Grupo | Função | Relevância |
|---|---|---|
| G01 | Binary Input | Estado de entradas digitais |
| G12 | CROB | Comandos de controle de saídas |
| G20 | Counter | Contadores cumulativos |
| G30 | Analog Input | Valores analógicos de sensores |
| G41 | Analog Output | Escrita/saída analógica |
| G50 | Time and Date | Sincronização temporal |
| G60 | Class 0 | Solicitação de dados estáticos |

Function codes destacados no laboratório incluem leitura, resposta e Direct Operate.

## 5. Análise de frames

Um frame DNP3 pode ser estudado em três camadas principais:

1. **Data Link:** start bytes, endereços e CRC;
2. **Transport:** fragmentação e sequência;
3. **Application:** function code, IIN e object groups.

A assinatura de início apresentada no material é `0x0564`.

## 6. Fragilidades estruturais

O módulo destaca quatro problemas do DNP3 base:

- ausência de autenticação;
- ausência de criptografia;
- ausência de integridade criptográfica de mensagens;
- ausência de proteção robusta contra replay.

O CRC-16 é tratado como mecanismo de detecção de erro de transmissão, não como autenticação criptográfica.

## 7. Taxonomia de ameaças estudada

O material apresenta reconhecimento, espionagem passiva, spoofing/falsificação, comandos não autorizados, denial of service e replay como categorias de ataque ao DNP3.

Para um portfólio de CTI, o ponto central não é reproduzir ataques contra sistemas reais, mas demonstrar capacidade de:

- identificar a superfície de ataque;
- interpretar evidências de rede;
- avaliar impacto operacional;
- correlacionar comportamento com ativos e arquitetura;
- recomendar controles defensivos.

## 8. Defesas

As principais defesas apresentadas são:

- DNP3 Secure Authentication v5;
- segmentação de rede IT/OT;
- whitelist de IPs e controle de fluxos;
- IDS/monitoramento específico para protocolos industriais;
- inventário e atualização de firmware;
- aplicação de frameworks e requisitos de segurança ICS.

## 9. Frameworks

O material apresenta IEC 62443, NERC CIP, NIST SP 800-82 e IEEE 1815 como referências relevantes para segurança industrial.

## 10. Insight de inteligência

Em OT, o valor da inteligência não está apenas no indicador técnico. Uma observação de tráfego deve ser relacionada ao ativo, função industrial, processo físico potencialmente afetado, contexto operacional e capacidade do adversário.
