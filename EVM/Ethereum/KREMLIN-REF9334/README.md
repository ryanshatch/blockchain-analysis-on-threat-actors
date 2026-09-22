# REF9334 / KREMLIN — Ethereum Operator and Malware Infrastructure

| Field | Assessment |
|---|---|
| Disclosure | September 14, 2026, Elastic Security Labs |
| Campaign | KREMLIN banking malware, tracked as REF9334 |
| Chain role | Ethereum configuration/dead-drop infrastructure and operator financial history |
| Primary target geography | Brazilian banking users |
| Direct indicators | One operator/developer wallet and three malicious configuration contracts |
| Contextual indicators | Four financial counterparties; no campaign-control attribution |
| Confidence | High for contract deployment/administration and malicious-infrastructure linkage |
| Evidence cutoff | Elastic publication; source checks September 22, 2026 |

[Elastic Security Labs](https://www.elastic.co/security-labs/threat-command/malicious-browser-extension-kremlin-banking-malware) links a single Ethereum wallet to contract deployment and configuration updates used by KREMLIN. The first contract explicitly stored the wallet as its administrator. This is an operational-control lead, not merely proximity to an alleged stolen-fund transfer.

## Operator and C2 Identifiers

| Address | Role | Treatment |
|---|---|---|
| `0x5C32A09873be70a92fd8bB5A9fED7967dE06BdE6` | Contract deployer and configuration administrator; assessed campaign developer/operator | High; P1 direct watch and cautious backward financial tracing |
| `0x902EDbFECFF38f285Bf26283fB9cEB3700061873` | Early Ethereum C2/dead-drop resolver | High; P1 infrastructure watch |
| `0x64Def0A6099c4DE9C413B108EAae85A3C7457615` | Successor C2/dead-drop resolver | High; P1 infrastructure watch |
| `0xCD7360A83E5cdbBbbbcEB0e78748babA6740d07b` | Resolver active at publication | High; P1 infrastructure watch; current activity not remeasured |

The contracts store configuration that malware reads to locate payload and command infrastructure. They are malicious infrastructure IOCs, not ordinary stolen-fund wallets. Passive configuration/history analysis can reveal operator changes; this report contains no malware payload or executable retrieval code. The campaign disclosure date is recorded separately from onset: its Ethereum financial history begins earlier, so `incident_date` is blank in the address dataset.

## Financial History and Non-Attributed Counterparties

Elastic observed **82 USDT transfers from June 19, 2025 through August 24, 2026**, with approximately **20,778.97 USDT received** and **19,016.96 USDT sent** by the operator wallet. These transfers predate and overlap infrastructure deployment. Elastic does not establish each transaction as payment for malware development, stolen funds, or revenue.

| Address | Reported relationship | Handling |
|---|---|---|
| `0x8a711333899C173A1DC1a3523335e52Becce9A44` | Approximately 16,347 USDT sent across nine transfers | Graph expansion only |
| `0x1AD4436893850Cc1dA180b2488e764bEB9E2A379` | Approximately 6,267 USDT received | Graph expansion only |
| `0x737A8DeA4Db63B3b24f19698AF9e5Bc6f08DE8EE` | Approximately 6,023 USDT received | Graph expansion only |
| `0x77e2d84e79D65CE84C2dB606E984380A88F4594f` | Approximately 3,015 USDT across 40 transfers, July 22–August 24, 2026 | Graph expansion only |

These counterparties could be exchanges, payment infrastructure, or unrelated parties. [addresses.csv](./addresses.csv) retains them with `threat_label=false` and unknown control attribution. Shared transactions do not make their controllers KREMLIN participants.

## Geographic and Identity Boundaries

At publication, Elastic observed **1,515 systems** checking its canary infrastructure, **98.75% in Brazil**. Those are observed systems, not a financial-loss or wallet-victim count. Portuguese artifacts and transaction times consistent with São Paulo working hours support a plausible geographic hypothesis, not confirmed nationality or operator location.

Despite the campaign name, Elastic found no evidence linking KREMLIN to Russia. No named operator is established. Malware infrastructure, infected endpoints, financial counterparties, and real-world identity remain separate attribution questions.

## Source

- [Elastic Security Labs — original REF9334/KREMLIN analysis, address tables, contract administration, financial history, and attribution limitations](https://www.elastic.co/security-labs/threat-command/malicious-browser-extension-kremlin-banking-malware)
