# Liquid Network Unauthorized Peg-Out

| Field | Assessment |
|---|---|
| Incident date | September 6, 2026 |
| Network path | Liquid / Elements to Bitcoin mainnet |
| Classification | Unauthorized federation-reserve peg-out; reported consensus and asset-validation exploit |
| Primary peg-out | 3,996.01834922 BTC |
| Reported value | Approximately $320 million |
| Confidence | High incident and address linkage; actor identity and whitehat claim unresolved |

## Executive Assessment

On September 6, approximately 3,996.018 BTC was released from the Liquid Federation's Bitcoin reserve in an unauthorized peg-out. Liquid publicly acknowledged that purported white-hat actors had withdrawn approximately 4,000 BTC and paused new transactions while federation members worked to restore normal operation.

GoPlus classified the event as an Elements consensus and asset-validation exploit involving unbacked L-BTC. That technical explanation is retained as security-firm analysis rather than a final protocol post-mortem. The on-chain payout and the destination addresses are independently verifiable at high confidence.

The actors' self-description as whitehat is not independently established. Until funds are returned or Liquid publishes a conclusive attribution, the addresses remain incident-linked exploit-proceeds seeds with unknown real-world ownership.

## Direct-Watch Bitcoin Seeds

| Address | Role | Confidence | Treatment |
|---|---|---|---|
| [`bc1qgslsydz56d0ed6827hdemfmk5w2f6ldyc6wt7p`](https://mempool.space/address/bc1qgslsydz56d0ed6827hdemfmk5w2f6ldyc6wt7p) | Primary unauthorized peg-out destination; received 3,996.01834922 BTC | High | P1 direct watch |
| [`bc1ql4mfu6aundtkksxklfajs2h3t9nzcd6gyqjlte`](https://mempool.space/address/bc1ql4mfu6aundtkksxklfajs2h3t9nzcd6gyqjlte) | Immediate proceeds-consolidation destination; received approximately 3,996 BTC from the primary address in the same block | High flow linkage; medium-high common-control inference | P1 direct watch and graph expansion |

The second address is retained because the primary destination spent essentially the full peg-out output to it immediately. That spend is strong proceeds-path evidence, but it does not establish a named operator or validate the whitehat claim.

## Transaction Evidence

| Network | Transaction | Event |
|---|---|---|
| Liquid | [`ce4caece413cd9d444ce7ed9f54e5b328b3da5e4af301aff59a3571f76e988f2`](https://blockstream.info/liquid/tx/ce4caece413cd9d444ce7ed9f54e5b328b3da5e4af301aff59a3571f76e988f2) | Liquid-side peg-out transaction encoding 3,996.01834922 L-BTC to the Bitcoin destination |
| Bitcoin | [`8db751a650ae2f12006b7e8c69a75e4df360e8afd6b9e05ae0b9fa6458a7b140`](https://mempool.space/tx/8db751a650ae2f12006b7e8c69a75e4df360e8afd6b9e05ae0b9fa6458a7b140) | Federation payout transaction; primary output paid 3,996.01834922 BTC to the first direct-watch seed |
| Bitcoin | [`85d2ca15bea33a592e73ed40c6a5da887feecf1e77f58ec7f580e00841645043`](https://mempool.space/tx/85d2ca15bea33a592e73ed40c6a5da887feecf1e77f58ec7f580e00841645043) | Immediate consolidation of approximately 3,996 BTC to the second direct-watch seed |

## Federation Infrastructure — Do Not Threat-Label

| Address | Role | Handling |
|---|---|---|
| [`bc1qdlld6antmv4xug242ed83q7k4rqw50cwfns38szx4qu2f4jwaxxsuhwxxr`](https://mempool.space/address/bc1qdlld6antmv4xug242ed83q7k4rqw50cwfns38szx4qu2f4jwaxxsuhwxxr) | Liquid Federation reserve and proof-of-reserves address | Victim/protocol infrastructure; retain for reserve-flow reconstruction only |

Normal peg-outs burn L-BTC and release Bitcoin from the federation reserve to an approved destination. The reserve address is therefore the source of the unauthorized payout, not evidence of attacker control.

## Monitoring Priorities

1. Alert on all spends from the immediate consolidation address and preserve transaction-level provenance.
2. Track splits, CoinJoin participation, exchanges, swap services, bridges, or return-of-funds transactions.
3. Retain the primary payout address even after it is emptied because it is the direct federation-reserve destination.
4. Monitor Liquid's signed on-chain communications and any designated recovery address before classifying later transfers as restitution.
5. Keep the federation reserve, federation members, SideSwap infrastructure, and ordinary peg-out users outside the threat-controlled set unless separately attributed.

## Attribution Boundaries

- No named person or threat group is established.
- The primary and immediate consolidation addresses are high-confidence incident-linked proceeds seeds.
- The word `whitehat` describes the actors' unverified claim, not an attribution conclusion.
- GoPlus's consensus and asset-validation explanation is a technical assessment pending a definitive public post-mortem.
- The Liquid Federation reserve is victim infrastructure and must not inherit the attacker label.
- Other outputs in the batched federation transaction are not automatically incident proceeds.

## Sources

- [Liquid Network — official incident acknowledgement](https://x.com/Liquid_BTC/status/2096696272447218108)
- [GoPlus Security — incident classification and address roles](https://x.com/GoPlusSecurity/status/2096859288585286025)
- [Blockstream Explorer — Liquid-side peg-out transaction](https://blockstream.info/liquid/tx/ce4caece413cd9d444ce7ed9f54e5b328b3da5e4af301aff59a3571f76e988f2)
- [mempool.space — Bitcoin federation payout transaction](https://mempool.space/tx/8db751a650ae2f12006b7e8c69a75e4df360e8afd6b9e05ae0b9fa6458a7b140)
- [Blockstream Help Center — normal Liquid peg-out mechanics](https://help.blockstream.com/liquid-network/faqs/what-is-a-liquid-peg-out/)
- [Reuters — Liquid response, network halt, and reported value](https://www.reuters.com/technology/bitcoin-based-liquid-network-says-320-million-withdrawn-hack-2026-09-07/)

---

## TLDR

The September 6 Liquid incident released 3,996.01834922 BTC to `bc1qgsls...6wt7p`, which immediately consolidated essentially the full amount at `bc1ql4mf...qjlte`. Both are direct-watch proceeds seeds. The Liquid Federation reserve is victim infrastructure, and the actors' whitehat claim remains unverified.
