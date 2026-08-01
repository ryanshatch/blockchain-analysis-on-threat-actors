<div align="center" style="text-align: center;">
<h1>New SOL Threat-Wallet Alert</h1>
<h2>DeFiTuna Lending Exploit</h2>
</div>

<table>
  <thead>
    <tr><th align="left">Field</th><th align="left">Details</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Chain</strong></td><td>Solana</td></tr>
    <tr><td><strong>Incident</strong></td><td>DeFiTuna leveraged-position health-check bypass and USDC lending-vault drain</td></tr>
    <tr><td><strong>Incident date</strong></td><td>July 16, 2026</td></tr>
    <tr><td><strong>Source type</strong></td><td>Protocol-endorsed incident analysis, CertiK, BlockSec, Solscan, and cross-chain explorer evidence</td></tr>
    <tr><td><strong>Confidence</strong></td><td>High for the incident, exploit transaction, protocol program, damaged vault, and published attacker addresses; medium for common-control attribution across every address</td></tr>
    <tr><td><strong>Estimated loss</strong></td><td>Approximately 569,601 USDC</td></tr>
    <tr><td><strong>Why it matters</strong></td><td>The protocol accepted a position with zero calculated asset value and non-zero debt as healthy. Attacker-controlled swap routing and a deliberately illiquid pool reduced the received TUNA value below an integer-conversion threshold, allowing the solvency check to be bypassed.</td></tr>
  </tbody>
</table>

<h2>Incident Summary</h2>

<p>
On July 16, 2026, attackers created a highly illiquid TUNA/USDC Fusion pool and placed two attacker-controlled limit-order positions into it. They then opened a DeFiTuna spot position with zero collateral, borrowed approximately 570,000 USDC from the protocol's lending vault, and supplied Jupiter route data that directed the borrowed funds through the malicious pool.
</p>

<p>
The swap sent approximately 569,601 USDC into the attacker-controlled pool but returned only a dust amount of TUNA to the DeFiTuna position. When DeFiTuna converted that TUNA balance into USDC terms, integer truncation reduced the calculated asset value to zero. The health-check branch treated a zero-value position as healthy without requiring the debt to also be zero.
</p>

<p>
The attackers then removed the USDC captured by their malicious liquidity positions, leaving the lending pool with approximately 569,601 USDC in bad debt.
</p>

<h2>Direct Incident-Watch Seeds</h2>

<h3>Primary Attacker / Orchestration Address</h3>
<p><a href="https://solscan.io/account/9ytGWP8tCRF1keREJ5VHqBpSuM9MZYwm3oFQQa1SvESb"><code>9ytGWP8tCRF1keREJ5VHqBpSuM9MZYwm3oFQQa1SvESb</code></a></p>
<p><strong>Recommended use:</strong> Watch directly and use for transaction-sequence and funding-source expansion.</p>

<h3>Attacker Address / Fake Pool Address</h3>
<p><a href="https://solscan.io/account/917DKTphW3rhBG5gsJpwKsNGisNV2dx74uUFd8HBEjtg"><code>917DKTphW3rhBG5gsJpwKsNGisNV2dx74uUFd8HBEjtg</code></a></p>
<p>CertiK identifies this address both as an attacker address and as the fake pool used in the exploit flow.</p>
<p><strong>Recommended use:</strong> Watch directly and inspect pool creation, route accounts, and connected withdrawals.</p>

<h3>Malicious Limit-Order Owner</h3>
<p><a href="https://solscan.io/account/7hiHL8AgDuLNVDQLfN3GHdLAEeCN1F7uz6nSANRvFJst"><code>7hiHL8AgDuLNVDQLfN3GHdLAEeCN1F7uz6nSANRvFJst</code></a></p>
<p>Owned one of the two limit-order positions that received approximately half of the routed USDC.</p>
<p><strong>Recommended use:</strong> Watch directly and trace Mayan bridge activity and downstream proceeds.</p>

<h3>Malicious Limit-Order Owner</h3>
<p><a href="https://solscan.io/account/BK9aTnKfPNnnj45Me5ACrky2vexzUrZHRzr4BjmQpH3c"><code>BK9aTnKfPNnnj45Me5ACrky2vexzUrZHRzr4BjmQpH3c</code></a></p>
<p>Owned the second limit-order position that received approximately half of the routed USDC.</p>
<p><strong>Recommended use:</strong> Watch directly and trace Mayan bridge activity and downstream proceeds.</p>

<h3>Additional Published Attacker Addresses</h3>
<ul>
  <li><code>8P3H7Hy98LWhw5QhuXdoigVdAzPCYRTYjdtQQKhGwvqD</code></li>
  <li><code>GrXBhM6Ty6YxubFp8zubtJF12WXmKj1dhMyakRPeaDpo</code></li>
  <li><code>F4xUroPaHro4gb2JAqa3e93E7DdZytRQJ4L2cHT5E53p</code></li>
  <li><code>ETGhosPrFApbiiKXDpxrhBz7J2MdTA3dxnL2Nkio9vEX</code></li>
  <li><code>4ZKkGZuoXqgSHbmsJXUib3dgn5WNhzbPEXrxuMYJ5oQ3</code></li>
</ul>
<p><strong>Recommended use:</strong> Retain as incident-linked graph-expansion seeds. Confirm the role of each address from transaction-level evidence before applying a narrower attacker label.</p>

<h3>Ethereum Proceeds Wallet</h3>
<p><a href="https://etherscan.io/address/0x509B9D094A6C26D716aaC131E8aDee5B16B86d3e"><code>0x509B9D094A6C26D716aaC131E8aDee5B16B86d3e</code></a></p>
<p>CertiK reported that bridged proceeds reached Ethereum and that approximately 291,696 DAI and 5 ETH remained in this wallet as of July 20, 2026.</p>
<p><strong>Recommended use:</strong> Watch directly for dispersal, exchange deposits, bridge reuse, and privacy-protocol interactions.</p>

<h2>Protocol and Victim Infrastructure — Do Not Threat-Label</h2>

<table>
  <thead>
    <tr><th align="left">Role</th><th align="left">Address</th><th align="left">Handling</th></tr>
  </thead>
  <tbody>
    <tr><td>DeFiTuna program</td><td><code>tuna4uSQZncNeeiAMKbstuxA9CUkHH6HmC64wgmnogD</code></td><td>Protocol infrastructure; use for exploit-call and program-interaction filtering</td></tr>
    <tr><td>Damaged USDC vault</td><td><code>D76dDcSU5HnAGqVEZCDLyGgLpTp4xZuqeZyVDtUdDv55</code></td><td>Victim vault; use as the source of the borrowed USDC and bad-debt evidence</td></tr>
  </tbody>
</table>

<h2>Primary Exploit Transaction</h2>
<p><a href="https://solscan.io/tx/124ibr7NU7AtJdeZ1WJjJy5YathNiBtCnV554uwJtkc7qEXeF64dmCziv4QoiEEMRG6EmCRx8ec2LkARpWH3kvEG"><code>124ibr7NU7AtJdeZ1WJjJy5YathNiBtCnV554uwJtkc7qEXeF64dmCziv4QoiEEMRG6EmCRx8ec2LkARpWH3kvEG</code></a></p>

<h2>Technical Root Cause</h2>

<ol>
  <li>The attacker controlled the Jupiter route and directed the borrowed USDC through a separate, attacker-created TUNA/USDC pool.</li>
  <li>The protocol's pre-swap oracle check validated the normal market pool rather than the pool used by the supplied route.</li>
  <li>The malicious pool returned only a dust amount of TUNA.</li>
  <li>Fixed-point-to-integer conversion truncated the position's calculated asset value to zero.</li>
  <li>The health check treated <code>total == 0</code> as healthy without enforcing <code>debt == 0</code>.</li>
  <li>The attacker-controlled liquidity positions retained the routed USDC and withdrew it.</li>
</ol>

<blockquote>
The core vulnerability was not simply low liquidity or price manipulation. The final security failure was a solvency check that accepted zero assets with outstanding debt as healthy.
</blockquote>

<h2>Classification</h2>
<ul>
  <li><strong>Incident type:</strong> Solana protocol-logic exploit / flawed health check</li>
  <li><strong>Primary direct-watch targets:</strong> the published attacker and malicious liquidity-position addresses</li>
  <li><strong>Cross-chain proceeds:</strong> Solana to Ethereum through Mayan</li>
  <li><strong>Privacy interaction:</strong> approximately 140 ETH was reported deposited into Railgun</li>
  <li><strong>Named actor:</strong> none publicly identified</li>
  <li><strong>Material unknown:</strong> whether all nine published Solana addresses were controlled by one actor or coordinated actors</li>
</ul>

<h2>Sources</h2>
<ul>
  <li><a href="https://www.certik.com/blog/defituna-incident-analysis">CertiK — DeFiTuna Incident Analysis</a></li>
  <li><a href="https://blocksec.com/blog/web3-security-barnbridge-defituna-exploits">BlockSec — DeFiTuna flawed health-check analysis</a></li>
  <li><a href="https://solscan.io/tx/124ibr7NU7AtJdeZ1WJjJy5YathNiBtCnV554uwJtkc7qEXeF64dmCziv4QoiEEMRG6EmCRx8ec2LkARpWH3kvEG">Solscan — primary exploit transaction</a></li>
</ul>

<hr>
<h2>In other words:</h2>
<p>
DeFiTuna let the attacker borrow roughly $570,000 with no collateral and choose the swap route. The attacker sent the borrowed USDC into a pool they controlled and returned almost no TUNA to the borrowing position. A rounding step converted the tiny TUNA value to zero, and the protocol mistakenly treated that zero-value position as healthy even though it still owed the full loan.
</p>
<p>
The code did not merely misprice an asset. It accepted a position with no meaningful assets and substantial debt as solvent.
</p>
<p><strong>TLDR:</strong> The attacker engineered a dust-valued position, triggered a zero-value rounding path, bypassed DeFiTuna's solvency check, and withdrew approximately 569,601 USDC through attacker-controlled liquidity positions.</p>
