**TLP:CLEAR** — Documento elaborado com base em fontes públicas (OSINT).

# Relatório de Inteligência de Ameaças
## FrostyGoop — Sabotagem do sistema de aquecimento em Lviv, Ucrânia (janeiro de 2024)

| Campo | Detalhe |
|---|---|
| **Data do relatório** | 2026 (reconstrução analítica) |
| **Data do incidente** | 22–23 de janeiro de 2024 |
| **Tipo de inteligência** | Operacional / Tática |
| **Setor afetado** | Energia / Aquecimento urbano (distrito de calefação) |
| **Ator de ameaça** | Não atribuído oficialmente por fornecedores; indícios apontam para nexo com a Rússia |
| **TLP** | CLEAR |
| **Fonte original** | Wired — [Russian-linked Cuts Off Heaters In 600 Apartments During Zero Temperatures](https://www.wired.com/story/russia-ukraine-frostygoop-malware-heating-utility/) |

---

## 1. Resumo Executivo

Entre 22 e 23 de janeiro de 2024, um ataque cibernético contra a concessionária municipal de aquecimento
**Lvivteploenergo**, na cidade de Lviv (Ucrânia), interrompeu o fornecimento de aquecimento e água quente
para mais de **600 prédios residenciais** (cerca de 100.000 pessoas), durante temperaturas abaixo de zero.
A empresa de segurança industrial **Dragos** identificou e nomeou o malware utilizado como **FrostyGoop**,
o primeiro malware conhecido capaz de interagir diretamente com dispositivos de controle industrial (ICS)
via protocolo **Modbus TCP**. A recuperação total do serviço levou cerca de **48 horas**.

## 2. Classificação da Fonte e Confiabilidade

| Critério (Código do Almirantado) | Avaliação |
|---|---|
| Confiabilidade da fonte | **B (bravo)** — relatório técnico publicado por empresa especializada em segurança de ICS (Dragos), corroborado por CSSC/SBU (Serviço de Segurança da Ucrânia) e cobertura jornalística independente (Wired, Recorded Future/The Record) |
| Credibilidade da informação | **(1) Confirmado por outras fontes** — múltiplas fontes independentes (Dragos, SBU/CSSC, imprensa) convergem sobre o mesmo incidente |

## 3. Atribuição

- Nenhum fornecedor de inteligência atribuiu formalmente o ataque a um grupo específico nomeado.
- Indícios levantados pela Dragos: conexões observadas a partir de **endereços IP com origem em Moscou**
  antes do incidente, o que reforça (sem confirmar) a hipótese de um nexo russo, consistente com o padrão
  de ataques contra infraestrutura energética ucraniana observado desde 2015 (Sandworm/BlackEnergy,
  Industroyer/Industroyer2).
- **Avaliação de confiança:** BAIXA a MÉDIA para atribuição estatal específica; MÉDIA para nexo geográfico
  (Rússia) com base em telemetria de rede.

## 4. Perfil Técnico da Ameaça

| Atributo | Descrição |
|---|---|
| Nome do malware | FrostyGoop |
| Linguagem | Golang, compilado para Windows |
| Protocolo abusado | Modbus TCP (porta 502) — protocolo ICS sem autenticação nativa |
| Classificação | 9º malware conhecido especificamente voltado a ICS (após Stuxnet, Havex, BlackEnergy2, Industroyer, entre outros) |
| Alvo específico | Controladores ENCO, usados na gestão de aquecimento central, água quente e ventilação |
| Superfície de exposição | Dragos identificou ~46.000 dispositivos com Modbus TCP expostos à internet globalmente |

## 5. Modelo Diamante

- **Adversário:** não nomeado; cluster com suspeita de nexo russo
- **Capacidades:** malware customizado em Golang com comunicação nativa Modbus TCP; capacidade de ler e
  escrever registradores de dispositivos ICS, alterando leituras e enviando comandos não autorizados
- **Infraestrutura:** acesso inicial via vulnerabilidade em roteador MikroTik exposto à internet (explorada
  já em abril de 2023); IPs de conexão rastreados até Moscou
- **Vitimologia:** concessionária municipal de energia/calefação (Lvivteploenergo), setor de infraestrutura
  crítica ucraniana, alvo recorrente de operações de sabotagem desde o início do conflito

## 6. Reconstrução da Cadeia de Ataque (Cyber Kill Chain)

| Fase | Descrição observada no incidente |
|---|---|
| 1. Reconnaissance | Varredura por dispositivos ICS com Modbus TCP exposto à internet |
| 2. Weaponization | Desenvolvimento do FrostyGoop em Go, com arquivo de configuração (`task_test.json`) apontando para o controlador-alvo |
| 3. Delivery | Exploração de vulnerabilidade em roteador MikroTik voltado à internet (acesso inicial em abril/2023) |
| 4. Exploitation | Uso da falha de acesso remoto para pivotar até a rede que hospedava os controladores ENCO |
| 5. Installation | Implantação do FrostyGoop em host Windows com visibilidade sobre a rede Modbus |
| 6. Command & Control | Comunicação direta com controladores via Modbus TCP (porta 502), sem necessidade de C2 tradicional |
| 7. Actions on Objectives | Envio de comandos Modbus não autorizados que corromperam registradores e leituras dos controladores ENCO, causando falha operacional e desligamento do fornecimento de calefação |

## 7. Mapeamento MITRE ATT&CK / ATT&CK for ICS

| Tática | Técnica (ID) |
|---|---|
| Initial Access | Exploit Public-Facing Application (T1190) |
| Execution | Command and Scripting Interpreter (T1059) |
| Command and Control (ICS) | Commonly Used Port (T0885) — Modbus TCP/502 |
| Impact (ICS) | Manipulation of Control (T0831) |
| Impact (ICS) | Denial of Control (T0813) |
| Impact (ICS) | Loss of Availability (T0826) |

## 8. Indicadores e Nível de Dor (Pyramid of Pain)

O elemento de maior "dor" para o adversário nesse caso é a **TTP central**: a capacidade de falar
nativamente o protocolo Modbus para manipular registradores de controladores ICS — algo que exige
conhecimento profundo de engenharia de sistemas industriais e não é trivialmente substituível. Indicadores
como hash do binário e o endereço IP do controlador-alvo têm utilidade tática imediata, mas vida útil curta.

## 9. Impacto

- Mais de **600 prédios** (~100.000 pessoas) sem aquecimento e água quente durante temperaturas
  sub-zero em Lviv.
- Tempo de remediação de aproximadamente **48 horas**.
- Demonstra a viabilidade de ataques a infraestrutura de calefação urbana como vetor de guerra híbrida,
  ampliando o escopo de ICS malware para além da geração/distribuição elétrica tradicional.

## 10. Recomendações (Course of Action)

| Ação | Descrição |
|---|---|
| **Detect** | Monitorar tráfego Modbus TCP anômalo (função codes incomuns, escritas fora de padrão operacional) |
| **Deny** | Eliminar exposição de dispositivos ICS/Modbus diretamente à internet; segmentação IT/OT com firewalls dedicados |
| **Disrupt** | Aplicar patches em roteadores e equipamentos de borda expostos (ex.: MikroTik) assim que disponíveis |
| **Degrade** | Implementar gateways de protocolo com inspeção profunda (deep packet inspection) para Modbus |
| **Deceive** | Uso de honeypots ICS emulando controladores ENCO para detecção precoce de reconhecimento |
| **Destroy** | Planos de contingência operacional manual para sistemas de calefação em caso de perda de controle remoto |

## 11. Referências

- Wired — Russian-Linked Malware Cuts Off Heaters in Ukraine: https://www.wired.com/story/russia-ukraine-frostygoop-malware-heating-utility/
- Dragos — FrostyGoop: Novel ICS Malware Impacting Heating Utility in Kyiv (2024)
- The Record (Recorded Future News) — FrostyGoop malware left 600 Ukrainian households without heat this winter
- SecurityWeek — FrostyGoop ICS Malware Left Ukrainian City's Residents Without Heating
