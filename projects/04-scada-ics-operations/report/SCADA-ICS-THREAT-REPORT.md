# SCADA/ICS Threat Intelligence Report

> **Template de portfólio — baseado no Módulo 03.** Não representa um incidente real nem uma avaliação de uma infraestrutura operacional.

## 1. Executive Summary

**Intelligence requirement:** Qual característica da arquitetura SCADA/ICS e do protocolo DNP3 apresenta maior relevância para a exposição operacional estudada?

**Key judgment:** documentar, com evidências, como arquitetura, protocolo, ativos e controles se relacionam com o risco operacional.

**Confidence:** [Alta / Média / Baixa]

## 2. Escopo

- Ambiente: laboratório ICS autorizado
- Tecnologia: SCADA / RTU / DNP3
- Evidências: documentação do módulo, arquitetura do laboratório e capturas autorizadas
- Fora de escopo: sistemas industriais reais não autorizados

## 3. Arquitetura e Attack Surface

Descrever o ambiente usando o Purdue Model e destacar:

- níveis 0–1;
- SCADA/HMI no nível 2;
- Historian/operações no nível 3;
- fronteira IT/OT e DMZ;
- caminhos de acesso remoto;
- protocolos e portas observadas.

## 4. Asset Analysis

| Ativo | Purdue | Função | Protocolo | Impacto potencial | Confiança |
|---|---|---|---|---|---|
| RTU | L1 | Controle remoto de campo | DNP3/TCP | Físico/operacional | — |
| SCADA Master | L2 | Supervisão e comando | DNP3 | Operacional | — |
| HMI | L2 | Visualização/controle | — | Operacional | — |

## 5. DNP3 Traffic Analysis

Registrar, para cada evidência:

| Campo | Observação |
|---|---|
| Source/Destination | — |
| TCP port | 20000, quando aplicável |
| Function Code | — |
| Object Group/Variation | — |
| IIN | — |
| Source/Destination address | — |
| Timestamp | — |
| Interpretação | — |

### Filtros de análise

```text
dnp3
dnp3.al.func == 1
dnp3.al.func == 129
dnp3.al.func == 3
tcp.port == 20000
dnp3.al.obj == 30
dnp3.al.obj == 12
dnp3.al.obj == 41
```

> Os filtros acima são os apresentados no material. A disponibilidade exata de campos pode variar conforme a versão/dissector do Wireshark.

## 6. Threat Scenarios

Avaliar separadamente:

1. reconhecimento;
2. espionagem passiva;
3. falsificação/spoofing;
4. comando não autorizado;
5. denial of service;
6. replay.

Para cada cenário: pré-condição, evidência, ativo afetado, impacto, detecção, mitigação e confiança.

## 7. Evidence Assessment

| ID | Evidência | Fonte | Relevância | Confiabilidade | Confiança |
|---|---|---|---|---|---|
| E-01 | — | Captura autorizada | — | — | — |
| E-02 | — | Material do módulo | — | — | — |

Separar claramente **observação**, **inferência** e **julgamento de inteligência**.

## 8. Defensive Assessment

Avaliar a presença/ausência de:

- SA5;
- firewall/segmentação IT/OT;
- whitelist;
- monitoramento IDS industrial;
- inventário de ativos;
- gestão de firmware;
- controles de acesso remoto.

## 9. Intelligence Gaps

- Quais ativos estão realmente expostos?
- Quais implementações DNP3 usam autenticação?
- Quais caminhos IT→OT existem?
- Existem comandos DNP3 fora do baseline operacional?
- Há cobertura de monitoramento suficiente?

## 10. Recommendations

Priorizar recomendações por risco e viabilidade:

**P1 — Segmentação e controle de fluxos**

Restringir comunicação entre zonas e permitir apenas fluxos necessários.

**P1 — Autenticação DNP3**

Avaliar adoção de DNP3 Secure Authentication v5 conforme compatibilidade e risco operacional.

**P2 — Monitoramento OT**

Estabelecer baseline de comunicação e alertas para comportamentos anômalos.

**P2 — Inventário/Firmware**

Manter inventário atualizado e avaliar ciclo de vida e suporte dos dispositivos.

## 11. Conclusion

A conclusão deve responder ao intelligence requirement, indicar nível de confiança, registrar limitações e explicar quais ações defensivas são suportadas pelas evidências.

## 12. References

- Material didático: Módulo 03 — SCADA/ICS | Operações Cibernéticas.
- IEC 62443.
- NIST SP 800-82.
- IEEE 1815 / DNP3.
