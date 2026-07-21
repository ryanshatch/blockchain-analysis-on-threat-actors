<div align="center">

<h1>Zunami Protocol Exploit Cluster</h1>

<p><strong>Materially updated Ethereum wallet attribution</strong></p>

</div>

<hr>

<h2>Incident Summary</h2>

<table>
  <tbody>
    <tr><td><strong>Published</strong></td><td>July 16, 2026</td></tr>
    <tr><td><strong>Network</strong></td><td>Ethereum</td></tr>
    <tr><td><strong>Actor / campaign</strong></td><td>Zunami Protocol exploit cluster</td></tr>
    <tr><td><strong>Source type</strong></td><td>Security and forensic investigation</td></tr>
    <tr><td><strong>Confidence</strong></td><td>Medium</td></tr>
    <tr><td><strong>Classification</strong></td><td>Exploit seeds, staging infrastructure, accumulation wallet, and operational pivots</td></tr>
  </tbody>
</table>

<p>
On <strong>July 16, 2026</strong>, Rekt published a forensic case file linking previously known Zunami Protocol exploit wallets to a longer-lived staging and cash-out network. The underlying exploits occurred in <strong>2023 and 2025</strong>, but the wallet relationships and operational attribution were newly documented.
</p>

<p>
<strong>Why it matters:</strong> The analysis identifies pre-exploit staging, direct operational interaction with an attacker wallet, repeated exchange off-ramps, and an anomalous connection between the protocol deployer and exploit infrastructure.
</p>

<h2>Direct Threat Seeds</h2>

<table>
  <thead>
    <tr><th align="left">Address</th><th align="left">Classification</th><th align="left">Monitoring</th></tr>
  </thead>
  <tbody>
    <tr><td><code>0x5f4C21c9Bb73c8B4a296cC256C0cDe324dB146DF</code></td><td>2023 attacker EOA / exploit seed</td><td><strong>Watch directly</strong></td></tr>
    <tr><td><code>0x051370419b871F7C05dEE8f7134401530832e250</code></td><td>2025 attacker EOA / privileged-access drain</td><td><strong>Watch directly</strong></td></tr>
    <tr><td><code>0xF00d0e11AcCe1eA37658f428d947C3FFFAeaDe70</code></td><td>Pre-exploit staging and operational wallet</td><td><strong>Watch directly</strong></td></tr>
    <tr><td><code>0x12e98c4EBD742ca9465789570e5cf4Df9EEd0Fb0</code></td><td>Accumulation and cash-out wallet</td><td><strong>Watch directly</strong></td></tr>
  </tbody>
</table>

<h2>Operational Pivots</h2>

<table>
  <thead>
    <tr><th align="left">Address</th><th align="left">Classification</th><th align="left">Handling</th></tr>
  </thead>
  <tbody>
    <tr><td><code>0xe9b2B067eE106A6E518fB0552F3296d22b82b32B</code></td><td>Zunami deployer / privileged wallet</td><td>Graph-expansion pivot; do not automatically threat-label</td></tr>
    <tr><td><code>0xF9605D8c4c987d7Cb32D0d11FbCb8EeeB1B22D5d</code></td><td><code>sterx.eth</code>, linked operationally to the deployer</td><td>Graph-expansion pivot; attribution remains inferential</td></tr>
  </tbody>
</table>

<h2>Key Relationships</h2>

<ul>
  <li>The 2023 attacker wallet interacted with staging wallet <code>0xF00d…De70</code> on exploit day.</li>
  <li>The staging wallet received funding from OKX and Binance months before the attack, indicating advance preparation rather than a purely opportunistic exploit.</li>
  <li>Wallet <code>0x12e9…0Fb0</code> reportedly routed approximately <strong>75.2 ETH</strong> through intermediary wallets into multiple Coinbase deposit addresses between November 2023 and October 2025.</li>
  <li>The Zunami deployer sent an on-chain settlement message directly to the 2023 attacker three days after the exploit.</li>
  <li>The same deployer later granted the privileges used in the 2025 drain.</li>
</ul>

<h2>Analyst Classification</h2>

<ul>
  <li><strong>Direct threat seeds:</strong> both attacker EOAs, the staging wallet, and the accumulation wallet.</li>
  <li><strong>Operational pivots:</strong> the Zunami deployer and <code>sterx.eth</code>.</li>
  <li><strong>Do not classify as attacker wallets:</strong> Coinbase, Binance, OKX, or Bybit deposit and hot-wallet addresses appearing in the flow.</li>
  <li><strong>Current attribution:</strong> Zunami exploit infrastructure with possible privileged-wallet involvement.</li>
  <li><strong>Unproven:</strong> insider participation, shared control between the deployer and attackers, or the identity of the exploit operator.</li>
</ul>

<blockquote>
The anomalous deployer relationships are materially relevant, but they do not prove that the protocol team controlled either attacker wallet.
</blockquote>

<h2>Source</h2>

<ul>
  <li><a href="https://rekt.news/zunami-protocol-case-file">Rekt — Zunami Protocol Case File</a></li>
</ul>
