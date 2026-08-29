# Iranian MOIS-Linked Cyber-Actor Wallet Network

| Field | Assessment |
|---|---|
| OFAC action date | August 24, 2026 |
| Networks | Bitcoin, Ethereum, and TRON |
| Source type | Official — U.S. Treasury / OFAC |
| Confidence | High for every identifier in `addresses.csv` |
| Classification | Officially sanctioned cyber-actor addresses; one separate Iran sanctions-finance seed |
| Monitoring | Watch listed identifiers directly; treat counterparties as graph-expansion pivots unless separately attributed |

## Executive Assessment

On August 24, 2026, the U.S. Department of the Treasury described an Iranian cyber group directed by the Ministry of Intelligence and Security (MOIS) and published cryptocurrency identifiers for four members: Keyvan Fayyaz Ghareh Blagh, Mojtaba Ghal'eh-Kuhi, Arman Kahzadian, and Behzad Mesri. Treasury says the group conducts computer-network exploitation on behalf of, or for the benefit of, MOIS and has compromised U.S. energy companies, defense contractors, healthcare institutions, information-technology firms, financial institutions, and government offices.

The action creates **30 direct, high-confidence sanctions-watch seeds** tied to the MOIS-linked cyber group:

- Six Bitcoin identifiers
- Twenty Ethereum identifiers
- Four TRON identifiers

OFAC also published one TRON-format USDT identifier for Almpertos Tsoris. That address is retained in the machine-readable dataset as a **separate Iran sanctions-finance seed** because OFAC lists Tsoris under `[IRAN-EO13902]`, not as a member of the MOIS cyber group.

No transactional counterparty, exchange deposit address, bridge, router, or service wallet should inherit an actor or sanctions label merely because it interacts with one of these seeds.

## Key Judgments

| Judgment | Confidence | Basis |
|---|---|---|
| The 30 MOIS-network identifiers are directly attributable to the named cyber actors for sanctions monitoring. | High | OFAC publishes each address under the corresponding SDN entry. |
| Ghal'eh-Kuhi and Mesri have led the MOIS-linked group since at least summer 2023. | High | Treasury's August 24 press release. |
| Blagh is associated with much of the group's network-compromise activity. | High | Treasury names Blagh among the actors responsible for the majority of the group's compromises. |
| Kahzadian is especially relevant to digital-asset theft analysis. | High | Treasury says he focused on digital-asset heists and illicitly gained control of a Bitcoin wallet containing more than $30,000 in summer 2023. |
| Mesri's cryptocurrency set is a material expansion of an existing attribution. | High | OFAC updated his existing SDN entry with 15 BTC, ETH, and TRON identifiers. |
| Tsoris belongs to the MOIS cyber cluster. | Unsupported | OFAC lists his USDT/TRON identifier under a separate Iran-related sanctions authority. |

## Address Summary

| Entity | BTC | ETH | TRON | Total | Dataset treatment |
|---|---:|---:|---:|---:|---|
| Keyvan Fayyaz Ghareh Blagh | 3 | 5 | 2 | 10 | P1 direct sanctioned cyber-actor seeds |
| Mojtaba Ghal'eh-Kuhi | 1 | 1 | 0 | 2 | P1 direct sanctioned cyber-actor seeds |
| Arman Kahzadian | 1 | 2 | 0 | 3 | P1 cyber-actor and digital-asset-theft seeds |
| Behzad Mesri | 1 | 12 | 2 | 15 | P1 materially updated sanctioned cyber-actor seeds |
| Almpertos Tsoris | 0 | 0 | 1 | 1 | P1 separate sanctions-finance seed; excluded from MOIS cluster count |

## Keyvan Fayyaz Ghareh Blagh

OFAC newly designated Blagh under `[CYBER4]`. Treasury identifies him as a member of the MOIS-linked group and names him among the actors responsible for the majority of its network-compromise activity.

| Network | Address |
|---|---|
| Bitcoin | `bc1qf6zxs4lkp9umh6hf087mh70w0ymcyt8cunp58r` |
| Bitcoin | `bc1qr2pwmvkpq5tc5um2g9uh34yyu6wepwx89rts70` |
| Bitcoin | `bc1q4ktvxxhhvf8qhs9qkdsm9arcxfmmeex6rl7n50` |
| Ethereum | `0x4060cbf80734193f521a3cc6fd4e985df2825279` |
| Ethereum | `0x56de1527136f76a809e5b14ded6103eecd072ba7` |
| Ethereum | `0x8694ed130432be2cd3efff2e4d9dc52351dc7423` |
| Ethereum | `0xbd3276f265b83b5e828c05f46cde9d10a1521a24` |
| Ethereum | `0xf1c4c44d2dcbcfa704349e3b57628dbd8404e597` |
| TRON | `TXR4FDAZZLDSvuRxveW9aBMybbaS12WWHk` |
| TRON | `TP3kVtnFgDSoSqzw178nLJtGWNjrbKNgB6` |

## Mojtaba Ghal'eh-Kuhi

Treasury identifies Ghal'eh-Kuhi as a leader of the MOIS-linked group since at least summer 2023. OFAC newly designated him under `[CYBER4]` and directly lists both identifiers below.

| Network | Address |
|---|---|
| Bitcoin | `1GXeCkFQq7SYo6B7wdLAPkkri6NFTFB7No` |
| Ethereum | `0x1b8579cf6ab12ea6b74ac5fa41f3829a3cb61e6e` |

## Arman Kahzadian

Treasury states that Kahzadian focused on digital-asset heists and illicitly gained control of a wallet containing more than $30,000 in Bitcoin in summer 2023. His three OFAC-published identifiers are therefore classified more specifically than generic sanctioned payment addresses.

| Network | Address |
|---|---|
| Bitcoin | `1JGPiQGK78xTxAVoxA1MjK3Z15M84Rj6BL` |
| Ethereum | `0xeb507efa9ee692a4c774ad1de9f3cb26fc459da3` |
| Ethereum | `0xef85a6fafa5942a964dc618e94e230881d29ce2a` |

## Behzad Mesri

Mesri was already sanctioned for prior malicious cyber activity. OFAC's August 24 action materially expanded his existing entry with 15 cryptocurrency identifiers. Treasury says Mesri and Ghal'eh-Kuhi have led the MOIS-linked group since at least summer 2023.

| Network | Address |
|---|---|
| Bitcoin | `12aNKp2iDKuhEde2YfPdd4DFGenRUTKupL` |
| Ethereum | `0x252a8bd2319d8a555b872990601221b3a2053bce` |
| Ethereum | `0x1CAb8177ACe78b1B6B1c393371F4f2dCAE40CbEB` |
| Ethereum | `0x6Fac4D18c912343BF86fa7049364Dd4E424Ab9C0` |
| Ethereum | `0xA40cFBFc8534FFC84E20a7d8bBC3729B26a35F6f` |
| Ethereum | `0x7F03679B56d8772530EFA516b58Bb83d4829E881` |
| Ethereum | `0x8ac5381FCD9e7395D14e02986c344aADA84B4bC6` |
| Ethereum | `0x9697749A9e8D6C119D8EEb0d6268a1b99C40684c` |
| Ethereum | `0x9DD7fA4B4950154F7e75BdD8A77266B99b94Ec08` |
| Ethereum | `0xb5A69Da691670F62510793F79a9B36c7db1A7b7c` |
| Ethereum | `0x6B0736Fed0634e15E19CC57fBA19cd179c13AbCA` |
| Ethereum | `0xd81414ABc631C6CADAe1C6198b0c2b15a9B4fDe5` |
| Ethereum | `0xF45Ecc3a59C7911181C659cE9115854c6175Be91` |
| TRON | `TAbbVaBKgH4VBLXgWqACuwoKF4cH1HinQh` |
| TRON | `TEsxMcVocweTM82Mdmc5diKC6qyCWqSpPv` |

## Separate Iran Sanctions-Finance Seed

| Entity | Network | Address | Treatment |
|---|---|---|---|
| Almpertos Tsoris | TRON / USDT | `TJCBpxZ3yC7C7oegSRZMFxBcscmUVeSA36` | Watch directly, but do not merge into the MOIS cyber-actor cluster. |

## Monitoring Priorities

1. Alert on all direct inflows and outflows involving the 30 MOIS-network identifiers.
2. Prioritize Kahzadian's three addresses for historical theft-cluster expansion and asset-recovery research.
3. Test Mesri's 12-address Ethereum set for common funding, consolidation, contract interaction, exchange usage, and cross-chain activity.
4. Record exchange, bridge, DEX, and service counterparties as contextual nodes until independently attributed.
5. Preserve entity and authority boundaries: Tsoris is a separate sanctions-finance seed, not a MOIS cyber-group member.
6. Retain OFAC publication dates and exact full identifiers; never trace from truncated forms.

## Attribution Boundaries

- OFAC publication supports direct sanctions monitoring of the listed identifiers; it does not prove that every counterparty is sanctioned or actor-controlled.
- A common interaction with an exchange, bridge, router, mixer, or service does not establish common ownership.
- The dataset does not claim that every member of the wider MOIS group controlled every address published under another named member.
- Kahzadian's Treasury-described Bitcoin-wallet theft does not establish that the exact stolen wallet is one of the three published sanctions identifiers.
- Mesri's address expansion is authoritative attribution, but address-to-address operational roles remain subjects for subsequent on-chain analysis.

## Sources

- [OFAC Recent Action — August 24, 2026](https://ofac.treasury.gov/recent-actions/20260824)
- [U.S. Treasury — Iranian critical-infrastructure intrusions and digital-asset theft](https://home.treasury.gov/news/press-releases/sb0613)

---

## TLDR

OFAC's August 24 action contributes 30 high-confidence BTC, ETH, and TRON seeds for four named members of a MOIS-linked Iranian cyber group. Kahzadian is the strongest digital-asset-theft lead, while Mesri's 15-address expansion is the largest newly attributable cluster. The Tsoris USDT/TRON address is also an official direct-watch seed but remains separate from the MOIS cyber case.
