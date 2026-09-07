# Matriz de Achados, Risco e Validação

| ID | Achado | Evidência mínima | OWASP | Prob. | Impacto | Score | Severidade | Correção | Critério de validação |
|---|---|---|---|---:|---:|---:|---|---|---|
| FND-001 | Controle de acesso quebrado em objetos | Request/response reproduzível + perfil + horário | A01 | 4 | 4 | 16 | Alto | Autorização por objeto no servidor | Recurso de outro usuário retorna 403 e tentativa é registrada |
| FND-002 | [Preencher] | [Preencher] | [Preencher] | | | | | | |

## Regras de avaliação

### Probabilidade

Considere autenticação necessária, exposição, facilidade de descoberta, repetibilidade, automação, PoC/exploit e controles existentes.

### Impacto

Considere dados afetados, escala, confidencialidade, integridade, disponibilidade, efeito financeiro/regulatório, fraude e interrupção operacional.

### Severidade

A pontuação apoia o julgamento, mas não o substitui. O relatório deve explicar por que a classificação é proporcional ao que foi demonstrado.

## Checklist de qualidade

- [ ] O título descreve o problema e o contexto.
- [ ] O ativo está identificado.
- [ ] O pré-requisito de exploração está claro.
- [ ] A evidência é suficiente e reproduzível.
- [ ] PII e segredos foram minimizados/mascarados.
- [ ] O impacto está ligado a uma consequência plausível.
- [ ] OWASP foi usado como taxonomia, não como nota automática.
- [ ] Kill Chain/MITRE só foram mapeados quando sustentados.
- [ ] Probabilidade e impacto foram justificados.
- [ ] A recomendação é acionável.
- [ ] Existe critério objetivo para validar a correção.
