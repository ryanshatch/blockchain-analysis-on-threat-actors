<!-- case-visual:start -->
<p align="center">
  <img src="../../assets/readme-headers/multi-chain-bitget-september-2026.svg" alt="Bitget September 2026 — Cross-chain wallet breach and proceeds tracing" width="1200">
</p>
<!-- case-visual:end -->

<!-- doc-nav:start -->
<p><a href="../../readme.md">Home</a> · <a href="../../wallets.md">Wallet index</a> · <a href="../../CATALOG.md">All case files</a> · <a href="../README.md">Parent index</a></p>
<!-- doc-nav:end -->

# Bitget September 2026 — Wallet Backend Breach

**Evidence cutoff:** October 1, 2026, with Bitquery's September 29 distribution snapshot. Figures describe source snapshots, not current balances.

| Field | Assessment |
|---|---|
| Detection | September 24, 2026, 18:31 UTC |
| Confirmed affected layers | Portions of Bitget hot and warm wallets; cold wallets unaffected per Bitget |
| Reported loss | Initial $351.6 million; Bitget's later reconciliation approximately **$387.5 million** across the same incident, **not** the amount deposited in one wallet |
| Attack mechanism | Bitget reports backend access and manipulated transaction data accepted by its authorization/signing process; precise initial access remains undisclosed |
| Networks | Ethereum and other EVM chains, XRP Ledger, Zcash, TRON; downstream Bitcoin and an unresolved Solana CCTP leg |
| Actor | Chainalysis attributes the **incident** to North Korean threat actors; attribution of any particular downstream wallet to TraderTraitor personnel remains separate |
| Address evidence | Six Ethereum records (one provisional pivot), plus official XRP Ledger, Zcash and TRON receiving seeds |

[Bitget's first notice](https://www.bitget.com/support/articles/12560603896024) confirmed unauthorized transfers; its [follow-up](https://www.bitget.com/support/articles/12560603896108) identified three further receiving addresses and revised the estimate to about $387.5M as additional assets were identified. These are changing estimates of **one breach**, not additive losses. [TRM's September 25 investigation](https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack) traced laundering overlap and assessed DPRK involvement as likely, while [Chainalysis' October 1 investigation](https://www.chainalysis.com/blog/387m-bitget-theft-2026/) explicitly attributed the incident to North Korean actors. Bitget describes backend authorization manipulation rather than direct private-key theft. Initial access details remain undisclosed.

<!-- contents:start -->
<details>
<summary>Contents</summary>
<ul>
<li><a href="#section-complete-monitoring-addresses">Complete monitoring addresses</a></li>
<li><a href="#section-laundering-and-attribution-boundaries">Laundering and attribution boundaries</a></li>
</ul>
</details>
<!-- contents:end -->

<a id="section-complete-monitoring-addresses"></a>
## Complete monitoring addresses

| Network | Address | Role | Confidence and treatment |
|---|---|---|---|
| Ethereum; also same identifier on several EVM networks | `0x770b10b273fC44Fe9197D6bF20F145c2e98463Ee` | Primary attacker collection/consolidation | High incident linkage; **P1 direct watch**, cross-chain graph expansion |
| Ethereum | `0xa6dd3f218b65e32ccc37be30f74884133c655545` | Major proceeds distribution/hub | High incident linkage per TRM; **P1 direct watch**; do not attribute all historical hub volume to this breach |
| Ethereum / EVM | `0x469Ac1406dE92f82C0563477240a3627057425DC` | Reported onward dispersal destination | **Medium for direct path**, unknown control; **P2 incident-flow watch/pivot**, no attacker-ownership label |
| Ethereum | `0x600cfedc6bd65fa79b604dc44964f419e45784b2` | Convergence and payout hub; empty at September 29 snapshot | High proceeds-flow linkage; P1 watch, historical and onward graph |
| Ethereum | `0xd2c2f029eff5cacc686f24377cfddcfc82d9f899` | Large holding wallet that began moving September 27 | High proceeds-flow linkage; P1 direct watch |
| Ethereum | `0xfd5ebe912e2061992437767e24e5bcb52a3f9e54` | Holding and payout wallet; 7,023.58 ETH at September 29 snapshot | High proceeds-flow linkage; P1 direct watch |
| XRP Ledger | `rwNhefsz1UQEusxhCvHip3RANinWi4CTck` | Officially identified primary receiving seed | High; P1 direct watch |
| Zcash | `t1WgMdtND8NF7NDUuYmq8MpMj1NTCXkMDVG` | Officially identified transparent receiving seed | High; P1 direct watch |
| TRON | `TBWNguTTgezw9dVorX441C6nDrZpRxYwKD` | Officially identified primary receiving seed | High; P1 direct watch |

TRM reports the first wallet received value on Ethereum, Arbitrum, Avalanche, Base, BNB Chain, and Optimism. The second sent funds to fresh wallets over roughly two hours; many received about 10,000 ETH. A [September 26 independent reconstruction](https://community.chainbounty.io/posts/01a0dd61-0077-745e-b37a-6294089adf97) cautions that not all larger gross hub outflows are incident-attributable and could not confirm the direct edge from the first to the third address. That third address remains a monitored lead without an attacker label. [Bitquery's September 29 distribution reconstruction](https://bitquery.io/investigations/bitget-hack) supplies the three additional complete Ethereum links and traces 51,899 ETH through hundreds of wallets. Its observations include about 29,088 ETH entering THORChain and $2.95M USDC routed to Solana via CCTP; no complete Solana destination is published. The XRP, Zcash and TRON rows come from Bitget's official notice. [addresses.csv](./addresses.csv) preserves all role boundaries.

<a id="section-laundering-and-attribution-boundaries"></a>
## Laundering and attribution boundaries

TRM and Bitquery trace portions through THORChain toward Bitcoin peel chains and through Across, Bridgers, Chainflip and FixedFloat. Complete public downstream BTC and Solana identifiers are absent from those reports, so none are guessed here. Bitquery separately rejects a circulating claim of 6,300 ETH in Bitget-linked Tornado Cash deposits. Routers, bridges, DEX settlement endpoints and ordinary counterparties **do not inherit attacker labels**. Monitoring an Ethereum row alone does not capture activity on other EVM networks.

TRM found laundering overlap with previously identified North Korean thefts, including Bybit and AFX Bridge, while stopping short of a definitive actor judgment on September 25. Chainalysis' later analysis attributes the broader theft to North Korean actors. Neither report proves that every downstream laundering wallet is operated by the same TraderTraitor member. No reported evidence supports classifying the breach as direct private-key theft.

The [Duelbits case](../Duelbits-September-2026/) is a separate incident. Complete downstream BTC, XRP relay and Solana CCTP destination sets and an authoritative initial-access postmortem remain outstanding.
