<!-- case-visual:start -->
<p align="center">
  <img src="../../../assets/readme-headers/evm-ethereum-maker-legacy-keeper.svg" alt="Legacy Auction Keeper — Third-party keeper authorization drain" width="1200">
</p>
<!-- case-visual:end -->

<!-- doc-nav:start -->
<p><a href="../../../readme.md">Home</a> · <a href="../../../wallets.md">Wallet index</a> · <a href="../../../CATALOG.md">All case files</a> · <a href="../../README.md">Parent index</a></p>
<!-- doc-nav:end -->

# Maker Legacy Auction Keeper — Unauthorized Drain

**Incident:** October 6, 2026. **Impact:** 200 WETH/ETH, approximately $538,000–$543,000 at reporting prices. **Classification:** missing authorization on a dormant third-party ETH-A liquidation keeper's `drain` path; **not a MakerDAO/Sky core-protocol compromise**. [CertiK's analysis](https://www-cn.certik.com/blog/makerdao-legacy-auction-keeper-incident-analysis) identifies the attacker EOA, attack contracts, victim keeper and exploit transaction.

| Ethereum identifier | Role | Treatment |
|---|---|---|
| `0x01EB957E5C7DcDDD60F3C875956cCc6fb9BdA5FA` | Fresh Tornado-funded attacker EOA; 200 ETH proceeds | P1 direct watch and historical tracing |
| `0xEc997d2aD033277913d6002277353368E8321dcF` | Attacker intermediary/attack contract | Malicious-infrastructure watch |
| `0xf09a13072Ed939B79Bc25B66AA3a836ea6DCC170` | Contract created for exploit, with delegated keeper access | Control-plane infrastructure watch |
| `0x9c05a05893Ada984FC20D0DA0c046De5Cc0e8273` | Affected keeper proxy | Victim context only; never threat-label |

The transaction `0xbb6940f7c2a1e68cafbae7bb9b94d09af9af06ec3a114f6996f2cab993f3a88c` used delegated keeper authority to extract 200 WETH, converted to ETH. Subsequent 10-ETH Tornado Cash deposits dispersed the proceeds; post-mixer recipients are unresolved. The router and Maker Vat, Flipper and GemJoin contracts remain infrastructure. [addresses.csv](./addresses.csv) separates the EOA and two attacker contracts from the victim keeper. [Independent transaction reconstruction](https://publicaml.org/makerdao-keeper-drain/) provides timing and mixer-flow context.
