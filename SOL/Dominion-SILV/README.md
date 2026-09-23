# Dominion Market / SILV — Multisig and Key Compromise

| Field | Assessment |
|---|---|
| Incident | September 11, 2026 |
| Origin and proceeds | Solana; documented Chainflip payouts on Ethereum |
| Classification | Compromised signing keys, treasury theft, and token liquidation |
| Authorization | Attacker held at least three keys satisfying both Squads multisigs' 3-of-5 threshold |
| Impact | Approximately 46,909 SILV; $2.98–3.0M pre-attack nominal value; approximately $238,000 realized proceeds |
| Other exposed wallets | At least 11 compromised wallets, excluding the two new primary attacker wallets |
| Confidence | High for incident and transaction linkage; initial key-theft vector and real-world identity unknown |
| Evidence cutoff | September 11 reconstruction and response; source checks September 22, 2026 |

[Bitquery's reconstruction](https://bitquery.io/investigations/dominion-silv-hack-3-million-silver-tokens) supports a key compromise sufficient to authorize ordinary multisig operations. It does not establish a vulnerability in Solana, Squads, or the SILV token contract. Dominion separately reported compromised wallets and cooperation with the Solana Incident Response Network and SEAL 911, as covered by [SolanaFloor](https://solanafloor.com/news/dominion-freezes-silv-bought-after-exploit-as-token-collapses-70).

## Monitoring Indicators

| Network | Complete identifier | Role | Confidence and treatment |
|---|---|---|---|
| Solana | `BmgpLvcQJPDuVHwGVGkJo1mkRVnRaeJ9JyhrYrRjrrkZ` | Primary attacker and proceeds consolidation | High; P1 direct watch |
| Solana | `Ge2GYHJm4MGiWiWpSVyru9vHdLBZGtVnYd7yHqnYAH7g` | Treasury-drain recipient and liquidation | High; P1 direct watch |
| Solana | `6QAoKpU6QKqHS2ZxkKPYp1bHbvZQf9q1jAWxeTH1qvtF` | Late proceeds staging for Chainflip | High; P1 direct watch |
| Ethereum | `0x8b3423a3c06ab16484ed2c561a86118f040adaaf` | Destination explicitly named by two early Chainflip swaps | High flow linkage; P1 direct watch and backward tracing |
| Ethereum | `0xd13772ef959a4b227c3e9e62a4c971ce8886eeff` | Secondary Chainflip proceeds destination; possible service endpoint | High flow linkage, Medium ownership confidence; P2 proceeds watch and graph expansion |
| Solana | `EHQZBu5y3G8Lo5Vb2HH48DRjtajdzJwX499Cs9E8mSfY` | New signer inserted using compromised authority | High insertion evidence; Medium-High inferred attacker control; P1 infrastructure watch |
| Solana | `SiLVFMgD3eD2rgK628NbTBq9MnuJF5FW2CRaVyTB35L` | SILV mint | Victim/technical pivot only; no threat label |

The full identifiers resolve from Bitquery's address links. [addresses.csv](./addresses.csv) keeps custody, authorization, and victim roles separate. The inserted signer is a control-plane indicator, not an extra proceeds wallet. Bitquery calls its attacker ownership highly likely; it had not itself signed a transaction at the source cutoff.

## Treasury Drain and Response

Proposal 45 executed at **01:50:24 UTC**, transferring **42,181.88 SILV**, approximately 45% of total supply, to the second attacker wallet. Three compromised signers proposed and approved it. The receiving wallet was about 42 minutes old and later sold roughly 43,100 SILV. Other SILV came from collateral positions and compromised-wallet balances. Ten wallets were swept into the first attacker wallet, each leaving exactly **890,880 lamports**, a pattern consistent with scripted control.

| Time, September 11 UTC | Event |
|---|---|
| 00:23–00:39 | Collateral repayment/withdrawal, first delivery to the new attacker wallet, and initial sales |
| 01:50:24 | Proposal 45 treasury transfer |
| 03:43:48 | Additional signer inserted into the authority multisig |
| Around 04:00 | Dominion detected the incident; minting and redemptions were disabled during the response |
| 06:19:24 | Compromised members removed from both multisigs |
| 10:51:39 | A compromised standalone wallet withdrew another 279.95 SILV from Loopscale, followed by sale |
| 13:50:20 | Approximately 1,923.50 SOL moved to the new staging wallet |

The late withdrawal illustrates the recovery limit: changing multisig membership does not revoke a copied private key for a standalone wallet. Four complete transaction signatures are retained in [transactions.csv](./transactions.csv).

Dominion subsequently froze approximately **2,819–2,823 token accounts**, holding around 33% of supply, and announced a USDC refund process for purchases during the compromised window. The account-count range preserves the difference between Bitquery's reconstruction and public response reporting; announcement is not proof that every refund completed.

## Cross-Chain Proceeds

Two early swaps delivered approximately **9.25 ETH** to `0x8b3423a3c06ab16484ed2c561a86118f040adaaf`. Its Ethereum history dates to May 2026; its first active day included Chainflip receipts, and its last pre-incident outgoing transaction was less than two hours before the attack. That history is a useful backward lead, without making historical counterparties part of this incident.

A later direct swap delivered approximately **9.83 ETH** to `0xd13772ef959a4b227c3e9e62a4c971ce8886eeff`, which already held about 214 ETH. Bitquery explicitly leaves open whether it belongs to the attacker or a paid service. Its `threat_label` is therefore false despite direct proceeds monitoring.

The staging wallet sent most remaining SOL into five Chainflip deposit channels, largely in approximately 400-SOL chunks. Their final payouts require Chainflip-chain evidence; do not assign those proceeds to either known Ethereum destination merely because the routing service matches. Chainflip agents, deposit infrastructure, DEX pools, and unrelated dust/poisoning senders are not attacker wallets by association.

## Evidence Boundaries

- Pre-attack nominal token value, sale proceeds, loan repayment, and net profit are different quantities. The approximately $238,000 figure is the reconstructed proceeds estimate, not the $3M nominal token valuation.
- Compromised Dominion signers and other stolen wallets are victim accounts under hostile use, not necessarily attacker-created infrastructure.
- The submission described the attack as one day after launch. Bitquery instead records an August launch and August 13–16 minting. This case does not repeat the disputed launch interval.
- The two submitted Dominion reports describe the same incident and are combined here. The dataset contains seven indicators, including the added signer and victim mint, rather than treating the stated five-wallet subtotal as the entire IOC set.

## Sources

- [Bitquery — transaction reconstruction, full linked identifiers, and ownership caveats](https://bitquery.io/investigations/dominion-silv-hack-3-million-silver-tokens)
- [SolanaFloor — Dominion response, account freezes, and proposed refunds](https://solanafloor.com/news/dominion-freezes-silv-bought-after-exploit-as-token-collapses-70)
- [DexPaprika — SILV/SOL market and mint context](https://dexpaprika.com/solana/pool/BJTTnSttBGXAGbjZXbMPH4aKyR2Qiy4EMBZsm37SWJd2)
