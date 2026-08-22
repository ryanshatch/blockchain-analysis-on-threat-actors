<div align="center" style="text-align: center;">
<h1>Allbridge 2026 Security Case History</h1>
<h2>Two Distinct Incidents: Solana Core and Base CCTP</h2>
</div>

<h2>Incident Comparison</h2>

<table>
  <thead>
    <tr><th align="left">Incident</th><th align="left">Date</th><th align="left">Environment</th><th align="left">Classification</th><th align="left">Estimated impact</th></tr>
  </thead>
  <tbody>
    <tr><td>Allbridge Core Solana pool</td><td>July 19, 2026</td><td>Solana origin; Ethereum proceeds</td><td>Account aliasing and liquidity-pool accounting manipulation</td><td>Approximately $1.65M</td></tr>
    <tr><td>Allbridge CCTP / Next</td><td>August 19, 2026</td><td>Polygon preparation; Base execution</td><td>Cross-chain message-validation and internal-accounting exploit</td><td>Approximately $189,751.55 attacker profit; approximately $191K legitimate Router liquidity</td></tr>
  </tbody>
</table>

<blockquote>
These are separate incidents in different implementations. Do not merge their attacker attribution, mechanics, or loss figures.
</blockquote>

<h2>Incident 1 — July 19 Solana Pool Exploit</h2>

<table>
  <thead>
    <tr><th align="left">Field</th><th align="left">Details</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Origin chain</strong></td><td>Solana</td></tr>
    <tr><td><strong>Proceeds chain</strong></td><td>Ethereum</td></tr>
    <tr><td><strong>Incident</strong></td><td>Allbridge Core Solana stablecoin-pool accounting manipulation funded through a Kamino flash loan</td></tr>
    <tr><td><strong>Incident date</strong></td><td>July 19, 2026</td></tr>
    <tr><td><strong>Source type</strong></td><td>Allbridge statements, CertiK, GoPlus Security, PeckShield, public explorers, and independent transaction analysis</td></tr>
    <tr><td><strong>Confidence</strong></td><td>High for the incident, primary exploit transaction, attacker addresses, affected vaults, and cross-chain proceeds path; medium-high for the precise internal writeback mechanism pending a fully reproducible official code-level report</td></tr>
    <tr><td><strong>Estimated loss</strong></td><td>Approximately $1.65 million in USDC and USDT</td></tr>
    <tr><td><strong>Why it matters</strong></td><td>The deployed Solana program accepted repeated swaps where send-side and receive-side accounts represented the same USDT state. Public analysis indicates the resulting account aliasing and virtual-balance updates corrupted pool accounting, enabling a small final input to withdraw approximately 2.24 million USDC.</td></tr>
  </tbody>
</table>

<h2>Incident 1 Summary</h2>

<p>
On July 19, 2026, the attacker borrowed approximately 1.12 million USDC through a Kamino flash loan and interacted with Allbridge Core's Solana USDC/USDT liquidity system. The attacker executed repeated USDT-to-USDT self-swaps using aliased send and receive accounts, progressively distorting the protocol's internal virtual balances.
</p>

<p>
After the accounting state had been skewed, the attacker exchanged approximately 3,987 USDT for about 2.24 million USDC, repaid the Kamino flash loan and fee, and retained approximately 1.65 million stablecoins. The proceeds were then moved from Solana to Ethereum through Mayan-related cross-chain infrastructure and consolidated at a publicly identified Ethereum address before further dispersion.
</p>

<p>
Allbridge paused Core, asked liquidity providers to withdraw from affected pools, requested that positive-arbitrage recipients return funds for LP compensation, and later relaunched Core using CCTP and LayerZero routing without the liquidity-pool model that had been attacked.
</p>

<h2>Incident 1 Direct Incident-Watch Seeds</h2>

<h3>Primary Solana Attacker Address</h3>
<p><a href="https://solscan.io/account/FhffBraZsGn4H2LxLNToEcaHWEfWwT2UcSz4oRHb7Qdc"><code>FhffBraZsGn4H2LxLNToEcaHWEfWwT2UcSz4oRHb7Qdc</code></a></p>
<p>Publicly identified as the signer and primary Solana attacker wallet associated with the exploit transaction.</p>
<p><strong>Recommended use:</strong> Highest-priority direct-watch seed. Expand funding, program calls, bridge preparation, Mayan interactions, and connected token accounts.</p>

<h3>Ethereum Proceeds-Consolidation Address</h3>
<p><a href="https://etherscan.io/address/0x651591b68A9c9650FB23F642162353306281ffDe"><code>0x651591b68A9c9650FB23F642162353306281ffDe</code></a></p>
<p>CertiK, PeckShield, GoPlus, and independent investigators linked this address to the Solana-to-Ethereum proceeds flow.</p>
<p><strong>Recommended use:</strong> Watch directly for asset dispersion, exchange deposits, privacy-protocol interactions, cross-chain routing, and recovery activity.</p>

<h2>Primary Exploit Transaction</h2>
<p><a href="https://solscan.io/tx/3LNLaGi36bqoSBFBqcQ3ZvDbnGCxrxu4rqahZrnfHZjKSYxfR1mqiCXtBXjjeBmoRQDeSiKxZ7c1nFb8pBgTY39Q"><code>3LNLaGi36bqoSBFBqcQ3ZvDbnGCxrxu4rqahZrnfHZjKSYxfR1mqiCXtBXjjeBmoRQDeSiKxZ7c1nFb8pBgTY39Q</code></a></p>

<h2>Protocol and Victim Infrastructure — Do Not Threat-Label</h2>

<table>
  <thead>
    <tr><th align="left">Role</th><th align="left">Address</th><th align="left">Handling</th></tr>
  </thead>
  <tbody>
    <tr><td>Allbridge Core Solana program</td><td><code>BrdgN2RPzEMWF96ZbnnJaUtQDQx7VRXYaHHbYCBvceWB</code></td><td>Protocol infrastructure; use for call filtering and exploit-path reconstruction</td></tr>
    <tr><td>Victim account</td><td><code>7DyZQw3iV5zhHssnNA6Nopi5zc8NGLbYjHMcaok6NN66</code></td><td>Victim-side account; preserve as incident evidence only</td></tr>
    <tr><td>USDT token vault</td><td><code>2xY9TDMjfvdoXQPYMATQLEY6z55KpJrHf8NpkNdAvohV</code></td><td>Affected protocol token account; do not classify as attacker infrastructure</td></tr>
    <tr><td>USDC token vault</td><td><code>G6Qo3WW7RbWpSmACAocTBVgx6JW5kgRpUhABphEoDMfP</code></td><td>Affected protocol token account; do not classify as attacker infrastructure</td></tr>
    <tr><td>Official return / LP-compensation address</td><td><code>0x01a494079DCB715f622340301463cE50cd69A4D0</code></td><td>Official recovery destination published by Allbridge; never threat-label</td></tr>
  </tbody>
</table>

<h2>Technical Root Cause</h2>

<ol>
  <li>The attacker flash-borrowed approximately 1,121,957 USDC from Kamino.</li>
  <li>A normal swap converted the borrowed USDC into approximately 948,928 USDT.</li>
  <li>The attacker submitted five USDT-to-USDT self-swaps while supplying the same or aliased mint, pool, vault, and user-token accounts on both sides of the swap.</li>
  <li>The deployed program accepted the account aliases even though the instruction logic assumed independent send and receive state.</li>
  <li>Public transaction analysis indicates the repeated calls caused inconsistent virtual-balance processing or stale-state writeback, progressively corrupting the USDT pool state.</li>
  <li>The attacker then exchanged approximately 3,987 USDT for about 2,240,207 USDC using the corrupted state.</li>
  <li>After repaying the flash loan and fee, the attacker retained approximately 1.65 million USDC and USDT.</li>
</ol>

<blockquote>
The flash loan supplied temporary capital, but it was not the vulnerability. The security failure was accepting aliased mutable accounts in a swap path whose accounting assumed distinct send and receive states.
</blockquote>

<h2>Fund Flow</h2>

<pre>
Kamino flash loan on Solana
        ↓
Allbridge USDC/USDT accounting manipulation
        ↓
FhffBraZsGn4H2LxLNToEcaHWEfWwT2UcSz4oRHb7Qdc
        ↓ Mayan / cross-chain routing
0x651591b68A9c9650FB23F642162353306281ffDe on Ethereum
        ↓
Further swaps, dispersion, privacy routes, and exchange-related paths
</pre>

<h2>Classification</h2>
<ul>
  <li><strong>Primary classification:</strong> Solana protocol-accounting exploit with multi-chain proceeds flow</li>
  <li><strong>Exploit origin:</strong> Solana</li>
  <li><strong>Protocol scope:</strong> Multi-chain bridge</li>
  <li><strong>Proceeds destination:</strong> Ethereum</li>
  <li><strong>Direct-watch targets:</strong> primary Solana attacker and Ethereum proceeds-consolidation address</li>
  <li><strong>Do not threat-label:</strong> Allbridge program, victim account, affected vaults, official return address, Mayan infrastructure, or ordinary counterparties</li>
  <li><strong>Named actor:</strong> none publicly identified</li>
</ul>

<h2>Response and Status</h2>
<ul>
  <li>Allbridge paused the affected Core system during investigation.</li>
  <li>The team confirmed an approximately $1.65 million withdrawal from liquidity pools.</li>
  <li>The team requested voluntary returns from positive-arbitrage recipients to compensate affected liquidity providers.</li>
  <li>Allbridge later stated that Core had resumed through CCTP and LayerZero routing without liquidity pools.</li>
  <li>No confirmed attacker fund return or law-enforcement attribution was identified in the reviewed sources at the time of this report.</li>
</ul>

<h2>Incident 2 — August 19 Base CCTP Message-Validation Exploit</h2>

<table>
  <thead>
    <tr><th align="left">Field</th><th align="left">Details</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Preparation chain</strong></td><td>Polygon</td></tr>
    <tr><td><strong>Execution chain</strong></td><td>Base</td></tr>
    <tr><td><strong>Incident date</strong></td><td>August 19, 2026; malicious message prepared July 26</td></tr>
    <tr><td><strong>Classification</strong></td><td>Cross-chain message-validation and internal-accounting exploit</td></tr>
    <tr><td><strong>Estimated impact</strong></td><td>Approximately 189,751.55 USDC attacker profit; approximately 191,112 USDC of legitimate user liquidity was present in the Router</td></tr>
    <tr><td><strong>Confidence</strong></td><td>High for the incident and reconstructed mechanism</td></tr>
  </tbody>
</table>

<p>
SlowMist's reconstruction found that Allbridge's <code>CCTPTokenMessenger</code> did not adequately validate the CCTP message-header <code>sender</code> and <code>recipient</code>. The Router then trusted an internally recorded <code>receivedTokenAmount</code> without proving that the corresponding USDC had actually arrived.
</p>

<ol>
  <li>On July 26, the attacker created a CCTP-style message on Polygon without the normal USDC burn and precomputed the Router message hash.</li>
  <li>The attacker waited approximately 24 days because the forwarding Router normally held little liquidity.</li>
  <li>On August 19, a legitimate user's CCTP transfer placed about 191,112 USDC in the Base Router.</li>
  <li>Roughly six seconds later, the attacker presented the crafted message and obtained a false internal credit of 1,000,000 USDC.</li>
  <li>An Aave flash loan temporarily supplied about 808,844 USDC, satisfying the manipulated accounting condition.</li>
  <li>The Router transferred 999,000 USDC to the attack contract. After flash-loan repayment and approximately 404 USDC in fees, the reported profit was about 189,751.55 USDC.</li>
</ol>

<blockquote>
This was not a recurrence of the July Solana pool exploit. July involved aliased accounts and corrupted liquidity-pool accounting on Solana; August involved forged CCTP-style message state and unverified internal credit on Base.
</blockquote>

<h3>Address Handling</h3>
<p>
No complete attacker EOA or contract address was available in the reviewed authoritative reporting. No new direct-watch seed is added to <code>addresses.csv</code> for this incident. Protocol contracts, the Base Router, Circle infrastructure, Aave, and the legitimate user's transfer must not be threat-labeled merely because they appear in the exploit path.
</p>

<h2>Sources</h2>
<ul>
  <li><a href="https://x.com/Allbridge_io/status/2078932561036722319">Allbridge — initial security notice</a></li>
  <li><a href="https://t.me/s/allbridge_announcements">Allbridge announcement channel — incident confirmation and recovery address</a></li>
  <li><a href="https://blog.autosec.dev/security-events/allbridge-core-solana-pool-manipulation-165m-exploit/">AUTOSEC — incident addresses and primary transaction</a></li>
  <li><a href="https://docs-core.allbridge.io/product/how-does-allbridge-core-work/allbridge-core-contracts">Allbridge documentation — Solana program and pool addresses</a></li>
  <li><a href="https://solscan.io/tx/3LNLaGi36bqoSBFBqcQ3ZvDbnGCxrxu4rqahZrnfHZjKSYxfR1mqiCXtBXjjeBmoRQDeSiKxZ7c1nFb8pBgTY39Q">Solscan — primary exploit transaction</a></li>
  <li><a href="https://www.kucoin.com/news/flash/allbridge-cross-chain-bridge-hacked-for-190-000-after-month-long-attack">SlowMist reconstruction reproduced by KuCoin/MetaEra — August Base/CCTP incident</a></li>
  <li><a href="https://www.theblock.co/news/defi/2026-07-19-allbridge-core-exploit-408855">The Block — July Solana incident and planned migration to CCTP/LayerZero</a></li>
</ul>

<hr>
<h2>Incident 1 in other words:</h2>
<p>
The attacker borrowed about $1.12 million for one transaction, repeatedly asked Allbridge to process USDT as both the asset being sent and the asset being received, and supplied overlapping accounts where the program expected separate state. Those calls damaged the pool's internal accounting. The attacker then traded only a few thousand USDT for roughly $2.24 million USDC, repaid the temporary loan, and kept the difference.
</p>
<p>
This was not a stolen key and the bridge did not accept a forged cross-chain message. It was a Solana account-validation and accounting failure inside Allbridge Core's liquidity-pool model.
</p>
<p>
For Incident 2, the attacker created a validly attested but economically unbacked CCTP-style message, waited for legitimate USDC to reach the Base Router, and used a flash loan to satisfy the Router's manipulated accounting condition before extracting the difference.
</p>
<p><strong>TLDR:</strong> July's Solana incident used aliased swap accounts to corrupt liquidity-pool accounting and extract approximately $1.65 million. A separate August 19 incident abused CCTP message validation and unverified Router credit on Base for approximately $189,751.55 in profit. Only the July incident currently has complete direct-watch addresses in this case.</p>
