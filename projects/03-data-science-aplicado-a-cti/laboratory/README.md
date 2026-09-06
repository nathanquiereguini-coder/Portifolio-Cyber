# Laboratory — Data Science aplicado a CTI

## Objetivo

Construir um pipeline seguro para coletar e estruturar informações de reconhecimento de um domínio autorizado.

## Ambiente

Use uma VM/laboratório ou ativos sob sua responsabilidade. Não execute enumeração contra terceiros sem autorização.

## Pipeline sugerido

```text
Input domain
    ↓
WHOIS
    ↓
DNS
    ↓
Subfinder / theHarvester
    ↓
HTTP enrichment
    ↓
Service discovery (quando autorizado)
    ↓
Normalization
    ↓
JSON
    ↓
Correlation / analysis
```

## Checklist

- [ ] Definir intelligence requirement.
- [ ] Escolher domínio de laboratório/autorizado.
- [ ] Registrar data/hora da coleta.
- [ ] Executar WHOIS.
- [ ] Coletar registros DNS relevantes.
- [ ] Enumerar subdomínios com Subfinder.
- [ ] Fazer descoberta OSINT com theHarvester.
- [ ] Enriquecer hosts com httpx quando permitido.
- [ ] Usar Shodan apenas para enriquecimento permitido.
- [ ] Normalizar os resultados.
- [ ] Gerar JSON.
- [ ] Correlacionar domínio, hostname, IP e serviço.
- [ ] Registrar fonte de cada dado.
- [ ] Produzir findings e confidence.

## Exemplo de entrada

```text
example.org
```

Substitua pelo domínio do seu laboratório.

## Exemplo de pipeline

```bash
subfinder -d example.org | httpx -status-code -title -tech-detect -fr -web-server -extract-fqdn
```

Para descoberta de portas, somente em escopo autorizado:

```bash
subfinder -d example.org | naabu -scan-all-ips -top-ports 1000
```

## Output esperado

O objetivo é gerar um artefato estruturado semelhante a:

```json
{
  "domain": "example.org",
  "subdomains": [],
  "dns": [],
  "services": [],
  "sources": []
}
```

Não colocar tokens, API keys ou credenciais no repositório. Use variáveis de ambiente para qualquer integração autenticada.
