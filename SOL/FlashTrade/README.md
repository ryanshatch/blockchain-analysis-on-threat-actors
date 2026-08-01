<div align="center" style="text-align: center;">
<h1>New SOL Threat-Wallet Alert</h1>
<h2>FlashTrade Ephemeral-Instance Exploit</h2>
</div>

<table>
  <thead>
    <tr><th align="left">Field</th><th align="left">Details</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Chain</strong></td><td>Solana / SVM ephemeral execution environment settled to Solana</td></tr>
    <tr><td><strong>Incident</strong></td><td>Forged buffer-account validation bypass during undelegation from a MagicBlock ephemeral instance</td></tr>
    <tr><td><strong>Incident date</strong></td><td>July 21, 2026 UTC / July 22, 2026 at 00:21 SGT</td></tr>
    <tr><td><strong>Source type</strong></td><td>FlashTrade team statements, MagicBlock root-cause information, Solana Media technical interview, and SlowMist incident tracking</td></tr>
    <tr><td><strong>Confidence</strong></td><td>High for the incident, loss amount, affected integration layer, root-cause class, containment, and reimbursement; unknown for attacker-wallet attribution because no complete public address was identified in the reviewed sources</td></tr>
    <tr><td><strong>Estimated loss</strong></td><td>98,000 USDC</td></tr>
    <tr><td><strong>Why it matters</strong></td><td>A callback trusted a signer-owned buffer account without proving that it was the canonical program-derived address. A fabricated buffer could therefore be substituted during undelegation and used to represent malicious state as legitimate user-deposit state.</td></tr>
  </tbody>
</table>

<h2>Incident Summary</h2>

<p>
FlashTrade detected an unauthorized withdrawal of 98,000 USDC from an ephemeral instance used for low-latency trading. The platform's monitoring and newly introduced withdrawal-batching controls surfaced the withdrawal quickly, after which trading, deposits, and withdrawals were paused while the team isolated and reconciled the affected state.
</p>

<p>
The vulnerability was traced to the MagicBlock SDK's <code>#[ephemeral]</code> Anchor macro and its undelegation callback path. During undelegation, the system accepted a caller-supplied buffer account after checking that the account was a signer and was owned by the delegation program. It did not also verify that the buffer account's seeds derived the expected canonical program-derived address.
</p>

<p>
That missing seed/PDA validation allowed the attacker to supply a forged buffer account that satisfied the weaker ownership and signer checks. The forged buffer was then processed as though it represented the legitimate delegated account state, enabling an unauthorized withdrawal.
</p>

<h2>Published Attacker-Wallet Status</h2>

<blockquote>
No complete Solana attacker address, exploit transaction signature, or Ethereum proceeds address was found in the reviewed public sources. The case should not invent or infer a wallet from ordinary FlashTrade, MagicBlock, Mayan, ChangeNOW, exchange, or protocol counterparties.
</blockquote>

<p><strong>Monitoring action:</strong> Retain this case as an incident report and add direct-watch wallet seeds only after FlashTrade, MagicBlock, a security firm, or transaction-level public evidence publishes a complete address or transaction signature.</p>

<h2>What Was Actually Exploited</h2>

<p>
This was not reported as a compromise of Solana consensus, FlashTrade's primary pool TVL, an oracle signer, or an administrative private key. The affected surface was the state-transition path between a MagicBlock ephemeral rollup instance and canonical Solana state.
</p>

<p>
FlashTrade used an ephemeral SVM environment to execute trading actions with very low latency. Accounts are delegated into the ephemeral environment and later undelegated back to Solana. The undelegation flow requires a buffer account to carry the state being reconciled.
</p>

<p>
The callback verified some properties of the buffer but failed to prove its exact identity. In Solana's account model, checking that an account is owned by the expected program is not equivalent to checking that it is the exact PDA required for that instruction.
</p>

<h2>Technical Root Cause</h2>

<ol>
  <li>The attacker created or supplied a fabricated buffer account.</li>
  <li>The buffer was passed into an undelegation callback as the state carrier for a sibling instruction.</li>
  <li>The callback verified signer status and delegation-program ownership.</li>
  <li>The callback did not verify that the buffer address was derived from the required seeds and canonical PDA.</li>
  <li>The forged buffer therefore passed validation despite not being the legitimate account expected by the integration.</li>
  <li>The malicious state was reconciled in a way that permitted the unauthorized 98,000 USDC withdrawal.</li>
</ol>

<blockquote>
Ownership checks answer which program controls an account. PDA seed validation answers whether it is the one specific account the instruction is authorized to trust. FlashTrade's integration needed both.
</blockquote>

<h2>Containment and Recovery</h2>
<ul>
  <li>Monitoring reportedly detected the withdrawal within approximately one minute.</li>
  <li>FlashTrade paused trading, deposits, and withdrawals as a precaution.</li>
  <li>A no-operation upgrade path was deployed quickly to stop further malicious state reconciliation.</li>
  <li>Fund isolation limited the incident to deposits associated with the affected ephemeral instance rather than the broader pool TVL.</li>
  <li>Trading resumed after state reconciliation, while deposits and withdrawals remained paused longer for verification.</li>
  <li>FlashTrade and MagicBlock stated that the full affected amount would be covered, leaving users with no final loss.</li>
  <li>MagicBlock released or recommended patched SDK version <code>0.16.2</code> for the affected validation path.</li>
</ul>

<h2>Classification</h2>
<ul>
  <li><strong>Primary classification:</strong> Solana integration / SDK account-validation exploit</li>
  <li><strong>Failure category:</strong> Missing canonical PDA and seed validation</li>
  <li><strong>Affected component:</strong> MagicBlock ephemeral undelegation callback used by FlashTrade</li>
  <li><strong>Reported withdrawal:</strong> 98,000 USDC</li>
  <li><strong>Final user loss:</strong> none expected because the amount was fully covered</li>
  <li><strong>Direct-watch addresses:</strong> unresolved</li>
  <li><strong>Named actor:</strong> none publicly identified</li>
</ul>

<h2>Attribution and Monitoring Limits</h2>
<ul>
  <li>Do not classify MagicBlock, FlashTrade, ChangeNOW, Mayan, or exchange infrastructure as attacker-controlled merely because they appeared in a reported funding or proceeds route.</li>
  <li>The reported funding path involving Monero and ChangeNOW is contextual and does not by itself expose a directly monitorable Monero origin.</li>
  <li>Add wallet data only when a complete address and evidence-supported role become public.</li>
  <li>Preserve the distinction between the vulnerable SDK integration and FlashTrade's broader Solana program and liquidity infrastructure.</li>
</ul>

<h2>Sources</h2>
<ul>
  <li><a href="https://solana.com/uk/podcasts/pirates-parley/episodes/the-100k-exploit-the-attacker-who-tuned-in-and-six-hours-to-recovery-e3mehjr">Solana Media — FlashTrade technical incident interview</a></li>
  <li><a href="https://hacked.slowmist.io/?c=Solana">SlowMist Hacked — FlashTrade incident record</a></li>
  <li><a href="https://www.bitgetapp.com/news/detail/12560605530790">Incident summary describing the MagicBlock SDK validation flaw and reimbursement</a></li>
</ul>

<hr>
<h2>In other words:</h2>
<p>
FlashTrade temporarily moved account state into a faster Solana-compatible execution environment. When that state was moved back, the integration checked that the supplied buffer account looked generally authorized, but it did not prove that the account was the exact PDA that should have been trusted.
</p>
<p>
The attacker supplied a fake buffer that passed the weaker checks and used it to withdraw 98,000 USDC. Fast monitoring, isolated user accounts, and an emergency upgrade prevented the issue from reaching the platform's broader liquidity.
</p>
<p><strong>TLDR:</strong> A forged buffer account passed incomplete undelegation checks because canonical PDA seeds were not verified. The attacker withdrew 98,000 USDC, and FlashTrade and MagicBlock covered the loss.</p>
