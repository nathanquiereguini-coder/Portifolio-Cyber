# Data Intelligence Report — Reconhecimento e Infraestrutura

> Modelo de relatório de portfólio para demonstrar o ciclo **coleta → processamento → análise → inteligência**.

## 1. Executive Summary

**Objetivo:** avaliar um domínio autorizado e transformar dados de WHOIS, DNS, subdomínios e serviços expostos em um conjunto estruturado de evidências para CTI.

**Resultado esperado:** inventário normalizado de infraestrutura, relações entre ativos e indicadores que possam ser utilizados em análises posteriores.

**Escopo:** somente ativos próprios, laboratório ou alvo explicitamente autorizado.

## 2. Intelligence Requirement

> Quais ativos e relações de infraestrutura podem ser identificados a partir de fontes de reconhecimento, e como esses dados podem ser estruturados para apoiar decisões de CTI?

## 3. Hipóteses

- **H1:** diferentes fontes públicas revelam ativos que não aparecem em um inventário inicial.
- **H2:** a correlação entre DNS, subdomínios e serviços expostos permite formar clusters de infraestrutura.
- **H3:** a automação e a normalização em JSON reduzem trabalho manual e facilitam enriquecimentos posteriores.

## 4. Fontes e coleta

| Fonte/Ferramenta | Dado | Finalidade |
|---|---|---|
| WHOIS | registro do domínio | contexto de registro |
| DNS | resolução e registros | relacionamento domínio/IP |
| theHarvester | descoberta OSINT | ampliação da superfície |
| Subfinder | subdomínios | descoberta automatizada |
| Shodan | serviços expostos | enriquecimento de infraestrutura |
| httpx | status/título/tecnologia | validação e fingerprinting web |
| naabu | portas | observação de exposição de serviços |

## 5. Data Processing

### Normalização

Padronizar:

- domínios em minúsculas;
- endereços IP em formato consistente;
- timestamps em UTC quando possível;
- tipos de observação em categorias fixas;
- campos ausentes como `null` em vez de strings arbitrárias.

### Esquema sugerido

```json
{
  "domain": "example.org",
  "whois": {
    "registrar": null,
    "created_at": null,
    "expires_at": null
  },
  "dns": [],
  "subdomains": [],
  "services": [],
  "sources": []
}
```

## 6. Correlation

Relacionar entidades por:

- domínio ↔ subdomínio;
- domínio ↔ IP;
- IP ↔ ASN;
- IP ↔ porta/serviço;
- hostname ↔ certificado;
- ativo ↔ fonte de observação.

Uma relação deve manter sua origem para permitir validação e auditoria posterior.

## 7. Findings

Preencher somente após a execução do laboratório:

1. **Finding F-01:** [descrição baseada em evidência]
2. **Finding F-02:** [descrição baseada em evidência]
3. **Finding F-03:** [descrição baseada em evidência]

Para cada finding registrar:

- evidência;
- fonte;
- data/hora da observação;
- confiabilidade;
- limitações;
- impacto para CTI.

## 8. Intelligence Assessment

**Julgamento principal:** [preencher]

**Confiança:** baixa / moderada / alta

**Justificativa:** [explicar a convergência das evidências e eventuais lacunas]

## 9. Intelligence Gaps

- dados históricos insuficientes;
- registros DNS não observados;
- fontes que exigem autenticação/API;
- mudanças de infraestrutura entre períodos;
- possíveis falsos positivos de atribuição de ativos.

## 10. Recommendations

- manter inventário estruturado de ativos;
- automatizar coleta recorrente dentro do escopo autorizado;
- armazenar timestamp e fonte de cada observação;
- enriquecer IPs/domínios com fontes independentes;
- priorizar achados que tenham impacto operacional claro.

## 11. Reproducibility

Registrar no laboratório:

- data/hora da coleta;
- domínio de teste;
- ferramentas e versões;
- comandos utilizados;
- parâmetros relevantes;
- hashes dos arquivos de evidência, quando aplicável;
- limitações da coleta.

## 12. Conclusion

O valor de Data Science aplicado a CTI está em transformar grandes volumes de observações heterogêneas em dados consistentes, correlacionáveis e auditáveis. O resultado final deve apoiar uma pergunta de inteligência — não apenas produzir uma coleção de outputs de ferramentas.
