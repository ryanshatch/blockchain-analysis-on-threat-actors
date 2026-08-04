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

## Verus–Ethereum Bridge Exploit — July 2026

**Incident date:** July 23, 2026  
**Networks:** Verus and Ethereum  
**Incident confidence:** High  
**Address-linkage confidence:** High  
**Named actor:** None identified  
**Case file:** [`Multi-Chain/Verus-Ethereum-Bridge-July-2026/`](./Multi-Chain/Verus-Ethereum-Bridge-July-2026/)

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
