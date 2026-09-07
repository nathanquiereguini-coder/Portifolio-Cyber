# SCADA/ICS — Cyber Operations

## Visão geral

Projeto de portfólio baseado no **Módulo 03 — SCADA/ICS | Operações Cibernéticas**, com foco em Cyber Threat Intelligence aplicada a ambientes industriais e infraestrutura crítica.

## Objetivos

- compreender a convergência OT/IT e seus riscos;
- modelar uma arquitetura industrial usando o Purdue Reference Model;
- identificar ativos e funções de RTU, PLC, DCS, SCADA/HMI;
- analisar DNP3 e seus principais objetos/function codes;
- interpretar tráfego DNP3 no Wireshark;
- reconhecer fragilidades estruturais do DNP3 base;
- relacionar ameaças a impacto operacional e físico;
- avaliar controles como DNP3 Secure Authentication v5, segmentação, IDS industrial e gestão de firmware/inventário.

## Ambiente estudado

O material apresenta um laboratório com uma RTU/outstation DNP3 simulada, um master SCADA e captura de tráfego em uma VM Ubuntu. O tráfego utiliza DNP3 sobre TCP/20000.

> **Segurança:** este projeto é documentado para fins educacionais. Qualquer reprodução prática deve ocorrer exclusivamente em laboratório autorizado e isolado. Não publicar credenciais, tokens ou infraestrutura operacional real.

## Frameworks e referências abordados

- Purdue Reference Model
- ISA-99 / IEC 62443
- NIST SP 800-82
- IEEE 1815 / DNP3 Secure Authentication v5
- MITRE ATT&CK — quando aplicável à análise de ameaças

## Estrutura

- `notes.md` — síntese técnica do módulo
- `report/SCADA-ICS-THREAT-REPORT.md` — modelo de relatório analítico
- `report/DNP3-ANALYSIS-MATRIX.md` — matriz de análise de protocolo e riscos
- `laboratory/README.md` — roteiro seguro de laboratório

## Escopo analítico

O projeto prioriza a pergunta de inteligência: **quais características da arquitetura OT e do DNP3 podem permitir observação, manipulação ou interrupção de processos industriais, e quais controles reduzem esses riscos?**

As conclusões devem distinguir fatos observados no laboratório, informações provenientes do material didático e inferências analíticas.
