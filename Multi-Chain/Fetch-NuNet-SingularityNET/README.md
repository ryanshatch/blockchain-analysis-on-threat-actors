# Fetch.ai / NuNet / SingularityNET — Privileged-Key and Bridge Compromise

| Field | Assessment |
|---|---|
| Incident | September 19–20, 2026; scope expansion reported September 20–21 |
| Scope | Ethereum converter and mint activity; broader Cardano and BNB Chain effects |
| Classification | Compromised privileged signing/mint authority; converter drain and unauthorized token issuance |
| Initial FET drain | 8,721,530.40 FET, rounded as reported |
| NuNet mint | Approximately 408.53M NTX delivered to the same recipient |
| Direct seeds | Two High-confidence Ethereum addresses, both P1 |
| Context | One victim converter and one compromised NuNet deployer |
| Confidence | High for the published initiator/recipient cluster; exact initial key-compromise vector unresolved |
| Evidence cutoff | September 19–21 source snapshots; checked September 22, 2026 |

The common Ethereum recipient connects the Fetch.ai drain with NuNet's unauthorized mint and the later SingularityNET ecosystem activity. The convergence supports a shared operational cluster. It does not establish that every affected project used the same private key or suffered the same contract-level defect.

## Direct-Watch Seeds

| Address | Role | Treatment |
|---|---|---|
| `0x1572F2af7696b39c85E3221CDE8EFb640F86c362` | Exploit initiator / attacker EOA | High; P1 direct watch; prioritize initial funding and historical interactions |
| `0x2dcc1085fDCf418B421E45e86e4e54637cc21dfE` | Proceeds and unauthorized-mint recipient | High; P1 direct watch; prioritize liquidation, bridges, exchange exposure, and dispersal |

[SlowMist's alert, reproduced by KuCoin](https://www.kucoin.com/news/insight/FET/6aaf6df162cf370007435a3d), identifies the initiator and recipient in full. [Blockaid's alert](https://x.com/blockaid_/status/2101426221825348095) and [Bitquery's reconstruction](https://bitquery.io/investigations/asi-bridge-counterfeit-supply) support the common recipient and expanded compromise scope. Four role-separated identifiers are in [addresses.csv](./addresses.csv).

SlowMist attributes the Fetch.ai drain to a leaked conversion-authorizer key: `conversionIn()` accepted a valid signature without the `checkLimits(amount)` protection present in `conversionOut()` or an independent source-chain burn/lock proof. Bitquery emphasizes that the privileged signatures were valid. The defensible classification combines key compromise with an insufficiently constrained trust path; it does not describe a forged cryptographic signature or prove an unrelated Safe/consensus vulnerability.

## Initial Transaction Evidence

| UTC, September 19 | Transaction | Observed event |
|---|---|---|
| 20:21:47 | [`0xfe12c63b322d52727c615f3342222138d1563400a9880cebb516a9a162ac69e2`](https://etherscan.io/tx/0xfe12c63b322d52727c615f3342222138d1563400a9880cebb516a9a162ac69e2) | Initiator calls Fetch.ai converter; 8,721,530.40 FET delivered to the proceeds wallet |
| 20:50:11 | [`0xe14442f6171d8a652e79d44336e58c00cdab271bdb69c668493d420e03ee13ab`](https://etherscan.io/tx/0xe14442f6171d8a652e79d44336e58c00cdab271bdb69c668493d420e03ee13ab) | Compromised NuNet authority mints approximately 408.53M NTX to the same wallet |

The interval is about 28 minutes. [transactions.csv](./transactions.csv) retains complete hashes and identifies the NTX mint's null address as an event source, not an attacker. NuNet's direct token `mint()` differs from the Fetch.ai converter withdrawal.

## Expanded Scope and Non-Comparable Estimates

| Source snapshot | Reported measure | Interpretation |
|---|---|---|
| PeckShield, September 20 at 09:21 UTC, reproduced in September 21 reporting | Approximately 260M AGIX and 53.838M WMTx minted, alongside approximately 408.5M NTX and the original FET drain | Published asset quantities for that alert; not a reconciled whole-cluster loss |
| Same PeckShield snapshot | Approximately 198.3M AGIX, 649 ETH, and 33.538M WMTx held, nominally valued around $16.77M | Mark-to-market holdings, not realized proceeds or net profit |
| Bitquery, September 20 reconstruction | Approximately 2.31B units minted or drained across five assets, with larger reconstructed AGIX/WMTX scope and additional CGV activity | Mixed-token counts across broader activity; cannot be converted into dollar theft by summing units |

The figures are retained with source and cutoff rather than silently substituted for one another. Thin liquidity and extreme price changes make nominal token holdings especially unreliable as a cash-out measure. Bitquery separately measures sale proceeds; neither the $16.77M holdings snapshot nor the 2.31B unit count should be labeled realized theft profit.

## Victim and Compromised Infrastructure

| Address | Role | Handling |
|---|---|---|
| `0xab424A430CC09864fA1277A38193111705ADF3A3` | Fetch.ai TokenConversionManagerV3 | Victim/abused converter; `threat_label=false` |
| `0x863F13e5B505f1Eb17803b94EC9d3DaF80092165` | NuNet deployer whose mint authority was abused | Compromised victim authority; `threat_label=false` |

A compromised deployer is not automatically an attacker-created wallet, and its pre-incident activity must not inherit the hostile-use label. Bridge agents, exchanges, recovery accounts, and ordinary counterparties also require independent role evidence.

Monitor the initiator backward and the recipient forward. Preserve exact network, asset, event, and custody distinctions when extending into Cardano or BNB Chain. No named person or threat group is established.

## Sources

- [SlowMist alert reproduced verbatim by KuCoin — initiator, recipient, converter, and authorization mechanism](https://www.kucoin.com/news/insight/FET/6aaf6df162cf370007435a3d)
- [Blockaid — initial linked-cluster alert](https://x.com/blockaid_/status/2101426221825348095)
- [PeckShield — expanded mint and holdings snapshot](https://x.com/PeckShieldAlert/status/2101602701251334368)
- [Bitquery — privileged keys, common recipient, expanded supply analysis, and realized-value distinctions](https://bitquery.io/investigations/asi-bridge-counterfeit-supply)
- [The Crypto Times, September 20 — full initial transaction trail](https://www.cryptotimes.io/2026/09/20/fetch-ai-and-nunet-hit-by-2m-exploit-ntx-crashes-over-65-in-hours/)
- [The Crypto Times, September 21 — PeckShield snapshot and wider scope](https://www.cryptotimes.io/2026/09/21/singularitynet-bridge-hack-widens-260m-agix-53-8m-wmtx-minted-16-77m-held-by-attacker/)
