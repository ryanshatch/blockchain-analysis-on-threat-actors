# August 20, 2026 Crypto Security Sweep

| Field | Details |
|---|---|
| Review cutoff | August 20, 2026 at 2:31 a.m. ET |
| Scope | Protocol exploits, wallet compromises, phishing and drainer campaigns, rug pulls, address poisoning, laundering pivots, and unresolved investigative intelligence |
| Networks | MAYAChain, Bitcoin, Ethereum, BNB Chain, Harmony, and other EVM environments |
| Sources reviewed | SlowMist, CertiK, TRM Labs, BlockSec, SEAL/Security Alliance, GoPlus, Defimon, PeckShield/Specter, Malwarebytes, protocol disclosures, public explorers, and corroborating reporting |
| Latest confirmed protocol incident at cutoff | Maya Protocol, August 18, 2026 |

> SlowMist's live tracker listed Maya Protocol as its newest incident at the review cutoff. No protocol exploit dated August 19 or August 20 appeared above it. This is a point-in-time observation, not proof that no undisclosed or later-indexed incident occurred.

## Executive Summary

| Project or target | Incident or report date | Classification | Estimated loss | Confidence |
|---|---|---|---:|---|
| Maya Protocol / MAYAChain | August 18 | Chained protocol accounting and state-management exploit | About $1.7M direct | High |
| Fake AMLBot / AML-checker sites | Reported August 19 | Wallet drainer, brand impersonation, and malicious approvals | Unknown | High campaign; unknown aggregate loss |
| FoxMarket | August 15 | Flash-loan-assisted spot-oracle manipulation | About $118.7K | High |
| Hyperliquid impersonation | August 13 | Google Ads phishing and wallet drain; not a Hyperliquid protocol exploit | About 550,019 USDC | High loss; medium-high attacker attribution |
| Ethereum whale drain | August 12 | Wallet or signing-environment compromise; exact vector unresolved | About $25.6M | High incident; medium root cause |
| Harmony | August 11-12 | Cross-shard receipt and quorum-validation flaw causing unauthorized minting | About $3.2M initial cash-loss estimate; token issuance estimates remain disputed | High |
| ODY / Odyssey / Ody DeFi | July 28; highlighted August 11-13 | Privileged mint, market dump, liquidity extraction, and exit scam | About $15M-$15.67M USDT | Medium-high |
| Coldcard | July 30 onward | Weak seed entropy and offline private-key brute forcing | About 1,816 BTC / $116M | High vulnerability and loss; medium actor clustering |
| Address-poisoning theft | Reported August 2026 | Automated look-alike address poisoning | About $100K USDT | High |
| Vultisig-related outflow | August 11; reported August 18 | Suspicious outflow and Tornado Cash routing; compromise unconfirmed | 1.284M USDC outflow; 1.092M USDC routed into 575.4 ETH | Medium investigative lead |

## 1. Maya Protocol — Newest Confirmed Protocol Exploit

**Incident date:** August 18, 2026  
**Environment:** MAYAChain / cross-chain liquidity protocol  
**Classification:** Protocol logic exploit involving six interacting accounting and state-handling edge cases  
**Direct loss:** Approximately $1.7 million  
**Confidence:** High

The attacker chained failures involving Trade Accounts, outbound processing, theft detection, subsidy calculation, pool-state persistence, and error handling. A legitimate outbound was incorrectly treated as missing, causing a false subsidy to inflate the thin ARB.LINK pool. Although the reserve could not fund the subsidy, the inflated state remained committed. The attacker then added negligible liquidity, obtained approximately 99.93% of the distorted pool position, withdrew about 48.87 million CACAO, and converted value into approximately 20.83 BTC and other assets.

The estimates describe different effects and should remain separate:

- Approximately **$1.36 million** in hard assets was reconstructed as moving to external L1s.
- Approximately **$1.7 million** is the commonly reported direct incident loss.
- Approximately **$10.9M-$11M** describes broader pool and market deterioration, including CACAO repricing and arbitrage; it should not be labeled as the amount stolen.

### Direct Incident-Watch Seed

| Network | Address | Role | Monitoring |
|---|---|---|---|
| MAYAChain | `maya1dl3yrfpedyr5jfr0r86s2apjltnjqgszmwsv8x` | Researcher-identified attacker address | Watch directly and expand L1 extraction, swaps, bridge routes, and recovery activity |

## 2. Fake AMLBot and AML-Checker Sites

**Report date:** August 19, 2026  
**Classification:** Wallet drainer, service impersonation, and malicious transaction approval  
**Aggregate loss:** Not publicly quantified  
**Confidence:** High that the campaign and TTP exist; unknown aggregate loss and actor clustering

Malwarebytes documented professional-looking sites that imitate AMLBot or generic AML-checking services. The sites prompt visitors to connect a Web3 wallet, then attempt to obtain transaction signatures, approvals, or payments. AMLBot independently states that its legitimate wallet check does not require a Web3 wallet connection and warns that imitation sites use malicious approvals to drain assets.

No complete attacker address set meeting this repository's evidence standard was identified. This entry is therefore retained as a campaign and TTP, not a fabricated wallet cluster.

## 3. FoxMarket

**Incident date:** August 15, 2026  
**Network:** BNB Chain  
**Classification:** Flash-loan-assisted spot-price manipulation and unsupported reward minting  
**Loss:** Approximately $118,700  
**Confidence:** High

`FoxLpBondsPool.stake()` derived the stake amount from a manipulable PancakeSwap FOX/USDT spot quote. Flash-loan liquidity distorted the reserves, while later liquidity accounting trusted the stale value and minted excess FOX and referral rewards that were sold in the same transaction.

| Role | Address or transaction | Treatment |
|---|---|---|
| Attacker | `0x5670d36f00bc7f6860b6afddb288e3668efc0ef9` | Direct incident-watch seed |
| Victim contract | `0x9fa6d8a13b35e051bfc145918db0111dec13d1a0` | Victim infrastructure; do not threat-label |
| Exploit transaction | `0x8e1775cbfd44db29744cc6687ff1822d2c47321de6e94062f789ad6181ad5514` | Transaction evidence |

## 4. Hyperliquid Impersonation and Google Ads Phishing

**Incident date:** August 13, 2026  
**Classification:** Sponsored-search phishing, platform impersonation, and wallet drain  
**Loss:** Approximately 550,019 USDC  
**Confidence:** High that the transfers and loss occurred; medium-high for direct attacker labeling based on the public investigator attribution

This was **not a Hyperliquid protocol exploit**. FlashRescue co-founder Darcy attributed the incident to a fraudulent paid Google result impersonating Hyperliquid and published three recipient addresses. SEAL's separate research documents the broader malicious Google Ads ecosystem, including hundreds of blocked URLs and campaigns targeting Hyperliquid, Jupiter, Raydium, Pump.fun, Uniswap, and other crypto applications.

| Address | Treatment |
|---|---|
| `0x98b2761559A348968C994D9856dCfc96B6f13C55` | Direct incident-watch seed |
| `0x93b6B24DC6E6a1D5d72399e3A35498c4DbA1d6D1` | Direct incident-watch seed |
| `0x6fE314fD4CF845f35fc461eD98e2FB8d9356B566` | Direct incident-watch seed; also observed in other phishing reporting, so do not assume single-campaign exclusivity |

## 5. Ethereum Whale Wallet Drain

**Incident date:** August 12, 2026  
**Network:** Ethereum  
**Classification:** High-value wallet compromise or unauthorized signing control  
**Loss:** Approximately $25.6 million  
**Confidence:** High for the theft and theft-address linkage; medium/unknown for the compromise vector

Public reporting described losses including approximately $6.3M aWBTC, $5.1M DAI, $4.7M WBTC, $2.6M ETH, and additional cbBTC, USDS, LDO, and CRV. Proceeds were consolidated into approximately 20M DAI and 3,000 ETH.

| Network | Address | Role | Monitoring |
|---|---|---|---|
| Ethereum | `0x8fEB0c6eF08B20bA19C04F951d4408bB5A1F95Ae` | Publicly identified theft and consolidation address | Watch directly |

The same victim reportedly lost approximately $24.23M in 2023 after malicious approvals, with most of that earlier loss returned. That historical event does not establish the 2026 root cause. The 2026 activity involved closing DeFi positions, withdrawing liquidity, and directly signed transfers. Available on-chain evidence supports effective signing control but cannot distinguish a stolen private key, compromised signer or device, session compromise, or another signing-path failure.

## 6. Harmony Cross-Shard Unauthorized Mint

**Incident window:** August 11-12, 2026  
**Network:** Harmony  
**Classification:** L1 cross-shard receipt and quorum-validation failure leading to unauthorized minting  
**Initial loss estimate:** Approximately $3.2 million  
**Confidence:** High

The disclosed failure involved cross-shard receipt validation and a quorum check that could accept a fabricated header or receipt without genuine validator signatures. Public technical reporting also describes insufficient binding of receipt-spend state to signed header data.

Two scope figures must be preserved rather than silently overwritten:

- SlowMist's initial tracker entry recorded approximately **4 billion ONE** and an estimated **$3.2M** loss.
- Later Harmony and CertiK reporting described **more than 3 trillion ONE** created across six abnormal blocks.

The token-creation figure, amount sold, amount frozen, market dilution, and recoverable cash loss are different measurements. The four pairs below are four accounts expressed in Harmony-native and hexadecimal form, not eight independent wallets.

| Harmony address | Hex equivalent | Treatment |
|---|---|---|
| `one1uap8dx2z0qsjxqthm5flgcxkeepsz3gsrghnfn` | `0xe7427699427821230177dd13f460d6ce43014510` | Direct incident-watch seed |
| `one17u300a40ll5wphd8kj5hktryhdjq3ml9f4phy4` | `0xf722f7f6afffe8e0dda7b4a97b2c64bb6408efe5` | Direct incident-watch seed |
| `one1a5hur07z5vtvzhr35zkw8tfqedemkz8t88xgd7` | `0xed2fc1bfc2a316c15c71a0ace3ad20cb73bb08eb` | Direct incident-watch seed |
| `one1h56hkxmua0uzfv07fu04cudvtrl35u96pq47vy` | `0xbd357b1b7cebf824b1fe4f1f5c71ac58ff1a70ba` | Direct incident-watch seed |

## 7. ODY / Odyssey / Ody DeFi

**Incident date:** July 28, 2026  
**Classification:** Privileged mint, market dump, liquidity extraction, and exit scam/rug  
**Direct ODY loss:** Approximately $15M-$15.67M USDT  
**Confidence:** Medium-high

GoPlus reported that the token retained mint, whitelist, and tax-management privileges despite decentralization claims. Approximately 10 billion ODY were minted, sold or injected into the PancakeSwap ODY/USDT market, and more than $15 million USDT was extracted. GoPlus reported more than 10,000 victims. Darcy's tracing placed ODY-related aggregation at at least 15,669,118 USDT.

An additional approximately $5.38M associated with KXG reportedly touched the same aggregation infrastructure, but it is not added to the ODY loss without evidence that it is part of the same victim-loss calculation.

The indexed reports expose the main aggregation address and mint transaction only in truncated form (`0x486f…`, `0xd2c85d49b…`). Neither is added to `addresses.csv` until a complete identifier is verified.

## 8. Coldcard Weak-Entropy Theft

**Incident window:** July 30, 2026 onward  
**Primary network:** Bitcoin; incident-linked laundering later reached Ethereum  
**Classification:** Hardware-wallet seed-generation weakness and offline brute forcing  
**Known impact:** Approximately 1,816 BTC / $116M from more than 5,200 addresses across at least four waves  
**Confidence:** High for the vulnerability and loss; medium for individual actor clustering

TRM Labs attributes the theft opportunity to affected Coldcard firmware generating seeds with effective entropy as low as roughly 40 bits, allowing offline private-key brute forcing without physical access. Updating firmware does not repair a seed created with weak entropy; affected seeds must be replaced.

TRM cautions that differences among theft waves may indicate multiple attackers. CertiK published the following Ethereum laundering pivot after incident-linked BTC moved through THORChain:

| Network | Address | Role | Treatment |
|---|---|---|---|
| Ethereum | `0x41B7529a411EeA979a8d468bdEBd36b0ad703268` | Incident-linked bridge and Tornado Cash pivot | Watch directly as a laundering pivot; do not label as the sole Coldcard attacker |

## 9. Address-Poisoning Theft

**Report date:** August 2026  
**Network:** Ethereum  
**Classification:** Automated look-alike address poisoning  
**Loss:** Approximately $100,000 USDT  
**Confidence:** High

GoPlus reported that the victim had received more than 400 poisoning transactions after its previous legitimate transfer, demonstrating sustained automation.

| Role | Address | Treatment |
|---|---|---|
| Victim | `0x9B4Ded0ab7754428F7eC0f63a42bAe70D2f51D83` | Victim; do not threat-label |
| Intended recipient | `0xae7C0ffAB6e77BE2D7d7880a4Ce433F59A4e2c85` | Legitimate counterparty; do not threat-label |
| Poisoning address | `0xAe7c08afAD91db18666EEAC055D7562c9f4e2c85` | Direct threat seed |

## 10. Vultisig-Related Outflow — Investigative Intelligence Only

**Observed outflow date:** August 11, 2026  
**Reported routing date:** August 18, 2026  
**Network:** Ethereum  
**Classification:** Suspicious outflow and privacy-protocol routing; exploit status unresolved  
**Confidence:** Medium

CertiK reported a suspicious 1.284M USDC outflow from a Vultisig-related address. Approximately 1.092M USDC was converted into 575.4 ETH and then deposited into Tornado Cash from two EOAs. The alert does not establish an exploit vector, unauthorized compromise, or a complete Vultisig source address suitable for direct attribution.

This item remains investigative intelligence and is intentionally excluded from the confirmed-hack count and machine-readable threat-address file.

## Monitoring Priorities

| Priority | Indicators | Action |
|---|---|---|
| P1 | Maya attacker; FoxMarket attacker; three Hyperliquid-phishing recipients; Ethereum whale theft address; four Harmony accounts | Direct monitoring, historical graph expansion, bridge and exchange-deposit alerts |
| P2 | Coldcard-linked Ethereum laundering pivot; poisoning address | Direct monitoring with narrower incident-role labels |
| TTP only | Fake AML-checker campaign | Track brands, domains, wallet-connection behavior, malicious approvals, and any later verified wallets |
| Case only | ODY | Preserve rug-pull report; withhold truncated identifiers |
| Investigative | Vultisig-related outflow | Monitor for a protocol statement, complete IOCs, root-cause evidence, and confirmation of unauthorized activity |

## Attribution Boundaries

- `addresses.csv` contains only complete, evidence-supported direct seeds or explicitly labeled incident-linked laundering pivots.
- Victims, legitimate recipients, protocol contracts, pools, routers, bridges, exchanges, and mixers are not automatically threat-controlled.
- Harmony native and hex forms are alternate representations of the same four accounts.
- The Hyperliquid case is phishing against a user, not a Hyperliquid protocol breach.
- The Coldcard Ethereum address is a laundering pivot, not proof of one actor controlling every theft wave.
- The 2026 Ethereum whale drain's exact compromise vector remains unresolved.
- ODY and Vultisig identifiers remain withheld where public evidence is truncated or attribution is incomplete.

## Sources

### Maya Protocol

- [SlowMist Hacked — live incident tracker](https://hacked.slowmist.io/)
- [CertiK Alert — Maya Protocol loss and asset estimate](https://x.com/CertiKAlert/status/2089900489752318181)
- [Vini Barbosa — six-bug technical reconstruction and attacker address](https://x.com/vinibarbosabr/status/2089827189768212659)

### Fake AML Checkers

- [Malwarebytes — fake crypto AML checkers](https://www.malwarebytes.com/blog/threat-intel/2026/08/scammers-are-using-fake-crypto-aml-checkers-to-drain-your-wallet)
- [AMLBot — impersonation and malicious-approval warning](https://blog.amlbot.com/dont-get-tricked-by-fake-amlbot-platforms-protect-your-crypto-from-scammers/)

### FoxMarket

- [SlowMist — FoxMarket technical alert](https://x.com/SlowMist_Team/status/2089196291800908164)
- [Defimon Alerts — real-time FoxMarket detection](https://t.me/s/defimon_alerts)
- [BscScan — exploit transaction](https://bscscan.com/tx/0x8e1775cbfd44db29744cc6687ff1822d2c47321de6e94062f789ad6181ad5514)

### Hyperliquid Impersonation

- [Darcy / FlashRescue — incident attribution and recipient addresses](https://x.com/DarcyAri/status/2087804729258594427)
- [Security Alliance / SEAL — malicious Google Ads targeting crypto](https://radar.securityalliance.org/malicious-google-ads-targeting-crypto/)

### Ethereum Whale Drain

- [Specter — theft report and theft address](https://x.com/SpecterAnalyst/status/2087661729945723040)
- [GoPlus — follow-up on the drain and consolidation](https://x.com/GoPlusSecurity/status/2087857323188637914)

### Harmony

- [Harmony — official freeze request and four account pairs](https://x.com/harmonyprotocol/status/2087410115200889135)
- [GoPlus — Harmony incident alert](https://x.com/GoPlusSecurity/status/2087433698224312484)
- [Rekt — technical and scope reconciliation](https://rekt.news/harmony-rekt2)
- [SlowMist Hacked — initial incident and loss estimate](https://hacked.slowmist.io/)

### ODY

- [GoPlus — ODY mint-and-run investigation](https://x.com/GoPlusZH/status/2087429254283972611?lang=en)

### Coldcard

- [TRM Labs — $116M Coldcard analysis](https://www.trmlabs.com/resources/blog/the-largest-hardware-wallet-exploit-of-2026-inside-the-usd-116-million-coldcard-hack)
- [CertiK Alert — THORChain-to-Ethereum laundering pivot](https://x.com/CertiKAlert/status/2084920866526114183)

### Address Poisoning and Vultisig Lead

- [GoPlus — $100K address-poisoning incident](https://x.com/GoPlusSecurity/status/2087521393558876545)
- [CertiK Alert — Vultisig-related USDC outflow and Tornado Cash routing](https://x.com/CertiKAlert/status/2089531153904718110)

---

## TLDR

Maya Protocol is the newest confirmed protocol exploit in the reviewed tracker window. The sweep adds complete direct-watch seeds for Maya, FoxMarket, Hyperliquid phishing, the Ethereum whale drain, Harmony, Coldcard-linked laundering, and address poisoning. Fake AML-checker sites are retained as a high-confidence TTP without an invented wallet cluster. ODY receives a documented rug-pull backfill without truncated IOCs, while the Vultisig-related outflow remains an unresolved investigative lead.
