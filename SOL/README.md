<div align="center">
<h1>Solana Threat and Incident Index</h1>
<p><strong>Solana-specific exploits, governance attacks, suspicious wallets, authorization drains, rug investigations, sanctions attributions, and Solana-origin multi-chain incidents.</strong></p>
</div>

<hr>

<p>
<strong>Recent tracked set:</strong> Eight individually identifiable Solana-origin security incidents from June 10 through July 21, 2026 are represented in <a href="./INCIDENTS.csv"><code>INCIDENTS.csv</code></a>. Multi-victim drainer campaigns and sanctions attributions are tracked separately and are not counted as individual protocol incidents.
</p>

<h2>Solana Case Directories</h2>

<table>
  <thead>
    <tr><th align="left">Case</th><th align="left">Incident date</th><th align="left">Classification</th><th align="left">Reported impact</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="./Raydium/"><code>Raydium/</code></a></td>
      <td>June 10, 2026</td>
      <td>Counterfeit LP mint accepted by deprecated AMM V3 withdrawal logic</td>
      <td>Approximately $1.34 million</td>
    </tr>
    <tr>
      <td><a href="./BonkDAO/"><code>BonkDAO/</code></a></td>
      <td>July 6, 2026</td>
      <td>Malicious governance proposal and treasury takeover</td>
      <td>Approximately 4.426 trillion BONK, valued near $19.3–20 million</td>
    </tr>
    <tr>
      <td><a href="./Genesis-Whale-Drain/"><code>Genesis-Whale-Drain/</code></a></td>
      <td>July 10–13, 2026</td>
      <td>Suspected private-wallet compromise / high-value drain; compromise vector unknown</td>
      <td>Approximately 180,900 SOL, valued near $14.2 million</td>
    </tr>
    <tr>
      <td><a href="./SUNUSI/"><code>SUNUSI/</code></a></td>
      <td>July 13, 2026</td>
      <td>Malicious burn-tool authorization and Permanent Delegate abuse</td>
      <td>More than $275,000 nominal SUNUSI value removed; approximately $94,300 reportedly realized through selling</td>
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
    <tr><th align="left">Case</th><th align="left">Incident date</th><th align="left">Why it is cross-listed</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="../Multi-Chain/Across-Protocol/"><code>Multi-Chain/Across-Protocol/</code></a></td>
      <td>July 17, 2026</td>
      <td>The exploit originated in forged Solana deposit-event processing, while fraudulent relayer payouts and recovery activity spanned numerous destination chains.</td>
    </tr>
    <tr>
      <td><a href="../Multi-Chain/Allbridge-Core/"><code>Multi-Chain/Allbridge-Core/</code></a></td>
      <td>July 19, 2026</td>
      <td>The vulnerable liquidity-pool deployment and exploit transaction were on Solana, while stolen proceeds were routed to Ethereum.</td>
    </tr>
  </tbody>
</table>

<h2>Related Solana Sanctions Cases</h2>

<table>
  <thead>
    <tr><th align="left">Case</th><th align="left">Date</th><th align="left">Solana indicator</th><th align="left">Classification</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="../Multi-Chain/Shelbit-Network/"><code>Multi-Chain/Shelbit-Network/</code></a></td>
      <td>August 7, 2026</td>
      <td><code>6wjqWWra8ombzaw6VHrG5xpQ972jCYF6bbHiFCbWmr4U</code></td>
      <td>High-confidence OFAC-sanctioned Shelbit Exchange infrastructure seed; watch directly</td>
    </tr>
  </tbody>
</table>

<h2>Related Solana-Targeting Campaigns</h2>

<table>
  <thead>
    <tr><th align="left">Campaign</th><th align="left">Scope</th><th align="left">Classification</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="../Multi-Chain/SpaceX-FIFA-Drainers/"><code>Multi-Chain/SpaceX-FIFA-Drainers/</code></a></td>
      <td>Solana and EVM users; observed May–July 2026</td>
      <td>Wallet-drainer, malicious dApp, fake-token, impersonation, and investment-scam campaign. Not counted as a single Solana protocol exploit.</td>
    </tr>
  </tbody>
</table>

<h2>Classification Rule</h2>

<p>
Cases are indexed here when the vulnerable program, governance system, execution environment, victim wallet, authorization path, sanctioned identifier, or initial exploit transaction was on Solana. A case may remain canonically stored under <code>Multi-Chain/</code> when its protocol scope, sanctions attribution, fraudulent payouts, bridge movement, proceeds tracing, recovery activity, or campaign infrastructure spans several networks.
</p>

<p>
The exploit-origin chain and the later proceeds chains are recorded separately. Bridging stolen funds to Ethereum does not reclassify the original vulnerability or wallet drain as an Ethereum incident. Sanctions cases remain distinct from exploit counts.
</p>

<h2>Monitoring Boundaries</h2>

<ul>
  <li>Direct-watch attacker, proceeds, and officially sanctioned addresses are separated from victim, protocol, bridge, exchange, router, vault, recovery, and transactional-counterparty infrastructure.</li>
  <li>Incomplete or truncated addresses are not added as monitoring seeds.</li>
  <li>The Shelbit Solana identifier is an official sanctions seed and should be watched directly; connected wallets do not automatically inherit the Shelbit or IRGC label.</li>
  <li>The Genesis-era whale case includes the complete victim and theft-linked addresses published by ZachXBT, but the compromise vector remains unknown.</li>
  <li>SUNUSI is classified as malicious authorization and Permanent Delegate abuse, not as a confirmed rug pull or private-key compromise.</li>
  <li>FlashTrade currently has no machine-readable attacker-address file because no complete public attacker address was resolved in the reviewed evidence.</li>
  <li>The SpaceX/FIFA drainer wave is tracked as a campaign because its domains, tokens, receiving addresses, and operator infrastructure rotate rapidly.</li>
  <li>Cross-chain counterparties are not automatically threat-labeled merely because they interacted with incident proceeds or sanctioned seeds.</li>
</ul>
