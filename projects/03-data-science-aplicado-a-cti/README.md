# Data Science aplicado a Cyber Threat Intelligence

Projeto de portfólio baseado no **Módulo 06 — Data Science aplicado a CTI**.

## Objetivo

Demonstrar como transformar dados de reconhecimento e infraestrutura em dados estruturados, reproduzíveis e úteis para análise de Cyber Threat Intelligence.

O material trabalha principalmente com:

- reconhecimento ativo e passivo;
- WHOIS e dados de registro de domínio;
- DNS e resolução de nomes;
- coleta de subdomínios;
- Shodan e exposição de serviços;
- theHarvester;
- Subfinder;
- pipelines de ferramentas;
- automação de coleta;
- saída estruturada em JSON.

O conteúdo do curso destaca a necessidade de automatizar a coleta e produzir outputs estruturados para posterior processamento analítico.

## Pergunta de inteligência

> Como estruturar e automatizar dados de reconhecimento de um domínio para permitir correlação, enriquecimento e análise posterior em um fluxo de CTI?

## Fluxo analítico

```text
Domínio
  ↓
WHOIS ───────┐
DNS ─────────┤
Subdomínios ─┤
Shodan ──────┤ → Normalização → JSON → Correlação → Análise CTI
Harvesting ──┤
Serviços ────┘
```

## Estrutura

- `notes.md` — síntese técnica do módulo.
- `report/DATA-INTELLIGENCE-REPORT.md` — modelo de relatório analítico.
- `laboratory/README.md` — laboratório seguro e reproduzível.
- `laboratory/whois_universal.py` — exemplo original de normalização/roteamento de consultas WHOIS, inspirado na lógica apresentada no material.

## Segurança e ética

Os exercícios devem ser executados somente contra ativos próprios, ambientes explicitamente autorizados ou alvos de laboratório/CTF. Não incluir no repositório credenciais, tokens, dados pessoais ou resultados operacionais sensíveis.

## Relação com o material

Este projeto **não é uma cópia do PDF**. É uma organização de estudo e aplicação prática baseada nos conceitos e ferramentas apresentados no módulo.
