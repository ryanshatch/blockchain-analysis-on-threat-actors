# Nesa / Cosmos EVM Exploit — Ethereum Proceeds

| Field | Assessment |
|---|---|
| Incident date | August 24, 2026 |
| Investigation publication | September 8, 2026 |
| Networks | Nesa to Ethereum through Hyperlane |
| Classification | Cosmos EVM balance-accounting exploit; Nesa-specific source-chain execution remains incompletely documented |
| Ethereum bridge receipt | 257,703,733.288579599652028616 NES; approximately 25.8% of stated token supply |
| Traced liquidation subset | Approximately 185.74M NES across 241 fills; approximately 95.97 ETH gross proceeds |
| Direct-watch records | Two Ethereum wallets: one High-confidence P1 seed and one Medium-confidence P2 seed |
| Real-world actor | Unidentified |
| Evidence cutoff | September 8 reporting; source and identifier checks September 11, 2026 |

The [September 8 Rekt investigation](https://rekt.news/nesa-rekt) identifies a primary Ethereum bridge recipient and a separate liquidation wallet for the August 24 Nesa exploit. The complete bridge transaction independently exposes the primary recipient and exact NES quantity. The liquidation wallet's relationship relies on Rarma's funding and trading reconstruction, so its confidence remains lower.

## Direct-Watch Wallets

| Network | Address | Role | Confidence | Treatment |
|---|---|---|---|---|
| Ethereum | [`0x9AE755D23Fc948fE94C9364A2398fd508a2AB0d2`](https://etherscan.io/address/0x9AE755D23Fc948fE94C9364A2398fd508a2AB0d2) | Primary attacker; cross-chain exploit-proceeds and consolidation wallet | High | P1 direct watch |
| Ethereum | [`0xB92dF70F3d25eD25265c7C341C9D2550c42Ff83A`](https://etherscan.io/address/0xB92dF70F3d25eD25265c7C341C9D2550c42Ff83A) | Exit-trading and liquidation wallet; exploit-derived proceeds hop | Medium | P2 direct incident-flow watch and cautious graph expansion |

The classifications apply to the documented incident roles. They do not establish a named operator or prove that every subsequent counterparty shares control of either wallet. Structured records are in [addresses.csv](./addresses.csv).

## Bridge Evidence and Liquidation

The Ethereum transaction [`0xd443eabd4cfa1be6ad5f7ef861db9a9f271305040615667ed336bc195af05080`](https://etherscan.io/tx/0xd443eabd4cfa1be6ad5f7ef861db9a9f271305040615667ed336bc195af05080) records a successful Hyperlane withdrawal from Nesa and an Ethereum-side mint of **257,703,733.288579599652028616 NES** to the P1 wallet. The exact decimal quantity is preserved as text in [transactions.csv](./transactions.csv). Its source field is the ERC-20 mint's null address, not a source-chain attacker account or the Ethereum transaction submitter.

[Rarma's reconstruction, reproduced by Rekt](https://rekt.news/nesa-rekt), describes approximately 1.11M NES initially acquired and bridged into Nesa. The later Ethereum receipt exceeded that observable deposit by more than 230 times. This imbalance supports the scale of the exploit; it does not independently identify the exact Nesa-side call or victim account.

The same reconstruction identifies the P2 wallet as funded by the primary recipient and reports approximately 185.74M NES sold through CoW Protocol and Uniswap V4 across 241 fills, yielding approximately 95.97 ETH. These are gross proceeds for a traced sale subset, not a complete cash-out or net-profit calculation. The bridged token quantity, nominal valuation, sale proceeds, and net profit must remain separate measures.

The supported sequence is funding and Nesa bridge-in, followed by the reported Cosmos EVM exploit, Hyperlane delivery to the P1 wallet, and reported liquidation through the P2 wallet. Later ETH, bridge, and exchange destinations require their own transaction evidence before ingestion.

## Root Cause and Attribution Limits

[Cosmos Labs' post-mortem for GHSA-7g4w-cg88-2cq2](https://github.com/cosmos/security/blob/main/communications/cosmos_evm_GHSA-7g4w-cg88-2cq2_post_mortem.md) documents a shared balance-accounting vulnerability chain involving underflow and overflow. It reports six exploited networks and supplies detailed timelines for MANTRA, TAC, and KiiChain. It does not identify Nesa by name in those detailed timelines; membership in the unnamed subset should not be presented as an explicit Cosmos Labs attribution.

[Nesa acknowledged malicious activity exploiting a Cosmos EVM vulnerability](https://x.com/nesaorg/status/2091915864497066077). At the report cutoff, public evidence still lacked a detailed Nesa-specific technical post-mortem and a complete source-chain attacker account. Ethereum receipt attribution is therefore stronger than the public source-chain reconstruction. Do not infer a Nesa address by copying an Ethereum address across networks.

Hyperlane relayers, bridge contracts, the mint null address, CoW Protocol, Uniswap, token contracts, and exchange infrastructure remain service or protocol context. They do not inherit attacker labels from processing these flows. Funding linkage to the P2 wallet supports incident monitoring while common control remains an inference.

## Monitoring

1. Prioritize the P1 wallet's token and ETH dispersal, bridge interactions, exchange deposits, and reuse.
2. Monitor the P2 wallet's liquidation proceeds while preserving Medium confidence on its relationship to the primary wallet.
3. Seek a Nesa-side post-mortem, source-chain account, and complete exploit transaction before extending source-chain attribution.
4. Preserve the dated reporting window. The submitted scan reported no additional qualifying BTC or SOL seed; that is not a claim that no later incident exists.

## Sources

- [Rekt — Nesa investigation, September 8, 2026](https://rekt.news/nesa-rekt)
- [Etherscan — exact Ethereum bridge delivery](https://etherscan.io/tx/0xd443eabd4cfa1be6ad5f7ef861db9a9f271305040615667ed336bc195af05080)
- [Rarma — original bridge and liquidation reconstruction](https://x.com/Rarma_/status/2092001755559309523)
- [Bubblemaps — broader wallet-cluster analysis](https://x.com/bubblemaps/status/2092613204396650888)
- [Nesa — incident acknowledgement](https://x.com/nesaorg/status/2091915864497066077)
- [Cosmos Labs — shared vulnerability post-mortem](https://github.com/cosmos/security/blob/main/communications/cosmos_evm_GHSA-7g4w-cg88-2cq2_post_mortem.md)
