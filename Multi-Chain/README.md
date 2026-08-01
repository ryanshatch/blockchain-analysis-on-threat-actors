<div align="center">
<h1>Multi-Chain Threat and Incident Index</h1>
<p><strong>Incidents whose exploit execution, treasury compromise, bridge movement, proceeds flow, or recovery activity spans more than one blockchain ecosystem.</strong></p>
</div>

<hr>

<table>
  <thead>
    <tr><th align="left">Case</th><th align="left">Origin or affected networks</th><th align="left">Classification</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="./Across-Protocol/"><code>Across-Protocol/</code></a></td>
      <td>Solana origin; fraudulent fills across multiple destination chains; Ethereum recovery activity</td>
      <td>Off-chain event-parser and relayer exploit</td>
    </tr>
    <tr>
      <td><a href="./Allbridge-Core/"><code>Allbridge-Core/</code></a></td>
      <td>Solana exploit origin; Ethereum proceeds flow</td>
      <td>Stablecoin-pool account-aliasing and accounting manipulation</td>
    </tr>
    <tr>
      <td><a href="./Triple-A/"><code>Triple-A/</code></a></td>
      <td>Ethereum, Solana, TRON, TON, Polygon, Arbitrum, Bitcoin, and related routing</td>
      <td>Multi-chain treasury-wallet compromise and proceeds consolidation</td>
    </tr>
  </tbody>
</table>

<h2>Storage Rule</h2>

<p>
A case is stored under <code>Multi-Chain/</code> when the full investigation cannot be accurately represented by one chain directory. Each report still records the exact exploit-origin chain, vulnerable deployment, destination networks, proceeds chains, recovery networks, and address roles separately.
</p>

<p>
Solana-origin cases are also cross-listed in <a href="../SOL/"><code>SOL/README.md</code></a> so chain-specific incident counts do not omit cross-chain cases such as Across Protocol or Allbridge Core.
</p>

<h2>Attribution Boundaries</h2>
<ul>
  <li>Bridge, relayer, exchange, router, protocol, victim, vault, and recovery addresses are not automatically classified as threat-controlled.</li>
  <li>Attacker seeds and proceeds wallets require a complete address and evidence-supported role.</li>
  <li>Origin-chain classification describes where the exploit began; proceeds-chain classification describes where stolen assets later moved.</li>
</ul>
