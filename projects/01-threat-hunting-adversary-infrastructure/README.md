# Threat Hunting — Adversary Infrastructure Investigation

## Executive Summary

Projeto de portfólio voltado à investigação de infraestrutura adversária por meio da combinação de **Threat Hunting + Cyber Threat Intelligence (CTI)**.

O objetivo é transformar um indicador inicial em uma visão correlacionada de domínios, subdomínios, IPs, ASN, certificados, serviços e tráfego de rede, produzindo IOCs, TTPs e uma avaliação de confiança.

## Intelligence Requirement

> Quais ativos e padrões técnicos podem estar relacionados à infraestrutura investigada e quais evidências sustentam essa hipótese?

## Fluxo analítico

```
Indicador inicial
      ↓
Certificado / domínio / IP / artefato
      ↓
Correlação de infraestrutura
      ↓
DNS / subdomínios / IP / ASN
      ↓
Serviços e fingerprinting
      ↓
PCAP / comportamento de rede
      ↓
IOCs + TTPs
      ↓
Avaliação de confiança
      ↓
Threat Hunting Report
```

## Competências demonstradas

- Threat Hunting
- Cyber Threat Intelligence
- OSINT
- Adversary Infrastructure Mapping
- C2 Analysis
- DNS / SSL-TLS / WHOIS
- PCAP Analysis
- IOC Extraction
- MITRE ATT&CK
- Intelligence Reporting

## Ferramentas do material

- crt.sh
- Censys
- DNSdumpster
- Shodan
- Wireshark

O material também aborda rastreamento de infraestrutura, fingerprinting de C2, análise de tráfego e extração de IOCs.

## Entregáveis

- [Threat Hunting Report](report/THREAT-HUNTING-REPORT.md)
- [Laboratório](laboratory/README.md)
- [IOC Template](report/IOC-TABLE.md)
- [Evidence Register](report/EVIDENCE-REGISTER.md)

## Segurança

Todos os testes devem ocorrer em ambientes próprios, CTFs ou alvos explicitamente autorizados. Não publicar credenciais, tokens, PII ou infraestrutura operacional sensível.

## Status

- [x] Estrutura profissional
- [x] Metodologia
- [x] Template de relatório
- [ ] Execução do laboratório
- [ ] Evidências sanitizadas
- [ ] Relatório final
