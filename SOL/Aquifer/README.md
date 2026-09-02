# Aquifer Solana AMM Exploit

| Field | Assessment |
|---|---|
| Incident date | August 31, 2026 |
| Assessment cutoff | September 1, 2026 |
| Network path | Solana exploit execution to Ethereum proceeds consolidation |
| Classification | Forged token-account and untrusted token-program validation exploit |
| Reconstructed loss | $2,469,729 |
| Malicious swaps | 212 successful calls in approximately 40 minutes |
| Assets drained | 18 tokens |
| Solana proceeds | Approximately 24,084 SOL |
| Ethereum proceeds | 1,000.7956 ETH |
| Confidence | High incident and address linkage; medium-high precise source-level root cause |

## Executive Assessment

Aquifer, a Solana trading venue used by routing infrastructure including Jupiter, was drained of $2,469,729 on August 31, 2026. Bitquery reconstructed 212 one-sided swaps between 03:41 and 04:21 UTC. Across those calls, Aquifer transferred genuine assets from its vaults while the attacker paid no tokens into the venue.

The supported explanation is an account and program validation failure. The attacker created 165-byte accounts that resembled legitimate SPL token accounts but were owned by a malicious program rather than the SPL Token Program. One forged account represented an impossible balance of approximately 18 trillion USDC. The attacker also supplied the malicious program as the incoming token program; it accepted the transfer-shaped instruction, moved nothing, and returned success.

Aquifer has not published source code. The on-chain behavior is consistent across all 212 successful calls, but the exact missing source-level checks are reconstructed rather than confirmed against code. The incident, loss, and address linkage are high confidence; the precise source-level root-cause classification is medium-high confidence.

## Direct Attacker and Proceeds Indicators

| Network | Address | Role | Confidence | Treatment |
|---|---|---|---|---|
| Solana | [`7fTe9pvrwXJRBHq9MaSyVPR4PgEuhqLiA93Dxf4gRk7J`](https://solscan.io/account/7fTe9pvrwXJRBHq9MaSyVPR4PgEuhqLiA93Dxf4gRk7J) | Primary attacker, exploit execution, and proceeds wallet | High | P1 direct watch |
| Solana | [`DMBpPMaMpGM2mWiUMaqcHx9FwhPg9Ys7qg1X59NRgb68`](https://solscan.io/account/DMBpPMaMpGM2mWiUMaqcHx9FwhPg9Ys7qg1X59NRgb68) | Malicious program impersonating the incoming token program | High | P1 malicious infrastructure and control-path pivot |
| Ethereum | [`0x2Dfe9e969796e2797278b02761dd9Ad6aE922746`](https://etherscan.io/address/0x2Dfe9e969796e2797278b02761dd9Ad6aE922746) | Cross-chain attacker and proceeds-consolidation wallet | High | P1 direct watch |

Bitquery reviewed all 379 transactions in the Solana attacker's history and reported that no other wallet called the malicious program during the attack. GoPlus independently published the same Solana and Ethereum attacker addresses and the complete malicious-program identifier.

Aquifer's on-chain whitehat offer, authorized through the program's upgrade authority, named the same Solana and Ethereum addresses. That protocol-origin message materially strengthens the original third-party attribution.

## Exploit and Proceeds Path

The repeated attack pattern was:

1. Supply a forged 165-byte account that resembles an SPL token account but is owned by the attacker's program.
2. Claim an impossible incoming balance and nominate the malicious program as the token program for the payment leg.
3. Cause Aquifer to transfer a genuine asset from its vault through the legitimate token program.
4. Have the malicious program accept the payment-shaped call, transfer nothing, and return success.
5. Convert the extracted assets to SOL and move the proceeds to Ethereum.

Bitquery reconstructed 24,082 SOL received through 54 fills and 24,084 SOL leaving in three transfers. The three matched cross-chain movements produced approximately 871.86 ETH, 122.51 ETH, and 6.43 ETH, totaling 1,000.7956 ETH at the Ethereum proceeds address.

At Bitquery's September 1 cutoff, the Ethereum address had received three transfers and sent none. That is a point-in-time observation, not a guarantee that the balance remains unmoved.

## Reconstructed Asset Loss

| Asset group | Approximate value at September 1 prices |
|---|---:|
| USDC | $1,281,035 |
| USDT | $459,371 |
| HYPE | $183,654 |
| cbBTC | $136,123 |
| Fourteen other assets | $409,546 |
| **Total** | **$2,469,729** |

The dollar total uses September 1 spot prices. The exact SOL and ETH quantities are independent of that valuation choice.

## Victim and Recovery Infrastructure — Do Not Threat-Label

| Network | Address | Role | Handling |
|---|---|---|---|
| Solana | [`AQU1FRd7papthgdrwPTTq5JacJh8YtwEXaBfKU3bTz45`](https://solscan.io/account/AQU1FRd7papthgdrwPTTq5JacJh8YtwEXaBfKU3bTz45) | Aquifer victim program | Protocol infrastructure; never inherit attacker label |
| Solana | [`GtwzYxBQcPFNFQcYbdELuaKzb4DGJpGVU2ehLhzbffCw`](https://solscan.io/account/GtwzYxBQcPFNFQcYbdELuaKzb4DGJpGVU2ehLhzbffCw) | Affected USDC vault | Victim vault; exploit-flow reconstruction only |
| Solana | [`7C7Y3fyPYeAYqpc29uahDUQ84PQ255Avj2YEP9KpvyKx`](https://solscan.io/account/7C7Y3fyPYeAYqpc29uahDUQ84PQ255Avj2YEP9KpvyKx) | Affected USDT vault | Victim vault; exploit-flow reconstruction only |
| Solana | [`AwtZZUJsRGLje9c5wE9q7zMNjA9ZkEuxTk8awBza14kr`](https://solscan.io/account/AwtZZUJsRGLje9c5wE9q7zMNjA9ZkEuxTk8awBza14kr) | Affected WSOL vault | Victim vault; exploit-flow reconstruction only |
| Solana | [`DKCGgPdyLcPFJGTZzkhYeenEUWXPu5VED5ourTrW8PAM`](https://solscan.io/account/DKCGgPdyLcPFJGTZzkhYeenEUWXPu5VED5ourTrW8PAM) | Affected WETH vault | Victim vault; exploit-flow reconstruction only |
| Solana | [`8af8RnAgyKzNt4fjDaP8w8pBekYVux1ja4AofavRyjox`](https://solscan.io/account/8af8RnAgyKzNt4fjDaP8w8pBekYVux1ja4AofavRyjox) | Aquifer-designated recovery address | Recovery infrastructure; alert only for restitution |
| Ethereum | [`0xb7EAA8cd5dFAD8021d9fB19c8a21613679f268F5`](https://etherscan.io/address/0xb7EAA8cd5dFAD8021d9fB19c8a21613679f268F5) | Aquifer-designated recovery address | Recovery infrastructure; alert only for restitution |

The affected program, vaults, recovery addresses, routers, bridges, settlement wallets, market makers, and ordinary counterparties must not inherit the attacker label merely because they occur in the transaction path.

## Whitehat Offer and Residual Risk

At 16:43 UTC on August 31, Aquifer published an on-chain message requesting the return of at least 80% of the assets by September 3 at 14:00 UTC and allowing the controller to retain 20% as a bounty. No return was observed at Bitquery's September 1 verification cutoff.

Bitquery also reported that Aquifer's program had not been upgraded after the exploit and that all 45 vaults held only about $70 at the September 1 cutoff. The public transaction pattern indicated that the same path could remain viable if liquidity returned. This status is time-sensitive and should be revalidated before relying on it operationally.

## Monitoring Priorities

1. Watch the Solana attacker wallet for program reuse, fresh funding, token-account creation, swaps, bridge activity, and recovery transfers.
2. Alert on any call to or interaction with the malicious program, especially if Aquifer liquidity is restored.
3. Watch the Ethereum proceeds address for movement, exchange deposits, bridges, mixers, OTC routing, or restitution.
4. Alert on payments to the two Aquifer-designated recovery addresses, but retain their non-attacker classification.
5. Keep the affected Aquifer program and vaults as transaction-filtering and loss-reconstruction pivots.
6. Do not ingest the truncated forged-account or transaction identifiers rendered in Bitquery's public article unless their complete values are independently published.

## Attribution Boundaries

- No named person or threat group is established.
- The Solana wallet and Ethereum wallet are direct P1 attacker/proceeds seeds.
- The malicious Solana program is P1 exploit infrastructure, not a wallet.
- Aquifer's program and vaults are victim infrastructure.
- Aquifer's two return addresses are recovery infrastructure.
- Shared settlement wallets, routers, bridges, market makers, and ordinary traders are graph context only.
- The precise source-code flaw is inferred from the on-chain instruction pattern because Aquifer has not published source code.
- Injective and Tectonic are documented separately as zero-seed cases until complete attacker identifiers are available.

## Sources

- [Bitquery — complete Aquifer on-chain reconstruction, loss accounting, proceeds path, whitehat offer, and scope limits](https://bitquery.io/investigations/aquifer-solana-hack-2-5-million)
- [GoPlus Security — complete attacker wallets, malicious program, affected program, and vault identifiers](https://x.com/GoPlusSecurity/status/2094757173121204271)
- [Defimon Alerts — Aquifer on-chain whitehat offer and recovery addresses](https://x.com/DefimonAlerts/status/2094467984030826622)
- [Solscan — primary Solana attacker wallet](https://solscan.io/account/7fTe9pvrwXJRBHq9MaSyVPR4PgEuhqLiA93Dxf4gRk7J)
- [Etherscan — Ethereum proceeds wallet](https://etherscan.io/address/0x2Dfe9e969796e2797278b02761dd9Ad6aE922746)

---

## TLDR

Aquifer lost $2,469,729 through 212 one-sided swaps after accepting forged token-account data and an attacker-supplied fake token program. The direct monitoring set contains the Solana attacker wallet, the malicious Solana program, and the Ethereum proceeds wallet. Aquifer's program, vaults, recovery addresses, routers, bridges, and settlement counterparties remain explicitly non-attacker infrastructure.
