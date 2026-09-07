# Laboratório — Elaboração de Relatório

## Objetivo

Produzir um relatório completo a partir de uma vulnerabilidade reproduzida em **ambiente de laboratório autorizado**, demonstrando a passagem de evidência técnica para decisão de risco e correção.

## Cenário sugerido

Utilizar uma aplicação web deliberadamente vulnerável ou um ambiente CTF local, com usuários e dados sintéticos. O caso pode reproduzir conceitualmente um **Broken Access Control/IDOR** sem atingir sistemas reais.

## Fluxo

1. Definir inteligência/objetivo da avaliação;
2. Delimitar escopo, período, perfis e exclusões;
3. Registrar comportamento esperado;
4. Observar comportamento anômalo;
5. Preservar evidência mínima;
6. Descrever reprodução controlada;
7. Avaliar impacto;
8. Calcular Probabilidade × Impacto;
9. Classificar com OWASP;
10. Mapear Kill Chain/MITRE somente quando houver suporte;
11. Elaborar recomendação acionável;
12. Definir teste de validação;
13. Escrever resumo executivo;
14. Registrar limitações e lacunas.

## Entregáveis

- `SECURITY-REPORT-TEMPLATE.md` preenchido;
- matriz de achados atualizada;
- evidências sanitizadas;
- conclusão executiva;
- critério de reteste/regressão.

## Critério de qualidade

Outra pessoa deve conseguir entender **o que aconteceu, por que importa, como foi demonstrado, qual risco representa, o que corrigir e como confirmar a correção** sem depender de explicações informais do avaliador.

## Segurança

Somente ambientes próprios, CTFs ou explicitamente autorizados. Não usar dados pessoais reais, credenciais reais, infraestrutura de terceiros ou testes destrutivos.
