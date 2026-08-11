<div align="center" style="text-align: center;">
<h1>New SOL Threat-Wallet Alert</h1>
<h2>SUNUSI Permanent-Delegate Drain</h2>
</div>

<table>
  <thead>
    <tr><th align="left">Field</th><th align="left">Details</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Chain</strong></td><td>Solana</td></tr>
    <tr><td><strong>Incident</strong></td><td>Malicious burn-tool interaction that granted Permanent Delegate authority and enabled token extraction</td></tr>
    <tr><td><strong>Incident date</strong></td><td>July 13, 2026</td></tr>
    <tr><td><strong>Source type</strong></td><td>Independent on-chain research with linked Solscan transactions and Solana token-extension documentation</td></tr>
    <tr><td><strong>Confidence</strong></td><td>Medium-high for the incident mechanism and published address linkage; lower than cases backed by protocol postmortems or major security firms</td></tr>
    <tr><td><strong>Nominal assets removed</strong></td><td>Approximately 484 million SUNUSI worth more than $275,000 at the time, plus approximately 205.5 ANSEM and 2.4 SOL</td></tr>
    <tr><td><strong>Reported realized extraction</strong></td><td>Approximately $94,300 from 37 SUNUSI sell transactions</td></tr>
    <tr><td><strong>Why it matters</strong></td><td>The victim did not need to lose a private key. By signing a malicious burn-tool transaction, the dev wallet granted persistent delegate authority that allowed the malicious contract to move token-account assets without another approval.</td></tr>
  </tbody>
</table>

<h2>Incident Summary</h2>

<p>
On July 13, 2026, the SUNUSI team reported that its dev wallet had been compromised while attempting to burn part of the token supply. Independent on-chain analysis found that the wallet interacted with a recently deployed burn-themed contract and unintentionally granted Permanent Delegate rights over its token accounts.
</p>

<p>
The first interaction attempted to burn approximately 242 million SUNUSI, but only a small fraction was genuinely burned while most of the tokens were redirected to an attacker-linked external wallet. The delegate authority was then used to pull the remaining SUNUSI allocation along with approximately 205.5 ANSEM and 2.4 SOL.
</p>

<p>
The reported on-chain evidence supports malicious authorization abuse rather than a stolen private key. It also does not currently support classifying the event as an insider rug pull.
</p>

<h2>Direct Incident-Watch Seeds</h2>

<h3>Malicious Burn Contract</h3>
<p><a href="https://solscan.io/account/BUrnPq1dRv7gxjdh5MM2mF51GYBkfLSUyAWx2zcgot6j"><code>BUrnPq1dRv7gxjdh5MM2mF51GYBkfLSUyAWx2zcgot6j</code></a></p>
<p>The contract was reported as deployed on July 9, four days before the incident, and its vanity-style <code>BUrn</code> prefix made it visually resemble legitimate burn infrastructure.</p>
<p><strong>Recommended use:</strong> Watch directly and expand deployer funding, authority-setting instructions, connected victim interactions, and downstream token movements.</p>

<h3>Attacker / Proceeds Wallet</h3>
<p><a href="https://solscan.io/account/Ah4mTqci95qbiydovW8123q2WQzMSCP3MiCzGR2Pje7n"><code>Ah4mTqci95qbiydovW8123q2WQzMSCP3MiCzGR2Pje7n</code></a></p>
<p><strong>Recommended use:</strong> Highest-priority direct watch for SUNUSI sales, SOL consolidation, exchange deposits, funding relationships, and further delegate-abuse campaigns.</p>

<h2>Primary Transactions</h2>

<table>
  <thead>
    <tr><th align="left">Role</th><th align="left">Transaction</th></tr>
  </thead>
  <tbody>
    <tr><td>Initial malicious burn interaction</td><td><a href="https://solscan.io/tx/nnEgahKvjdpZrSkJGXwt9bthfjpqm4YP7CAXPvt8afvBvqcZB9aG8KN2bAxknuzP7uToQ5tsCaRkm3TY6ytVLPA"><code>nnEgahKvjdpZrSkJGXwt9bthfjpqm4YP7CAXPvt8afvBvqcZB9aG8KN2bAxknuzP7uToQ5tsCaRkm3TY6ytVLPA</code></a></td></tr>
    <tr><td>Subsequent delegated token extraction</td><td><a href="https://solscan.io/tx/5ksnbtjfxySRHVWrD9A6crtYiPkEpuibHb3oFCskUQU5NdHYNQGrYr38jvoAUxzNBgu1dytj1xvUrYADpYnoiDWa"><code>5ksnbtjfxySRHVWrD9A6crtYiPkEpuibHb3oFCskUQU5NdHYNQGrYr38jvoAUxzNBgu1dytj1xvUrYADpYnoiDWa</code></a></td></tr>
  </tbody>
</table>

<h2>Technical Root Cause</h2>

<ol>
  <li>The SUNUSI dev wallet attempted to use a third-party burn website.</li>
  <li>The site routed the wallet into a recently deployed contract presented as burn infrastructure.</li>
  <li>The signed transaction granted Permanent Delegate authority over token accounts.</li>
  <li>Permanent Delegate is a legitimate Solana token-extension capability that can authorize later token movement without a second owner signature once properly granted.</li>
  <li>The malicious contract redirected most of the intended burn amount to an attacker-linked wallet.</li>
  <li>The persistent delegate authority was then used to extract the remaining SUNUSI and additional supported token assets.</li>
  <li>The attacker subsequently sold SUNUSI through a series of transactions, reportedly realizing about $94,300 despite the larger nominal token value removed.</li>
</ol>

<blockquote>
The critical failure was not a broken Solana token feature. The victim authorized a malicious contract to receive a legitimate persistent authority, and that authority was then abused exactly as the token system allowed.
</blockquote>

<h2>Classification</h2>
<ul>
  <li><strong>Primary classification:</strong> phishing / malicious-contract authorization drain</li>
  <li><strong>Mechanism:</strong> Permanent Delegate authority abuse</li>
  <li><strong>Private-key compromise:</strong> not supported by the reviewed on-chain analysis</li>
  <li><strong>Confirmed rug pull:</strong> no</li>
  <li><strong>Solana protocol exploit:</strong> no</li>
  <li><strong>Direct-watch targets:</strong> malicious burn contract and attacker/proceeds wallet</li>
  <li><strong>Named actor:</strong> none publicly identified</li>
</ul>

<h2>Attribution Limits</h2>
<ul>
  <li>The primary research source is an independent research group rather than law enforcement or a major protocol-security firm, so address attribution should remain medium-high rather than absolute.</li>
  <li>The Binance-linked funding trail described by the source is useful for investigative escalation but must not be used to classify Binance infrastructure as malicious.</li>
  <li>Do not treat every user who interacted with the burn site or every counterparty of the attacker wallet as part of the same threat actor.</li>
  <li>Future evidence could change whether the malicious contract, funding wallets, and proceeds wallet are attributed to one operator or a broader affiliate operation.</li>
</ul>

<h2>Sources</h2>
<ul>
  <li><a href="https://smcresearchers.com/article/sunusi-compromised-what-we-know-so-far">SMC Researchers — SUNUSI on-chain incident analysis</a></li>
  <li><a href="https://solscan.io/tx/nnEgahKvjdpZrSkJGXwt9bthfjpqm4YP7CAXPvt8afvBvqcZB9aG8KN2bAxknuzP7uToQ5tsCaRkm3TY6ytVLPA">Solscan — initial malicious burn interaction</a></li>
  <li><a href="https://solscan.io/tx/5ksnbtjfxySRHVWrD9A6crtYiPkEpuibHb3oFCskUQU5NdHYNQGrYr38jvoAUxzNBgu1dytj1xvUrYADpYnoiDWa">Solscan — delegated extraction transaction</a></li>
</ul>

<hr>
<h2>In other words:</h2>
<p>
The SUNUSI dev did not need to hand an attacker the wallet seed phrase. The wallet signed a transaction from a fake burn tool that granted the malicious contract long-lived authority over the token accounts.
</p>
<p>
Once that authority existed, the attacker could move the tokens without another approval. The feature worked as designed; the malicious part was convincing the wallet to authorize the wrong contract.
</p>
<p><strong>TLDR:</strong> A fake Solana burn tool obtained Permanent Delegate authority, redirected roughly 484 million SUNUSI plus other assets, and enabled an attacker-linked wallet to liquidate part of the stolen supply.</p>
