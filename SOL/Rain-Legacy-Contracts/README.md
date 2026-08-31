# Rain Legacy Solana Card-Contract Exploit

| Field | Assessment |
|---|---|
| Incident date | August 28, 2026 |
| Assessment date | August 30, 2026 |
| Network | Solana |
| Infrastructure | Rain legacy Solana card contracts |
| Confirmed affected programs | Avici and Tria |
| Classification | Shared-infrastructure authorization and signature-validation exploit |
| Confirmed victims | 2,321 |
| Reconciled loss | $932,804.22 |
| Broader observed proceeds | Approximately $1.0-$1.1 million |
| Confidence | High |

## Executive Assessment

The August 28 incident is a Rain shared-infrastructure exploit, not an Avici-only breach. Avici reconciled 1,685 affected users and $500,859.22 in unauthorized withdrawals. Tria subsequently confirmed another 636 affected users and $431,945 from Solana card balances. The two program disclosures establish at least 2,321 victims and $932,804.22 in confirmed losses.

Rain said a small number of programs were still using an outdated version of its Solana contracts. It upgraded every program running the vulnerable version, engaged external forensic specialists, and reported no further unauthorized activity after remediation.

The approximately $1.0-$1.1 million observed on-chain is larger than the reconciled Avici and Tria total by roughly $67,000-$167,000. That difference may reflect another affected program, valuation timing, or differences in proceeds accounting. It is unresolved and must not be assigned to a third victim without confirmation.

## Confirmed Program Impact

| Program | Affected users | Reconciled unauthorized withdrawals | Recovery |
|---|---:|---:|---|
| Avici | 1,685 | $500,859.22 | Full balance restoration plus 10% additional compensation |
| Tria | 636 | $431,945.00 | Full balance restoration plus 10% additional compensation |
| **Confirmed combined** | **2,321** | **$932,804.22** | Both programs report completed make-whole payments plus 10% |

The affected assets were card balances already transferred into Rain-powered Solana contracts. Avici and Tria both said their users' ordinary self-custodial wallets were not compromised.

## Direct Attacker Seed

| Network | Address | Role | Confidence | Treatment |
|---|---|---|---|---|
| Solana | [`FVNFzqAny8spWdPmYw6RQ9TkYa29ueFFiqCFD1gQnCEj`](https://solscan.io/account/FVNFzqAny8spWdPmYw6RQ9TkYa29ueFFiqCFD1gQnCEj) | Principal drainer and proceeds-consolidation wallet | High | P1 direct watch |

Earlier reporting exposed this wallet only as `FVNFzq...CEj`. The Defiant and a transaction-level Solana reconstruction later published the complete address. The dataset retains that published full form; it was not reconstructed from the truncated identifier.

## Exploit Mechanics

Public transaction analysis describes a repeated three-stage pattern:

1. The attacker invoked the authorization program's signature-submission path alongside Solana's Ed25519 signature-verification program.
2. The attacker used the resulting authorization state to add itself as an administrator on individual card-collateral accounts.
3. The attacker called the collateral-withdrawal path and moved user balances into attacker-controlled token accounts.

This supports an authorization or signature-validation flaw in shared card-contract infrastructure. It does not support a Solana consensus failure, compromise of users' private keys, or an Avici- or Tria-specific wallet exploit.

## Response and Recovery

- Rain upgraded every program using the vulnerable contract version.
- Rain engaged third-party forensic investigators and said it would cooperate with law enforcement and regulators.
- Rain reported no further related unauthorized activity after the upgrades.
- Avici and Tria each reported full reimbursement of affected balances plus an additional 10%.
- Avici filed a report with the FBI's Internet Crime Complaint Center.

Refunds reduce the final customer loss but do not change the gross amount removed by the attacker.

## Monitoring Priorities

1. Watch the full Solana drainer for reuse, residual token accounts, fresh funding, swaps, consolidation, bridges, and exchange deposits.
2. Preserve Rain contract addresses and affected collateral accounts as infrastructure or victim context, not attacker wallets.
3. Reconcile the approximately $67,000-$167,000 difference between the two confirmed program totals and broader on-chain estimates.
4. Monitor for Rain's final forensic report, additional affected-program disclosures, and any law-enforcement recovery action.
5. Keep Solana DEX, deBridge, exchange, and market-maker counterparties outside the actor cluster unless independent evidence supports control.

## Attribution Boundaries

- No named attacker or real-world identity is established.
- The full principal drainer is a direct incident seed; its ordinary counterparties do not inherit that label.
- Rain is the vulnerable infrastructure provider, while Avici and Tria are confirmed affected integrations.
- User card-collateral accounts are victims, not attacker-controlled wallets.
- The $932,804.22 figure is the confirmed program-level loss. The approximately $1.0-$1.1 million on-chain estimate remains a separate, unresolved measure.
- Refund and 10% compensation amounts are recovery costs, not additional attacker proceeds.

## Sources

- [Rain — vulnerable legacy Solana-contract versions upgraded across affected programs](https://x.com/raincards/status/2093435073081053518)
- [Rain — impacted cardholders repaid](https://x.com/raincards/status/2093781877295653267)
- [Avici — 1,685 users and $500,859.22 reconciled](https://x.com/avici/status/2093439613201482068)
- [Avici — full refunds and 10% additional compensation](https://x.com/avici/status/2093745374683082767)
- [Tria — 636 users and $431,945 reconciled](https://x.com/useTria/status/2093651836079116392)
- [Tria — completed refunds plus 10%](https://x.com/useTria/status/2093775283799327079)
- [FinanceFeeds — combined Tria and Avici impact](https://financefeeds.com/tria-and-avici-report-2321-users-hit-by-rain-solana-card-vulnerability/)
- [The Defiant — complete drainer address and transaction-level exploit mechanics](https://thedefiant.io/news/hacks/attacker-drains-more-than-usd1-million-from-avici-users-in-live-solana-neobank-attack)
- [SolScanner — complete drainer address and on-chain reconstruction](https://www.solscanner.app/blog/inside-the-avici-exploit)

---

## TLDR

The August 28 drain affected at least two Rain-powered Solana card programs: Avici and Tria. Together they confirmed 2,321 affected users and $932,804.22 in unauthorized withdrawals, with both reporting full refunds plus 10%. The complete principal drainer is now publicly available as `FVNFzqAny8spWdPmYw6RQ9TkYa29ueFFiqCFD1gQnCEj`; Rain contracts, victim accounts, DEXs, bridges, and service counterparties remain non-actor infrastructure.
