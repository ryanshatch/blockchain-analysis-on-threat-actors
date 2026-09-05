# August 20-September 4, 2026 Crypto Security Sweep

| Field | Details |
|---|---|
| Review cutoff | August 20, 2026 at 2:31 a.m. ET |
| Follow-up cutoff | September 4, 2026 |
| Scope | Protocol exploits, wallet compromises, phishing and drainer campaigns, rug pulls, address poisoning, laundering pivots, and unresolved investigative intelligence |
| Networks | MAYAChain, Bitcoin, Ethereum, Solana, ICON, Sonic, Cronos, BNB Chain, Harmony, TRON, Base, and other EVM environments |
| Sources reviewed | SlowMist, CertiK, TRM Labs, BlockSec, Blockaid, SEAL/Security Alliance, Bitquery, GoPlus, Defimon, PeckShield/Specter, Malwarebytes, Protos, ICON Foundation, protocol disclosures, public explorers, and corroborating reporting |
| Latest confirmed protocol incidents in the follow-up window | Aquifer on Solana and Injective binary-options settlement, August 31, 2026; Aquifer has three complete P1 indicators while Injective remains a zero-seed case |

> SlowMist's live tracker listed Maya Protocol as its newest incident at the review cutoff. No protocol exploit dated August 19 or August 20 appeared above it. This is a point-in-time observation, not proof that no undisclosed or later-indexed incident occurred.

## Executive Summary

| Project or target | Incident or report date | Classification | Estimated loss | Confidence |
|---|---|---|---:|---|
| Aquifer | August 31; reconstruction verified September 1 | Forged token-account and untrusted token-program validation exploit | $2,469,729 across 212 malicious swaps | High incident and address linkage; medium-high precise source-level root cause |
| Injective binary-options module | August 31; reported September 1 | Market-identifier collision and settlement-logic exploit | Approximately $4.9M | High incident; incomplete attacker IOC |
| Tectonic / Cronos | August 30-31 | Lending-market exploit involving manipulated thin-liquidity TONIC collateral pricing | Approximately $74M-$75M reported | High incident; incomplete attacker IOCs |
| Rain legacy Solana card contracts / Avici and Tria | August 28; attribution update September 2 | Shared-infrastructure authorization and signature-validation exploit | $932,804.22 confirmed across 2,321 users; approximately $1.02M in broader attacker proceeds | High |
| ICON Network migration contracts | August 27; official post-mortem August 30 | Signed-message replay and withdrawal-uniqueness validation exploit | 119,866,000 ICX and 531,600 bnUSD released; approximately 150.2 ETH plus 31,204 USDC unrecovered | High |
| Moonwell / MAMO collateral market | August 27 | Thin-liquidity collateral-price manipulation on Base | Approximately $8.7M | High incident; incomplete attacker IOC |
| Term Finance / Term Meta Vaults | August 23; laundering update August 25 | Governance-layer takeover, malicious vault asset movements, and active Tornado Cash dispersal | About $8.5M; 300 ETH later deposited to Tornado Cash | High |
| Bofur Capital wallet | August 22 | Automated look-alike address poisoning and proceeds consolidation | About $2M / about 2M DAI | High theft; medium-high campaign attribution |
| The Sandbox SAND bridge | August 22 | Unauthorized minting of unbacked SAND on Base and BNB Smart Chain | 14.9B unbacked SAND reported; realized loss unresolved | High incident; incomplete IOCs |
| Maya Protocol / MAYAChain | August 18 | Chained protocol accounting and state-management exploit | About $1.7M direct | High |
| Allbridge CCTP / Allbridge Next | August 19 | Base-side cross-chain message-validation and accounting exploit | About $189,752 attacker profit / $191K victim liquidity | High |
| Fake AMLBot / AML-checker sites | Reported August 19 | Wallet drainer, brand impersonation, and malicious approvals | Unknown | High campaign; unknown aggregate loss |
| FoxMarket | August 15 | Flash-loan-assisted spot-oracle manipulation | About $118.7K | High |
| Hyperliquid impersonation | August 13 | Google Ads phishing and wallet drain; not a Hyperliquid protocol exploit | About 550,019 USDC | High loss; medium-high attacker attribution |
| Ethereum whale drain | August 12 | Wallet or signing-environment compromise; exact vector unresolved | About $25.6M | High incident; medium root cause |
| Harmony | August 11-12 | Cross-shard receipt and quorum-validation flaw causing unauthorized minting | About $3.2M initial cash-loss estimate; token issuance estimates remain disputed | High |
| Coinsbuy | August 9 | Coordinated Ethereum and TRON wallet drain; exact access vector unresolved | More than $7.9M / about $8.07M | High incident linkage; unknown attacker identity |
| ODY / Odyssey / Ody DeFi | July 28; highlighted August 11-13 | Privileged mint, market dump, liquidity extraction, and exit scam | About $15M-$15.67M USDT | Medium-high |
| COLDCARD | July 30 onward; Ethereum attribution update September 3-4 | Weak seed entropy, offline private-key brute forcing, and cross-chain laundering | Bitquery tracks 1,789.28 BTC; prior broader estimate about 1,816 BTC / $116M | High vulnerability and address linkage; unresolved actor and cross-wave clustering |
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

### Direct Incident-Watch Seeds

| Network | Address | Role | Monitoring |
|---|---|---|---|
| MAYAChain | `maya1dl3yrfpedyr5jfr0r86s2apjltnjqgszmwsv8x` | Researcher-identified attacker address | Watch directly and expand L1 extraction, swaps, bridge routes, and recovery activity |
| Bitcoin | `bc1q0hsgwunccczelq05ucpmfz268eyy5jr2y5l646` | Exploit-proceeds consolidation address; approximately 20.83 BTC | Watch directly; high-confidence external-L1 proceeds seed |
| Arbitrum | `0xa2f246f82995CBcCA8eD0d9F251383881A5E423e` | Secondary exploit-proceeds address; approximately 6.03 ARB.ETH plus other assets | Watch directly; medium-high attribution based on AMLBot monitoring |

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
**Known impact:** Bitquery tracks 1,789.28 BTC from 8,865 victim addresses; prior broader reporting estimated approximately 1,816 BTC / $116M

**Confidence:** High for the vulnerability, incident linkage, and complete addresses; unresolved individual actor and cross-wave clustering

TRM Labs attributes the theft opportunity to affected Coldcard firmware generating seeds with effective entropy as low as roughly 40 bits, allowing offline private-key brute forcing without physical access. Updating firmware does not repair a seed created with weak entropy; affected seeds must be replaced.

TRM cautions that differences among theft waves may indicate multiple attackers. CertiK previously published the following Ethereum laundering pivot after incident-linked BTC moved through THORChain:

| Network | Address | Role | Treatment |
|---|---|---|---|
| Ethereum | `0x41B7529a411EeA979a8d468bdEBd36b0ad703268` | Incident-linked bridge and Tornado Cash pivot | Watch directly as a laundering pivot; do not label as the sole Coldcard attacker |

Bitquery's September 3-4 update resolves three complete Ethereum destinations for 20.69 BTC routed through 36 THORChain swaps. The destination address is encoded in each Bitcoin-side protocol memo, so the chain linkage does not depend solely on behavioral inference.

| Network | Address | Role | Treatment |
|---|---|---|---|
| Ethereum | `0x160a7A4c067B084F03400c6980Ac29F73F6782f6` | Primary Wave 3 proceeds and consolidation destination; approximately 20.15 BTC across 26 swaps | P1 direct watch |
| Ethereum | `0x8B5b650067841ff3bF28fF3EC8ED1eE635e3D200` | Secondary September destination; approximately 0.30 BTC across eight swaps | P2 direct watch |
| Ethereum | `0x6A08B5B20F23FcFE09f5da506Be59CAD1eC0df06` | Historical August 2 destination; approximately 0.24 BTC across two swaps | P2 historical graph pivot |

Bitquery also publishes six Bitcoin addresses in its `CONFIRMED` tier:

| Address | September 3 snapshot | Treatment |
|---|---:|---|
| `bc1qq85v2c926eg6pgxhwp6q7lf6cnsz80qs3fcu9r` | 562.02147793 BTC; dormant | P1 direct watch |
| `bc1qx76cae2706qd5q576feh7xq8rfcsjpf2htfhe3` | 398.47576957 BTC; dormant | P1 direct watch |
| `bc1q8jy96fe5lf8vfugydnte3cguk92gpev7kwtp3q` | 89.62329890 BTC; dormant | P1 direct watch |
| `bc1qtfrwa4j6rmj9rsgspv6a0yjumkg39js2numu75` | 45.90254994 BTC; dormant | P1 direct watch |
| `bc1qnk4zh9qcnap2mycp56qjrgza3cc8ylrh8fecp0` | 32.45061090 BTC; prior spends | P1 direct watch and spend-path expansion |
| `bc1qmd5m5ktv7m5ffujxv4248fxv36myvdx79n8jp6` | 0.00002000 BTC; prior spends | P2 historical pivot |

The `CONFIRMED` tier means an independent source corroborated the address as part of this exploit. Bitquery's larger `TRACED`, `REPORTED`, `ATTRIBUTED`, `VENUE`, and `UNDER REVIEW` sets are not promoted to equivalent attacker status. A common incident path also does not prove that the same individual controlled every Ethereum destination or all four theft waves.

The canonical report and ten machine-readable records are maintained in [`Multi-Chain/Coldcard-Weak-Entropy-Theft/`](../Coldcard-Weak-Entropy-Theft/).

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

## 11. Coinsbuy Cross-Chain Drain

**Incident date:** August 9, 2026  
**Networks:** Ethereum and TRON  
**Classification:** Coordinated wallet drain and laundering; exact access vector unresolved  
**Loss:** More than $7.9 million; later reporting calculated approximately $8.07 million  
**Confidence:** High for incident linkage and the three published theft/proceeds addresses; attacker identity and root cause unknown

Specter published two Ethereum and one TRON theft/proceeds address after wallets associated with crypto payment processor Coinsbuy were drained across both networks. Subsequent reporting described approximately 6.04M USDT leaving eight TRON wallets and roughly 1.89M USDT plus 77 ETH leaving Ethereum wallets in under an hour. On-chain researchers linked the two network legs through Bridgers routing, while proceeds moved through services including FixedFloat, ChangeNOW, and BingX.

| Network | Address | Role | Treatment |
|---|---|---|---|
| Ethereum | `0x4d1bEF2Fe998B3E3C4029EF9EA6A0534d95661d3` | Published theft/proceeds address | Watch directly |
| Ethereum | `0x66790b54B891e2ebdef58a15B969Ff6fb4374b17` | Published theft/proceeds address | Watch directly |
| TRON | `TVpX9xCzrj6KHeNhhDJoqjzEqFMxdgubGR` | Published theft/proceeds address | Watch directly |

The simultaneous multi-chain activity is consistent with privileged withdrawal or wallet-management access, but it does not prove private-key theft, API compromise, insider access, or any other specific mechanism. Coinsbuy later said the incident was contained and customer losses were covered, but did not disclose the technical cause.

## 12. Allbridge CCTP / Base — Second Distinct 2026 Incident

**Incident date:** August 19, 2026  
**Networks:** Polygon preparation and Base execution  
**Classification:** Cross-chain message-validation and internal-accounting exploit  
**Loss:** Approximately $189,751.55 attacker profit; approximately $191,112 of legitimate user liquidity was present in the Router  
**Confidence:** High for the incident and reconstructed mechanism

This was distinct from Allbridge's July 19 Solana pool exploit. SlowMist's reconstruction describes missing `sender` and `recipient` validation in `CCTPTokenMessenger`, combined with Router accounting that trusted a recorded `receivedTokenAmount` without proving the corresponding USDC had arrived.

The attacker prepared a malicious CCTP-style message on Polygon on July 26, then waited approximately 24 days. After a legitimate transfer placed about 191,112 USDC in the Base Router on August 19, the attacker acted roughly six seconds later. An Aave flash loan temporarily added about 808,844 USDC; the manipulated internal record then authorized a 999,000 USDC transfer. After repayment and fees, the reported profit was approximately 189,751.55 USDC.

No complete attacker EOA or contract address was available from the reviewed authoritative reporting. The incident is therefore documented without adding a direct-watch seed. See the expanded [`Allbridge-Core`](../Allbridge-Core/) case for the two-incident comparison.

No new confirmed Solana protocol exploit or complete qualifying Solana threat address was identified in the follow-up scan.

## 13. Bofur Capital Address-Poisoning Campaign

**Incident date:** August 22, 2026  
**Network:** Ethereum  
**Classification:** Automated look-alike address poisoning, stolen-funds swapping, and proceeds consolidation  
**Loss:** Approximately $2 million; proceeds converted into approximately 2 million DAI  
**Confidence:** High for the theft, poisoned destination, and proceeds flow; medium-high for the broader controller and campaign-infrastructure attribution

After a wallet labeled Bofur Capital withdrew funds from Compound, the attacker seeded its transaction history with a 0.0002 USDC dust transfer from a look-alike address. The victim later copied the poisoned destination instead of the intended payee. The reported transaction-level path moved the stolen assets through a swap/consolidation account and into DAI held at the final proceeds address.

### Direct-Watch Seeds

| Address | Role | Confidence | Monitoring |
|---|---|---|---|
| `0xf0e6a49668de1195b931a3717c9cc36fc19721af` | Spoofed destination used in the theft | High | P1 direct watch |
| `0x692729bcd0887b8d02b8ff3169220ba0f4e17251` | Stolen-funds swap and consolidation account | High | P1 direct watch |
| `0xe2ebfd6f329a6330ab7eee68ce1328c21d31816a` | Final DAI storage and consolidation address | High | P1 direct watch; highest-priority current proceeds endpoint |
| `0xedda4e01669d30faa04a9cb75488abc366ee4143` | Address-poisoning campaign controller | Medium-high | P1 direct watch and historical graph expansion |
| `0xde39ef679e12574279e3ed35de4b0721beae27de` | Forgery and poisoning contract | Medium-high | P2 infrastructure monitoring |

The controller was reported as generating more than 126,000 dust transfers against over 80,000 distinct addresses since late May. Explorer activity independently shows repeated tiny token transfers consistent with the reported poisoning pattern. This supports campaign-level monitoring, but the controller and contract retain medium-high confidence because their broader attribution rests on fewer independent role-specific sources than the theft path.

### Address-Similarity Mechanism and Exclusions

```text
Legitimate: 0xf0e67a1896e814e30c011e36174de28caa9ab1af
Spoofed:    0xf0e6a49668de1195b931a3717c9cc36fc19721af
```

| Indicator | Role | Treatment |
|---|---|---|
| `0x7ba7f4773fa7890bad57879f0a1faa0edffb3520` | Bofur Capital victim wallet | Do not threat-label |
| `0xf0e67a1896e814e30c011e36174de28caa9ab1af` | Legitimate intended payee | Do not threat-label |
| `0xe2ebba3e64f25f8badf35d2760473748d673416a` | Separate look-alike reportedly used to poison the attacker's own proceeds wallet | Graph-expansion-only infrastructure pivot; exclude from primary direct-watch CSV |

## 14. Term Finance / Term Meta Vault Governance Exploit

**Incident date:** August 23, 2026  
**Network:** Ethereum  
**Classification:** Governance-layer takeover affecting Term Strategy/Meta Vaults  
**Loss:** Approximately $8.5 million  
**Confidence:** High for the incident, loss estimate, and proceeds address; unknown attacker identity and unresolved governance-control path

Term Labs confirmed a governance exploit affecting Term vaults. PeckShield and CertiK independently estimated that approximately $8.5 million was removed. Term later irreversibly shut down all Meta Vaults, revoked their DAO governance roles, permanently stopped new deposits, and left withdrawals open. Based on Term's preliminary investigation, the underlying Term protocol and direct borrowing and lending markets were not affected.

The affected vaults use Yearn V3 architecture, but Yearn stated that the incident involved Term's custom governance wrapper and did not apply to standard Yearn vault deployments. Available evidence supports a governance-control exploit; it does not yet establish the exact path by which the attacker obtained or exercised sufficient authority.

### Asset Flow and Direct-Watch Seed

| Asset | Reported amount | Handling |
|---|---:|---|
| ETH | Approximately 2,843 ETH / about $6.9M | Consolidated at the address below |
| USDC | Approximately 1.68M USDC | Swapped into approximately 1.68M DAI and consolidated at the same address |

| Network | Address | Role | Confidence | Monitoring |
|---|---|---|---|---|
| Ethereum | `0xD5183d8BfC65a50863C62aF2538198A8288FFc13` | Exploit-proceeds and consolidation address | High | P1 direct watch; highest priority |

At Ethereum block 25,822,718 on August 24, public reporting placed approximately 2,843.20 ETH and 1,679,642 DAI at the address. Monitor outbound dispersion, DEX swaps, bridges, exchange deposits, privacy-protocol interactions, recovery activity, and any later actor attribution.

### August 25 Laundering Update

PeckShield monitoring reported that the proceeds address deposited **300 ETH**, worth approximately **$741,000** at the time, into Tornado Cash on August 25. The movement was reported as three 100 ETH deposits. This changes the address's operational role from passive proceeds storage to active dispersal and privacy-protocol routing.

```text
0xD5183d8BfC65a50863C62aF2538198A8288FFc13

Exploit seed
→ proceeds consolidation
→ active dispersal
→ Tornado Cash laundering source
```

The Term address remains a P1 direct-watch seed. Tornado Cash pool, router, and relayer contracts are laundering-infrastructure pivots and must not inherit the attacker label.

PeckShield traced the incident's initial funding to approximately 2 ETH withdrawn from Tornado Cash. That is useful graph evidence, not attribution to a named person or group. Tornado Cash contracts, Term and Yearn infrastructure, ordinary governance participants, and later exchange or service counterparties must not be threat-labeled merely because they appear in the flow.

## 15. The Sandbox SAND Bridge — IOC Withheld

**Incident date:** August 22, 2026  
**Networks:** Base and BNB Smart Chain  
**Classification:** Cross-chain bridge exploit enabling unauthorized minting of unbacked SAND  
**Reported mint:** Approximately 14.9 billion unbacked SAND across two attacker addresses  
**Confidence:** High for the incident and containment; incomplete address intelligence and unresolved realized loss

The Sandbox confirmed that an attacker minted unbacked SAND on Base and BNB Smart Chain and disabled bridging to and from both networks. The project reported that SAND on Ethereum and Polygon, user wallets, and Ethereum reserves backing legitimate bridged SAND were unaffected. The large minted-token total is not equivalent to cash stolen or realized loss.

The reviewed high-confidence reports expose only truncated attacker identifiers:

```text
0xAbE0...4D22
0x638C...F296
```

Neither identifier is retained in `addresses.csv`. The case remains documented with zero direct seeds until complete 42-character addresses are independently verified.

## 16. August 24-25 Solana Watch — Investigative Items

No new high-confidence Solana protocol exploit, confirmed rug pull, or complete attacker-wallet disclosure cleared the repository's direct-watch threshold in this follow-up. The following items are retained as disputed activity, campaign intelligence, or contextual IOCs rather than threat-wallet attributions.

### FOMO iOS Wallet-Drain Allegations

| Field | Assessment |
|---|---|
| Report window | August 23-24, 2026 |
| Classification | Disputed wallet-drain allegation / possible client-side compromise |
| Verified artifact | A 662 SOL transfer, approximately $62,000 at the reported valuation |
| Claimed aggregate loss | Approximately $6 million; unverified |
| Confidence | High that the transfer occurred; low that FOMO caused it; low on the aggregate-loss estimate |
| Repository treatment | Investigative only; zero direct wallet seeds |

Protos independently confirmed that the cited 662 SOL transaction exists but could not establish that it was unauthorized or caused by FOMO. The allegation originated from a third-party trader rather than the cited wallet owner. FOMO co-founder Prashan Dharmasena denied an exploit and said the account had no transaction signed by FOMO's fee payer.

No complete victim/attacker pair, common recipient cluster, exploit path, affected-wallet list, or methodology supporting the $6 million estimate has been published. FOMO must not be classified as a confirmed exploiter on the current evidence.

### Fake Solana Seeker / SKR and `$WAR` Reward Pages

The fake Solana Seeker / SKR page at `skr.solplanet[.]cc/early` and separately documented fake `$WAR` reward pages impersonate legitimate ecosystem names and attempt to induce wallet connections or signatures. They are wallet-drainer phishing campaigns, not vulnerabilities in Solana, Solana Mobile, Seeker, SKR, War On USD, or their underlying tokens.

| Indicator | Type | Classification | Confidence | Treatment |
|---|---|---|---|---|
| `skr.solplanet.cc/early` | URL | Fake Seeker / SKR claim page | Medium-high | Block and investigate as a campaign IOC; not a wallet seed |

No defensible aggregate loss or complete attacker-wallet cluster was available. The URL is retained in [`investigative_iocs.csv`](./investigative_iocs.csv); no wallet address is added to `addresses.csv`.

### Kylie Jenner X Account / `$KYLIE` Token Promotion

Public reporting described Kylie Jenner's verified X account promoting a newly created Solana token on August 24 before the posts disappeared. The token reportedly reached approximately $1.2 million in market capitalization and then fell approximately 68%-90%, depending on the observation point.

| Indicator | Type | Classification | Confidence | Treatment |
|---|---|---|---|---|
| `6b7KQsXqb6JR5Nmeer5zGRmo51dwDfttM5b5Nu2rpump` | Solana token mint | Contextual malicious-token-promotion pivot | Medium-high for the event; low for rug and actor attribution | Retain in `investigative_iocs.csv`; do not threat-label as an attacker wallet |

The current evidence supports reported social-account compromise and malicious token promotion. It does not establish a quantified confirmed rug pull, a verified deployer/proceeds cluster, or the identity of the person controlling the token.

### Reviewed Exclusions

- Automated token-risk failures are not proof that an executed rug pull occurred and are excluded from confirmed-incident counts.
- Earlier Rain/Avici reporting exposed the principal drainer only as `FVNFzq...CEj`; subsequent independent transaction-level reporting published the complete Solana address, which is retained in the dedicated case without reconstruction.
- The earlier statement that no qualifying August 24 OFAC wallet disclosure existed is superseded. OFAC published 30 BTC, ETH, and TRON identifiers for four MOIS-linked cyber actors plus one separate Tsoris USDT/TRON seed; those authoritative attributions are stored in a dedicated case.
- The August 24 Profit Connect conviction is material criminal-case reporting but publishes no wallet identifiers.

## 17. Moonwell / MAMO Collateral-Price Manipulation

| Field | Assessment |
|---|---|
| Incident date | August 27, 2026 |
| Network | Base |
| Classification | Thin-liquidity collateral-price manipulation / lending-market exploit |
| Estimated loss | Approximately $8.7 million |
| Proceeds | Reported consolidated into DAI |
| Confidence | High that the exploit occurred; incomplete public attacker IOC |
| Direct seeds | Zero |

CertiK, Blockaid, and PeckShield reporting described an attacker manipulating thin MAMO collateral pricing and borrowing against the inflated value through Moonwell on Base. Publicly indexed reporting exposed the proceeds address only as `0xD71d...C384` at this cutoff.

The truncated identifier is not retained in `addresses.csv` and must not be reconstructed from prefix and suffix fragments. Moonwell and MAMO protocol contracts, oracles, liquidity venues, and affected users remain infrastructure or victim context rather than attacker-controlled seeds.

## 18. August 24 OFAC MOIS Cyber-Actor Attribution

The August 28 review identified a material official disclosure missed by the prior cutoff. OFAC published 30 Bitcoin, Ethereum, and TRON identifiers for Keyvan Fayyaz Ghareh Blagh, Mojtaba Ghal'eh-Kuhi, Arman Kahzadian, and Behzad Mesri. A separate USDT/TRON identifier for Almpertos Tsoris was published under a different Iran-related sanctions authority.

The complete address set, entity roles, monitoring treatment, and attribution boundaries are maintained in [`Iranian-MOIS-Cyber-Network/`](../Iranian-MOIS-Cyber-Network/). These official identifiers are direct sanctions-watch seeds; counterparties remain graph context unless independently attributed.

## 19. Rain Legacy Solana Card-Contract Exploit

| Field | Assessment |
|---|---|
| Incident date | August 28, 2026 |
| Infrastructure | Rain legacy Solana card contracts |
| Confirmed affected programs | Avici and Tria |
| Classification | Shared-infrastructure authorization and signature-validation exploit |
| Avici | 1,685 users / $500,859.22 |
| Tria | 636 users / $431,945 |
| Confirmed combined impact | 2,321 users / $932,804.22 |
| Broader attacker proceeds | Approximately $1.02 million; difference unresolved |
| Confidence | High |
| Direct seeds | Two Ethereum funding seeds, two Solana P1 seeds, and one Ethereum laundering/proceeds pivot |

The August 28 incident was broader than an Avici-only breach. Tria confirmed that the same Rain infrastructure issue affected another 636 users and $431,945 in Solana card balances. Combined with Avici's reconciliation, the confirmed minimum is 2,321 affected users and $932,804.22 in unauthorized withdrawals.

Rain said a small number of programs were using outdated Solana contract versions. It upgraded all affected deployments, engaged external forensic specialists, and reported no further unauthorized activity. Avici and Tria each reported restoring affected balances in full plus 10% additional compensation.

The approximately $1.02 million traced through the attacker cluster remains separate from the program-level reconciliation. The roughly $87,000 difference must not be assigned to a third victim program without confirmation.

Blockaid's September 2 post-mortem disclosed two complete Ethereum addresses that funded the Solana operation before the exploit. Both were already flagged as malicious in Blockaid's threat-intelligence network. They are retained as P1 pre-exploit infrastructure seeds; their high-confidence transaction linkage does not, by itself, prove common ownership with the Solana exploiter.

| Network | Address | Role | Monitoring |
|---|---|---|---|
| Ethereum | `0xa1a15f1b0d4878873f2933573e4385ab1e4df25c` | Pre-exploit funding seed that bridged operating gas to Solana | P1 direct watch and graph expansion |
| Ethereum | `0x775028b2ce02844e8947905e4d655940a76cf559` | Upstream pre-exploit funding seed | P1 direct watch and graph expansion |

### Direct Attacker and Proceeds Cluster

| Network | Address | Role | Monitoring |
|---|---|---|---|
| Solana | `FVNFzqAny8spWdPmYw6RQ9TkYa29ueFFiqCFD1gQnCEj` | Principal drainer, collection wallet, and source of the 10,000 SOL transfer | P1 direct watch |
| Solana | `4kjsW9dPsqzvuhQVP3P23cvZisdoHE5dR8NdD1TMPKKE` | Proceeds and conversion wallet receiving more than $1 million in SOL before USDC swaps | P1 direct watch |
| Ethereum | `0x2cE21E4921d3Eb116526c3651Dac0257657338D5` | Cross-chain laundering and proceeds pivot routing funds toward Tornado Cash | P1 direct watch with proceeds-role label |

The complete principal address was published by The Defiant and a transaction-level Solana analysis after earlier reports showed only `FVNFzq...CEj`. On-chain investigators later resolved the next Solana wallet and the Ethereum-side proceeds address. Blockaid reconstructed 2,945 unauthorized `AddCollateralAdmin` calls and 5,288 `WithdrawCollateralAsset` calls, totaling 8,233 core exploit transactions over approximately 2 hours and 29 minutes. The supported path is Ethereum funding seeds → deBridge → principal Solana drain and collection → Solana conversion → approximately $1.02 million USDC → Ethereum laundering pivot → approximately 455.9 ETH deposited through Tornado Cash infrastructure.

Blockaid also published four Rain card-contract deployments and the Tornado Cash router. They are retained only as victim/protocol or laundering-infrastructure context, not attacker-controlled wallets.

The canonical report and ten machine-readable records—five P1 seeds and five explicit non-attacker infrastructure pivots—are maintained in [`SOL/Rain-Legacy-Contracts/`](../../SOL/Rain-Legacy-Contracts/).

No additional high-confidence Solana protocol exploit, wallet-drainer campaign, or confirmed rug pull cleared the repository's evidence threshold in the September 2 follow-up. The material Solana development is the resolution of Rain's upstream funding seeds and the stronger reconstruction of its existing exploit cluster.

## 20. ICON Network Migration-Contract Replay Exploit

| Field | Assessment |
|---|---|
| Incident date | August 27, 2026 |
| Official post-mortem | August 30, 2026 |
| Networks | ICON, Sonic, and Ethereum |
| Classification | Signed-message replay and withdrawal-uniqueness validation exploit |
| Gross unauthorized release | 119,866,000 ICX and 531,600 bnUSD |
| Currently unrecovered | Approximately 150.2 ETH plus 31,204 USDC |
| Confidence | High |
| Direct-watch representation | Three unique accounts represented as four chain-specific rows |

ICON Foundation reports that an attacker replayed two previously legitimate signed withdrawal messages 1,492 times in a 20-minute window. A serial-number precision defect allowed the attacker to vary unsigned high bits while the cryptographically signed low 256 bits remained unchanged. Of the replay calls, 1,490 succeeded and credited the same attacker-controlled ICON relayer wallet.

Approximately 11 hours before the exploit, the attacker opened a Sonic money-market position. Exploited assets were later used as collateral, producing USDC borrowings, while ICX moved through exchange deposits. ICON identifies approximately 150.2 ETH and 31,204 USDC as the currently unrecovered portion.

### Officially Identified Attacker-Controlled Accounts

| Network | Address | Role | Monitoring |
|---|---|---|---|
| ICON | `hx130b7e31ad0fb67c8b0442df308d349202212b88` | Exploit relayer and distribution wallet | P1 direct watch |
| Sonic | `0x72659d1bcc69f15c62ad7eb0f2311952856f0fec` | Pre-positioned attacker hub and collateral wallet | P1 direct watch |
| Sonic | `0xA1b828019B43F92f7E5B6d340ccAFF08228fCB52` | Shared attacker EOA on Sonic | P1 direct watch |
| Ethereum | `0xA1b828019B43F92f7E5B6d340ccAFF08228fCB52` | Cross-chain proceeds and consolidation address | P1 direct watch |

The shared EOA is intentionally retained once per network but represents one unique account key. The approximately 24 exchange deposit addresses cited in the post-mortem are exchange custody and evidence pivots; they must not be threat-labeled as attacker wallets.

The canonical report and machine-readable records are maintained in [`Multi-Chain/ICON-Migration-Replay-Exploit/`](../ICON-Migration-Replay-Exploit/).

## 21. Tectonic / Cronos Exploit — Zero-Seed Review

| Field | Assessment |
|---|---|
| Incident date | August 30, 2026 |
| Network | Cronos |
| Classification | Lending-market exploit involving manipulated thin-liquidity TONIC collateral pricing |
| Reported impact | Approximately $74M-$75M; estimates remain subject to reconciliation |
| Confidence | High that the exploit occurred; incomplete public attacker IOCs |
| Direct seeds | Zero |

Tectonic and Cronos acknowledged the incident, and Cronos halted the network during containment. PeckShield reported three attacker or proceeds locations, including an Ethereum destination holding roughly $6 million, but indexed sources expose them only as `0xc404...72dd`, `0x7d4e...4f2dc`, and `0x215a...d3fc`.

The truncated identifiers are not retained in a wallet dataset and must not be reconstructed from prefixes and suffixes. Tectonic contracts, Cronos validators, bridges, exchanges, and other protocol counterparties remain infrastructure or evidence context unless separately attributed.

## 22. Aquifer Solana AMM Exploit

| Field | Assessment |
|---|---|
| Incident date | August 31, 2026 |
| Network path | Solana exploit execution to Ethereum proceeds consolidation |
| Classification | Forged token-account and untrusted token-program validation exploit |
| Reconstructed loss | $2,469,729 across 212 successful malicious swaps |
| Proceeds | Approximately 24,084 SOL converted into 1,000.7956 ETH |
| Confidence | High incident and address linkage; medium-high precise source-level root cause |

Bitquery reconstructed 212 swaps in approximately 40 minutes that paid genuine assets from Aquifer's vaults while receiving no tokens. The attacker supplied 165-byte accounts that resembled SPL token accounts but were owned by a malicious program. One forged account claimed approximately 18 trillion USDC. The same malicious program was nominated as the incoming token program, accepted the payment-shaped instruction, moved nothing, and returned success.

Aquifer has not published its source code. The missing owner and token-program validation is inferred from the complete on-chain instruction pattern rather than confirmed against source code.

| Network | Address | Role | Treatment |
|---|---|---|---|
| Solana | `7fTe9pvrwXJRBHq9MaSyVPR4PgEuhqLiA93Dxf4gRk7J` | Primary attacker, exploit execution, and proceeds wallet | P1 direct watch |
| Solana | `DMBpPMaMpGM2mWiUMaqcHx9FwhPg9Ys7qg1X59NRgb68` | Malicious program impersonating the incoming token program | P1 exploit infrastructure and control-path pivot |
| Ethereum | `0x2Dfe9e969796e2797278b02761dd9Ad6aE922746` | Cross-chain attacker and proceeds-consolidation wallet | P1 direct watch |

Aquifer's on-chain whitehat offer, authorized through its program upgrade authority, named the same Solana and Ethereum attacker addresses and requested at least 80% back by September 3 at 14:00 UTC. At Bitquery's September 1 cutoff, the Ethereum address held 1,000.7956 ETH and had sent no transactions; no return to the designated Solana recovery address was observed.

The Aquifer program `AQU1FRd7papthgdrwPTTq5JacJh8YtwEXaBfKU3bTz45`, affected vaults, recovery addresses, routers, bridge settlement wallets, market makers, and ordinary counterparties are victim, recovery, or service infrastructure. They must not inherit the attacker label.

The canonical report and ten machine-readable role-separated records are maintained in [`SOL/Aquifer/`](../../SOL/Aquifer/). Three rows are P1 attacker or exploit-infrastructure indicators; seven rows preserve explicit victim and recovery exclusions.

## 23. Injective Binary-Options Exploit — Zero-Seed Review

| Field | Assessment |
|---|---|
| Incident date | August 31, 2026 |
| Network path | Injective to Ethereum |
| Classification | Binary-options market-identifier collision and settlement-logic exploit |
| Reported impact | Approximately $4.9 million; roughly 1,980 ETH reportedly consolidated on Ethereum |
| Confidence | High incident; incomplete public attacker IOC |
| Direct seeds | Zero |

Public reporting describes an attacker creating 299 binary-options markets and exploiting identifier-collision and no-price settlement behavior to extract approximately $4.9 million before bridging proceeds to Ethereum. Indexed sources expose the Ethereum destination only as `0x5a18...69ea`.

The truncated identifier is not retained in a machine-readable dataset and must not be reconstructed from prefix and suffix fragments. Injective protocol modules, oracles, bridge infrastructure, and exchange counterparties remain protocol or graph context unless separately attributed.

## Monitoring Priorities

| Priority | Indicators | Action |
|---|---|---|
| P1 | COLDCARD primary Ethereum destination plus five confirmed high-value or active Bitcoin seeds; Aquifer Solana attacker, malicious program, and Ethereum proceeds wallet; Rain five-address funding/exploit/proceeds set; four ICON chain-specific records; Term Finance active laundering source; Bofur spoof, swap, final-DAI, and campaign-controller addresses; Maya MAYAChain/BTC addresses; FoxMarket attacker; three Hyperliquid-phishing recipients; Ethereum whale theft address; two Coinsbuy Ethereum addresses; Coinsbuy TRON address; four Harmony accounts | Direct monitoring, historical graph expansion, bridge, exchange-deposit, malicious-program, and privacy-protocol alerts |
| P2 | Three COLDCARD secondary, historical, or earlier Ethereum/BTC pivots; Bofur poisoning contract; Maya Arbitrum proceeds address; poisoning address | Direct monitoring with narrower incident-role labels |
| TTP only | Fake AML-checker campaign | Track brands, domains, wallet-connection behavior, malicious approvals, and any later verified wallets |
| Campaign IOCs | Fake Seeker / SKR domain and fake `$WAR` rewards activity | Block known domains, monitor replacements, and preserve the distinction from legitimate projects and tokens |
| Case only | ODY; Moonwell / MAMO; Tectonic / Cronos; Injective binary-options exploit | Preserve confirmed incident reporting while withholding truncated identifiers |
| Investigative | Vultisig-related outflow; FOMO iOS allegations; Kylie Jenner / `$KYLIE` promotion | Monitor for complete IOCs, root-cause evidence, victim confirmation, deployer/proceeds attribution, and authoritative statements |

## Attribution Boundaries

- `addresses.csv` contains only complete, evidence-supported direct seeds or explicitly labeled incident-linked laundering pivots.
- Victims, legitimate recipients, protocol contracts, pools, routers, bridges, exchanges, and mixers are not automatically threat-controlled.
- Harmony native and hex forms are alternate representations of the same four accounts.
- The Hyperliquid case is phishing against a user, not a Hyperliquid protocol breach.
- The COLDCARD set contains six Bitcoin addresses in Bitquery's `CONFIRMED` tier, three memo-linked Ethereum destinations, and one previously retained Ethereum pivot. It does not imply one actor controlled every destination or theft wave; lower Bitquery tiers remain separate.
- The 2026 Ethereum whale drain's exact compromise vector remains unresolved.
- The Coinsbuy drain's exact compromise vector remains unresolved; cross-chain timing alone does not prove private-key compromise.
- The Allbridge CCTP/Base incident has no complete authoritative attacker identifier in this update and contributes no machine-readable seed.
- The Bofur Capital victim, legitimate payee, and secondary self-poisoning look-alike are excluded from primary threat labels; campaign-controller and contract roles remain medium-high confidence.
- The Term Finance address is a high-confidence proceeds and active-laundering seed, but no named actor or exact governance-control path is established; Tornado Cash and ordinary protocol counterparties remain graph context only.
- The Sandbox attacker identifiers are truncated and withheld; the 14.9B unbacked-token mint is not labeled as realized theft value.
- The verified 662 SOL transfer does not establish that FOMO caused or authorized a wallet drain; FOMO receives no threat-wallet label.
- Fake Seeker / SKR and `$WAR` pages are phishing infrastructure, not Solana protocol exploits or evidence against the legitimate projects and tokens.
- The `$KYLIE` mint is a contextual token-promotion IOC, not an attacker wallet or a confirmed rug classification.
- The Moonwell / MAMO exploit is confirmed at high confidence, but `0xD71d...C384` is truncated and contributes no machine-readable seed.
- The 30 MOIS-network addresses and separate Tsoris seed are official OFAC identifiers; interacting wallets do not automatically inherit those labels.
- The Rain monitoring set contains two Ethereum funding seeds, two Solana P1 seeds, and one Ethereum laundering/proceeds pivot. Funding linkage is high confidence, but common ownership of the Ethereum funders and Solana exploiter remains unresolved. Rain contracts, Avici and Tria accounts, affected users, DEXs, bridges, exchanges, Tornado Cash contracts, and service counterparties do not inherit attacker labels.
- ICON officially identifies three unique attacker-controlled accounts, represented as four chain-specific records because one EOA is shared across Sonic and Ethereum. The 24 exchange deposit addresses remain custody and evidence pivots, not attacker labels.
- Tectonic's three published address representations remain truncated and are withheld from machine-readable wallet data.
- The Aquifer direct set contains one Solana attacker wallet, one malicious Solana program, and one Ethereum proceeds wallet. The Aquifer victim program, affected vaults, recovery addresses, routers, bridges, settlement wallets, market makers, and ordinary counterparties remain explicitly non-attacker context.
- Aquifer's precise source-level root cause is reconstructed from a consistent on-chain instruction pattern because the source code is not public.
- Injective's reported Ethereum destination remains truncated as `0x5a18...69ea` and contributes no machine-readable seed.
- ODY and Vultisig identifiers remain withheld where public evidence is truncated or attribution is incomplete.

## Sources

### Maya Protocol

- [SlowMist Hacked — live incident tracker](https://hacked.slowmist.io/)
- [CertiK Alert — Maya Protocol loss and asset estimate](https://x.com/CertiKAlert/status/2089900489752318181)
- [Vini Barbosa — six-bug technical reconstruction and attacker address](https://x.com/vinibarbosabr/status/2089827189768212659)
- [Bitcoin.com News — PeckShield-attributed Bitcoin proceeds address](https://news.bitcoin.com/security/maya-protocol-exploit-1-7-million-peckshield/)
- [AMLBot monitoring reproduced by KuCoin — Arbitrum proceeds address](https://www.kucoin.com/ar/news/community/BTC/6a85cb0bec098c0007113843)

### Coinsbuy

- [Specter Investigation — published theft addresses](https://t.me/specterinvestigation/222)
- [CoinDesk — cross-chain incident reconstruction and Coinsbuy response](https://www.coindesk.com/business/2026/08/10/crypto-exchange-coinsbuy-loses-usd8-million-in-coordinated-two-blockchain-attack)

### Allbridge CCTP / Base

- [SlowMist reconstruction reproduced by KuCoin/MetaEra](https://www.kucoin.com/news/flash/allbridge-cross-chain-bridge-hacked-for-190-000-after-month-long-attack)
- [The Block — July Solana incident and planned move to CCTP/LayerZero](https://www.theblock.co/news/defi/2026-07-19-allbridge-core-exploit-408855)

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
- [Alex Thorn — Wave 3 BTC-to-ETH movement through THORChain](https://x.com/intangiblecoins/status/2095297452681158840)
- [Cointelegraph — Wave 3 THORChain movement and unpublished Ethereum destination](https://cointelegraph.com/news/coldcard-hacker-swaps-stolen-bitcoin-eth-thorchain)
- [Bitquery — live tracker, confirmed Bitcoin tier, complete Ethereum destinations, and THORChain memo linkage](https://bitquery.io/coldcard-hack/)
- [CryptoSlate — Bitquery update and later primary-destination balance observation](https://cryptoslate.com/parked-coldcard-loot-begins-moving-as-attacker-routes-1-6m-in-stolen-bitcoin-to-ethereum/)

### Address Poisoning and Vultisig Lead

- [GoPlus — $100K address-poisoning incident](https://x.com/GoPlusSecurity/status/2087521393558876545)
- [CertiK Alert — Vultisig-related USDC outflow and Tornado Cash routing](https://x.com/CertiKAlert/status/2089531153904718110)

### Bofur Capital Address Poisoning

- [CoinNess — PeckShield-attributed theft and final DAI endpoint](https://coinness.com/en/news/1084945)
- [CoinGabbar — transaction-level reconstruction and campaign pivots](https://www.coingabbar.com/en/crypto-currency-news/crypto-hack-news-bofur-capital-2m-address-poisoning)
- [RouteScan — controller-linked dust-transfer transaction evidence](https://ethereum.routescan.io/tx/0x4f968f22c94eb1affcdfe1796aeec8f16b21bb5a7c7513ce458843e8ab9a1b4c/eventlog?chainid=1)

### Term Finance

- [Term Labs — protocol confirmation and vault shutdown update](https://x.com/term_labs/status/2091428394130886740)
- [PeckShield Alert — asset accounting, funding trail, and proceeds address](https://x.com/PeckShieldAlert/status/2091452165932175659)
- [CertiK Alert — independent loss estimate and proceeds-address linkage](https://x.com/CertiKAlert/status/2091433962795106499)
- [Etherscan — proceeds and consolidation address](https://etherscan.io/address/0xD5183d8BfC65a50863C62aF2538198A8288FFc13)
- [Yearn — custom governance-wrapper scope clarification](https://x.com/yearnfi/status/2091599858323075144)
- [The Block — corroborating incident report](https://www.theblock.co/news/defi/2026-08-23-defi-lending-protocol-term-finance-loses-an-estimated-8-5-million-to-governance-exploit-412543)
- [BBX — PeckShield-attributed 300 ETH Tornado Cash deposit update](https://beta.bbx.com/news-detail/3046354)

### The Sandbox SAND Bridge

- [The Sandbox bridge-incident reporting and IOC truncation context](https://www.ccn.com/news/crypto/sandbox-exploit-14-9b-sand-korean-exchanges-freeze-transfers/)

### August 24-25 Solana Watch

- [Protos — FOMO iOS allegations, verified 662 SOL transfer, and denial](https://protos.com/crypto-trading-platform-fomo-denies-hack-of-its-ios-app/)
- [MalwareTips — fake Solana Seeker / SKR claim page](https://malwaretips.com/blogs/solana-seeker-skr-airdrop-scam/)
- [MalwareTips — fake `$WAR` reward pages](https://malwaretips.com/blogs/war-on-usd-rewards-scam/)
- [BeInCrypto — Kylie Jenner X account and `$KYLIE` promotion](https://beincrypto.com/kylie-jenner-x-account-hack-meme-coin/)
- [U.S. Department of Justice — Profit Connect conviction; no wallet identifiers published](https://www.justice.gov/usao-nv/pr/jury-convicts-las-vegas-business-owner-cryptocurrency-ponzi-scheme)

### August 27 Moonwell / MAMO Exploit

- [Crypto Times — Moonwell loss, MAMO price manipulation, and truncated proceeds address](https://www.cryptotimes.io/2026/08/27/moonwell-loses-nearly-8-7m-in-base-exploit-after-mamo-price-manipulation/)

### August 24 OFAC MOIS Cyber-Actor Attribution

- [OFAC Recent Action — official SDN entries and digital-currency identifiers](https://ofac.treasury.gov/recent-actions/20260824)
- [U.S. Treasury — MOIS cyber group, critical-infrastructure intrusions, and digital-asset theft](https://home.treasury.gov/news/press-releases/sb0613)

### August 28 Rain Legacy Solana Card-Contract Exploit

- [Rain — vulnerable Solana contract versions upgraded](https://x.com/raincards/status/2093435073081053518)
- [Avici — 1,685 users and $500,859.22 reconciled](https://x.com/avici/status/2093439613201482068)
- [Tria — 636 users and $431,945 reconciled](https://x.com/useTria/status/2093651836079116392)
- [FinanceFeeds — combined Avici and Tria impact](https://financefeeds.com/tria-and-avici-report-2321-users-hit-by-rain-solana-card-vulnerability/)
- [The Defiant — complete drainer and exploit mechanics](https://thedefiant.io/news/hacks/attacker-drains-more-than-usd1-million-from-avici-users-in-live-solana-neobank-attack)
- [SolScanner — complete drainer and transaction-level reconstruction](https://www.solscanner.app/blog/inside-the-avici-exploit)
- [inno — next Solana proceeds wallet and four-call exploit sequence](https://x.com/inno_sol/status/2093415789848412448)
- [Onchain Lens — cross-chain USDC, ETH, and Tornado Cash path](https://x.com/OnchainLens/status/2093501494033273339)
- [Blockaid — funding seeds, contract deployments, exploit counts, and Tornado Cash routing](https://blockaid.io/blog/11m-rain-ecosystem-exploit-how-onchain-monitoring-gives-stablecoin-card-issuers-fleet-level-coverage)

### August 27 ICON Network Migration-Contract Replay Exploit

- [ICON Foundation — official replay-exploit post-mortem, attacker-controlled accounts, and recovery status](https://www.icon.foundation/blog/2026/icon-network-replay-exploit-post-mortem)

### August 30 Tectonic / Cronos Exploit

- [Tectonic — incident acknowledgement and interaction warning](https://x.com/TectonicFi)
- [PeckShield Alert — approximately $74M estimate and truncated proceeds representations](https://x.com/PeckShieldAlert/status/2094217367434015065)

### August 31 Aquifer Solana AMM Exploit

- [Bitquery — complete on-chain reconstruction, loss accounting, cross-chain proceeds, and scope limits](https://bitquery.io/investigations/aquifer-solana-hack-2-5-million)
- [GoPlus Security — complete attacker wallets, malicious program, affected program, and vault identifiers](https://x.com/GoPlusSecurity/status/2094757173121204271)
- [Defimon Alerts — Aquifer on-chain whitehat offer and designated recovery addresses](https://x.com/DefimonAlerts/status/2094467984030826622)

### August 31 Injective Binary-Options Exploit

- [Defimon Alerts — incident and Ethereum proceeds report](https://x.com/DefimonAlerts)
- [PANews — binary-options exploit, network interruption, and zero-seed context](https://www.panewslab.com/en/articles/01a05a75-a70e-765e-8982-ab931191e00d)

---

## TLDR

The September 3-4 follow-up resolves three complete Ethereum destinations for 20.69 BTC moved through 36 THORChain swaps from the COLDCARD theft graph. The dedicated case retains those destinations, six Bitcoin addresses from Bitquery's `CONFIRMED` tier, and the earlier CertiK-linked Ethereum pivot. Lower-confidence Bitquery tiers and service infrastructure remain separate. No new official OFAC, FBI, or DOJ BTC, ETH, or SOL full-address disclosure was identified in this follow-up.
