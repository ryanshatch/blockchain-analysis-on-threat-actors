# Liquid Network Unauthorized Peg-Out

| Field | Assessment |
|---|---|
| Incident date | September 6, 2026 |
| Attribution and recovery update | September 8, 2026; return occurred September 7 |
| Network path | Liquid / Elements to Bitcoin mainnet |
| Classification | Unauthorized federation-reserve peg-out; reported consensus and asset-validation exploit |
| Primary peg-out | 3,996.01834922 BTC |
| Reported value | Approximately $320 million |
| Partial return | 3,400 BTC to the Liquid Federation reserve |
| Residual holding | Approximately 598.49 BTC at the cited post-return snapshot; not a live balance |
| Confidence | High incident and address linkage; actor identity and whitehat claim unresolved |

## Executive Assessment

On September 6, approximately 3,996.018 BTC was released from the Liquid Federation's Bitcoin reserve in an unauthorized peg-out. Liquid publicly acknowledged that purported white-hat actors had withdrawn approximately 4,000 BTC and paused new transactions while federation members worked to restore normal operation.

GoPlus classified the event as an Elements consensus and asset-validation exploit involving unbacked L-BTC. That technical explanation is retained as security-firm analysis rather than a final protocol post-mortem. The on-chain payout and the destination addresses are independently verifiable at high confidence.

The actors' self-description as whitehat is not independently established. The September 7 partial return strengthens attribution of the consolidation wallet's operational role, but does not establish the actors' identity or permission to retain the remaining funds.

## Direct-Watch Bitcoin Seeds

| Address | Role | Confidence | Treatment |
|---|---|---|---|
| [`bc1ql4mfu6aundtkksxklfajs2h3t9nzcd6gyqjlte`](https://mempool.space/address/bc1ql4mfu6aundtkksxklfajs2h3t9nzcd6gyqjlte) | Primary consolidation, negotiation, partial-return source, and residual proceeds wallet | High incident linkage and operational control; identity unknown | P1 direct watch and graph expansion |
| [`bc1qgslsydz56d0ed6827hdemfmk5w2f6ldyc6wt7p`](https://mempool.space/address/bc1qgslsydz56d0ed6827hdemfmk5w2f6ldyc6wt7p) | Initial unauthorized peg-out recipient and intermediary; received 3,996.01834922 BTC | High flow linkage; attacker ownership unresolved | P2 direct incident-flow watch and historical reconstruction |

Both addresses already existed in this case. This update changes their roles and priorities without adding duplicate wallet records. The initial recipient forwarded 3,995.99999857 BTC to the consolidation wallet in the same block.

**Ownership caveat:** Bitquery describes that forwarding transaction as SideSwap paying its customer. This supports a service-intermediary interpretation of the initial recipient and does not establish common attacker control. It remains directly monitored at P2 for incident flows, with `threat_label=false`. The consolidation wallet remains the P1 attacker-proceeds seed. [Bitquery reconstruction](https://bitquery.io/investigations/liquid-network-hack-4000-btc-op-return)

## September 7 Partial Return

The return transaction spends 15 inputs from the consolidation wallet and sends exactly **3,400 BTC** to Liquid's federation reserve. It also sends **598.49955894 BTC** in change back to the consolidation address. The transaction confirmed in Bitcoin block **965,950** on September 7. The return followed Blockstream's on-chain statement that bridge nodes had been patched, as reconstructed by Bitquery. [Return transaction](https://mempool.space/tx/a6d697a25266ce3c78774fd1d75f896b7af522ada209b0f6228ea497bc49a46d), [Bitquery](https://bitquery.io/investigations/liquid-network-hack-4000-btc-op-return)

The approximately 598.49 BTC residual snapshot was worth roughly $47 million at the reported prices. It is not the result of simply subtracting 3,400 BTC from the principal peg-out: the consolidation wallet also received earlier approximately 2.4975 BTC payouts and other small inflows. Preserve the principal peg-out, returned amount, and wallet balance as separate measures.

The supported role progression is **exploit consolidation → negotiation → partial-return source → residual holding**. No public agreement establishes that the remaining balance is an authorized bounty. The self-described whitehat status remains unverified.

## Transaction Evidence

| Network | Transaction | Event |
|---|---|---|
| Liquid | [`ce4caece413cd9d444ce7ed9f54e5b328b3da5e4af301aff59a3571f76e988f2`](https://blockstream.info/liquid/tx/ce4caece413cd9d444ce7ed9f54e5b328b3da5e4af301aff59a3571f76e988f2) | Liquid-side peg-out transaction encoding 3,996.01834922 L-BTC to the Bitcoin destination |
| Bitcoin | [`8db751a650ae2f12006b7e8c69a75e4df360e8afd6b9e05ae0b9fa6458a7b140`](https://mempool.space/tx/8db751a650ae2f12006b7e8c69a75e4df360e8afd6b9e05ae0b9fa6458a7b140) | Federation payout transaction; primary output paid 3,996.01834922 BTC to the initial recipient |
| Bitcoin | [`85d2ca15bea33a592e73ed40c6a5da887feecf1e77f58ec7f580e00841645043`](https://mempool.space/tx/85d2ca15bea33a592e73ed40c6a5da887feecf1e77f58ec7f580e00841645043) | Immediate forwarding of 3,995.99999857 BTC to the P1 consolidation wallet |
| Bitcoin | [`a6d697a25266ce3c78774fd1d75f896b7af522ada209b0f6228ea497bc49a46d`](https://mempool.space/tx/a6d697a25266ce3c78774fd1d75f896b7af522ada209b0f6228ea497bc49a46d) | September 7 partial return: 3,400 BTC to the federation reserve, with 598.49955894 BTC change back to the consolidation wallet |

The `incident_date` column in `transactions.csv` remains September 6 for case linkage; the return row's notes state its September 7 event date.

## Federation Infrastructure — Do Not Threat-Label

| Address | Role | Handling |
|---|---|---|
| [`bc1qdlld6antmv4xug242ed83q7k4rqw50cwfns38szx4qu2f4jwaxxsuhwxxr`](https://mempool.space/address/bc1qdlld6antmv4xug242ed83q7k4rqw50cwfns38szx4qu2f4jwaxxsuhwxxr) | Liquid Federation reserve, proof-of-reserves address, and 3,400 BTC return destination | Victim/protocol infrastructure; retain for reserve-flow reconstruction only |

Normal peg-outs burn L-BTC and release Bitcoin from the federation reserve to an approved destination. The reserve address is therefore the source of the unauthorized payout, not evidence of attacker control.

## Monitoring Priorities

1. Alert on all spends of residual proceeds from the P1 consolidation address and preserve transaction-level provenance.
2. Track splits, CoinJoin participation, exchanges, swap services, bridges, or return-of-funds transactions.
3. Retain the P2 initial payout intermediary for historical reconstruction and reuse monitoring without assuming attacker ownership.
4. Monitor Liquid's signed on-chain communications and any designated recovery address before classifying later transfers as restitution.
5. Keep the federation reserve, federation members, SideSwap infrastructure, and ordinary peg-out users outside the threat-controlled set unless separately attributed.

## Attribution Boundaries

- No named person or threat group is established.
- The consolidation wallet is a high-confidence attacker-proceeds seed. The initial recipient has high-confidence incident linkage, with a service-custody caveat.
- The word `whitehat` describes the actors' unverified claim, not an attribution conclusion.
- GoPlus's consensus and asset-validation explanation is a technical assessment pending a definitive public post-mortem.
- The Liquid Federation reserve is victim infrastructure and must not inherit the attacker label.
- Other outputs in the batched federation transaction are not automatically incident proceeds.
- Returning funds does not independently verify the whitehat claim or authorize retention of the remaining balance.
- This update introduces no new wallet identifiers. The scan's newly referenced COLDCARD CoinJoin destinations remain excluded because complete identifiers were not published in the supplied reporting.

## Sources

- [Liquid Network — official incident acknowledgement](https://x.com/Liquid_BTC/status/2096696272447218108)
- [GoPlus Security — incident classification and address roles](https://x.com/GoPlusSecurity/status/2096859288585286025)
- [Blockstream Explorer — Liquid-side peg-out transaction](https://blockstream.info/liquid/tx/ce4caece413cd9d444ce7ed9f54e5b328b3da5e4af301aff59a3571f76e988f2)
- [mempool.space — Bitcoin federation payout transaction](https://mempool.space/tx/8db751a650ae2f12006b7e8c69a75e4df360e8afd6b9e05ae0b9fa6458a7b140)
- [mempool.space — September 7 return transaction](https://mempool.space/tx/a6d697a25266ce3c78774fd1d75f896b7af522ada209b0f6228ea497bc49a46d)
- [Bitquery — consolidation, signed communications, and partial-return reconstruction](https://bitquery.io/investigations/liquid-network-hack-4000-btc-op-return)
- [Blockstream Help Center — normal Liquid peg-out mechanics](https://help.blockstream.com/liquid-network/faqs/what-is-a-liquid-peg-out/)
- [Reuters — Liquid response, network halt, and reported value](https://www.reuters.com/technology/bitcoin-based-liquid-network-says-320-million-withdrawn-hack-2026-09-07/)

---

## TLDR

The P1 consolidation wallet `bc1ql4mf...qjlte` returned 3,400 BTC on September 7 and retained approximately 598.49 BTC at the cited snapshot. The initial payout address `bc1qgsls...6wt7p` is a P2 incident-flow intermediary with an ownership caveat. Liquid's reserve remains victim infrastructure. The actors' identity, whitehat claim, and any authorized bounty remain unresolved.
