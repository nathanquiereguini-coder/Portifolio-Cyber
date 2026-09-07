# Notas — Elaboração de Relatório

## 1. Relatório como ponte de decisão

Um relatório de exploração não deve ser uma coleção de screenshots. A função é conectar **prova técnica → contexto → impacto → risco → decisão/correção**.

A evidência isolada mostra que algo ocorreu; a narrativa técnica explica por que isso importa, quais condições foram necessárias e como o achado pode ser corrigido e validado.

## 2. Estrutura mínima

1. Capa;
2. Escopo e metodologia;
3. Resumo executivo;
4. Achados técnicos;
5. Evidências;
6. Impacto e risco;
7. Recomendações;
8. Critérios de validação.

O documento deve servir a públicos diferentes: diretoria, gestão técnica, equipe de correção e auditoria.

## 3. Escopo e metodologia

Registrar explicitamente:

- período do teste;
- aplicações/URLs avaliadas;
- perfis e credenciais utilizadas, sem expor segredos;
- limitações e exclusões;
- regras de engajamento;
- testes destrutivos ou de negação de serviço não realizados, quando aplicável.

Um escopo claro evita interpretar o relatório como uma garantia total de segurança.

## 4. Resumo executivo

Responder de forma orientada à decisão:

- qual sistema foi avaliado;
- qual o principal risco;
- quais dados/processos podem ser impactados;
- quais achados exigem prioridade;
- quais dependências existem para correção.

Evitar jargão sem explicação, listas de CVEs sem contexto e afirmações absolutas.

## 5. OWASP Top 10

OWASP funciona como **taxonomia da falha técnica**. No caso-base do módulo, um IDOR é associado a **A01 — Broken Access Control**.

A categoria não determina automaticamente a severidade. A prioridade depende de pré-requisitos, exploração, escala e impacto no negócio.

## 6. Cyber Kill Chain

Usar como linha temporal para explicar onde um achado favorece a progressão do ataque. Não é necessário forçar todas as fases se a evidência não sustentar isso.

## 7. MITRE ATT&CK

Mapear comportamento observável somente quando a evidência sustenta a relação e quando o mapeamento ajuda a detectar ou mitigar.

Exemplo conceitual do módulo: sessão válida + enumeração de objetos → comportamento associado a conta válida/descoberta/coleta, conforme telemetria disponível.

## 8. Evidência

A evidência mínima deve permitir entender e reproduzir o comportamento:

- requisição;
- resposta;
- perfil utilizado;
- ambiente;
- horário;
- resultado esperado;
- resultado observado.

Usar o **mínimo de dados sensíveis necessário** e mascarar PII quando possível.

## 9. Reprodução

O passo a passo existe para validação técnica controlada, não para fornecer exploração ofensiva gratuita. Ferramentas como Burp Suite, curl ou Postman são meios; a vulnerabilidade está na lógica do sistema.

## 10. Severidade

### Informativo
Contexto, hardening ou redução de superfície sem exploração direta ou impacto material demonstrado.

### Baixo
Impacto limitado, exploração restrita ou dependência de condições específicas.

### Médio
Impacto real com contenções importantes, como exposição parcial ou necessidade de interação adicional.

### Alto
Exploração prática e repetível com impacto relevante, como exposição significativa de dados ou bypass de autorização em função sensível.

### Crítico
Impacto máximo ou cadeia ampla, como RCE sem autenticação, bypass total de autenticação, acesso administrativo indevido ou exfiltração massiva com baixo pré-requisito.

## 11. Probabilidade × Impacto

Pontuação = **Probabilidade × Impacto**, em escala 1–5.

Probabilidade considera, entre outros fatores:
- autenticação necessária;
- exposição;
- repetibilidade/automação;
- facilidade de descoberta;
- controles existentes.

Impacto considera:
- dados afetados;
- escala de usuários;
- efeito financeiro/regulatório;
- confidencialidade, integridade e disponibilidade;
- interrupção operacional.

Exemplo do módulo: **4 × 4 = 16 → Alto**.

## 12. Anatomia de um achado

Um bom achado contém:

**Título → ativo → condição → evidência → impacto → severidade → recomendação → validação.**

O título deve descrever o problema e seu contexto, e não apenas declarar “vulnerabilidade crítica”.

## 13. Correção acionável

Uma recomendação útil informa:

- onde corrigir;
- qual regra deve ser aplicada;
- qual comportamento deve ser esperado;
- quais logs/controles devem existir;
- como validar que a correção funcionou.

## Regra de ouro

> **Prova técnica sem narrativa vira ruído. Narrativa sem prova vira opinião.**

O objetivo final do relatório é permitir **decidir, corrigir, validar e reduzir risco** de forma objetiva.
