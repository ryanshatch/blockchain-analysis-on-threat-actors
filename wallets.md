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
