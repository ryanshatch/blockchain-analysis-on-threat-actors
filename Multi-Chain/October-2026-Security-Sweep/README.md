<!-- case-visual:start -->
<p align="center">
  <img src="../../assets/readme-headers/multi-chain-october-2026-security-sweep.svg" alt="October 2026 security sweep — New exploit seeds and returned-funds corrections" width="1200">
</p>
<!-- case-visual:end -->

<!-- doc-nav:start -->
<p><a href="../../readme.md">Home</a> · <a href="../../wallets.md">Wallet index</a> · <a href="../../CATALOG.md">All case files</a> · <a href="../README.md">Parent index</a></p>
<!-- doc-nav:end -->

# October 2026 Security Sweep — Initial Reconciliation

**Coverage:** October 1–3, 2026 reports and material recovery updates. **Repository check:** October 5, 2026 UTC. This is a dated intelligence update; balances and operational status can change.

<!-- contents:start -->
<details>
<summary>Contents</summary>
<ul>
<li><a href="#section-new-case-coverage">New Case Coverage</a></li>
<li><a href="#section-key-classification-corrections">Key Classification Corrections</a></li>
<li><a href="#section-attribution-boundaries">Attribution Boundaries</a></li>
<li><a href="#section-sources">Sources</a></li>
<li><a href="#section-tldr">TLDR</a></li>
</ul>
</details>
<!-- contents:end -->

<a id="section-new-case-coverage"></a>
## New Case Coverage

| Submitted report | Canonical case | Dataset treatment |
|---|---|---|
| MALT swap-function exploit | [MALT](../../EVM/Ethereum/MALT/) | One P1 Ethereum attacker seed; victim and vulnerable contract retained as non-threat context |
| FlashLoopAdapter Safe-module exploit | [FlashLoopAdapter](../../EVM/Ethereum/FlashLoopAdapter/) | One P1 attacker seed; two victim Safes and vulnerable third-party adapter explicitly excluded from attacker labeling |
| NEAR Intents October exploit and return | [NEAR-Intents-October-2026](../NEAR-Intents-October-2026/) | Three historical BTC proceeds IoCs, four recovery network records representing three unique non-threat addresses, and one disputed BTC destination withheld |

[addresses.csv](./addresses.csv) contains **14 network/address records**: four threat-labelled historical or direct seeds and ten victim, protocol, or recovery records. These are not 14 attacker wallets.

[incidents.csv](./incidents.csv) contains three current-state incident records. `direct_monitor_count` describes threat or historical-proceeds seeds requiring direct monitoring; it excludes recovery and victim infrastructure.

<a id="section-key-classification-corrections"></a>
## Key Classification Corrections

- **NEAR Intents:** three BTC proceeds wallets move from active holdings to historical returned-funds IoCs. The published recovery destinations are not malicious.
- **Largest NEAR BTC destination:** excluded because complete public representations conflict. A shortened match is not enough to select between full addresses.
- **Lazarus proximity:** not attribution. Dust sent after public disclosure can be permissionless, adversarial, or misleading.
- **FlashLoopAdapter:** third-party adapter exploit, not an Aave V3 core compromise.
- **MALT:** application-specific reserve accounting and external-call ordering flaw; no CVE was identified in the reviewed disclosure.

<a id="section-attribution-boundaries"></a>
## Attribution Boundaries

- Victims, vulnerable contracts, recovery wallets, bridges, routers, exchanges, flash-loan providers, and ordinary counterparties do not inherit attacker labels.
- Historical IoCs remain useful for clustering after funds are returned, but alert severity should distinguish them from wallets still holding stolen assets.
- A complete address is necessary but not sufficient for actor attribution; role and control evidence remain separate fields.

<a id="section-sources"></a>
## Sources

- [MALT SlowMist alert](https://x.com/SlowMist_Team/status/2106418632041668784)
- [FlashLoopAdapter incident registry](https://hacked.slowmist.io/)
- [FlashLoopAdapter reconstruction](https://crypto.news/flashloopadapter-exploit-drains-305k-from-aave-linked-safe-wallets/)
- [Bitquery NEAR Intents investigation](https://www.bitquery.io/investigations/near-intents-hack)
- [NEAR Intents full-return announcement](https://x.com/AlexAuroraDev/status/2106049685928677585)

---

<a id="section-tldr"></a>
## TLDR

This sweep adds two new High-confidence Ethereum attacker seeds, retains three NEAR BTC wallets as returned-funds historical IoCs, explicitly excludes recovery/victim infrastructure, and withholds the unresolved largest NEAR BTC destination.
