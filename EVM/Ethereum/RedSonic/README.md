# RedSonic / Reddio Vault Exploit

| Field | Assessment |
|---|---|
| Incident date | September 5, 2026 |
| Network | Ethereum |
| Classification | Cross-vault asset double counting and flash-loan share-price manipulation |
| Reported loss | Approximately 9.25 ETH |
| Confidence | High incident, transaction, and attacker-address linkage |

## Executive Assessment

RedSonic Vault was exploited for approximately 9.25 ETH through a flash-loan transaction. SlowMist identified the attacker address and described a cross-vault accounting flaw: stETH deposited into one vault was also counted in another vault's total assets, allowing the same underlying collateral to support two sets of shares.

The attacker used flash liquidity to amplify the accounting error, redeemed excess ETH, separately recovered the stETH, and repaid the loan. The address and transaction are suitable for direct defensive monitoring. No named person or group is attributed.

## Direct Threat Seed

| Network | Address | Role | Confidence | Treatment |
|---|---|---|---|---|
| Ethereum | [`0x70f2333d21ed7e7d105f6578227a9a747687982c`](https://etherscan.io/address/0x70f2333d21ed7e7d105f6578227a9a747687982c) | Exploit execution and proceeds wallet | High | P1 direct watch |

## Attack Transaction

| Transaction | Role | Confidence |
|---|---|---|
| [`0xe3cba90e865c6cba950ebce36a52607f51f1fd33cd9fb920c78803f19b57791a`](https://etherscan.io/tx/0xe3cba90e865c6cba950ebce36a52607f51f1fd33cd9fb920c78803f19b57791a) | Primary flash-loan exploit transaction | High |

## Victim Infrastructure — Do Not Threat-Label

| Address | Role | Handling |
|---|---|---|
| [`0x4315990d9eeaffdfafd49958b4851f203fa1126f`](https://etherscan.io/address/0x4315990d9eeaffdfafd49958b4851f203fa1126f) | RedSonic Diamond / victim entry point | Protocol infrastructure; exploit-flow reconstruction only |
| [`0x92ecc5deacb14937867686ca8b85dd8a65b74704`](https://etherscan.io/address/0x92ecc5deacb14937867686ca8b85dd8a65b74704) | Vulnerable vault implementation | Protocol infrastructure; code and call-path analysis only |

These contracts are affected protocol components. They must not inherit the attacker label from their presence in the exploit transaction.

## Monitoring Priorities

1. Watch the attacker address for swaps, bridges, mixers, exchange deposits, and reuse in later exploits.
2. Preserve the full attack trace and internal calls involving both victim contracts.
3. Review deployments, funding, and prior transactions linked to the attacker without automatically labeling counterparties.
4. Track remediation and any recovery transfers separately from attacker proceeds.

## Attribution Boundaries

- No real-world actor or threat group is identified.
- The attacker wallet and exploit transaction are high-confidence incident indicators.
- The Diamond and vault implementation are victim infrastructure, not attacker-controlled addresses.
- Flash-loan providers, DEXs, liquid-staking contracts, and ordinary counterparties remain service infrastructure unless separately attributed.

## Sources

- [SlowMist — RedSonic exploit alert, identifiers, and root-cause analysis](https://x.com/SlowMist_Team/status/2096439593403089077)
- [ExVulSec — independent exploit monitoring](https://x.com/exvulsec)
- [Etherscan — primary exploit transaction](https://etherscan.io/tx/0xe3cba90e865c6cba950ebce36a52607f51f1fd33cd9fb920c78803f19b57791a)
- [Altcoinvest — transaction and address reconstruction](https://altcoinvest.com/redsonic-vault-exploit-drains-9-25-eth-in-ethereum-flash-loan-attack/)

---

## TLDR

RedSonic lost approximately 9.25 ETH through a cross-vault double-counting and flash-loan exploit. `0x70f2...982c` is the direct-watch attacker and proceeds seed; the RedSonic Diamond and vulnerable vault implementation are non-attacker protocol context.
