<div align="center">
<h1>Multi-Chain Threat and Incident Index</h1>
<p><strong>Incidents and threat campaigns whose exploit execution, treasury compromise, bridge movement, proceeds flow, recovery activity, sanctions attribution, or malicious infrastructure spans more than one blockchain ecosystem.</strong></p>
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
      <td>Two 2026 incidents across Solana, Ethereum, Polygon, and Base</td>
      <td>July Solana pool-accounting exploit plus distinct August Base/CCTP message-validation exploit</td>
    </tr>
    <tr>
      <td><a href="./August-2026-Security-Sweep/"><code>August-2026-Security-Sweep/</code></a></td>
      <td>MAYAChain, Bitcoin, Ethereum, Solana, ICON, Sonic, Cronos, Arbitrum, BNB Chain, Harmony, TRON, Polygon, Base, and multi-chain users</td>
      <td>August 20-31, 2026 cross-ecosystem sweep covering Rain's complete attacker/proceeds cluster, the ICON replay exploit, the zero-seed Tectonic/Cronos and Moonwell/MAMO cases, Term Finance laundering, Sandbox Base/BSC, Bofur Capital, Maya external-L1, Coinsbuy Ethereum/TRON, Allbridge Base/CCTP, and prior exploit, phishing, rug-pull, and laundering intelligence</td>
    </tr>
    <tr>
      <td><a href="./ICON-Migration-Replay-Exploit/"><code>ICON-Migration-Replay-Exploit/</code></a></td>
      <td>ICON exploit execution, Sonic collateral activity, and Ethereum proceeds consolidation</td>
      <td>August 27 signed-message replay and withdrawal-uniqueness exploit with three officially identified attacker-controlled accounts represented as four chain-specific records</td>
    </tr>
    <tr>
      <td><a href="./Iranian-MOIS-Cyber-Network/"><code>Iranian-MOIS-Cyber-Network/</code></a></td>
      <td>Bitcoin, Ethereum, and TRON</td>
      <td>August 24, 2026 OFAC attribution: 30 direct seeds for four MOIS-linked cyber actors plus one separate Iran sanctions-finance USDT/TRON seed</td>
    </tr>
    <tr>
      <td><a href="./Shelbit-Network/"><code>Shelbit-Network/</code></a></td>
      <td>Bitcoin, Ethereum, Solana, and TRON</td>
      <td>August 7, 2026 OFAC counterterrorism sanctions attribution covering Siavash Kayvanpour, Shelbit Exchange, and Crypto Home DMCC</td>
    </tr>
    <tr>
      <td><a href="./SpaceX-FIFA-Drainers/"><code>SpaceX-FIFA-Drainers/</code></a></td>
      <td>Solana and EVM users; broader campaign set also used direct Bitcoin and Ethereum deposit scams</td>
      <td>Wallet-drainer, malicious dApp, fake-token, impersonation, and investment-scam campaign</td>
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
A case is stored under <code>Multi-Chain/</code> when the full investigation cannot be accurately represented by one chain directory. Each report still records the exact exploit-origin chain, vulnerable deployment, destination networks, proceeds chains, recovery networks, sanctions programs, campaign targets, and address roles separately.
</p>

<p>
Solana-origin cases are also cross-listed in <a href="../SOL/"><code>SOL/README.md</code></a> so chain-specific incident counts do not omit cross-chain cases such as Across Protocol or Allbridge Core. Multi-victim campaigns such as the SpaceX/FIFA drainer wave are cross-referenced there but are not counted as single Solana protocol incidents. Official multi-chain sanctions cases such as the Shelbit and Iranian MOIS cyber-actor networks are cross-linked from the affected chain indexes but are not counted as exploit incidents.
</p>

<h2>Attribution Boundaries</h2>
<ul>
  <li>Bridge, relayer, exchange, router, protocol, victim, vault, and recovery addresses are not automatically classified as threat-controlled.</li>
  <li>Attacker seeds and proceeds wallets require a complete address and evidence-supported role.</li>
  <li>Official OFAC digital-currency identifiers are direct sanctions-watch seeds; transactional proximity to them does not automatically transfer the sanctioned entity or actor label.</li>
  <li>Origin-chain classification describes where an exploit or drain began; proceeds-chain classification describes where stolen assets later moved.</li>
  <li>Campaign domains, token lures, commercial drainer-kit names, and receiving addresses should remain separate indicator classes rather than being collapsed into a single actor attribution.</li>
</ul>
