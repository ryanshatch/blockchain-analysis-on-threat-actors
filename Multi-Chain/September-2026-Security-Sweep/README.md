<!-- case-visual:start -->
<p align="center">
  <img src="../../assets/readme-headers/multi-chain-september-2026-security-sweep.svg" alt="September 2026 security sweep — Case coverage, corrections and new wallet disclosures" width="1200">
</p>
<!-- case-visual:end -->

# September 2026 Security Sweep — Submission Reconciliation

**Coverage:** September 11–25 reports plus reconciliation of the resubmitted September 4–9 findings. **Repository check:** September 28, 2026. This is a dated intelligence update, not a claim that every wallet balance or operational status remains current.

## New Case Coverage

| Submitted report | Canonical case | Dataset treatment |
|---|---|---|
| Bitget exchange wallet backend breach and TRM expansion | [Bitget-September-2026](../Bitget-September-2026/) | Two P1 Ethereum seeds, one P2 provisional proceeds pivot; DPRK/TraderTraitor association Medium and unconfirmed |
| Dominion SILV incident and expanded SOL/ETH wallet alert | [Dominion-SILV](../../SOL/Dominion-SILV/) | Combined into one incident: seven indicators, including the added signer and victim mint; four complete transaction signatures |
| FomoPeek malicious iOS releases | [FomoPeek](../FomoPeek/) | Campaign report, four release records, one primary Ethereum attacker seed, and five proceeds pivots; September 24 attribution update |
| Safe/rsETH auxiliary authorization exploit | [Safe-rsETH-Module](../../EVM/Ethereum/Safe-rsETH-Module/) | Six indicators; original exploiter, MEV actor/bot, proceeds holder, and victim infrastructure separated |
| KREMLIN / REF9334 | [KREMLIN-REF9334](../../EVM/Ethereum/KREMLIN-REF9334/) | One operator wallet, three malicious contracts, and four non-attributed financial pivots |
| Fetch.ai / NuNet / SingularityNET | [Fetch-NuNet-SingularityNET](../Fetch-NuNet-SingularityNET/) | Two P1 Ethereum seeds, two victim/compromised infrastructure records, and two transaction hashes |
| ether.fi AtomicQueue, previously withheld | [Etherfi-AtomicQueue](../../EVM/Ethereum/Etherfi-AtomicQueue/) | Complete attacker address and transaction now resolved; one P1 seed and one victim queue |

[addresses.csv](./addresses.csv) mirrors the seven address-bearing canonical cases: **36 distinct network/address records**, of which **16 have a threat label**, **nine further records are directly monitored for incident proceeds/MEV roles without that label**, and **eleven are contextual only**. These are not 33 attacker wallets. Malicious contracts and the inserted signer are also separate indicator classes.

[incidents.csv](./incidents.csv) contains seven cases, including the updated FomoPeek campaign. `direct_monitor_count` includes directly monitored proceeds and infrastructure; `threat_indicator_count` counts `threat_label=true`. Neither count represents identified people or independently proved common ownership. Canonical and sweep rows are intentional mirrors, deduplicated by case, network, and full address when combined.

## Reports Already Present — Preserved Without Duplicate Ingestion

| Resubmitted finding | Existing canonical coverage | Preserved boundary |
|---|---|---|
| Liquid initial unauthorized peg-out | [Liquid-Network-Peg-Out](../Liquid-Network-Peg-Out/) | 3,996.01834922 BTC initial payout; reserve is victim infrastructure |
| Liquid consolidation and September 7 return correction | [Liquid correction and transaction dataset](../Liquid-Network-Peg-Out/transactions.csv) | Consolidation wallet remains P1; initial payout intermediary remains P2; 3,400 BTC return and dated residual balance retained |
| RedSonic / Reddio | [RedSonic](../../EVM/Ethereum/RedSonic/) | One P1 exploiter, exact attack transaction, two victim contract exclusions |
| Suspected GoMining-linked drain | [Suspected-GoMining-Drain](../../EVM/Ethereum/Suspected-GoMining-Drain/) | P2 proceeds seed; ecosystem association remains Medium/provisional |
| COLDCARD Wave 3 CoinJoin activity | [Coldcard-Weak-Entropy-Theft](../Coldcard-Weak-Entropy-Theft/) | September 5/6 15.48-BTC and 61.12-BTC paths documented; 6.34-BTC vault cause remains open; no guessed new address |
| Dream Health Chain | [Dream-Health-Chain](../../EVM/BNB-Chain/Dream-Health-Chain/) | Two High-confidence BNB Chain indicators; P3 cross-chain intelligence |
| Nesa / Cosmos EVM | [Nesa-Cosmos-EVM](../Nesa-Cosmos-EVM/) | High P1 bridge recipient, Medium P2 liquidation wallet, exact NES bridge receipt |
| Xinbi Guarantee OFAC set | [Xinbi-Guarantee](../../TRON/Xinbi-Guarantee/) | All 52 official TRON addresses already present; no inferred ten-wallet freeze subset |
| Nomic / Osmosis nBTC disclosure | [Earlier sweep incidents](../August-2026-Security-Sweep/incidents.csv) | Zero-seed review; no reconstructed attacker address |

The newer Liquid evidence is more conservative than the resubmitted phrase “intermediate attacker-controlled address.” The existing [Bitquery-backed case](../Liquid-Network-Peg-Out/) identifies a SideSwap service interpretation for the initial recipient. It remains `threat_label=false`, P2 incident-flow monitoring. The primary consolidation wallet remains the P1 threat seed. This update does not regress that distinction or infer an authorized bounty from the partial return.

## Reviewed Exclusions and Scope

- **ether.fi AtomicQueue correction:** the submitted truncated-only exclusion is superseded. September 22 inspection resolves the full attacker from the linked explorer, corroborating security-firm alerts, and a successful Blockscout transaction with the same initiator. The [dedicated case](../../EVM/Ethereum/Etherfi-AtomicQueue/) records one P1 seed; the victim queue remains non-threatening context and a truncated exploit contract remains withheld.
- **Bitget:** the submitted third Ethereum identifier remains P2 and without an attacker label because its direct edge from the main collector has not been independently corroborated. Official Bitget reporting says cold wallets were unaffected; suspected DPRK/TraderTraitor links remain provisional. No truncated Duelbits or unpublished Bitget BTC/XRP addresses are ingested.
- **OFAC September 10:** the reviewed Iran/counterterrorism action does not supply a digital-currency address set for this update. It is kept separate from the already ingested September 9 Xinbi disclosure. [Official action](https://ofac.treasury.gov/recent-actions/20260910)
- FomoPeek is distinct from August's disputed FOMO allegation. Salus now supplies six complete Ethereum identifiers and approximately 579,900 USDT in attributed proceeds; no additional wallet, CVE mapping, or victim count is inferred.
- The submitted “no newer qualifying disclosure” statements describe their respective historical scans, including the September 21 Solana cutoff. They are not presented as an exhaustive negative search through September 24.
- No new BTC records are needed for this batch; the repeated Liquid and COLDCARD material is already covered. Network-specific monitoring does not transfer threat labels to bridges, exchanges, ordinary counterparties, or recovery infrastructure.

## Source and Classification Corrections

Dominion's on-chain history predates the claimed one-day launch interval. The Safe pool had a zero hook, while the defect lay in auxiliary authorization. Fetch/SingularityNET mint quantities and nominal holdings differ by source scope and observation time. Each canonical report preserves these qualifications and links its supporting source evidence.
