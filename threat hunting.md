# 🔍 Cyber Threat Intelligence Portfolio
### Threat Hunting | Adversary Tracking | Intelligence Production

---

> *"Intelligence is knowing the adversary's intent before they act."*

---

## 👋 About

Cyber Threat Intelligence analyst focused on **proactive threat hunting**, adversary behavior analysis, and the production of actionable intelligence. This portfolio documents my methodology, toolset, and real-world work across the full intelligence lifecycle.

**Areas of focus:**
- Threat hunting hypothesis development and execution
- MITRE ATT&CK-based adversary profiling
- IOC collection, enrichment, and dissemination
- Strategic, tactical, and operational intelligence reporting

---

## 📂 Repository Structure

```
📁 cti-portfolio/
├── 📁 threat-hunting/
│   ├── 📁 hypotheses/        # Hunt hypotheses with MITRE ATT&CK mapping
│   ├── 📁 queries/           # KQL, SPL, YARA, Sigma rules
│   └── 📁 playbooks/         # Step-by-step hunting playbooks
│
├── 📁 reports/
│   ├── 📁 strategic/         # Executive-level threat landscape reports
│   ├── 📁 tactical/          # TTPs and campaign analysis
│   └── 📁 operational/       # IOC-focused, real-time intel
│
├── 📁 iocs/
│   ├── 📁 malware/           # Hashes, YARA rules, malware analysis
│   ├── 📁 phishing/          # Domains, URLs, lure samples (sanitized)
│   └── 📁 infrastructure/    # C2 IPs, ASNs, certificates
│
├── 📁 tools/
│   ├── 📁 osint/             # OSINT scripts and automations
│   ├── 📁 automation/        # Pipeline and enrichment tools
│   └── 📁 parsers/           # Log and IOC parsers
│
└── 📁 resources/             # Templates, methodology docs, references
```

---

## 🎯 Threat Hunting Methodology

My hunting approach is hypothesis-driven and anchored in the **Intelligence-Driven Threat Hunting** model:

```
[Intelligence Input] → [Hypothesis] → [Hunt Plan] → [Execution] → [Findings] → [Detection/Report]
```

1. **Consume** — ingest threat intel feeds, reports, and advisories
2. **Hypothesize** — formulate testable hypotheses based on adversary TTPs
3. **Plan** — define scope, tools, and data sources
4. **Hunt** — execute queries, analyze anomalies, pivot on findings
5. **Document** — produce findings reports and update detections

See [`threat-hunting/playbooks/`](./threat-hunting/playbooks/) for full playbooks.

---

## 📊 Featured Work

| # | Type | Title | MITRE Techniques | Status |
|---|------|-------|-----------------|--------|
| 01 | Hunt Playbook | [Detecting Living-off-the-Land Binaries (LOLBins)](./threat-hunting/playbooks/lolbins-hunting.md) | T1218, T1059 | ✅ Complete |
| 02 | Hunt Hypothesis | [Suspicious PowerShell via Scheduled Tasks](./threat-hunting/hypotheses/powershell-scheduled-tasks.md) | T1053.005, T1059.001 | ✅ Complete |
| 03 | Tactical Report | [APT Campaign TTP Analysis Template](./reports/tactical/ttp-analysis-template.md) | Multiple | 📝 Template |
| 04 | Tool | [IOC Enrichment Script](./tools/automation/ioc-enricher.py) | — | ✅ Complete |

---

## 🧠 Skills & Tooling

**Detection & Hunting**
- KQL (Microsoft Sentinel), SPL (Splunk), YARA, Sigma
- MITRE ATT&CK Navigator, Velociraptor, OSQuery

**Intelligence Platforms**
- MISP, OpenCTI, TAXII/STIX 2.1
- VirusTotal Enterprise, Shodan, Censys

**OSINT & Investigation**
- Maltego, Spiderfoot, theHarvester
- WHOIS, RiskIQ/PassiveDNS, URLScan.io

**Adversary Emulation**
- Atomic Red Team, MITRE Caldera

---

## 📈 Intelligence Production

All reports in this portfolio follow a structured methodology:

| Report Type | Purpose | Audience | Cadence |
|-------------|---------|----------|---------|
| Strategic | Threat landscape, risk outlook | CISO, Board | Monthly |
| Tactical | Campaign TTPs, adversary profiles | SOC Lead, Blue Team | Weekly |
| Operational | Live IOCs, immediate detections | SOC Analysts, L1/L2 | Daily/As-needed |

---

## 🔗 Frameworks & Standards

- [MITRE ATT&CK](https://attack.mitre.org/) — Adversary TTP mapping
- [Diamond Model](https://www.activeresponse.org/the-diamond-model/) — Intrusion analysis
- [Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) — Attack lifecycle
- [Traffic Light Protocol (TLP)](https://www.cisa.gov/tlp) — Information sharing classification
- [STIX 2.1 / TAXII](https://oasis-open.github.io/cti-documentation/) — Structured intel exchange

---

> ⚠️ **Disclaimer:** All IOCs, malware samples, and threat data in this repository are **sanitized, defanged, or fictional** unless explicitly marked otherwise. This content is for educational and professional portfolio purposes only.

---

*Last updated: 2025 | TLP: WHITE*
