**TLP:CLEAR** — Documento elaborado com base em fontes públicas (OSINT).

# Relatório de Inteligência de Ameaças
## Silver Dragon — Campanha de espionagem vinculada ao APT41 contra governos (Europa e Sudeste Asiático)

| Campo | Detalhe |
|---|---|
| **Data do relatório** | 2026 (reconstrução analítica) |
| **Período da campanha** | Desde meados de 2024, com divulgação pública em março de 2026 |
| **Tipo de inteligência** | Operacional / Tática |
| **Setor afetado** | Governo (entidades governamentais na Europa e Sudeste Asiático) |
| **Ator de ameaça** | Silver Dragon (cluster de atividade vinculado ao guarda-chuva APT41) |
| **TLP** | CLEAR |
| **Fonte original** | The Hacker News — [APT41-Linked Silver Dragon Targets Governments Using Cobalt Strike and Google Drive C2](https://thehackernews.com/2026/03/apt41-linked-silver-dragon-targets.html) (baseado em pesquisa da Check Point Research) |

---

## 1. Resumo Executivo

Em março de 2026, a **Check Point Research** divulgou detalhes sobre um cluster de atividade denominado
**Silver Dragon**, ativo desde meados de 2024 contra entidades governamentais de alto perfil na
**Europa** e, principalmente, no **Sudeste Asiático**. O grupo é avaliado como operando dentro do
guarda-chuva do **APT41**, ator de espionagem cibernética vinculado à China e ativo desde ao menos 2012.
Silver Dragon se destaca pelo uso de múltiplas cadeias de infecção (exploração de servidores expostos,
phishing e sequestro de serviços legítimos do Windows) e por abusar de serviços confiáveis como o
**Google Drive** para comunicação de comando e controle (C2), dificultando a detecção por se misturar a
tráfego HTTPS legítimo.

## 2. Classificação da Fonte e Confiabilidade

| Critério (Código do Almirantado) | Avaliação |
|---|---|
| Confiabilidade da fonte | **B (bravo)** — pesquisa técnica publicada por fornecedor de inteligência de ameaças com histórico consistente (Check Point Research), replicada por múltiplos veículos especializados (The Hacker News, SecurityAffairs, SANS ISC) |
| Credibilidade da informação | **(2) Provavelmente verdadeiro** — atribuição ao guarda-chuva APT41 baseada em sobreposição de ferramentas e técnicas (não confirmada judicialmente, mas tecnicamente consistente) |

## 3. Atribuição

- **Cluster:** Silver Dragon
- **Guarda-chuva avaliado:** APT41 (também conhecido por outros codinomes na indústria, ator chinês
  historicamente associado a espionagem e, paralelamente, atividade financeiramente motivada)
- **Base da atribuição (avaliação MÉDIA de confiança):**
  - Sobreposição de táticas em scripts de pós-exploração previamente atribuídos ao APT41.
  - O mecanismo de decriptação usado pelo carregador **BamboLoader** já havia sido observado em
    shellcode loaders associados a atividade de nexo chinês.
  - Padrão de alvos (entidades governamentais) consistente com histórico de espionagem do APT41.
- **Motivação avaliada:** espionagem cibernética estatal, com foco em coleta de inteligência de governos
  no Sudeste Asiático (foco primário) e Europa (atividade secundária).

## 4. Perfil do Ator de Ameaça (Threat Profiling)

| Atributo | Descrição |
|---|---|
| Nome do cluster | Silver Dragon |
| Guarda-chuva | APT41 |
| Origem avaliada | China |
| Ativo desde | Meados de 2024 (divulgação em março de 2026) |
| Alvos primários | Entidades governamentais no Sudeste Asiático |
| Alvos secundários | Entidades governamentais na Europa |
| Ferramentas customizadas | GearDoor (C2 via Google Drive), SSHcmd (utilitário .NET para execução remota via SSH), SliverScreen (captura de tela), BamboLoader (carregador/loader) |
| Ferramentas de terceiros | Cobalt Strike (beacons de pós-exploração) |

## 5. Modelo Diamante

- **Adversário:** Silver Dragon (vinculado ao APT41)
- **Capacidades:** três cadeias de infecção distintas (AppDomain hijacking, service DLL maliciosa e
  phishing com anexos armados); uso de Cobalt Strike para persistência e movimentação lateral; DNS
  tunneling e C2 baseado em serviços de nuvem legítimos (Google Drive) para evasão de detecção
- **Infraestrutura:** servidores públicos vulneráveis explorados para acesso inicial; contas/pastas do
  Google Drive abusadas como canal de C2; serviços legítimos do Windows sequestrados para persistência
- **Vitimologia:** entidades governamentais de alto perfil, majoritariamente no Sudeste Asiático, com
  atividade adicional na Europa

## 6. Reconstrução da Cadeia de Ataque (Cyber Kill Chain)

| Fase | Descrição observada na campanha |
|---|---|
| 1. Reconnaissance | Identificação de servidores públicos vulneráveis e de alvos governamentais para phishing direcionado |
| 2. Weaponization | Preparação de anexos LNK maliciosos ("weaponized LNK attachments") e DLLs maliciosas para sequestro de serviços |
| 3. Delivery | (a) exploração direta de servidores expostos à internet; (b) e-mails de phishing com anexos maliciosos |
| 4. Exploitation | Execução de código via exploração de vulnerabilidade em servidor ou abertura de anexo malicioso pela vítima |
| 5. Installation | Sequestro de serviços legítimos do Windows (service hijacking) e técnica de **AppDomain hijacking** para persistência furtiva, mesclando-se a processos legítimos |
| 6. Command & Control | Beacons Cobalt Strike; comunicação C2 via **GearDoor** abusando do Google Drive; uso de DNS tunneling como canal alternativo |
| 7. Actions on Objectives | Coleta de inteligência (espionagem) via captura de tela (SliverScreen), execução remota de comandos (SSHcmd) e exfiltração através dos mesmos canais de C2 baseados em nuvem |

## 7. Mapeamento MITRE ATT&CK

| Tática | Técnica (ID) |
|---|---|
| Initial Access | Exploit Public-Facing Application (T1190) |
| Initial Access | Phishing: Spearphishing Attachment (T1566.001) |
| Execution | User Execution: Malicious File (T1204.002) |
| Persistence | Hijack Execution Flow (T1574) — inclui AppDomain hijacking e service DLL maliciosa |
| Persistence | Server Software Component (T1505) |
| Command and Control | Web Service (T1102) — abuso do Google Drive |
| Command and Control | DNS (T1071.004) — DNS tunneling |
| Command and Control | Ingress Tool Transfer (T1105) — Cobalt Strike |
| Collection | Screen Capture (T1113) — via SliverScreen |
| Lateral Movement / Execution | Remote Services: SSH (T1021.004) — via SSHcmd |
| Exfiltration | Exfiltration Over Web Service (T1567) |

## 8. Indicadores e Nível de Dor (Pyramid of Pain)

O elemento de maior "dor" para o adversário é o conjunto de **TTPs** — as três cadeias de infecção
combinadas (exploração de servidor, service hijacking e phishing), e especialmente o uso de
**infraestrutura confiável (Google Drive) como canal de C2**, que exige reengenharia significativa da
operação caso seja bloqueado. Ferramentas customizadas (GearDoor, BamboLoader, SliverScreen, SSHcmd) estão
em nível intermediário — mudar de ferramenta é mais custoso que trocar domínios ou hashes, mas ainda
viável para um ator "bem-recursado e adaptável", como descrito pela Check Point.

## 9. Impacto

- Campanha de espionagem **de longa duração** (ativa desde meados de 2024, identificada apenas em 2026),
  o que indica alto grau de furtividade e persistência bem-sucedida em ambientes governamentais.
- Comprometimento potencial de informações sensíveis de política externa e segurança nacional em
  múltiplos países do Sudeste Asiático e da Europa.
- O abuso de serviços de nuvem legítimos (Google Drive) para C2 representa um desafio relevante para
  ferramentas de detecção tradicionais baseadas em reputação de domínio/IP, exigindo abordagens de
  detecção comportamental.

## 10. Recomendações (Course of Action)

| Ação | Descrição |
|---|---|
| **Detect** | Baseline de uso de serviços de nuvem (Google Drive, etc.) por host, com alertas para padrões de acesso incomuns (volume, horário, tipo de arquivo); caça a beacons Cobalt Strike |
| **Deny** | Patch imediato de servidores públicos e serviços expostos; hardening contra AppDomain hijacking e sequestro de serviços do Windows |
| **Disrupt** | Filtragem de DNS para identificar e bloquear padrões de DNS tunneling |
| **Degrade** | Inspeção de tráfego HTTPS para serviços de nuvem autorizados vs. não autorizados (CASB) |
| **Deceive** | Uso de documentos-isca e credenciais-isca em ambientes governamentais de alto valor |
| **Destroy** | Threat hunting periódico por indicadores de comportamento (não apenas IOCs estáticos) associados a Silver Dragon/APT41 |

## 11. Referências

- The Hacker News — APT41-Linked Silver Dragon Targets Governments Using Cobalt Strike and Google Drive C2: https://thehackernews.com/2026/03/apt41-linked-silver-dragon-targets.html
- Check Point Research — Silver Dragon Targets Organizations in Southeast Asia and Europe (2026)
- SecurityAffairs — From phishing to Google Drive C2: Silver Dragon expands APT41 playbook
