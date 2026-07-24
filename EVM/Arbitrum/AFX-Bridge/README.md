<div align="center">

<h1>AFX Bridge Compromise</h1>

<p>
  <strong>
    Arbitrum custody-bridge withdrawal, validator-signature compromise,
    payout, and cross-chain fund-flow analysis
  </strong>
</p>

</div>

<hr>

<h2>Incident Summary</h2>

<table>
  <tbody>
    <tr>
      <td><strong>Incident date</strong></td>
      <td>July 22, 2026</td>
    </tr>
    <tr>
      <td><strong>Detection time</strong></td>
      <td>Approximately 21:30 UTC</td>
    </tr>
    <tr>
      <td><strong>Origin network</strong></td>
      <td>Arbitrum One</td>
    </tr>
    <tr>
      <td><strong>Origin chain ID</strong></td>
      <td><code>42161</code></td>
    </tr>
    <tr>
      <td><strong>Downstream network</strong></td>
      <td>Ethereum</td>
    </tr>
    <tr>
      <td><strong>Actor / incident</strong></td>
      <td>AFX Trade bridge exploiter</td>
    </tr>
    <tr>
      <td><strong>Source type</strong></td>
      <td>
        Blockaid-attributed incident, explorer labels, transaction-level
        evidence, and public forensic reporting
      </td>
    </tr>
    <tr>
      <td><strong>Wallet confidence</strong></td>
      <td>High</td>
    </tr>
    <tr>
      <td><strong>Mechanism confidence</strong></td>
      <td>
        Medium — validator-signature compromise is strongly reported, but
        the exact key-compromise method remains unresolved
      </td>
    </tr>
    <tr>
      <td><strong>Confirmed amount</strong></td>
      <td>24,150,000 USDC</td>
    </tr>
    <tr>
      <td><strong>Likely attack class</strong></td>
      <td>
        Compromised bridge-validator hot keys or equivalent access to
        validator-signing infrastructure
      </td>
    </tr>
    <tr>
      <td><strong>Affected component</strong></td>
      <td>AFX-operated USDC custody bridge</td>
    </tr>
    <tr>
      <td><strong>Not affected</strong></td>
      <td>Arbitrum's native bridge</td>
    </tr>
  </tbody>
</table>

<p>
  On <strong>July 22, 2026</strong>, an unauthorized withdrawal removed
  <strong>24,150,000 USDC</strong> from a custody bridge operated by
  AFX Trade on Arbitrum.
</p>

<p>
  Public reporting indicates that enough AFX bridge-validator signatures
  approved the withdrawal to satisfy the bridge's quorum. After the
  applicable dispute window expired, the bridge contract accepted a
  withdrawal-finalization call and released the USDC to the attacker's
  payout wallet.
</p>

<p>
  The publicly available evidence therefore points to an
  <strong>off-chain authorization failure</strong>, rather than a confirmed
  flaw in the contract's finalization logic. The contract appears to have
  processed a withdrawal that carried apparently valid authorization.
</p>

<blockquote>
  <p>
    The validator-key compromise mechanism remains provisional pending a
    complete technical postmortem. It is not yet publicly established how
    the signing keys were obtained, whether the signers were compromised
    separately, or whether a single intrusion exposed multiple validators.
  </p>
</blockquote>

<hr>

<h2>How the Exploit Worked</h2>

<ol>
  <li>
    The AFX custody bridge held USDC on Arbitrum for users moving value
    into or out of the AFX environment.
  </li>
  <li>
    A withdrawal required approval from a quorum of authorized bridge
    validators.
  </li>
  <li>
    The attacker apparently obtained enough valid validator signatures
    to authorize a withdrawal of 24,150,000 USDC.
  </li>
  <li>
    The signed withdrawal entered the bridge's normal processing path.
  </li>
  <li>
    After the reported dispute window elapsed, the execution wallet called
    <code>batchedFinalizeWithdrawals(bytes32[] messages)</code>.
  </li>
  <li>
    The bridge contract treated the withdrawal as authorized and transferred
    the USDC to the attacker's payout wallet.
  </li>
  <li>
    The stolen USDC was subsequently moved from Arbitrum to Ethereum and
    exchanged for approximately 12,467 ETH.
  </li>
</ol>

<p>
  A cryptographic signature remains valid even when the private key was
  stolen. Unless a bridge has another control capable of detecting or
  stopping the fraudulent withdrawal, its contract cannot distinguish
  between the legitimate signer and an attacker using that signer's key.
</p>

<hr>

<h2>Direct Threat Seeds</h2>

<table>
  <thead>
    <tr>
      <th align="left">Address</th>
      <th align="left">Role</th>
      <th align="left">Monitoring</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <a href="https://arbiscan.io/address/0x2f2974fAbc54dbA33442261211c06BD20E0FEefc">
          <code>0x2f2974fAbc54dbA33442261211c06BD20E0FEefc</code>
        </a>
      </td>
      <td>
        Primary payout wallet; labeled
        <strong>AFX Trade Exploiter 1</strong> by Arbiscan and recipient
        of 24,150,000 USDC
      </td>
      <td>
        <strong>Highest-priority direct watch</strong>; monitor on Arbitrum
        and Ethereum and use as a cross-chain graph-expansion seed
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://arbiscan.io/address/0x5553EA7Bda594aDE7AFe91D279779a42b2B84208">
          <code>0x5553EA7Bda594aDE7AFe91D279779a42b2B84208</code>
        </a>
      </td>
      <td>
        Withdrawal-finalization execution wallet; labeled
        <strong>AFX Trade Exploiter 2</strong> by Arbiscan
      </td>
      <td>
        <strong>Watch directly</strong> and use as a bridge-control-path
        and transaction-origin pivot
      </td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Infrastructure Pivot</h2>

<table>
  <thead>
    <tr>
      <th align="left">Address</th>
      <th align="left">Type</th>
      <th align="left">Handling</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <a href="https://arbiscan.io/address/0xCb3B9A3E5668AFE84DC7A864B36b845dCE062e67">
          <code>0xCb3B9A3E5668AFE84DC7A864B36b845dCE062e67</code>
        </a>
      </td>
      <td>
        Affected AFX custody-bridge contract that finalized the withdrawal
        and released the USDC
      </td>
      <td>
        Use as a <strong>graph-expansion and control-path pivot</strong>.
        Do not classify the contract itself as attacker-controlled solely
        because it released the funds.
      </td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Confirmed Exploit Transaction</h2>

<table>
  <tbody>
    <tr>
      <td><strong>Transaction</strong></td>
      <td>
        <a href="https://arbiscan.io/tx/0x50d0b3ec6c3f5fce0f10abf81540bbb508f421494aa2b3480c4a264b0436547b">
          <code>0x50d0b3ec6c3f5fce0f10abf81540bbb508f421494aa2b3480c4a264b0436547b</code>
        </a>
      </td>
    </tr>
    <tr>
      <td><strong>Timestamp</strong></td>
      <td>July 22, 2026 at 21:30:25 UTC</td>
    </tr>
    <tr>
      <td><strong>Origin</strong></td>
      <td>
        <code>0x5553EA7Bda594aDE7AFe91D279779a42b2B84208</code>
      </td>
    </tr>
    <tr>
      <td><strong>Called contract</strong></td>
      <td>
        <code>0xCb3B9A3E5668AFE84DC7A864B36b845dCE062e67</code>
      </td>
    </tr>
    <tr>
      <td><strong>Function</strong></td>
      <td>
        <code>batchedFinalizeWithdrawals(bytes32[] messages)</code>
      </td>
    </tr>
    <tr>
      <td><strong>Payout destination</strong></td>
      <td>
        <code>0x2f2974fAbc54dbA33442261211c06BD20E0FEefc</code>
      </td>
    </tr>
    <tr>
      <td><strong>Asset</strong></td>
      <td>USDC</td>
    </tr>
    <tr>
      <td><strong>Amount</strong></td>
      <td>24,150,000 USDC</td>
    </tr>
    <tr>
      <td><strong>Withdrawal nonce</strong></td>
      <td><code>2784725241</code></td>
    </tr>
    <tr>
      <td><strong>Withdrawal message</strong></td>
      <td>
        <code>0x558A989F405D706935FA15EFEE8EAC6E32FBBA7EA3F70DFD930C66436E7ED8C2</code>
      </td>
    </tr>
  </tbody>
</table>

<p>
  The execution wallet called the AFX bridge contract with a withdrawal
  message. The resulting transaction transferred 24,150,000 USDC from the
  custody contract to the payout wallet and emitted a finalized-withdrawal
  event naming the same destination.
</p>

<hr>

<h2>Cross-Chain Fund Flow</h2>

<p>
  Public security reporting states that the stolen USDC was subsequently
  moved from Arbitrum to Ethereum and exchanged for approximately
  <strong>12,467 ETH</strong>.
</p>

<p>
  The direct Ethereum-side conversion and consolidation addresses should be
  added to this case only after their complete addresses and transaction
  hashes have been independently captured. An abbreviated address should
  not be entered into the machine-readable threat-wallet dataset.
</p>

<hr>

<h2>Why It Matters</h2>

<p>
  The two threat-wallet addresses are not merely adjacent to the incident.
  The execution wallet directly submitted the withdrawal-finalization
  transaction, while the payout wallet directly received the stolen
  24,150,000 USDC.
</p>

<p>
  The case also demonstrates that bridge security depends on more than
  smart-contract correctness. A bridge contract can execute exactly as
  programmed and still release funds fraudulently when its trusted signing
  infrastructure is compromised.
</p>

<hr>

<h2>Analyst Classification</h2>

<ul>
  <li>
    <strong>Direct-watch payout seed:</strong>
    <code>0x2f2974…FEefc</code>.
  </li>
  <li>
    <strong>Direct-watch execution seed:</strong>
    <code>0x5553EA…4208</code>.
  </li>
  <li>
    <strong>Infrastructure pivot:</strong>
    <code>0xCb3B9A…2e67</code>.
  </li>
  <li>
    <strong>Likely attack class:</strong>
    compromised bridge-validator hot keys or equivalent signing access.
  </li>
  <li>
    <strong>Confirmed on-chain action:</strong>
    finalization of a withdrawal transferring 24,150,000 USDC to the
    payout wallet.
  </li>
  <li>
    <strong>Not affected:</strong>
    Arbitrum's native bridge.
  </li>
  <li>
    <strong>Do not automatically threat-label:</strong>
    Arbitrum bridge infrastructure, Circle contracts, CCTP infrastructure,
    exchanges, liquidity pools, or unrelated counterparties appearing
    downstream.
  </li>
  <li>
    <strong>Unresolved:</strong>
    how the validator-signing authority was obtained, whether one intrusion
    exposed multiple signers, and whether any additional validator or
    operator infrastructure remains compromised.
  </li>
</ul>

<hr>

<h2>Attribution Boundaries</h2>

<ul>
  <li>
    The two explorer-labeled exploiter EOAs are direct threat seeds.
  </li>
  <li>
    The AFX custody-bridge contract is affected infrastructure, not
    automatically an attacker-controlled address.
  </li>
  <li>
    A valid withdrawal signature establishes authorization under the
    contract's rules; it does not establish that the legitimate key owner
    intentionally approved the withdrawal.
  </li>
  <li>
    An interaction with the payout wallet does not independently prove
    common control or malicious intent.
  </li>
  <li>
    Exchange, bridge, swap-router, liquidity-pool, and stablecoin-contract
    addresses should remain investigative pivots unless separate evidence
    establishes attacker control.
  </li>
</ul>

<hr>

<h2>Sources</h2>

<ul>
  <li>
    <a href="https://arbiscan.io/tx/0x50d0b3ec6c3f5fce0f10abf81540bbb508f421494aa2b3480c4a264b0436547b">
      Arbiscan — Confirmed AFX withdrawal-finalization transaction
    </a>
  </li>
  <li>
    <a href="https://www.theblock.co/post/409482/arbitrum-protocol-afx-trade-exploit">
      The Block — AFX Trade bridge incident and Blockaid attribution
    </a>
  </li>
  <li>
    <a href="https://unchainedcrypto.com/arbitrum-based-afx-trade-drained-of-24-million/">
      Unchained — Reported validator-signature and dispute-window mechanics
    </a>
  </li>
</ul>
