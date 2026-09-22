# Safe / rsETH — Auxiliary Authorization Exploit and Yoink Interception

| Field | Assessment |
|---|---|
| Incident | September 15, 2026, Ethereum |
| Classification | Authorization failure in an enabled auxiliary executor/module path |
| Initial extraction | Approximately 2,900 rsETH underlying Aave collateral, valued around $7.7–7.8M in the submitted reports |
| Main holding leg | Approximately 2,882.37 rsETH at the publication snapshot |
| Other initial disposition | Approximately 17.63 rsETH sold for 18.95 ETH |
| Confidence | High for the documented transaction roles; operator identities and recovery intent unresolved |
| Evidence cutoff | September 15 reporting/reconstruction; source checks September 22, 2026 |

The incident affected an unidentified user's Safe through an enabled auxiliary path. The vulnerability is not attributed to Safe's core contracts. [Bitquery's call-trace reconstruction](https://bitquery.io/investigations/rseth-safe-module-drain) corroborates the full identifiers and distinguishes the original exploiter from the Yoink MEV actor that captured the principal proceeds first.

## Separate Actors and Proceeds Roles

| Address | Role | Treatment |
|---|---|---|
| `0x0dC2c5D6b05A317076CF501f7E7be36a5dfe9b66` | Original exploiter EOA | High; P1 direct watch and backward attribution tracing |
| `0xFDe0d1575Ed8E06FBf36256bcdfA1F359281455A` | Yoink MEV frontrunner EOA | High observed role; direct incident-flow watch; not the original exploiter |
| `0xC70f00CD7E461686b04B0E912E309becA8b80ea0` | Yoink-associated holder of the 2,882.37-rsETH leg | High receipt linkage; P1 direct proceeds watch |
| `0x80BF7Db69556D9521c03461978B8fC731DBBD4e4` | Yoink bot contract | Monitor MEV infrastructure and control path; not original attacker infrastructure |

The original attacker prepared the extraction. Yoink observed the opportunity and executed first. This does not establish common control between them, a named Yoink operator, or whether the captured assets would be returned. In [addresses.csv](./addresses.csv), the original exploiter has `threat_label=true`; the MEV EOA, bot, and proceeds holder retain `threat_label=false` with explicit direct-monitoring instructions. That flag withholds the original-threat attribution and does not certify benign conduct.

## Mechanism and Transaction Evidence

The public executor accepted a self-referential authorization path and reached modules that the victim Safe had already enabled. It could consequently initiate asset movement without fresh Safe-owner signatures. The trace reconstructs transfer of 2,900 aEthrsETH, use of a Uniswap v4 pool, Aave unwrapping, and Yoink's rsETH split.

The capture transaction is [`0x0e7680b06cb8a6f86c149d9ba90d98e3d334e7b072dde03909d43fcfd98a8705`](https://etherscan.io/tx/0x0e7680b06cb8a6f86c149d9ba90d98e3d334e7b072dde03909d43fcfd98a8705), block 25,980,525, **04:38:47 UTC**. [transactions.csv](./transactions.csv) records the holding-address leg and distinguishes the economic victim from the immediate token-transfer sender.

The submission referred to malicious pool/hook infrastructure. Bitquery's reconstruction instead finds **the pool's hook field was zero** and distinguishes an ordinary Pool Manager unlock call from a hook. This case therefore records the auxiliary authorization defect without asserting a custom malicious-hook vulnerability or a defect in Uniswap or Aave.

The 2,900-rsETH figure covers the initial capture transaction. Bitquery also reports later liquidation and copycat activity; it should not be treated as a reconciled total for every subsequent drain through the same path.

## Victim Infrastructure — No Threat Label

| Address | Role |
|---|---|
| `0x40E93a52F6Af9fCD3b476aeDADD7FeABD9f7AbA8` | Victim Safe |
| `0x4f0055926c839D1d960a82CBF84E2eE933958ebC` | Flawed public executor / auxiliary protocol infrastructure |

[Kelp DAO reported](https://x.com/KelpDAO/status/2099740756865159562) a 24-hour restriction involving the suspicious rsETH holder. Preserve that dated protocol statement separately from on-chain observations: Bitquery reports no rsETH outflow at its cutoff but does not claim to have located the pause call. Neither statement establishes a permanent freeze, present-day balance, or completed recovery.

Prioritize the original EOA for attribution history and the holding wallet for asset movement. Keep exchanges, liquidity venues, ordinary counterparties, and the victim's other owners outside the attacker set absent further evidence.

## Sources

- [Bitquery — full call trace, linked addresses, and zero-hook correction](https://bitquery.io/investigations/rseth-safe-module-drain)
- [Defimon — initial exploiter and MEV distinction](https://t.me/s/defimon_alerts)
- [Blockaid — incident alert](https://x.com/blockaid_/status/2099732957803999342)
- [Kelp DAO — reported temporary restriction](https://x.com/KelpDAO/status/2099740756865159562)
- [ChainBounty — forensic review and proceeds split](https://community.chainbounty.io/posts/01a0a75e-9ca9-7b1f-b977-da411a9edd2d)
- [Crypto Economy — BlockSec/SlowMist reporting and auxiliary-contract boundary](https://crypto-economy.com/attacker-drains-2900-rseth-from-gnosis-safe-wallet-in-major-ethereum-heist/)
