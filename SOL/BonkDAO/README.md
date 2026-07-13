<div align="center" style="text-align: center;">
<h1>New SOL Threat-Wallet Alert</h1>
<h2>BonkDAO Governance Takeover</h2>
<table>
  <thead>
    <tr>
      <th align="left">Field</th>
      <th align="left">Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Chain</strong></td>
      <td>Solana</td>
    </tr>
    <tr>
      <td><strong>Incident</strong></td>
      <td>BonkDAO malicious governance proposal / treasury takeover</td>
    </tr>
    <tr>
      <td><strong>Date published</strong></td>
      <td>July 10, 2026</td>
    </tr>
    <tr>
      <td><strong>Source type</strong></td>
      <td>Security incident report with on-chain links; corroborated by BONK, Specter, QuillAudits, and Chainalysis reporting</td>
    </tr>
    <tr>
      <td><strong>Confidence</strong></td>
      <td>Medium–High</td>
    </tr>
    <tr>
      <td><strong>Estimated loss</strong></td>
      <td>Approximately 4.426 trillion BONK, valued at around $19.3 million when transferred</td>
    </tr>
    <tr>
      <td><strong>Why it matters</strong></td>
      <td>
        The attacker appears to have purchased or borrowed enough BONK to meet quorum, passed a proposal transferring the treasury, and executed it immediately because the DAO had no timelock. This was a governance attack, not a contract exploit or stolen-key event.
      </td>
    </tr>
  </tbody>
</table>
<h2>Addresses</h2>
<h3>Proposal Creator — Seed / Governance Address</h3>
<p>
  <code>8xxRdtzsw1CJWfEahViqNjZwh5dYJAdSbBctWwcbycVo</code>
</p>
<p>
  Submitted the malicious BIP #76 proposal.
</p>
<p>
  <strong>Recommended use:</strong> Watch directly and use for graph expansion.
</p>
<hr>
<h3>Principal Voting Wallet — Governance Manipulation Address</h3>
<p>
  <code>CyEE7oHVDaFJ5xZLbXY3h2Z2uk1VwhTkdy72kPUEtypQ</code>
</p>
<p>
  Cast approximately 99.87% of the successful <strong>YES</strong> vote.
</p>
<p>
  <strong>Recommended use:</strong> Watch directly, particularly for exchange funding and BONK disposal flows.
</p>
<hr>
<h3>Secondary Voting Wallet — Graph-Expansion Pivot</h3>
<p>
  <code>FQnQYaYe1UiQZiokdDH39ybRbhJYfzzwXSghnA32pWxc</code>
</p>
<p>
  Cast a much smaller <strong>YES</strong> vote.
</p>
<p>
  <strong>Recommended use:</strong> Use mainly as a relationship and funding pivot unless additional attribution emerges.
</p>
<hr>
<h3>Initial Treasury Recipient — Attacker Wallet</h3>
<p>
  <code>9bxWkNf3BtJ6iehq9KbX9uCWMjem4TFiPZ19T2sYJHvQ</code>
</p>
<p>
  Received the BonkDAO treasury directly after the vote. Solscan reportedly labels the wallet as funded by Bybit.
</p>
<p>
  <strong>Recommended use:</strong> Highest-priority direct-watch address.
</p>
<hr>
<h3>Subsequent Destination — Consolidation / Custody Wallet</h3>
<p>
  <code>EXaJnmrLf7RAKLfn1hehoKX94keKYmvZm5H5zuYVeh42</code>
</p>
<p>
  Received the treasury balance roughly ten hours later. Reporting describes the destination as part of a three-key multisig called <strong>BONK 2.0</strong>.
</p>
<p>
  <strong>Recommended use:</strong> Watch directly and use as the primary downstream graph-expansion seed.
</p>
<blockquote>
  This address should not yet be described as a separate attacker without stronger evidence.
</blockquote>
<hr>
<h3>Drained Treasury — Source Address</h3>
<p>
  <code>F8FqZuUKfoy58aHLW6bfeEhfW9sTtJyqFTqnxVmGZ6dU</code>
</p>
<p>
  This is the victim treasury, not an attacker wallet.
</p>
<p>
  <strong>Recommended use:</strong> Use only to identify the original transfer and related governance activity.
</p>
<h2>Classification</h2>
<ul>
  <li>
    <strong>Direct-watch priority</strong>
    <ul>
      <li><code>9bxWkNf3BtJ6iehq9KbX9uCWMjem4TFiPZ19T2sYJHvQ</code></li>
      <li><code>EXaJnmrLf7RAKLfn1hehoKX94keKYmvZm5H5zuYVeh42</code></li>
      <li><code>CyEE7oHVDaFJ5xZLbXY3h2Z2uk1VwhTkdy72kPUEtypQ</code></li>
    </ul>
  </li>
  <li>
    <strong>Graph-expansion pivots</strong>
    <ul>
      <li>Proposal creator</li>
      <li>Secondary voting wallet</li>
    </ul>
  </li>
  <li>
    <strong>Do not threat-label</strong>
    <ul>
      <li>BonkDAO treasury address</li>
    </ul>
  </li>
  <li>
    <strong>Current attribution</strong>
    <ul>
      <li>Malicious BonkDAO governance participants</li>
      <li>No publicly confirmed individual identity or criminal charge</li>
    </ul>
  </li>
  <li>
    <strong>Material unknown</strong>
    <ul>
      <li>
        Whether the proposal creator, voting wallets, and treasury recipients were controlled by one actor or by coordinated actors remains unproven.
      </li>
    </ul>
  </li>
</ul><hr>