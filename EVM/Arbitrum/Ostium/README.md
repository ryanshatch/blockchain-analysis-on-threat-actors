<div align="center">

<h1>Ostium Oracle-Manipulation Exploit</h1>

<p><strong>Arbitrum exploit execution, payout, and oracle-control-path analysis</strong></p>

</div>

<hr>

<h2>Incident Summary</h2>

<table>
  <tbody>
    <tr><td><strong>Incident date</strong></td><td>July 15, 2026</td></tr>
    <tr><td><strong>Network</strong></td><td>Arbitrum One</td></tr>
    <tr><td><strong>Chain ID</strong></td><td><code>42161</code></td></tr>
    <tr><td><strong>Actor / incident</strong></td><td>Ostium exploiter</td></tr>
    <tr><td><strong>Source type</strong></td><td>Security-firm reporting, explorer attribution, and on-chain forensic analysis</td></tr>
    <tr><td><strong>Wallet confidence</strong></td><td>High</td></tr>
    <tr><td><strong>Loss confidence</strong></td><td>Medium — public totals vary depending on downstream flows included</td></tr>
    <tr><td><strong>Classification</strong></td><td>Exploit execution wallet and payout / consolidation wallet</td></tr>
  </tbody>
</table>

<p>
On <strong>July 15, 2026</strong>, an attacker exploited Ostium's oracle-delivery infrastructure on Arbitrum by using a registered <code>PriceUpKeep</code> forwarder and authorized, future-dated price reports. The exploit created artificial profits on BTC/USD positions and drained at least <strong>11,861,520 USDC</strong> in the confirmed primary transaction.
</p>

<p>
Broader public loss estimates range from approximately <strong>$18 million</strong> to <strong>$24 million</strong>, depending on which additional flows are counted. These wider totals remain less certain than the confirmed primary transaction.
</p>

<h2>Direct Threat Seeds</h2>

<table>
  <thead>
    <tr><th align="left">Address</th><th align="left">Role</th><th align="left">Monitoring</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://arbiscan.io/address/0xD1794196f0fc99c7f27970e661597d77d9a85869"><code>0xD1794196f0fc99c7f27970e661597d77d9a85869</code></a></td>
      <td>Exploit execution / transaction-origin wallet; labeled <strong>Ostium Exploiter 2</strong> by Arbiscan</td>
      <td><strong>Watch directly</strong> and use as a control-path pivot</td>
    </tr>
    <tr>
      <td><a href="https://arbiscan.io/address/0x321Df194646029e7A6193Ea05573d4B9c398bfD9"><code>0x321Df194646029e7A6193Ea05573d4B9c398bfD9</code></a></td>
      <td>Primary trader / payout wallet; labeled <strong>Ostium Exploiter 1</strong> by Arbiscan</td>
      <td><strong>Highest-priority direct watch</strong> and graph-expansion seed</td>
    </tr>
  </tbody>
</table>

<h2>Infrastructure Pivot</h2>

<table>
  <thead>
    <tr><th align="left">Address</th><th align="left">Type</th><th align="left">Handling</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://arbiscan.io/address/0xfE12F6360000dE49D5506d52eE5aC4bC9Dd5bd2E"><code>0xfE12F6360000dE49D5506d52eE5aC4bC9Dd5bd2E</code></a></td>
      <td>Exploit entry contract</td>
      <td>Use as a control-path and graph-expansion pivot; do not classify it as an attacker EOA</td>
    </tr>
  </tbody>
</table>

<h2>Confirmed Transaction</h2>

<p>
The execution wallet submitted the atomic exploit batch through the entry contract. The payout wallet received approximately <strong>11,861,520 USDC</strong> after positions were opened at a fabricated BTC price of approximately <strong>$5,000</strong> and closed near <strong>$60,000</strong> inside the same transaction.
</p>

<p>
<a href="https://arbiscan.io/tx/0x359f8c05b86a4409d60cfba02084334313fd94b19f74a294fb7fc4ea7d4870e0"><code>0x359f8c05b86a4409d60cfba02084334313fd94b19f74a294fb7fc4ea7d4870e0</code></a>
</p>

<h2>Why It Matters</h2>

<p>
These are not merely adjacent addresses. Both wallets are directly present in the exploit transaction and are explorer-labeled as Ostium exploiters. The payout wallet received the stolen USDC, while the execution wallet initiated the malicious batch through Ostium's price-submission path.
</p>

<h2>Analyst Classification</h2>

<ul>
  <li><strong>Direct-watch seed:</strong> <code>0x321D…bfD9</code>.</li>
  <li><strong>Direct-watch execution seed:</strong> <code>0xD179…5869</code>.</li>
  <li><strong>Graph pivots:</strong> the entry contract and subsequent ETH or Tornado Cash destinations.</li>
  <li><strong>Do not automatically threat-label:</strong> Ostium vault, trading-storage, callback, oracle, USDC, or unrelated Tornado Cash addresses.</li>
  <li><strong>Confirmed mechanism:</strong> falsified oracle pricing and future-dated authorized reports.</li>
  <li><strong>Still unresolved:</strong> whether the attacker compromised an oracle signer, abused an already authorized forwarder, or exploited weak validation around registered price reports.</li>
</ul>

<h2>Sources</h2>

<ul>
  <li><a href="https://defiprime.com/ostium-exploit">DeFi Prime — The Ostium Exploit</a></li>
  <li><a href="https://arbiscan.io/tx/0x359f8c05b86a4409d60cfba02084334313fd94b19f74a294fb7fc4ea7d4870e0">Arbiscan — Confirmed primary exploit transaction</a></li>
</ul>
