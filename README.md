# Cyber Threat Intelligence — Portfólio de Relatórios

Repositório com relatórios de Cyber Threat Intelligence (CTI) produzidos como exercício prático de
operacionalização do **Ciclo de Inteligência** (Planejamento e Direcionamento → Coleta → Processamento →
Análise → Produção e Disseminação → Feedback), aplicado a incidentes reais de segurança cibernética.

Cada relatório segue uma metodologia consistente, incluindo:

- **Classificação da fonte e da informação** com o [Código do Almirantado](https://en.wikipedia.org/wiki/Admiralty_code) (confiabilidade A–F / credibilidade 1–6)
- **Atribuição** do agente de ameaça, quando aplicável
- **Perfil do ator de ameaça** (Threat Profiling)
- **Mapeamento de TTPs** com o [MITRE ATT&CK](https://attack.mitre.org/)
- **Cyber Kill Chain** (Lockheed Martin) para reconstrução da cadeia de ataque
- **Avaliação de impacto** e **recomendações** acionáveis (Course of Action)
- **Classificação TLP** (Traffic Light Protocol) da informação divulgada

> Estes relatórios foram elaborados a partir de fontes públicas (OSINT) — reportagens, advisories de
> fabricantes de segurança (Dragos, Check Point, Mandiant) e órgãos oficiais — como exercício analítico.
> Não contêm informações privilegiadas ou não divulgadas publicamente.

## Relatórios

| # | Relatório | Setor / Alvo | Ator de Ameaça | Tipo de Inteligência | TLP |
|---|-----------|--------------|-----------------|----------------------|-----|
| 1 | [Ataque à rede elétrica da Ucrânia (2015)](reports/lab1-ukraine-power-grid-2015.md) | Energia / Infraestrutura crítica | Sandworm Team (BlackEnergy3) | Operacional | CLEAR |
| 2 | [FrostyGoop — Sabotagem do aquecimento em Lviv (2024)](reports/lab2-frostygoop-lviv-2024.md) | Energia / Aquecimento urbano | Não atribuído oficialmente (suspeita de nexo russo) | Operacional/Tática | CLEAR |
| 3 | [Comprometimento do U.S. Department of the Treasury (2024)](reports/lab3-us-treasury-2024.md) | Governo / Financeiro | APT vinculado ao Estado chinês (via BeyondTrust) | Estratégica/Operacional | CLEAR |
| 4 | [Silver Dragon (APT41) contra entidades governamentais (2026)](reports/lab4-silver-dragon-apt41-2026.md) | Governo (Europa e Sudeste Asiático) | Silver Dragon (cluster vinculado ao APT41) | Operacional/Tática | CLEAR |

## Metodologia e Frameworks Utilizados

- **Ciclo de Inteligência** — planejamento, coleta, processamento, análise, produção/disseminação e feedback
- **Diamond Model of Intrusion Analysis** — Adversário, Capacidades, Infraestrutura, Vitimologia
- **Cyber Kill Chain** (Lockheed Martin) — 7 fases, do reconhecimento à ação sobre objetivos
- **MITRE ATT&CK Enterprise Matrix** — táticas, técnicas e procedimentos (TTPs)
- **Pyramid of Pain** (David Bianco) — priorização de indicadores por dificuldade de mudança para o adversário
- **Código do Almirantado (NATO)** — avaliação de confiabilidade da fonte e credibilidade da informação
- **TLP v2** — classificação de compartilhamento da informação

## Sobre

Relatórios elaborados como parte de estudos práticos em Cyber Threat Intelligence, inspirados no módulo
*"Operacionalização do Ciclo de Inteligência"* (ADINT School).

**Aviso legal:** todo o conteúdo é baseado exclusivamente em fontes públicas já divulgadas por veículos de
imprensa, empresas de segurança e órgãos governamentais, com fins educacionais e de portfólio profissional.
