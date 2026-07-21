<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<div align="center">
  <img alt="Header image" src="https://i0.wp.com/thegeorgiasun.com/wp-content/uploads/2021/12/shutterstock_1919690516-scaled.jpg?fit=2000%2C1333&quality=89&ssl=1">
  <h1>Blockchain Analysis on Threat Actors</h1>
  <p><strong>A defensive on-chain intelligence repository for tracking sanctioned wallets, threat actors, exploit flows, scams, rug pulls, and suspicious cryptocurrency activity.</strong></p>
</div>

<hr>

<h2>Overview</h2>

<p>This repository contains cryptocurrency addresses and transaction data collected through:</p>

<ul>
  <li>Official government and law-enforcement disclosures</li>
  <li>Public blockchain explorers</li>
  <li>Security researchers and threat-intelligence providers</li>
  <li>Public reporting</li>
  <li>Personally encountered fraud and scam-baiting investigations</li>
  <li>Independent on-chain analysis</li>
</ul>

<p>Entries range from <strong>official, high-confidence attributions</strong> to <strong>provisional investigative leads</strong>. Each case should be evaluated according to its source type, confidence level, supporting evidence, and stated limitations.</p>

<blockquote>
  Inclusion in this repository does not independently prove criminal activity. Addresses associated with active investigations, suspected incidents, or third-party reporting should be treated as provisional unless confirmed by an authoritative source.
</blockquote>

<hr>

<h2>Repository Structure</h2>

<h3>Analysis Directories</h3>

<table>
  <thead>
    <tr><th align="left">Directory</th><th align="left">Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="./1VPNS/"><code>1VPNS/</code></a></td><td>OFAC-designated wallets associated with Dmytro Rashevskyi and First VPN Service / 1VPNS across BTC, ETH, and SOL.</td></tr>
    <tr><td><a href="./EVM/"><code>EVM/</code></a></td><td>Ethereum and EVM-compatible threat-wallet, exploit, sanctions, bridge-flow, and protocol-incident investigations.</td></tr>
    <tr><td><a href="./FTX/"><code>FTX/</code></a></td><td>Historical FTX and Alameda Research wallet analysis, balances, addresses, and transaction activity.</td></tr>
    <tr><td><a href="./HBAR/"><code>HBAR/</code></a></td><td>Hedera-to-Ethereum suspected theft and bridge-flow analysis.</td></tr>
    <tr><td><a href="./Lazarus/"><code>Lazarus/</code></a></td><td>DPRK TraderTraitor / Lazarus Group wallets, including addresses connected to the Bybit theft and earlier incidents.</td></tr>
    <tr><td><a href="./SOL/"><code>SOL/</code></a></td><td>Solana-specific threat-actor, governance, exploit, and suspicious-wallet investigations.</td></tr>
    <tr><td><a href="./SOL/BonkDAO/"><code>SOL/BonkDAO/</code></a></td><td>Analysis of the BonkDAO governance attack and associated on-chain activity.</td></tr>
    <tr><td><a href="./SOL/HOPE/"><code>SOL/HOPE/</code></a></td><td>Analysis of the Solana-based HOPE token, wallet concentration, transfers, sales, and suspected rug activity.</td></tr>
    <tr><td><a href="./TRON/"><code>TRON/</code></a></td><td>TRON-specific sanctions, state-linked attribution, and threat-wallet investigations.</td></tr>
    <tr><td><a href="./TRON/Central-Bank-of-Iran/"><code>TRON/Central-Bank-of-Iran/</code></a></td><td>OFAC attribution involving TRON addresses associated with the Central Bank of Iran.</td></tr>
  </tbody>
</table>

<h3>Current EVM Cases</h3>

<table>
  <thead>
    <tr><th align="left">Directory</th><th align="left">Network</th><th align="left">Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="./EVM/Ethereum/Zunami-Protocol/"><code>EVM/Ethereum/Zunami-Protocol/</code></a></td>
      <td>Ethereum</td>
      <td>Zunami Protocol exploit-cluster analysis covering 2023 and 2025 attacker wallets, staging infrastructure, cash-out activity, and operational attribution.</td>
    </tr>
    <tr>
      <td><a href="./EVM/Arbitrum/Ostium/"><code>EVM/Arbitrum/Ostium/</code></a></td>
      <td>Arbitrum One</td>
      <td>Ostium oracle-manipulation exploit analysis covering the execution wallet, payout wallet, entry contract, confirmed transaction, and attribution boundaries.</td>
    </tr>
  </tbody>
</table>

<h3>Data and Supporting Directories</h3>

<table>
  <thead>
    <tr><th align="left">Directory</th><th align="left">Description</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="./parsing/"><code>parsing/</code></a></td><td>Transaction exports, CSV datasets, combined transfer records, parsing scripts, and analysis notes.</td></tr>
    <tr><td><a href="./parsing/sol%20tx%20history/"><code>parsing/sol tx history/</code></a></td><td>Raw and processed Solana transaction-history exports.</td></tr>
    <tr><td><a href="./img/"><code>img/</code></a></td><td>Images and supporting visual evidence used by repository documentation.</td></tr>
  </tbody>
</table>

<h3>Root Files</h3>

<table>
  <thead>
    <tr><th align="left">File</th><th align="left">Purpose</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="./readme.md"><code>readme.md</code></a></td><td>Main repository overview and navigation.</td></tr>
    <tr><td><a href="./wallets.md"><code>wallets.md</code></a></td><td>Compact wallet index separating direct threat seeds from operational and infrastructure pivots.</td></tr>
    <tr><td><a href="./scammer%20DB.html"><code>scammer DB.html</code></a></td><td>Legacy HTML-format scammer and wallet database.</td></tr>
  </tbody>
</table>

<hr>

<h2>Current Research Coverage</h2>

<table>
  <thead>
    <tr><th align="left">Category</th><th align="left">Examples</th></tr>
  </thead>
  <tbody>
    <tr><td>Sanctions intelligence</td><td>OFAC-designated infrastructure, state-linked wallets, and sanctioned actors</td></tr>
    <tr><td>State-sponsored activity</td><td>DPRK TraderTraitor / Lazarus Group</td></tr>
    <tr><td>Cybercrime infrastructure</td><td>First VPN Service / 1VPNS</td></tr>
    <tr><td>Exchange and protocol incidents</td><td>FTX, Alameda Research, Bybit, Hedera, Zunami Protocol, Ostium, and related exploit or theft flows</td></tr>
    <tr><td>Oracle and privileged-access exploits</td><td>Ostium oracle manipulation and Zunami privileged-wallet relationships</td></tr>
    <tr><td>Governance attacks</td><td>BonkDAO</td></tr>
    <tr><td>Rug pulls and token manipulation</td><td>HOPE and other Solana ecosystem cases</td></tr>
    <tr><td>Personally encountered fraud</td><td>Spear-phishing, impersonation, hacked-account, and payment scams</td></tr>
    <tr><td>Transaction analysis</td><td>Wallet clustering, bridge activity, swaps, consolidation, exchange deposits, and contract-control paths</td></tr>
  </tbody>
</table>

<hr>

<h2>Chain Coverage</h2>

<table>
  <thead>
    <tr><th align="left">Chain</th><th align="left">Coverage</th></tr>
  </thead>
  <tbody>
    <tr><td>Bitcoin</td><td>Sanctioned wallets, fraud payments, DPRK-linked addresses, and scam-related transfers</td></tr>
    <tr><td>Ethereum</td><td>Exploit seeds, staging wallets, sanctioned addresses, cash-out paths, token swaps, and privileged-wallet pivots</td></tr>
    <tr><td>Arbitrum</td><td>L2 exploit execution, oracle manipulation, malicious contract paths, payout wallets, and downstream laundering activity</td></tr>
    <tr><td>Other EVM chains</td><td>Bridge destinations, contract interactions, exchange deposits, and consolidation activity</td></tr>
    <tr><td>Solana</td><td>Rug pulls, governance attacks, NFT-related fraud, token concentration, and scam wallets</td></tr>
    <tr><td>TRON</td><td>Sanctions attribution and state-linked financial infrastructure</td></tr>
    <tr><td>Hedera</td><td>Suspected exploit and cross-chain bridge activity</td></tr>
  </tbody>
</table>

<hr>

<h2>Confidence Levels</h2>

<table>
  <thead>
    <tr><th align="left">Confidence</th><th align="left">Meaning</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>High</strong></td><td>Official attribution or direct, well-corroborated transaction-level evidence from authoritative explorers, law enforcement, courts, or established security firms</td></tr>
    <tr><td><strong>Medium</strong></td><td>Supported by reputable researchers, security firms, blockchain records, or multiple reporting sources, but material attribution questions remain</td></tr>
    <tr><td><strong>Low</strong></td><td>Preliminary lead, personally encountered wallet, unconfirmed attribution, or incomplete transaction evidence</td></tr>
    <tr><td><strong>Unknown</strong></td><td>Address retained for monitoring but attribution has not been sufficiently established</td></tr>
  </tbody>
</table>

<p>Confidence describes the strength of the attribution, not the certainty that every transaction involving the address is malicious.</p>

<hr>

<h2>Recommended Case Format</h2>

<p>Each investigation directory should contain a <code>README.md</code> and, where useful, machine-readable address or transaction datasets.</p>

<table>
  <thead>
    <tr><th align="left">Field</th><th align="left">Description</th></tr>
  </thead>
  <tbody>
    <tr><td>Incident or actor</td><td>Name of the actor, organization, protocol, scam, or incident</td></tr>
    <tr><td>Published date</td><td>Date the attribution or alert was published</td></tr>
    <tr><td>Source type</td><td>OFAC, FBI, explorer attribution, security researcher, public reporting, personal investigation, or another source</td></tr>
    <tr><td>Confidence</td><td>High, medium, low, or unknown</td></tr>
    <tr><td>Classification</td><td>Sanctioned wallet, exploit seed, staging wallet, payout wallet, bridge-flow wallet, operational pivot, contract pivot, or another role</td></tr>
    <tr><td>Network and chain ID</td><td>Exact blockchain network and chain ID where applicable</td></tr>
    <tr><td>Address</td><td>Complete blockchain address</td></tr>
    <tr><td>Address type</td><td>EOA, contract, custodial deposit address, token contract, or other type</td></tr>
    <tr><td>Monitoring action</td><td>Recommended direct-watch, graph-expansion, or exclusion handling</td></tr>
    <tr><td>Evidence</td><td>Source links, transaction hashes, screenshots, exports, or supporting notes</td></tr>
    <tr><td>Limitations</td><td>Unresolved questions, conflicting evidence, or provisional assumptions</td></tr>
  </tbody>
</table>

<hr>

<h2>Research Workflow</h2>

<ol>
  <li>Identify an address through an authoritative disclosure, reputable alert, public report, or direct investigation.</li>
  <li>Confirm the address, network, chain ID, and address type using an appropriate blockchain explorer.</li>
  <li>Record the original source and publication date.</li>
  <li>Assign an attribution confidence level.</li>
  <li>Separate direct threat seeds from operational, infrastructure, exchange, and contract pivots.</li>
  <li>Review direct counterparties, token transfers, bridge activity, swaps, contract calls, and consolidation behavior.</li>
  <li>Store machine-readable address and transaction records alongside the case file.</li>
  <li>Add material attribution changes or newly discovered addresses to the relevant case directory.</li>
  <li>Preserve previous findings when attribution changes instead of silently replacing them.</li>
</ol>

<hr>

<h2>Common Monitoring Uses</h2>

<ul>
  <li>Sanctions-exposure screening</li>
  <li>Wallet and counterparty monitoring</li>
  <li>Graph-expansion seeds</li>
  <li>Bridge-flow and contract-control-path analysis</li>
  <li>Exchange-deposit detection</li>
  <li>Mixer-interaction analysis</li>
  <li>Theft-fund tracing</li>
  <li>Scam-pattern comparison</li>
  <li>Threat-intelligence enrichment</li>
  <li>Historical incident research</li>
</ul>

<hr>

<h2>Source Standards</h2>

<ul>
  <li>U.S. Department of the Treasury and OFAC</li>
  <li>FBI, IC3, DOJ, courts, and official seizure notices</li>
  <li>Blockchain explorers and transaction-level evidence</li>
  <li>Established blockchain-security and forensic firms</li>
  <li>Reputable on-chain researchers</li>
  <li>Exchange-security disclosures and protocol postmortems</li>
</ul>

<p>Social-media posts, anonymous claims, and unverified community reports should be treated as leads rather than confirmed attribution.</p>

<hr>

<h2>Data Handling</h2>

<ul>
  <li>Preserve addresses exactly as published.</li>
  <li>Record the exact blockchain network and chain ID.</li>
  <li>Separate EOAs, contracts, custodial infrastructure, and token contracts.</li>
  <li>Separate confirmed facts from analytical conclusions.</li>
  <li>Clearly identify provisional or disputed attribution.</li>
  <li>Avoid publishing unnecessary personally identifiable information.</li>
  <li>Do not assume every counterparty of a malicious wallet is also malicious.</li>
  <li>Do not automatically threat-label exchange, bridge, protocol, token, or mixer infrastructure.</li>
  <li>Reassess older entries when new attribution or transaction evidence becomes available.</li>
</ul>

<hr>

<h2>Disclaimer</h2>

<p><strong>This repository is maintained for defensive security research, fraud analysis, threat intelligence, education, and historical documentation.</strong></p>

<blockquote>
The information may be incomplete, outdated, provisional, or dependent on third-party reporting. Users should independently verify addresses, transactions, and attribution before relying on the data for legal, compliance, enforcement, or financial decisions.
</blockquote>

</body>
</html>
