# DNP3 Analysis Matrix

| Element | O que observar | Relevância para CTI |
|---|---|---|
| Start bytes | `0x0564` | Identificação do protocolo |
| Source/Destination | IDs Master/Outstation | Modelagem de comunicação |
| Function Code | Read / Response / Direct Operate | Identificação de comportamento |
| G01 | Binary Input | Estado digital |
| G12 | CROB | Comando de saída |
| G30 | Analog Input | Telemetria/sensores |
| G41 | Analog Output | Alteração de valor analógico |
| G50 | Time and Date | Correlação temporal |
| G60 | Class 0 | Inventário/reconhecimento de dados |
| IIN | Estado/alarmes | Contexto operacional |
| TCP/20000 | Transporte DNP3 | Identificação de fluxo |

## Risco → Evidência → Impacto → Controle

| Risco | Evidência esperada | Impacto potencial | Controle |
|---|---|---|---|
| Acesso não autenticado | Direct Operate em ambiente sem SA5 | Comando indevido | SA5 + segmentação |
| Espionagem | Tráfego DNP3 observável | Exposição de telemetria/topologia | Segmentação + monitoramento |
| Manipulação | Valores/objetos incompatíveis com baseline | Decisão operacional incorreta | IDS OT + integridade/autenticação |
| Replay | Mensagens antigas reaparecendo | Mascaramento de estado | Anti-replay/SA5 + detecção |
| DoS | Volume anômalo de requisições | Perda de comunicação | Rate limiting + monitoramento |

## Regra analítica

Nenhum pacote isolado deve ser tratado automaticamente como prova de comprometimento. Correlacionar protocolo, ativo, temporalidade, baseline operacional, arquitetura e outras evidências antes de produzir um julgamento de inteligência.
