# Crypto Wallet Analysis

## Overview

This document provides a compact index of cryptocurrency wallets retained for ongoing defensive analysis. Detailed evidence, attribution limits, transaction data, and source links belong in each linked case directory.

> Verify every address, network, and attribution before using this index. A listed operational pivot is not automatically a threat-controlled wallet.

## Existing Tracking List

1. **Under analysis:** `2GsFJ1JR1j8RAWuUfdJPXdjknq5VmKG9XSfoTZdqQeoR`
2. **Under analysis:** `0xAAcE3E2dB13C372C74BDaE118f045D49daC8AE18`
3. **Sam Bankman-Fried / Alameda Research 25:** `0x84D34f4f83a87596Cd3FB6887cFf8F17Bf5A7B83`
4. **Fz Pamajj — Burner 2:** `3LT9mkc7yQTofJVa3MSeEFg15Wehk4y7ZWwmfmUu7qvx`
5. **Fz Pamajj — Burner 1:** `41tCXQbqaTDfkYzEPRQzkL1d8kVck7GgCXQsMcT7bnUk`
6. **Fz Pamajj — Main:** `HSRjRJmTu9UVugqNea2X2WVFnb329SywgBGipJhMLKU5`
7. **Alex Becker — Main:** `0xaE4D837cAA0C53579f8a156633355Df5058B02f3`
8. **Alex Becker — USDC Cash Out:** `0x907b322d33121a50a9f7bc5305761b0ca40c6113`
9. **Alex Becker — Sidus/Senate:** `0x5E6119CC5881598eA9F10521BAE21EF8AAF612d3`
10. **Alex Becker — Dalarnia:** `0x128f0081Fdcb8b902fF0f45Ae90bBE93d87dF47b`
11. **Kmoney / kmoney.sol:** `7byBtWp7uW8eYNs1N4uDesGf5hw8gkCdbPUWi6ckyUNX`
12. **Dusting-attack wallet:** `777vxoS8tWgLEgr6yMp5scadhnWxkksRKDMQFBJKD24N`
13. **0xfxnction / kingofsolanabeach.sol:** `6SFShytsPZ61KuauRbBppAcs6WwuNXmEHpFxBUp68EKP`
14. **Hacked Facebook account / Faith Spires:** `bc1q9etmuux673pkrtqsh6m3fratuqxw22nc70s2gu`
15. **Hacked Facebook account / Faith Spires:** `3B8PAG1ynzghVixBNDfGAijfWthob8sgQo`
16. **Hacked Facebook account / Hollie Harvell:** `35jFVWx6fNUV8QA5vsVtw6iXE5XpBDFJet`
17. **Luwizop / Panic Station Pythons:** `3YaGKXSuxwfvKiJ83V92hKRvh23w1RdYgrwY7C5CSNG6`

---

## Zunami Protocol Exploit Cluster

**Network:** Ethereum  
**Confidence:** Medium  
**Case file:** [`EVM/Ethereum/Zunami-Protocol/`](./EVM/Ethereum/Zunami-Protocol/)

### Direct Threat Seeds

| Address | Classification | Monitoring |
|---|---|---|
| `0x5f4C21c9Bb73c8B4a296cC256C0cDe324dB146DF` | 2023 attacker EOA / exploit seed | Watch directly |
| `0x051370419b871F7C05dEE8f7134401530832e250` | 2025 attacker EOA / privileged-access drain | Watch directly |
| `0xF00d0e11AcCe1eA37658f428d947C3FFFAeaDe70` | Pre-exploit staging and operational wallet | Watch directly |
| `0x12e98c4EBD742ca9465789570e5cf4Df9EEd0Fb0` | Accumulation and cash-out wallet | Watch directly |

### Operational Pivots — Not Automatically Threat-Labeled

| Address | Classification | Handling |
|---|---|---|
| `0xe9b2B067eE106A6E518fB0552F3296d22b82b32B` | Zunami deployer / privileged wallet | Graph-expansion pivot only |
| `0xF9605D8c4c987d7Cb32D0d11FbCb8EeeB1B22D5d` | `sterx.eth`, operationally linked to deployer | Graph-expansion pivot; inferential attribution |

---

## Ostium Oracle-Manipulation Exploit

**Network:** Arbitrum One  
**Chain ID:** `42161`  
**Wallet confidence:** High  
**Case file:** [`EVM/Arbitrum/Ostium/`](./EVM/Arbitrum/Ostium/)

### Direct Threat Seeds

| Address | Classification | Priority |
|---|---|---|
| `0x321Df194646029e7A6193Ea05573d4B9c398bfD9` | Primary payout and consolidation wallet / Ostium Exploiter 1 | Highest-priority direct watch |
| `0xD1794196f0fc99c7f27970e661597d77d9a85869` | Exploit execution and transaction-origin wallet / Ostium Exploiter 2 | Direct watch |

### Infrastructure Pivot — Not an Attacker EOA

| Address | Classification | Handling |
|---|---|---|
| `0xfE12F6360000dE49D5506d52eE5aC4bC9Dd5bd2E` | Exploit entry contract | Control-path and graph-expansion pivot only |

---

<h2>Triple-A Treasury-Wallet Compromise</h2>

<p>
  <strong>Incident window:</strong> July 24–25, 2026<br>
  <strong>Primary network:</strong> Ethereum<br>
  <strong>Incident confidence:</strong> High<br>
  <strong>Address-linkage confidence:</strong> High<br>
  <strong>Direct-control confidence:</strong> Medium to high<br>
  <strong>Named actor:</strong> None identified<br>
  <strong>Case file:</strong>
  <a href="./Multi-Chain/Triple-A/">
    Multi-Chain/Triple-A
  </a>
</p>

<h3>Direct-Watch Address</h3>

<table>
  <thead>
    <tr>
      <th align="left">Address</th>
      <th align="left">Classification</th>
      <th align="left">Monitoring</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <a href="https://etherscan.io/address/0x01F83B5d4fb30E8AA3daC1681B4048D9135253b1">
          <code>0x01F83B5d4fb30E8AA3daC1681B4048D9135253b1</code>
        </a>
      </td>
      <td>
        Primary stolen-fund consolidation and holding address
      </td>
      <td>
        Highest-priority direct monitoring and graph expansion
      </td>
    </tr>
  </tbody>
</table>

<p>
  The address received approximately 5,287.08568411 ETH across 12 inbound
  transfers on July 24–25, 2026. Triple-A confirmed unauthorized access
  to its treasury wallets but did not formally publish or attribute this
  address.
</p>

<h3>Related Indicators Under Review</h3>

<table>
  <thead>
    <tr>
      <th align="left">Network</th>
      <th align="left">Address</th>
      <th align="left">Handling</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EVM network unresolved</td>
      <td><code>0x8335D258438E47Cd8EB1532C04Cfe445E011aEf6</code></td>
      <td>Graph-expansion pivot; do not automatically threat-label</td>
    </tr>
    <tr>
      <td>Solana</td>
      <td><code>EdtthafhQA23if9PcZvBLhKb9uJM7M6TeyNXozDDon3K</code></td>
      <td>Graph-expansion pivot; do not automatically threat-label</td>
    </tr>
    <tr>
      <td>TRON</td>
      <td><code>TRSr81kTZAL2zMoWBsjE4QBc9B4v8WpSkw</code></td>
      <td>Graph-expansion pivot; do not automatically threat-label</td>
    </tr>
    <tr>
      <td>TRON</td>
      <td><code>TNLLM9z6b1TtpcXXaAg4Gb9dFyG11x187a</code></td>
      <td>Graph-expansion pivot; do not automatically threat-label</td>
    </tr>
    <tr>
      <td>EVM network unresolved</td>
      <td><code>0x6caC9dB6A61bC4bEA37086DD6DaA6eCa35Dbc1d7</code></td>
      <td>Graph-expansion pivot; do not automatically threat-label</td>
    </tr>
  </tbody>
</table>

<p>
  The five related addresses were disclosed in connection with the
  incident, but their exact roles have not been sufficiently established.
  They may represent attacker wallets, compromised Triple-A source
  wallets, or intermediate routing addresses.
</p>

---

## Across Protocol Solana Relayer Exploit

**Incident date:** July 17, 2026  
**Origin network:** Solana  
**Destination scope:** 18 reported chains  
**Incident confidence:** High  
**Address-linkage confidence:** High  
**Named actor:** None identified  
**Case file:** [`Multi-Chain/Across-Protocol/`](./Multi-Chain/Across-Protocol/)

### Direct Incident-Watch Seeds

| Network | Address | Classification | Monitoring |
|---|---|---|---|
| Solana | `8bkoZToaTBBtAPczgHqD4XVxWtvBkiy4crtexEtYDYSL` | Incident-linked Solana investigation and orchestration seed | Watch directly and expand through source transactions and program calls |
| EVM role under review | `0xa0C0e9f307b5A26cA3FB5891c19154fc7A02BeF7` | Incident-linked EVM investigation seed | Watch directly and review destination fills and proceeds flows |
| EVM role under review | `0xA6fb971F3B7a9b9F76EdA76bc89268fe26560189` | Incident-linked EVM investigation seed | Watch directly and review destination fills and proceeds flows |

### Recovery and Protocol Infrastructure — Do Not Threat-Label

| Network | Address | Classification | Handling |
|---|---|---|---|
| Ethereum | `0xB524735356985D2f267FA010D681f061DfF03715` | Across Protocol Hub Pool Owner multisig and reported recovery destination | Preserve as protocol infrastructure and recovery evidence only |

The attack exploited off-chain event-reading software rather than directly draining an Across smart contract. The parser accepted forged Solana deposit event representations and caused the Risk Labs relayer to advance its own destination-chain funds.

The three published investigation addresses are suitable for direct incident monitoring. No named attacker attribution has been established, and connected protocol, bridge, exchange, token, router, or counterparty addresses should not be automatically threat-labeled.

---

## Verus–Ethereum Bridge Exploit

**Incident date:** July 23, 2026  
**Networks:** Verus and Ethereum  
**Incident confidence:** High  
**Address-linkage confidence:** High  
**Named actor:** None identified  
**Case file:** [`Multi-Chain/Verus-Ethereum-Bridge/`](./Multi-Chain/Verus-Ethereum-Bridge/)

### Direct Threat-Wallet Seeds

| Network | Address | Classification | Monitoring |
|---|---|---|---|
| Ethereum | `0xBda71b58cEc0b1C20A8f87cCD52FA0679747855c` | Exploit execution and malicious proof-relay wallet | Watch directly |
| Ethereum | `0xCFd0A20703cD11E0b9f665e1C3F1Ef989C142D54` | Profit, consolidation, swap, and laundering wallet | Highest-priority direct watch |
| Verus | `RXo2PqXjgRVJ8w8QVDErVqVLavz4TToyuu` | Source-chain export and cross-chain exploit seed | Watch directly |

### Victim, Technical, and Laundering Infrastructure

| Network | Address | Classification | Handling |
|---|---|---|---|
| Ethereum | `0x71518580f36FeCEFfE0721F06bA4703218cD7F63` | Compromised Verus–Ethereum Bridge | Victim infrastructure; graph-expansion only |
| Ethereum | `0x54e03a1682fd0bb065b669f6296f97028dcfd4ce` | VerusProof contract | Technical pivot only; not attacker-controlled |
| Ethereum | `0xd90e2f925DA726b50C4Ed8D0Fb90Ad053324F31b` | Tornado Cash router | Laundering-path infrastructure; do not label as attacker |

The July attack used the same bridge contract, entry path, and general vulnerability class reported in the May 2026 incident, but public reporting described a different attacker and new wallet set.

Do not merge the May and July wallet clusters without independent evidence of shared funding, control, infrastructure, or laundering activity.

---

## Genesis-Era Solana Whale Drain

**Incident window:** July 10–13, 2026  
**Origin network:** Solana  
**Downstream network:** Ethereum  
**Incident confidence:** High for the published flow; medium-high for theft characterization  
**Compromise vector:** Unknown  
**Named actor:** None identified  
**Case file:** [`SOL/Genesis-Whale-Drain/`](./SOL/Genesis-Whale-Drain/)

### Direct Incident-Watch Seeds

| Network | Address | Classification | Monitoring |
|---|---|---|---|
| Solana | `Ffd1oB2aYM5UzMYUM7TmxULDRQb6KzgrBwmgj9U1C2bE` | Theft-linked address published by ZachXBT | Watch directly and expand victim transfers, swaps, consolidation, and bridge preparation |
| Solana | `653pnn5fzF51FfotBwxua55Es4QXxTdaXJLbPczVmswp` | Theft-linked address published by ZachXBT | Watch directly and expand Solana-side graph and bridge activity |
| Ethereum | `0xaa5cfa4e96dda0f9aa30f4dc948b542a9b5817c6` | Theft-linked address published by ZachXBT | Watch directly for downstream proceeds activity |
| Ethereum | `0x536b4ee7507c41143e1b0bd1bf3f2b84be404836` | Theft-linked address published by ZachXBT | Watch directly for downstream proceeds activity |
| Ethereum | `0xbf11bdfbeb9ed137c352c81e45d191cacae6b0cf` | Theft-linked address published by ZachXBT | Watch directly for downstream proceeds activity |

### Victim Address — Do Not Threat-Label

| Network | Address | Classification | Handling |
|---|---|---|---|
| Solana | `HwtbQBNnLERakdUDuCCLWmUs2oETLFQZeHUWeQdPads` | Genesis-era victim wallet | Preserve for source-flow reconstruction; do not classify as attacker-controlled |

No public evidence currently establishes how the victim wallet was compromised. Do not describe this as a Solana protocol exploit or assert a stolen key, seed phrase, compromised hardware wallet, or malicious signer without additional evidence.

---

## SUNUSI Permanent-Delegate Drain

**Incident date:** July 13, 2026  
**Network:** Solana  
**Incident confidence:** Medium-high  
**Named actor:** None identified  
**Case file:** [`SOL/SUNUSI/`](./SOL/SUNUSI/)

### Direct Incident-Watch Seeds

| Address | Classification | Monitoring |
|---|---|---|
| `BUrnPq1dRv7gxjdh5MM2mF51GYBkfLSUyAWx2zcgot6j` | Malicious burn contract / Permanent Delegate authority pivot | Watch directly and expand deployer funding, authority grants, and victim interactions |
| `Ah4mTqci95qbiydovW8123q2WQzMSCP3MiCzGR2Pje7n` | Attacker / proceeds wallet | Highest-priority direct watch for token sales, SOL consolidation, exchange deposits, and related campaigns |

The reviewed on-chain analysis supports malicious authorization abuse rather than a private-key compromise. SUNUSI is not currently classified as a confirmed rug pull or a Solana protocol exploit.

---

## Dmytro Rashevskyi / First VPN Service (1VPNS)

**Designation date:** July 13, 2026  
**Networks:** Bitcoin, Ethereum, Solana, Litecoin, Zcash, Dash, TRON, Dogecoin  
**Source type:** Official OFAC SDN List update  
**Confidence:** High  
**Case file:** [`1VPNS/`](./1VPNS/)

### BTC / ETH / SOL Direct Sanctions-Watch Seeds

| Network | Address | Attribution | Monitoring |
|---|---|---|---|
| Bitcoin | `1MTndG4K51RRMvkzyvguaHnQpiMLnxFGzM` | Dmytro Rashevskyi | Watch directly |
| Bitcoin | `1DfyWkiXVVqWfcSduj23qTDis9kb2qvRDa` | Dmytro Rashevskyi | Watch directly |
| Ethereum | `0x1d19b52b54e7ef5ea1a4b40b616165e798eac9f8` | Dmytro Rashevskyi | Watch directly |
| Ethereum | `0x2C7DcD774b33e10367F7d6385479e04F97d179dc` | Dmytro Rashevskyi | Watch directly |
| Solana | `Fc1EwQUZyTEagaDvA1utHXCcZNyG1x2PLt2DfNu1cJdH` | Dmytro Rashevskyi | Watch directly |
| Solana | `FuCC7GoYwt5TsNTjWL23Xx9UKCvC18chjMEFPL3vJDCC` | Dmytro Rashevskyi | Watch directly |
| Bitcoin | `bc1qdnr88f4d2yqunnc4mjsguezm6g3mlwe44z5dw8` | First VPN Service / 1VPNS | Watch directly |
| Bitcoin | `bc1qr4ankqmvmrhce3ydvzse86dfx5s3zhehfr9tg9` | First VPN Service / 1VPNS | Watch directly |
| Ethereum | `0x2711d73d559f62f4f855ee21f38378f528e07985` | First VPN Service / 1VPNS | Watch directly |

### Cross-Chain High-Confidence Sanctions Seeds

| Network | Address | Attribution | Monitoring |
|---|---|---|---|
| Litecoin | `LcP1DumXkNJbBtSYD3XxAfsJ2nZR5hLdpM` | Dmytro Rashevskyi | Watch directly |
| Litecoin | `LbPAqHvemZBv3pvAqiAtDnZ3U1t6EziaL1` | Dmytro Rashevskyi | Watch directly |
| Zcash | `t1LHesgnkapziGQCJtrfZWYXhyjfTVo1dvh` | Dmytro Rashevskyi | Watch directly |
| Dash | `XcuGqRfrR85zyDrzVr1gSL5RNjwwpbu2KS` | Dmytro Rashevskyi | Watch directly |
| Dash | `XowUeMFa1FkEUnAHL78E5oqpezMfSB6xP1` | Dmytro Rashevskyi | Watch directly |
| TRON | `TTLRNgLpz5H5tLPuNU4FViUs7zmmAtyvzW` | Dmytro Rashevskyi | Watch directly |
| TRON | `TBFW9gF4oDX5cG44gS7AoxQeujScmm3z6h` | Dmytro Rashevskyi | Watch directly |
| Dogecoin | `DHzAVdEoL3PjGeLWNdEJwwMA1CeQ9J9Cpo` | Dmytro Rashevskyi | Watch directly |
| Dogecoin | `DTqpKQ96rqkTvHcohQQd9BksmgRjasHgGo` | Dmytro Rashevskyi | Watch directly |
| Litecoin | `ltc1qr8ntsedq8tv0svmxqhzvdcdl5k7kntdmnhwep7` | First VPN Service / 1VPNS | Watch directly |
| TRON | `TUuaxBAWfA5nmsqNfycxYrzEvz4a5GJMGY` | First VPN Service / 1VPNS | Watch directly |

All listed identifiers are official OFAC digital-currency identifiers. Connected customer wallets, exchanges, hosting providers, routers, or counterparties should initially be treated as graph-expansion pivots unless separately attributed.

---

## DeFiTuna Lending Exploit

**Incident date:** July 16, 2026  
**Origin network:** Solana  
**Downstream network:** Ethereum  
**Incident confidence:** High  
**Named actor:** None identified  
**Case file:** [`SOL/DeFiTuna/`](./SOL/DeFiTuna/)

### Direct Incident-Watch Seeds

| Network | Address | Classification | Monitoring |
|---|---|---|---|
| Solana | `9ytGWP8tCRF1keREJ5VHqBpSuM9MZYwm3oFQQa1SvESb` | Attacker 1 / orchestration seed | Watch directly |
| Solana | `917DKTphW3rhBG5gsJpwKsNGisNV2dx74uUFd8HBEjtg` | Attacker 2 / fake pool | Watch directly; preserve dual role |
| Solana | `7hiHL8AgDuLNVDQLfN3GHdLAEeCN1F7uz6nSANRvFJst` | Attacker 3 / malicious limit-order owner | Watch directly and trace Mayan bridge activity |
| Solana | `BK9aTnKfPNnnj45Me5ACrky2vexzUrZHRzr4BjmQpH3c` | Attacker 4 / malicious limit-order owner | Watch directly and trace Mayan bridge activity |
| Solana | `8P3H7Hy98LWhw5QhuXdoigVdAzPCYRTYjdtQQKhGwvqD` | Attacker 5 | Direct incident seed; confirm narrower role transaction-by-transaction |
| Solana | `GrXBhM6Ty6YxubFp8zubtJF12WXmKj1dhMyakRPeaDpo` | Attacker 6 | Direct incident seed; confirm narrower role transaction-by-transaction |
| Solana | `F4xUroPaHro4gb2JAqa3e93E7DdZytRQJ4L2cHT5E53p` | Attacker 7 | Direct incident seed; confirm narrower role transaction-by-transaction |
| Solana | `ETGhosPrFApbiiKXDpxrhBz7J2MdTA3dxnL2Nkio9vEX` | Attacker 8 | Direct incident seed; confirm narrower role transaction-by-transaction |
| Solana | `4ZKkGZuoXqgSHbmsJXUib3dgn5WNhzbPEXrxuMYJ5oQ3` | Attacker 9 | Direct incident seed; confirm narrower role transaction-by-transaction |
| Ethereum | `0x509B9D094A6C26D716aaC131E8aDee5B16B86d3e` | Cross-chain proceeds / consolidation wallet | Watch directly for dispersal, exchange deposits, bridge reuse, and privacy interactions |

### Victim and Protocol Infrastructure — Do Not Threat-Label

| Network | Address | Classification | Handling |
|---|---|---|---|
| Solana | `tuna4uSQZncNeeiAMKbstuxA9CUkHH6HmC64wgmnogD` | DeFiTuna program | Protocol infrastructure; graph filtering only |
| Solana | `D76dDcSU5HnAGqVEZCDLyGgLpTp4xZuqeZyVDtUdDv55` | Damaged USDC vault | Victim infrastructure; preserve for loss reconstruction |

CertiK reported that proceeds from the two malicious liquidity-position owners were bridged through Mayan to Ethereum, with 140 ETH deposited into Railgun and 291,696 DAI plus 5 ETH remaining in the published Ethereum wallet as of July 20, 2026.

---

## Central Bank of Iran — TRON Address Expansion

**Material update date:** July 14, 2026  
**Network:** TRON  
**Source type:** Official OFAC SDN List update  
**Confidence:** High  
**Case file:** [`TRON/Central-Bank-of-Iran/`](./TRON/Central-Bank-of-Iran/)

### Direct Sanctions-Watch Seeds

| Address | Status | Monitoring |
|---|---|---|
| `TNiq9AXBp9EjUqhDhrwrfvAA8U3GUQZH81` | Existing OFAC identifier retained | Watch directly |
| `TTiDLWE6fZK8okMJv6ijg42yrH6W2pjSr9` | Existing OFAC identifier retained | Watch directly |
| `TAhwhFv3JpK39Nc2m8W5LPCcoTisutiRfp` | Newly added July 14, 2026 | Watch directly and prioritize historical-flow review |
| `TJdgB1k6ot3f2nLuZug6D8eD3HavTmzmSK` | Newly added July 14, 2026 | Watch directly and prioritize historical-flow review |
| `TXGHxdYbGy574z5hBu4LNzq9NzjZQ9bhUf` | Newly added July 14, 2026 | Watch directly and prioritize historical-flow review |
| `TFQbqaNbmq2xsVor2NbufLkYZvxFC9wC7k` | Newly added July 14, 2026 | Watch directly and prioritize historical-flow review |

The July action materially expanded an existing sanctioned-wallet attribution. Transactional proximity to these addresses should not automatically transfer the Central Bank of Iran or OFAC label to counterparties.

---

## El-Kahira / Zaid Issam Ahmed Al-Jebouri

**Designation date:** July 23, 2026  
**Network:** TRON  
**Source type:** Official OFAC SDN List update  
**Confidence:** High  
**Case file:** [`TRON/El-Kahira/`](./TRON/El-Kahira/)

### Direct Sanctions-Watch Seeds

| Address | Classification | Monitoring |
|---|---|---|
| `TPyE2oSoaysrXfLzwf9wetBVr9JudLwjtD` | Official OFAC blocked identifier | Watch directly |
| `TVgUsVzA7mpFExP4zS7HHbtKti6UuBDuwZ` | Official OFAC blocked identifier | Watch directly |
| `TLoG3vbjDgqmTD5bM7w9rMgA6ysaNReuRy` | Official OFAC blocked identifier | Watch directly |
| `TAhHpxPRwo1Bmm1A9m51uZ31tcB7EPq7SY` | Official OFAC blocked identifier | Watch directly |
| `TScXZTbDjjZ6a6jiC7dZjgCqfNo4vm7atV` | Official OFAC blocked identifier | Watch directly |
| `TGr2i8ZQiiMRjP3mWyQUH2MQBfKu8GJNqm` | Official OFAC blocked identifier | Watch directly |
| `THJUJFyTnrBWb1ijWav7qfRBrjUuKgP49Z` | Official OFAC blocked identifier | Watch directly |

OFAC directly attributed these TRON identifiers to Zaid Issam Ahmed Al-Jebouri and linked him to El-Kahira for General Trading. Connected exchanges, OTC services, bridges, token contracts, and counterparties should initially remain graph-expansion pivots unless separately attributed.
---

## August 20, 2026 Multi-Chain Security Sweep

**Review cutoff:** August 20, 2026 at 2:31 a.m. ET  
**Case file:** [`Multi-Chain/August-2026-Security-Sweep/`](./Multi-Chain/August-2026-Security-Sweep/)  
**Machine-readable seeds:** [`addresses.csv`](./Multi-Chain/August-2026-Security-Sweep/addresses.csv)

### Direct Incident-Watch Seeds

| Incident | Network | Address | Classification | Confidence | Monitoring |
|---|---|---|---|---|---|
| Maya Protocol | MAYAChain | `maya1dl3yrfpedyr5jfr0r86s2apjltnjqgszmwsv8x` | Attacker address | High | P1 direct watch |
| FoxMarket | BNB Chain | `0x5670d36f00bc7f6860b6afddb288e3668efc0ef9` | Attacker controller | High | P1 direct watch |
| Hyperliquid impersonation | Ethereum | `0x98b2761559A348968C994D9856dCfc96B6f13C55` | Phishing proceeds recipient | Medium-high attribution | P1 direct watch |
| Hyperliquid impersonation | Ethereum | `0x93b6B24DC6E6a1D5d72399e3A35498c4DbA1d6D1` | Phishing proceeds recipient | Medium-high attribution | P1 direct watch |
| Hyperliquid impersonation | Ethereum | `0x6fE314fD4CF845f35fc461eD98e2FB8d9356B566` | Phishing proceeds recipient; appears in other phishing reporting | Medium-high attribution | P1 direct watch; do not assume campaign exclusivity |
| Ethereum whale drain | Ethereum | `0x8fEB0c6eF08B20bA19C04F951d4408bB5A1F95Ae` | Theft and consolidation address | High | P1 direct watch |
| Address-poisoning theft | Ethereum | `0xAe7c08afAD91db18666EEAC055D7562c9f4e2c85` | Look-alike poisoning address | High | P2 direct watch |

### Harmony Incident Accounts

The native and hexadecimal strings in each row are alternate representations of one Harmony account. This table contains four accounts, not eight wallets.

| Harmony address | Hex equivalent | Classification | Monitoring |
|---|---|---|---|
| `one1uap8dx2z0qsjxqthm5flgcxkeepsz3gsrghnfn` | `0xe7427699427821230177dd13f460d6ce43014510` | Unauthorized-mint incident account | P1 direct watch |
| `one17u300a40ll5wphd8kj5hktryhdjq3ml9f4phy4` | `0xf722f7f6afffe8e0dda7b4a97b2c64bb6408efe5` | Unauthorized-mint incident account | P1 direct watch |
| `one1a5hur07z5vtvzhr35zkw8tfqedemkz8t88xgd7` | `0xed2fc1bfc2a316c15c71a0ace3ad20cb73bb08eb` | Unauthorized-mint incident account | P1 direct watch |
| `one1h56hkxmua0uzfv07fu04cudvtrl35u96pq47vy` | `0xbd357b1b7cebf824b1fe4f1f5c71ac58ff1a70ba` | Unauthorized-mint incident account | P1 direct watch |

### Incident-Linked Laundering Pivot

| Incident | Network | Address | Classification | Confidence | Handling |
|---|---|---|---|---|---|
| Coldcard weak-entropy theft | Ethereum | `0x41B7529a411EeA979a8d468bdEBd36b0ad703268` | BTC-to-ETH bridge and Tornado Cash pivot | High linkage; medium actor clustering | Watch directly as a laundering pivot; do not label as the sole Coldcard attacker |

### Explicit Exclusions

| Incident | Indicator | Why excluded from threat seeds |
|---|---|---|
| FoxMarket | `0x9fa6d8a13b35e051bfc145918db0111dec13d1a0` | Victim contract |
| Address poisoning | `0x9B4Ded0ab7754428F7eC0f63a42bAe70D2f51D83` | Victim address |
| Address poisoning | `0xae7C0ffAB6e77BE2D7d7880a4Ce433F59A4e2c85` | Intended legitimate recipient |
| ODY | `0x486f…` and `0xd2c85d49b…` | Truncated identifiers; insufficient for machine-readable attribution |
| Vultisig-related outflow | No complete source address retained | Exploit status and direct attribution remain unresolved |

Fake AMLBot and AML-checker sites are tracked as a high-confidence wallet-drainer TTP without an invented address cluster. Hyperliquid itself was not exploited; that case concerns a fraudulent sponsored result and impersonation site targeting a user.

### August 21 Follow-Up: External-L1 and Coinsbuy Seeds

| Incident | Network | Address | Classification | Confidence | Monitoring |
|---|---|---|---|---|---|
| Maya Protocol | Bitcoin | `bc1q0hsgwunccczelq05ucpmfz268eyy5jr2y5l646` | Exploit-proceeds consolidation address; approximately 20.83 BTC | High | P1 direct watch |
| Maya Protocol | Arbitrum | `0xa2f246f82995CBcCA8eD0d9F251383881A5E423e` | Secondary exploit-proceeds address | Medium-high | P2 direct watch |
| Coinsbuy | Ethereum | `0x4d1bEF2Fe998B3E3C4029EF9EA6A0534d95661d3` | Theft/proceeds address | High incident linkage | P1 direct watch |
| Coinsbuy | Ethereum | `0x66790b54B891e2ebdef58a15B969Ff6fb4374b17` | Theft/proceeds address | High incident linkage | P1 direct watch |
| Coinsbuy | TRON | `TVpX9xCzrj6KHeNhhDJoqjzEqFMxdgubGR` | Theft/proceeds address | High incident linkage | P1 direct watch |

The Coinsbuy access vector remains unresolved; simultaneous Ethereum/TRON activity does not by itself prove private-key compromise, API compromise, or insider access. The Allbridge August Base/CCTP incident is documented as a second exploit but contributes no direct-watch seed because no complete attacker identifier was available in authoritative reporting.

The Harmony native and hex identifiers above remain four underlying accounts, not eight. No new complete qualifying Solana threat address was identified in the follow-up scan. Truncated Lazarus BTC destinations and other incomplete identifiers remain excluded.

---

## August 22 Follow-Up: Bofur Capital Address Poisoning

**Case file:** [`Multi-Chain/August-2026-Security-Sweep/`](./Multi-Chain/August-2026-Security-Sweep/)  
**Incident:** Approximately $2 million stolen after a look-alike address was seeded into the victim's transaction history; proceeds were converted into approximately 2 million DAI.

| Network | Address | Classification | Confidence | Monitoring |
|---|---|---|---|---|
| Ethereum | `0xf0e6a49668de1195b931a3717c9cc36fc19721af` | Spoofed destination used in the theft | High | P1 direct watch |
| Ethereum | `0x692729bcd0887b8d02b8ff3169220ba0f4e17251` | Stolen-funds swap and consolidation account | High | P1 direct watch |
| Ethereum | `0xe2ebfd6f329a6330ab7eee68ce1328c21d31816a` | Final DAI storage and consolidation address | High | P1 direct watch; highest-priority proceeds endpoint |
| Ethereum | `0xedda4e01669d30faa04a9cb75488abc366ee4143` | Address-poisoning campaign controller | Medium-high | P1 direct watch and graph expansion |
| Ethereum | `0xde39ef679e12574279e3ed35de4b0721beae27de` | Forgery and poisoning contract | Medium-high | P2 infrastructure monitoring |

### Explicit Exclusions and Graph-Only Pivot

| Address | Role | Treatment |
|---|---|---|
| `0x7ba7f4773fa7890bad57879f0a1faa0edffb3520` | Victim wallet | Do not threat-label |
| `0xf0e67a1896e814e30c011e36174de28caa9ab1af` | Legitimate intended payee | Do not threat-label |
| `0xe2ebba3e64f25f8badf35d2760473748d673416a` | Separate self-poisoning look-alike | Graph expansion only; exclude from primary threat-address CSV |

The real and spoofed destinations share a similar visible prefix and suffix (`0xf0e67a...a9ab1af` versus `0xf0e6a4...19721af`). The controller and contract are retained at medium-high confidence for broader campaign attribution; the theft path and final DAI endpoint are high confidence.

---

## August 24 Follow-Up: Term Finance Vault Governance Exploit

**Case file:** [`Multi-Chain/August-2026-Security-Sweep/`](./Multi-Chain/August-2026-Security-Sweep/)  
**Incident:** Approximately $8.5 million removed from Term Strategy/Meta Vaults after a governance-layer takeover; roughly 2,843 ETH and approximately 1.68 million DAI were consolidated at one address.

| Network | Address | Classification | Confidence | Monitoring |
|---|---|---|---|---|
| Ethereum | `0xD5183d8BfC65a50863C62aF2538198A8288FFc13` | Exploit-proceeds and consolidation address | High | P1 direct watch; highest priority |

### Attribution and Infrastructure Boundaries

- No named threat actor is established.
- The exact path used to obtain or exercise sufficient vault-governance authority remains unresolved.
- Approximately 2 ETH sourced from Tornado Cash is funding-path evidence, not identity attribution.
- Tornado Cash contracts, Term and Yearn infrastructure, ordinary governance participants, and later exchange or service counterparties remain graph pivots unless separately attributed.
- The Sandbox SAND bridge indicators `0xAbE0...4D22` and `0x638C...F296` are truncated and are not added to the wallet dataset.
---

## CYBERLEEK / GTA VI Leak-and-Token Campaign

**Assessment date:** August 25, 2026  
**Network:** Solana  
**Status:** Active; real-world identity and initial-access vector unresolved  
**Case file:** [`SOL/CYBERLEEK/`](./SOL/CYBERLEEK/)  
**Machine-readable indicators:** [`addresses.csv`](./SOL/CYBERLEEK/addresses.csv)

### Direct Actor-Linked Wallet

| Address | Classification | Confidence | Monitoring |
|---|---|---|---|
| `Hok9nbV89yBSKCttxe3goqajwbiqQa9mtHvQBsbJH3Np` | CYBERLEEK token creator and Raydium pool creator | High | P1 direct watch for new deployments, funding, exchange deposits, consolidation, and Fee Key interactions |

### Strongly Linked Financial Pivot — Ownership Unresolved

| Address | Classification | Confidence | Monitoring |
|---|---|---|---|
| `Ec2qmcpCCD9hjahAcquiQf5JkZWCK68BUahCje1izYC7` | Purpose-built funding funnel that sent 10 SOL and 311.42 SOL to the deployer | High transaction linkage; unknown common control | P1 financial-support monitoring; do not automatically inherit the actor label |

### Campaign Infrastructure — Do Not Threat-Label as Wallets

| Address | Type | Handling |
|---|---|---|
| `ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg` | Primary token mint | Watch exact mint; separate from same-ticker copycats |
| `EVQ9RCaHggai12cje6vTtFfNkhBuJfFZHhbgB3yyprVw` | Original 1B-token account | Historical evidence; current balance reported zero |
| `CbfbaNpCGV64g2fbLBC2NXKSygeJJuC7S6i36cy8RMPo` | 270M allocation account and burn source | Historical evidence; retained balance was burned rather than sold |
| `G8kgi7aUpeX8EVR8VMkrth9SKEv5BietWC33UjAiiMGh` | Primary Raydium CPMM pool | Monitor liquidity, volume, and fee activity; protocol infrastructure |
| `44isRZNypWAsseobWTKLcQP56A3STe8Um7XdstgFttrS` | Raydium Fee Key NFT | Critical revenue indicator; alert on transfer or fee collection |
| `CMLqxbQU7CDKqzWPpAbKTgiQKuPV1tzYZNLyDjr1BwZz` | Secondary Meteora pool | Cross-pool market pivot; protocol infrastructure |

### Attribution Boundaries

- Public evidence supports playable-build access but does not establish that CYBERLEEK personally breached Rockstar or retained access to its systems.
- The 270M creator allocation was burned; the reviewed evidence does not support a developer-allocation dump.
- Approximately 98.43% of the creator-origin Raydium LP supply was reported permanently locked, while the Fee Key preserves an ongoing fee claim.
- The approximately $128,809 fee figure is an accrual estimate; no fee harvest was found by the cited analysis at its cutoff.
- Five high-profit early traders and four same-ticker copycat mints are retained in the case CSV as explicit non-actor rows and must not inherit the CYBERLEEK label.
- Upstream hubs, relays, feeder wallets, services, pools, exchanges, token accounts, and look-alike dust addresses remain graph context unless independently attributed.
- No named person, nationality, or link to the 2022 LAPSUS$ or April 2026 ShinyHunters cases is established.
