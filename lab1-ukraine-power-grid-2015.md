**TLP:CLEAR** — Documento elaborado com base em fontes públicas (OSINT).

# Relatório de Inteligência de Ameaças
## Ataque cibernético à rede elétrica de Ivano-Frankivsk, Ucrânia (dezembro de 2015)

| Campo | Detalhe |
|---|---|
| **Data do relatório** | 2026 (reconstrução analítica) |
| **Data do incidente** | 23 de dezembro de 2015 |
| **Tipo de inteligência** | Operacional |
| **Setor afetado** | Energia / Infraestrutura crítica |
| **Ator de ameaça** | Sandworm Team |
| **TLP** | CLEAR |
| **Fonte original** | BBC News — [Hackers caused power cut in western Ukraine – US](https://www.bbc.com/news/technology-35297464) |

---

## 1. Resumo Executivo

Em 23 de dezembro de 2015, cerca de 230.000 consumidores nas regiões de Ivano-Frankivsk e áreas
vizinhas do oeste da Ucrânia ficaram sem energia elétrica por um período de até seis horas, após um
ataque cibernético contra a distribuidora **Prykarpattyaoblenergo** e outras concessionárias regionais.
O incidente é reconhecido como o **primeiro apagão confirmado publicamente causado por um ataque
cibernético a uma rede elétrica**. A responsabilidade foi atribuída ao grupo russo **Sandworm Team**,
com o uso do malware **BlackEnergy3**, entregue via spear-phishing.

## 2. Atribuição

| Critério (Código do Almirantado) | Avaliação |
|---|---|
| Confiabilidade da fonte | **B (bravo)** — geralmente confiável (agências governamentais dos EUA/Ucrânia + empresas de inteligência de ameaças com histórico consistente) |
| Credibilidade da informação | **(2) Provavelmente verdadeiro** — não confirmado judicialmente à época, mas consistente entre múltiplas fontes independentes |

- **Ator:** Sandworm Team (também rastreado como Voodoo Bear / Iron Viking / APT44 em atribuições
  posteriores), avaliado pela comunidade de inteligência como vinculado ao GRU (inteligência militar russa).
- **Base da atribuição:** reutilização de infraestrutura e malware (BlackEnergy) previamente associados ao
  grupo em campanhas contra alvos ucranianos e ocidentais desde 2014; o Serviço de Segurança da Ucrânia
  (SBU) atribuiu publicamente o ataque a atores estatais russos; o Departamento de Segurança Interna dos
  EUA (DHS) corroborou tecnicamente a cadeia de ataque sem, à época, nomear formalmente o autor.
- **Motivação avaliada:** sabotagem de infraestrutura crítica no contexto da guerra híbrida
  Rússia–Ucrânia, com objetivo de demonstrar capacidade ofensiva e gerar efeito psicológico/desestabilizador
  sobre a população civil.

## 3. Perfil do Ator de Ameaça (Threat Profiling)

| Atributo | Descrição |
|---|---|
| Nome | Sandworm Team |
| Origem | Rússia (avaliado como vinculado ao GRU) |
| Atividade conhecida desde | Pelo menos 2009; campanhas contra ICS desde 2014 |
| Setores historicamente visados | Energia, governo, telecomunicações, mídia (Ucrânia, EUA, Europa) |
| Ferramentas associadas | BlackEnergy2/3, KillDisk, Industroyer/Industroyer2 (em campanhas posteriores) |
| Nível de sofisticação | Alto — capacidade de operar contra sistemas de controle industrial (ICS/SCADA) |

## 4. Modelo Diamante

- **Adversário:** Sandworm Team
- **Capacidades:** malware modular (BlackEnergy3), componente destrutivo KillDisk, ferramentas de acesso
  remoto (RAT), conhecimento de protocolos e operação de sistemas SCADA/ICS
- **Infraestrutura:** e-mails de spear-phishing com documentos Microsoft Word maliciosos (macros), servidores
  de comando e controle (C2) associados a campanhas anteriores do grupo
- **Vitimologia:** concessionárias de energia regionais ucranianas (Prykarpattyaoblenergo e outras),
  inseridas no contexto do conflito Rússia–Ucrânia iniciado em 2014

## 5. Reconstrução da Cadeia de Ataque (Cyber Kill Chain)

| Fase | Descrição observada no incidente |
|---|---|
| 1. Reconnaissance | Levantamento prévio sobre funcionários e estrutura das concessionárias de energia |
| 2. Weaponization | Documentos Microsoft Office armados com macros maliciosas para entrega do BlackEnergy3 |
| 3. Delivery | E-mails de spear-phishing direcionados a funcionários administrativos e de TI |
| 4. Exploitation | Execução da macro maliciosa mediante engenharia social ("habilitar conteúdo") |
| 5. Installation | Instalação do BlackEnergy3, estabelecendo persistência e acesso remoto |
| 6. Command & Control | Comunicação com servidores C2 controlados pelo grupo por meses antes da ação destrutiva |
| 7. Actions on Objectives | Abertura remota de disjuntores (breakers) das subestações; uso do KillDisk para apagar
  registros e dificultar a recuperação; ataque de negação de serviço telefônico (flood de ligações) contra a
  central de atendimento, impedindo que clientes reportassem a falta de energia |

## 6. Mapeamento MITRE ATT&CK (retroativo)

| Tática | Técnica (ID) |
|---|---|
| Initial Access | Phishing: Spearphishing Attachment (T1566.001) |
| Execution | User Execution: Malicious File (T1204.002) |
| Persistence | Boot or Logon Autostart Execution (T1547) |
| Command and Control | Application Layer Protocol (T1071) |
| Impact | Data Destruction (T1485) — via KillDisk |
| Impact | Inhibit System Recovery (T1490) |
| Impact | Denial of Service (T1499) — flood telefônico contra call center |

## 7. Indicadores e Nível de Dor (Pyramid of Pain)

O ataque foi identificado majoritariamente por **TTPs** (topo da pirâmide — mais custoso de mudar para o
adversário): uso de spear-phishing corporativo, abuso de macros do Office, movimentação para o ambiente
OT/ICS e manipulação remota de disjuntores. Indicadores de baixo nível (hashes do BlackEnergy3, domínios
de C2) também foram publicados por fornecedores de inteligência, mas têm vida útil curta diante da
capacidade de reengenharia do grupo.

## 8. Impacto

- Aproximadamente **230.000 consumidores** sem energia elétrica por até **6 horas**.
- Primeiro caso publicamente confirmado de apagão causado por ciberataque, tornando-se caso de referência
  mundial em segurança de infraestrutura crítica (ICS/SCADA).
- Impacto reputacional e estratégico: demonstrou viabilidade de ataques cibernéticos com efeito físico
  direto sobre populações civis.

## 9. Recomendações (Course of Action)

| Ação | Descrição |
|---|---|
| **Detect** | Monitoramento de macros do Office e alertas para execução de scripts a partir de anexos de e-mail |
| **Deny** | Desabilitar macros por padrão em documentos originados da internet; segmentação de rede entre TI e OT |
| **Disrupt** | Implementar autenticação multifator e listas de controle de acesso (ACL) rígidas entre redes corporativas e ICS |
| **Degrade** | Uso de honeypots/honeytokens em ambientes OT para desviar e detectar reconhecimento adversário |
| **Deceive** | Redirecionamento de tráfego suspeito para ambientes controlados de análise |
| **Destroy** | Playbooks de resposta a incidentes específicos para ICS, com capacidade de operação manual (fallback) das subestações |

## 10. Referências

- BBC News — Hackers caused power cut in western Ukraine – US: https://www.bbc.com/news/technology-35297464
- SANS ICS / E-ISAC — Analysis of the Cyber Attack on the Ukrainian Power Grid (2016)
- Wikipedia — 2015 Ukraine power grid hack: https://en.wikipedia.org/wiki/2015_Ukraine_power_grid_hack
- Reuters — Cyberattack that crippled Ukrainian power grid was highly coordinated (jan/2016)
