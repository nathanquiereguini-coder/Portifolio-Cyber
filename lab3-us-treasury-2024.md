**TLP:CLEAR** — Documento elaborado com base em fontes públicas (OSINT).

# Relatório de Inteligência de Ameaças
## Comprometimento do U.S. Department of the Treasury via cadeia de suprimentos (dezembro de 2024)

| Campo | Detalhe |
|---|---|
| **Data do relatório** | 2026 (reconstrução analítica) |
| **Data do incidente** | Início de dezembro de 2024 (divulgado em 30/12/2024) |
| **Tipo de inteligência** | Estratégica / Operacional |
| **Setor afetado** | Governo / Financeiro (sanções e política econômica) |
| **Ator de ameaça** | APT estatal chinês (não nomeado formalmente pelo Tesouro dos EUA) |
| **TLP** | CLEAR |
| **Fonte original** | Die Welt — [IT-Sicherheit: US-Finanzministerium meldet Cyberattacke aus China](https://www.welt.de/politik/ausland/article255000602/IT-Sicherheit-US-Finanzministerium-meldet-Cyberattacke-aus-China.html) |

---

## 1. Resumo Executivo

Em 30 de dezembro de 2024, o **Departamento do Tesouro dos Estados Unidos** notificou o Congresso sobre um
incidente cibernético classificado como **"major incident"**, no qual um agente de ameaça patrocinado pelo
Estado chinês obteve acesso remoto a estações de trabalho do departamento e a documentos não classificados.
O vetor de acesso inicial não foi uma falha direta no Tesouro, mas sim o comprometimento de uma chave de
API do fornecedor terceirizado **BeyondTrust**, usada para prestação remota de suporte técnico — um caso
típico de **ataque à cadeia de suprimentos (supply chain attack)**.

## 2. Classificação da Fonte e Confiabilidade

| Critério (Código do Almirantado) | Avaliação |
|---|---|
| Confiabilidade da fonte | **A (alfa)** — comunicação oficial do próprio Departamento do Tesouro ao Comitê Bancário do Senado dos EUA, corroborada por CISA, BeyondTrust e múltiplos veículos de imprensa (Reuters, AP, Washington Post, The Hacker News) |
| Credibilidade da informação | **(1) Confirmado por outras fontes** — fato institucionalmente reconhecido, com detalhes técnicos (CVEs) publicamente catalogados |

## 3. Atribuição

- O Departamento do Tesouro atribuiu o ataque a um **agente de ameaça persistente avançada (APT) patrocinado
  pelo governo chinês**, sem nomear publicamente um grupo específico (ex.: não confirmado como APT41,
  Salt Typhoon ou outro cluster nomeado).
- O governo chinês, por meio de sua embaixada em Washington, **negou** qualquer envolvimento, classificando
  as acusações como infundadas.
- **Contexto relevante:** o incidente ocorreu no mesmo período em que atores chineses associados ao cluster
  **Salt Typhoon** comprometiam ao menos nove operadoras de telecomunicações nos EUA, reforçando o padrão de
  campanhas chinesas coordenadas contra infraestrutura crítica e governo americano em 2024.
- **Avaliação de confiança:** ALTA para atribuição de nexo estatal chinês (fonte primária governamental);
  BAIXA para atribuição a um grupo nomeado específico, dado que essa informação não foi tornada pública.

## 4. Detalhes Técnicos do Ataque

| Item | Detalhe |
|---|---|
| Vetor inicial | Comprometimento de chave de API do serviço em nuvem BeyondTrust Remote Support |
| Vulnerabilidades associadas | CVE-2024-12356 (CVSS 9.8 — injeção de comando) e CVE-2024-12686 (CVSS 6.6) |
| Método | Uso da chave de API roubada para redefinir senhas de contas locais e obter acesso remoto não autorizado a estações de trabalho do Tesouro |
| Escopo do acesso | Estações de trabalho do "Departmental Offices" (DO); segundo reportagens, incluiu o Office of Foreign Assets Control (OFAC) e o gabinete da Secretaria do Tesouro |
| Dados afetados | Documentos não classificados; volume estimado em reportagens da imprensa em milhares de arquivos |
| Contenção | BeyondTrust revogou a chave de API e suspendeu as instâncias afetadas no mesmo dia da descoberta; o Tesouro descontinuou o uso do serviço BeyondTrust |

## 5. Modelo Diamante

- **Adversário:** APT patrocinado pelo Estado chinês (não nomeado publicamente)
- **Capacidades:** exploração de falhas de injeção de comando em software de suporte remoto; uso de
  credenciais/chaves de API roubadas para movimentação sem necessidade de malware customizado detectável
- **Infraestrutura:** serviço SaaS legítimo do fornecedor BeyondTrust, abusado como ponto de acesso
- **Vitimologia:** órgãos governamentais dos EUA responsáveis por sanções econômicas e política financeira
  (OFAC, gabinete da Secretaria do Tesouro) — alvo de alto valor para inteligência sobre política de sanções

## 6. Reconstrução da Cadeia de Ataque (Cyber Kill Chain)

| Fase | Descrição observada no incidente |
|---|---|
| 1. Reconnaissance | Identificação do BeyondTrust como fornecedor terceirizado de suporte remoto ao Tesouro (ataque à cadeia de suprimentos) |
| 2. Weaponization | Exploração de CVE-2024-12356/CVE-2024-12686 para comprometer a chave de API do serviço em nuvem |
| 3. Delivery | Acesso direto à infraestrutura SaaS do fornecedor (sem entrega via e-mail/phishing) |
| 4. Exploitation | Uso da chave de API comprometida para redefinir senhas de contas locais |
| 5. Installation | Não identificada implantação de malware; abuso de funcionalidade legítima do software (living-off-the-land em nível de fornecedor) |
| 6. Command & Control | Acesso remoto via o próprio canal legítimo do BeyondTrust Remote Support |
| 7. Actions on Objectives | Acesso e coleta de documentos não classificados em estações de trabalho de escritórios estratégicos do Tesouro |

## 7. Mapeamento MITRE ATT&CK

| Tática | Técnica (ID) |
|---|---|
| Initial Access | Trusted Relationship (T1199) — abuso de fornecedor terceirizado |
| Initial Access | Exploit Public-Facing Application (T1190) — CVEs no BeyondTrust |
| Credential Access | Steal Application Access Token (T1528) — chave de API |
| Persistence | Account Manipulation: Additional Cloud Credentials (T1098) |
| Collection | Data from Local System (T1005) |
| Exfiltration | Exfiltration Over Web Service (T1567) |

## 8. Impacto

- Classificado formalmente como **"major incident"** conforme legislação federal de segurança da informação dos EUA (FISMA).
- Exposição de documentos não classificados de escritórios sensíveis, incluindo o órgão responsável por
  sanções econômicas (OFAC), com potencial valor de inteligência sobre alvos futuros de sanções dos EUA.
- Reforço do escrutínio regulatório sobre dependência de fornecedores terceirizados (SaaS) por agências
  federais, no contexto mais amplo de campanhas chinesas contra o governo e infraestrutura crítica dos EUA em 2024.

## 9. Legislações e Frameworks Aplicáveis (contexto EUA)

- **FISMA** (Federal Information Security Modernization Act) — determina a classificação e notificação de
  "major incidents" ao Congresso.
- **CISA Binding Operational Directives** — diretrizes de resposta e mitigação para agências federais.
- **CVE / KEV Catalog (CISA)** — CVE-2024-12356 foi incluída no catálogo de vulnerabilidades conhecidas
  exploradas (Known Exploited Vulnerabilities), exigindo remediação prioritária por agências federais.

## 10. Recomendações (Course of Action)

| Ação | Descrição |
|---|---|
| **Detect** | Monitoramento de uso anômalo de chaves de API de fornecedores terceirizados (geolocalização, volume, horário) |
| **Deny** | Rotação periódica obrigatória de credenciais/chaves de API de serviços de suporte remoto; least privilege para contas de fornecedores |
| **Disrupt** | Segmentação de acesso de fornecedores terceirizados, sem privilégios administrativos amplos por padrão |
| **Degrade** | Auditoria contínua (SBOM/TPRM) de fornecedores com acesso privilegiado a sistemas governamentais |
| **Deceive** | Uso de credenciais-isca (canary tokens) em integrações de terceiros para detecção precoce de abuso |
| **Destroy** | Plano de resposta a incidentes de cadeia de suprimentos, com capacidade de isolamento imediato de serviços SaaS comprometidos |

## 11. Referências

- Die Welt — IT-Sicherheit: US-Finanzministerium meldet Cyberattacke aus China: https://www.welt.de/politik/ausland/article255000602/IT-Sicherheit-US-Finanzministerium-meldet-Cyberattacke-aus-China.html
- The Hacker News — Chinese APT Exploits BeyondTrust API Key to Access U.S. Treasury Systems and Documents
- Wikipedia — 2024 United States Department of the Treasury hack
- ABC News / Reuters — Treasury Department hit in cyberbreach by China-sponsored actor, officials say
