<div align="center">
<h1>Solana Threat and Incident Index</h1>
<p><strong>Solana-specific exploits, governance attacks, suspicious wallets, rug investigations, and Solana-origin multi-chain incidents.</strong></p>
</div>

<hr>

<h2>Solana Case Directories</h2>

<table>
  <thead>
    <tr><th align="left">Case</th><th align="left">Incident date</th><th align="left">Classification</th><th align="left">Reported impact</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="./BonkDAO/"><code>BonkDAO/</code></a></td>
      <td>July 10, 2026</td>
      <td>Malicious governance proposal and treasury takeover</td>
      <td>Approximately 4.426 trillion BONK, valued near $19.3 million when transferred</td>
    </tr>
    <tr>
      <td><a href="./DeFiTuna/"><code>DeFiTuna/</code></a></td>
      <td>July 16, 2026</td>
      <td>Leveraged-position health-check and solvency-validation exploit</td>
      <td>Approximately 569,601 USDC</td>
    </tr>
    <tr>
      <td><a href="./FlashTrade/"><code>FlashTrade/</code></a></td>
      <td>July 21–22, 2026</td>
      <td>Forged ephemeral buffer / missing canonical PDA validation</td>
      <td>98,000 USDC; amount covered by FlashTrade and MagicBlock</td>
    </tr>
    <tr>
      <td><a href="./Raydium/"><code>Raydium/</code></a></td>
      <td>June 10, 2026</td>
      <td>Counterfeit LP mint accepted by deprecated AMM V3 withdrawal logic</td>
      <td>Approximately $1.34 million</td>
    </tr>
    <tr>
      <td><a href="./HOPE/"><code>HOPE/</code></a></td>
      <td>Historical / ongoing investigation</td>
      <td>Token concentration, transfers, sales, and suspected rug activity</td>
      <td>See case report</td>
    </tr>
  </tbody>
</table>

<h2>Solana-Origin Cases Stored Under Multi-Chain</h2>

<table>
  <thead>
    <tr><th align="left">Case</th><th align="left">Why it is cross-listed</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="../Multi-Chain/Across-Protocol/"><code>Multi-Chain/Across-Protocol/</code></a></td>
      <td>The exploit originated in forged Solana deposit-event processing, while fraudulent relayer payouts and recovery activity spanned numerous destination chains.</td>
    </tr>
    <tr>
      <td><a href="../Multi-Chain/Allbridge-Core/"><code>Multi-Chain/Allbridge-Core/</code></a></td>
      <td>The vulnerable liquidity-pool deployment and exploit transaction were on Solana, while stolen proceeds were routed to Ethereum.</td>
    </tr>
  </tbody>
</table>

<h2>Classification Rule</h2>

<p>
Cases are indexed here when the vulnerable program, governance system, execution environment, or initial exploit transaction was on Solana. A case may remain canonically stored under <code>Multi-Chain/</code> when its protocol scope, fraudulent payouts, bridge movement, proceeds tracing, or recovery activity spans several networks.
</p>

<p>
The exploit-origin chain and the later proceeds chains are recorded separately. Bridging stolen funds to Ethereum does not reclassify the original vulnerability as an Ethereum exploit.
</p>

<h2>Monitoring Boundaries</h2>

<ul>
  <li>Direct-watch attacker and proceeds addresses are separated from victim, protocol, bridge, exchange, router, vault, and recovery infrastructure.</li>
  <li>Incomplete or truncated addresses are not added as monitoring seeds.</li>
  <li>FlashTrade currently has no machine-readable attacker-address file because no complete public attacker address was resolved in the reviewed evidence.</li>
  <li>Cross-chain counterparties are not automatically threat-labeled merely because they interacted with incident proceeds.</li>
</ul>
