# COLDCARD Weak-Entropy Theft — Cross-Chain Laundering Update

| Field | Assessment |
|---|---|
| Theft window | July 30-August 3, 2026 |
| Assessment date | September 4, 2026 |
| Networks | Bitcoin to Ethereum through THORChain |
| Classification | Hardware-wallet weak-entropy theft with cross-chain laundering |
| Bitquery tracked impact | 1,789.28 BTC from 8,865 victim addresses |
| Prior broader estimate | Approximately 1,816 BTC / $116 million |
| Newly public Ethereum destinations | Three |
| Confirmed Bitcoin seeds retained | Six |
| Confidence | High for incident linkage; unresolved actor identity and cross-wave clustering |

## Executive Assessment

The 2026 COLDCARD theft has shifted from a predominantly Bitcoin custody and cash-out investigation into an active Bitcoin-to-Ethereum laundering graph. Bitquery traced 20.69 BTC through 36 THORChain swaps to three complete Ethereum destinations. Each swap's Bitcoin-side THORChain memo encoded the destination Ethereum address, making the cross-chain linkage protocol-level evidence rather than a behavioral-clustering inference.

The primary destination received theft-linked value equivalent to approximately 20.15 BTC across 26 swaps. A second September destination received approximately 0.30 BTC across eight swaps. A third address received approximately 0.24 BTC across two August 2 swaps and is now resolvable in full.

This update does not establish a real-world attacker identity or one operator across all theft waves. Bitquery's `CONFIRMED`, `TRACED`, `ATTRIBUTED`, `UNDER REVIEW`, `VENUE`, and `REPORTED` categories must remain distinct. Only the six Bitcoin addresses in its `CONFIRMED` tier are promoted into this case dataset.

## Ethereum Cross-Chain Proceeds

| Address | Role | Observed flow | Confidence | Treatment |
|---|---|---:|---|---|
| [`0x160a7A4c067B084F03400c6980Ac29F73F6782f6`](https://eth.blockscout.com/address/0x160a7A4c067B084F03400c6980Ac29F73F6782f6) | Primary cross-chain proceeds and consolidation wallet | Approximately 20.15 BTC across 26 THORChain swaps | High | P1 direct watch |
| [`0x8B5b650067841ff3bF28fF3EC8ED1eE635e3D200`](https://eth.blockscout.com/address/0x8B5b650067841ff3bF28fF3EC8ED1eE635e3D200) | Secondary September THORChain destination and laundering hop | Approximately 0.30 BTC across eight swaps | High | Direct watch; P2 secondary role |
| [`0x6A08B5B20F23FcFE09f5da506Be59CAD1eC0df06`](https://eth.blockscout.com/address/0x6A08B5B20F23FcFE09f5da506Be59CAD1eC0df06) | Earlier August THORChain destination and historical laundering hop | Approximately 0.24 BTC across two swaps | High | P2 historical graph pivot |

Bitquery recorded approximately 649.5 ETH at the primary address at 16:15 UTC on September 3. A later Blockscout-derived balance reported in follow-up coverage was approximately 644.5 ETH, indicating that downstream movement had begun. Balance and transaction-count observations are time-sensitive.

The secondary and historical destinations are high-confidence incident-linked proceeds addresses. A common flow source does not, by itself, prove that the same individual controlled all three destinations.

## Previously Retained Ethereum Pivot

| Address | Role | Confidence | Treatment |
|---|---|---|---|
| [`0x41B7529a411EeA979a8d468bdEBd36b0ad703268`](https://etherscan.io/address/0x41B7529a411EeA979a8d468bdEBd36b0ad703268) | Earlier incident-linked Ethereum and Tornado Cash laundering pivot | High linkage; medium actor clustering | P2 direct watch; do not treat as the sole COLDCARD attacker |

This previously published pivot remains part of the wider incident graph. It is not merged into the Wave 3 destination cluster without additional control evidence.

## Confirmed Bitcoin Seeds

Bitquery's September 3 tracker lists the following six addresses in its `CONFIRMED` tier, defined as independently corroborated to the exploit.

| Address | Snapshot balance | UTXO status | Treatment |
|---|---:|---|---|
| [`bc1qq85v2c926eg6pgxhwp6q7lf6cnsz80qs3fcu9r`](https://mempool.space/address/bc1qq85v2c926eg6pgxhwp6q7lf6cnsz80qs3fcu9r) | 562.02147793 BTC | None spent | P1 dormant direct-watch seed |
| [`bc1qx76cae2706qd5q576feh7xq8rfcsjpf2htfhe3`](https://mempool.space/address/bc1qx76cae2706qd5q576feh7xq8rfcsjpf2htfhe3) | 398.47576957 BTC | None spent | P1 dormant direct-watch seed |
| [`bc1q8jy96fe5lf8vfugydnte3cguk92gpev7kwtp3q`](https://mempool.space/address/bc1q8jy96fe5lf8vfugydnte3cguk92gpev7kwtp3q) | 89.62329890 BTC | None spent | P1 dormant direct-watch seed |
| [`bc1qtfrwa4j6rmj9rsgspv6a0yjumkg39js2numu75`](https://mempool.space/address/bc1qtfrwa4j6rmj9rsgspv6a0yjumkg39js2numu75) | 45.90254994 BTC | None spent | P1 dormant direct-watch seed |
| [`bc1qnk4zh9qcnap2mycp56qjrgza3cc8ylrh8fecp0`](https://mempool.space/address/bc1qnk4zh9qcnap2mycp56qjrgza3cc8ylrh8fecp0) | 32.45061090 BTC | 341 spent | P1 direct watch and spend-path expansion |
| [`bc1qmd5m5ktv7m5ffujxv4248fxv36myvdx79n8jp6`](https://mempool.space/address/bc1qmd5m5ktv7m5ffujxv4248fxv36myvdx79n8jp6) | 0.00002000 BTC | 93 spent | P2 historical direct-watch pivot |

Balances and spend counts reflect Bitquery's September 3 snapshot and will change if funds move. The first four dormant addresses are the highest-priority Bitcoin alerts because they retained approximately 1,096 BTC combined at that snapshot.

## Cross-Chain Flow

```text
Confirmed and traced COLDCARD Bitcoin cluster
→ Wave 3 Bitcoin staging addresses
→ 36 THORChain swaps
→ 0x160a...82f6 — approximately 20.15 BTC of traced value
→ 0x8B5b...D200 — approximately 0.30 BTC

Earlier August path
→ two THORChain swaps
→ 0x6A08...df06 — approximately 0.24 BTC
```

THORChain routers, liquidity providers, vaults, nodes, relayers, and ordinary users remain cross-chain infrastructure or counterparties. They do not inherit the attacker label from the traced flow.

## Monitoring Priorities

1. Alert immediately on outbound activity from `0x160a...82f6` and the four dormant high-balance Bitcoin seeds.
2. Track DEX swaps, bridges, privacy protocols, exchange deposits, and new consolidation addresses downstream of the three Ethereum destinations.
3. Preserve THORChain memo data and Bitcoin transaction identifiers when correlating cross-chain transfers.
4. Expand spends from `bc1qnk4...fecp0` and `bc1qmd5...8jp6` without automatically promoting every downstream address to confirmed status.
5. Keep `CONFIRMED`, `TRACED`, `ATTRIBUTED`, `UNDER REVIEW`, `VENUE`, and `REPORTED` tiers separate in exports and alerting logic.
6. Do not merge the four reported theft waves into one operator cluster absent stronger wallet-control or off-chain evidence.

## Attribution Boundaries

- No named person or threat group is established.
- The three new Ethereum addresses are high-confidence proceeds destinations because THORChain memos directly name them.
- Incident linkage does not prove that the same individual controlled every Ethereum destination or every COLDCARD theft wave.
- Only Bitquery's six `CONFIRMED` Bitcoin addresses are promoted here. Its larger `TRACED`, `REPORTED`, and `UNDER REVIEW` sets remain graph or investigative context.
- Exchange and service endpoints are custody or cash-out pivots, not attacker-controlled wallets by association.
- The Bitquery tracked total of 1,789.28 BTC and the earlier approximately 1,816 BTC estimate reflect different source scopes and are not forced into one number.

## Official-Source Scan Boundary

OFAC's September 3 action covered Cuba designations and a Russia-related removal; its September 2 action covered Venezuela licenses and blocked-property reporting. Neither action published new BTC, ETH, or SOL identifiers. No newer qualifying FBI or DOJ full-address disclosure or additional Solana attacker wallet was identified for this update.

## Sources

- [Bitquery — live COLDCARD tracker, address tiers, cross-chain memo linkage, and September 3 snapshot](https://bitquery.io/coldcard-hack/)
- [TRM Labs — COLDCARD weak-entropy exploit analysis and broader loss estimate](https://www.trmlabs.com/resources/blog/the-largest-hardware-wallet-exploit-of-2026-inside-the-usd-116-million-coldcard-hack)
- [Alex Thorn — Wave 3 movement through THORChain](https://x.com/intangiblecoins/status/2095297452681158840)
- [CryptoSlate — Bitquery cross-chain update and later Ethereum balance observation](https://cryptoslate.com/parked-coldcard-loot-begins-moving-as-attacker-routes-1-6m-in-stolen-bitcoin-to-ethereum/)
- [OFAC — September 3 Cuba designations and Russia-related removal](https://ofac.treasury.gov/recent-actions/20260903)
- [OFAC — September 2 Venezuela licenses and blocked-property reporting](https://ofac.treasury.gov/recent-actions/20260902)

---

## TLDR

Bitquery resolved three complete Ethereum destinations for 20.69 BTC routed through 36 THORChain swaps from the COLDCARD theft graph. `0x160a...82f6` is the new P1 proceeds and consolidation seed; `0x8B5b...D200` and `0x6A08...df06` are secondary and historical direct-watch pivots. Six independently corroborated Bitcoin addresses are retained in the `CONFIRMED` tier, while Bitquery's larger traced and reported sets remain excluded from direct attribution.
