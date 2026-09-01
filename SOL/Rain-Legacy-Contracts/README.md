# Rain Legacy Solana Card-Contract Exploit

| Field | Assessment |
|---|---|
| Incident date | August 28, 2026 |
| Assessment date | September 1, 2026 |
| Network | Solana |
| Infrastructure | Rain legacy Solana card contracts |
| Confirmed affected programs | Avici and Tria |
| Classification | Shared-infrastructure authorization and signature-validation exploit |
| Confirmed victims | 2,321 |
| Reconciled loss | $932,804.22 |
| Broader attacker proceeds | Approximately $1.02 million |
| Confidence | High |

## Executive Assessment

The August 28 incident is a Rain shared-infrastructure exploit, not an Avici-only breach. Avici reconciled 1,685 affected users and $500,859.22 in unauthorized withdrawals. Tria subsequently confirmed another 636 affected users and $431,945 from Solana card balances. The two program disclosures establish at least 2,321 victims and $932,804.22 in confirmed losses.

Rain said a small number of programs were still using an outdated version of its Solana contracts. It upgraded every program running the vulnerable version, engaged external forensic specialists, and reported no further unauthorized activity after remediation.

The approximately $1.02 million traced through the attacker cluster is larger than the reconciled Avici and Tria total by roughly $87,000. That difference may reflect another affected program, valuation timing, or differences in proceeds accounting. It is unresolved and must not be assigned to a third victim without confirmation.

## Confirmed Program Impact

| Program | Affected users | Reconciled unauthorized withdrawals | Recovery |
|---|---:|---:|---|
| Avici | 1,685 | $500,859.22 | Full balance restoration plus 10% additional compensation |
| Tria | 636 | $431,945.00 | Full balance restoration plus 10% additional compensation |
| **Confirmed combined** | **2,321** | **$932,804.22** | Both programs report completed make-whole payments plus 10% |

The affected assets were card balances already transferred into Rain-powered Solana contracts. Avici and Tria both said their users' ordinary self-custodial wallets were not compromised.

## Direct Attacker and Proceeds Cluster

| Network | Address | Role | Confidence | Treatment |
|---|---|---|---|---|
| Solana | [`FVNFzqAny8spWdPmYw6RQ9TkYa29ueFFiqCFD1gQnCEj`](https://solscan.io/account/FVNFzqAny8spWdPmYw6RQ9TkYa29ueFFiqCFD1gQnCEj) | Principal drainer, collection wallet, and source of the 10,000 SOL proceeds transfer | High | P1 direct watch |
| Solana | [`4kjsW9dPsqzvuhQVP3P23cvZisdoHE5dR8NdD1TMPKKE`](https://solscan.io/account/4kjsW9dPsqzvuhQVP3P23cvZisdoHE5dR8NdD1TMPKKE) | Proceeds and conversion wallet receiving more than $1 million in SOL before USDC swaps | High | P1 direct watch |
| Ethereum | [`0x2cE21E4921d3Eb116526c3651Dac0257657338D5`](https://etherscan.io/address/0x2cE21E4921d3Eb116526c3651Dac0257657338D5) | Cross-chain laundering and proceeds pivot routing Ethereum-side funds toward Tornado Cash | High incident linkage; medium-high control | P1 direct watch with proceeds-role label |

Earlier reporting exposed the principal wallet only as `FVNFzq...CEj`. The Defiant and a transaction-level Solana reconstruction later published the complete address. The dataset retains that published full form; it was not reconstructed from the truncated identifier.

The Defiant independently confirmed that the principal wallet sent exactly 10,000 SOL and was emptied shortly afterward. Transaction-level tracing identifies `4kjs...PKKKE` as the next Solana proceeds wallet, where more than $1 million in SOL was converted into USDC. Onchain Lens traced the broader path through approximately $1.02 million USDC and roughly 418 ETH to the Ethereum-side proceeds address.

The supported monitoring sequence is:

```text
FVNFzq...QnCEj — exploit and collection seed
→ 4kjs...PKKKE — Solana proceeds and conversion seed
→ 0x2cE2...338D5 — Ethereum laundering and proceeds pivot
→ Tornado Cash infrastructure
```

The Tornado Cash contracts are laundering-infrastructure pivots, not attacker-controlled wallets.

## Exploit Mechanics

Public transaction analysis describes a repeated four-call pattern:

1. The attacker invoked the authorization program's signature-submission path alongside Solana's Ed25519 signature-verification program.
2. The attacker used `AddCollateralAdmin` to add itself as an administrator on individual card-collateral accounts.
3. A second `SubmitSignatures` call supplied authorization state for the withdrawal.
4. The attacker called `WithdrawCollateralAsset` and moved user balances into attacker-controlled token accounts.

This supports an authorization or signature-validation flaw in shared card-contract infrastructure. It does not support a Solana consensus failure, compromise of users' private keys, or an Avici- or Tria-specific wallet exploit.

## Response and Recovery

- Rain upgraded every program using the vulnerable contract version.
- Rain engaged third-party forensic investigators and said it would cooperate with law enforcement and regulators.
- Rain reported no further related unauthorized activity after the upgrades.
- Avici and Tria each reported full reimbursement of affected balances plus an additional 10%.
- Avici filed a report with the FBI's Internet Crime Complaint Center.

Refunds reduce the final customer loss but do not change the gross amount removed by the attacker.

## Monitoring Priorities

1. Watch the full three-address cluster for reuse, residual token accounts, fresh funding, swaps, consolidation, bridges, exchange deposits, and mixer routing.
2. Preserve the two Solana roles separately: `FVNFzq...QnCEj` is the exploit and collection seed; `4kjs...PKKKE` is the proceeds and conversion seed.
3. Track `0x2cE2...338D5` as an Ethereum laundering and proceeds pivot without threat-labeling Tornado Cash contracts or ordinary mixer users.
4. Reconcile the roughly $87,000 difference between the confirmed program total and the approximately $1.02 million attacker-proceeds estimate.
5. Monitor for Rain's final forensic report, additional affected-program disclosures, and any law-enforcement recovery action.
6. Keep Rain contracts, victim accounts, DEXs, bridges, exchanges, and market-maker counterparties outside the actor cluster unless independent evidence supports control.

## Attribution Boundaries

- No named attacker or real-world identity is established.
- The principal drainer and downstream Solana proceeds wallet are direct P1 seeds; the Ethereum address is a high-confidence cross-chain laundering and proceeds pivot.
- Rain is the vulnerable infrastructure provider, while Avici and Tria are confirmed affected integrations.
- User card-collateral accounts are victims, not attacker-controlled wallets.
- The $932,804.22 figure is the confirmed program-level loss. The approximately $1.02 million attacker-proceeds estimate remains a separate, unresolved measure.
- Refund and 10% compensation amounts are recovery costs, not additional attacker proceeds.
- Tornado Cash contracts, relayers, DEXs, bridges, exchanges, and ordinary counterparties do not inherit the attacker label.

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
- [inno — next Solana proceeds wallet and transaction sequence](https://x.com/inno_sol/status/2093415789848412448)
- [Onchain Lens — cross-chain USDC, ETH, and Tornado Cash path](https://x.com/OnchainLens/status/2093501494033273339)

---

## TLDR

The August 28 drain affected at least two Rain-powered Solana card programs: Avici and Tria. Together they confirmed 2,321 affected users and $932,804.22 in unauthorized withdrawals, with both reporting full refunds plus 10%. The complete monitoring cluster now contains the Solana exploit seed `FVNFzq...QnCEj`, Solana proceeds wallet `4kjs...PKKKE`, and Ethereum laundering pivot `0x2cE2...338D5`. Rain contracts, victim accounts, DEXs, bridges, exchanges, Tornado Cash infrastructure, and ordinary counterparties remain outside the attacker cluster.
