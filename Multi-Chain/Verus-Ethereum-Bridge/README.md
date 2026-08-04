<div align="center">

<h1>Verus–Ethereum Bridge Exploit</h1>

<p>
  <strong>
    Cross-chain notarization poisoning, forged Ethereum import proofs,
    bridge-reserve theft, consolidation, and laundering analysis
  </strong>
</p>

</div>

<hr>

<h2>Incident Summary</h2>

<p>
  On <strong>July 23, 2026</strong>, an attacker exploited the
  Verus–Ethereum Bridge by causing malicious duplicate state-root entries
  to be included in Verus notarization data and then relaying that signed
  data to Ethereum.
</p>

<p>
  Verus software and the Ethereum bridge contract interpreted the same
  serialized notarization differently. Verus accepted the legitimate root,
  while the Ethereum-side processing logic allowed later duplicate entries
  to overwrite the genuine trusted Verus state root.
</p>

<p>
  After installing an attacker-controlled state root on Ethereum, the
  attacker submitted a fabricated import proof that authorized withdrawals
  far exceeding the approximately <strong>0.01 VRSC</strong> source-chain
  export.
</p>

<table>
  <tbody>
    <tr>
      <td><strong>Incident date</strong></td>
      <td>July 23, 2026</td>
    </tr>
    <tr>
      <td><strong>Detailed analysis date</strong></td>
      <td>July 30, 2026</td>
    </tr>
    <tr>
      <td><strong>Origin network</strong></td>
      <td>Verus</td>
    </tr>
    <tr>
      <td><strong>Destination network</strong></td>
      <td>Ethereum</td>
    </tr>
    <tr>
      <td><strong>Incident</strong></td>
      <td>Verus–Ethereum Bridge exploit</td>
    </tr>
    <tr>
      <td><strong>Attack class</strong></td>
      <td>
        Cross-chain proof-validation and semantic-consistency failure
      </td>
    </tr>
    <tr>
      <td><strong>Primary failure</strong></td>
      <td>
        Duplicate state-root handling and inconsistent notarization
        interpretation across Verus and Ethereum
      </td>
    </tr>
    <tr>
      <td><strong>Additional failure</strong></td>
      <td>
        Ethereum bridge logic did not adequately confirm that the requested
        payout corresponded to the value actually exported from Verus
      </td>
    </tr>
    <tr>
      <td><strong>CertiK loss estimate</strong></td>
      <td>Approximately $7.44 million</td>
    </tr>
    <tr>
      <td><strong>Blockaid-related estimate</strong></td>
      <td>Approximately $7.54 million</td>
    </tr>
    <tr>
      <td><strong>Assets reported withdrawn</strong></td>
      <td>ETH, tBTC, USDC, USDT, EURC, MKR, and scrvUSD</td>
    </tr>
    <tr>
      <td><strong>Incident confidence</strong></td>
      <td>High</td>
    </tr>
    <tr>
      <td><strong>Wallet-linkage confidence</strong></td>
      <td>High</td>
    </tr>
    <tr>
      <td><strong>Named attacker</strong></td>
      <td>None identified</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Direct Threat-Wallet Seeds</h2>

<h3>Ethereum Execution Wallet</h3>

<pre><code>0xBda71b58cEc0b1C20A8f87cCD52FA0679747855c</code></pre>

<p>
  CertiK identifies this address as the attacker address on Ethereum. It
  relayed the malicious notarization data, called the Ethereum bridge's
  state-update path, and submitted the forged import transaction.
</p>

<ul>
  <li><strong>Role:</strong> exploit execution and proof-relay wallet</li>
  <li><strong>Incident linkage:</strong> high confidence</li>
  <li><strong>Control confidence:</strong> high</li>
  <li><strong>Monitoring:</strong> watch directly</li>
</ul>

<h3>Ethereum Profit and Consolidation Wallet</h3>

<pre><code>0xCFd0A20703cD11E0b9f665e1C3F1Ef989C142D54</code></pre>

<p>
  CertiK identifies this address as the attacker profit address on
  Ethereum. It received the bridge payouts, consolidated stolen assets,
  and participated in the subsequent conversion and laundering flow.
</p>

<ul>
  <li>
    <strong>Role:</strong>
    profit, consolidation, swap, and laundering wallet
  </li>
  <li><strong>Incident linkage:</strong> high confidence</li>
  <li><strong>Control confidence:</strong> high</li>
  <li>
    <strong>Monitoring:</strong>
    highest-priority direct watch
  </li>
</ul>

<h3>Verus-Side Attacker Address</h3>

<pre><code>RXo2PqXjgRVJ8w8QVDErVqVLavz4TToyuu</code></pre>

<p>
  CertiK identifies this as the attacker address on Verus. It initiated
  the low-value source-chain export used as the legitimate-looking basis
  for the later fabricated Ethereum import proof.
</p>

<ul>
  <li>
    <strong>Role:</strong>
    source-chain export and cross-chain exploit seed
  </li>
  <li><strong>Incident linkage:</strong> high confidence</li>
  <li><strong>Control confidence:</strong> high</li>
  <li><strong>Monitoring:</strong> watch directly</li>
</ul>

<hr>

<h2>Infrastructure and Technical Pivots</h2>

<table>
  <thead>
    <tr>
      <th align="left">Network</th>
      <th align="left">Address</th>
      <th align="left">Classification</th>
      <th align="left">Handling</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ethereum</td>
      <td>
        <code>0x71518580f36FeCEFfE0721F06bA4703218cD7F63</code>
      </td>
      <td>Compromised Verus–Ethereum Bridge</td>
      <td>
        Victim and exploit-entry infrastructure; do not threat-label
      </td>
    </tr>
    <tr>
      <td>Ethereum</td>
      <td>
        <code>0x54e03a1682fd0bb065b669f6296f97028dcfd4ce</code>
      </td>
      <td>VerusProof contract</td>
      <td>
        Vulnerable proof-validation component; technical pivot only
      </td>
    </tr>
    <tr>
      <td>Ethereum</td>
      <td>
        <code>0xd90e2f925DA726b50C4Ed8D0Fb90Ad053324F31b</code>
      </td>
      <td>Tornado Cash router</td>
      <td>
        Laundering-path infrastructure; do not classify as attacker-owned
      </td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Simplified Attack Flow</h2>

<ol>
  <li>
    The attacker created notarization data containing legitimate entries
    followed by malicious duplicate Verus state-root entries.
  </li>
  <li>
    Verus processing retained the legitimate interpretation of the
    notarization.
  </li>
  <li>
    Verus notaries signed the serialized notarization bytes.
  </li>
  <li>
    The Ethereum execution wallet extracted and relayed the signed data to
    the Verus–Ethereum Bridge.
  </li>
  <li>
    Ethereum-side deserialization processed each matching root in sequence.
  </li>
  <li>
    The later malicious duplicate entry overwrote the genuine Verus root.
  </li>
  <li>
    The attacker initiated an approximately 0.01 VRSC Verus export.
  </li>
  <li>
    The attacker constructed a fabricated import proof under the poisoned
    Ethereum-side state root.
  </li>
  <li>
    The bridge accepted the proof and released reserves far exceeding the
    real source-chain export.
  </li>
  <li>
    The profit wallet received the withdrawn ETH and tokens.
  </li>
  <li>
    Stolen assets were converted into ETH and routed toward Tornado Cash.
  </li>
</ol>

<hr>

<h2>Technical Root Cause</h2>

<h3>Cross-Chain Semantic Inconsistency</h3>

<p>
  Verus and Ethereum did not interpret the signed notarization bytes in an
  equivalent way.
</p>

<p>
  Verus processed the serialized proof-root entries through data structures
  that effectively retained the legitimate checkpoint, while Ethereum
  processed matching entries sequentially and allowed later duplicate
  entries to replace the trusted state root.
</p>

<h3>Duplicate-Key Handling Failure</h3>

<p>
  The Ethereum-side bridge logic did not reject duplicate proof-root entries
  for the same system identifier.
</p>

<p>
  A secure parser should reject duplicated security-critical identifiers
  rather than silently accepting the final entry.
</p>

<h3>Payout-to-Export Validation Failure</h3>

<p>
  The bridge also failed to independently prove that the assets and amounts
  requested in the Ethereum import matched the value actually exported on
  Verus.
</p>

<blockquote>
  <p>
    The bridge accepted a proof that was internally consistent with the
    attacker-controlled root, but did not prove that the root represented
    the canonical Verus state or that the withdrawal matched a genuine
    funded export.
  </p>
</blockquote>

<hr>

<h2>Key Ethereum Transactions</h2>

<table>
  <thead>
    <tr>
      <th align="left">Time</th>
      <th align="left">Transaction</th>
      <th align="left">Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>July 23, 2026 03:23:35 UTC</td>
      <td>
        <code>0x8f21bd8f0fce72ac959caa93a9923d85f902dfc6eddac2785ac5bc49c3b28d8f</code>
      </td>
      <td>
        First attacker call relaying poisoned notarization data through
        <code>setLatestData</code>
      </td>
    </tr>
    <tr>
      <td>July 23, 2026 03:41:47 UTC</td>
      <td>
        <code>0x51b1c8341da4092b7d1e0e4865f7b318de4e96245358b05b2bff2df50adaf0c9</code>
      </td>
      <td>
        Second attacker call relaying later poisoned notarization data
      </td>
    </tr>
    <tr>
      <td>July 23, 2026 03:45:59 UTC</td>
      <td>
        <code>0xa1f1e65c1cea4dba4ae439cd4dcdba6cc2dbda0ed1228e61f29ae9c9324eb099</code>
      </td>
      <td>
        Forged import and bridge-reserve withdrawal
      </td>
    </tr>
  </tbody>
</table>

<p>
  The final Ethereum transaction transferred approximately
  1,137.45281584 ETH and multiple ERC-20 assets from the Verus bridge to
  the profit wallet.
</p>

<hr>

<h2>Key Verus Transactions</h2>

<table>
  <thead>
    <tr>
      <th align="left">Transaction</th>
      <th align="left">Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code>4f4f81d9a19df2dc5f39033288b5259199c4c78c57b668d89e602628ff647816</code>
      </td>
      <td>Genuine notarization preceding the malicious sequence</td>
    </tr>
    <tr>
      <td>
        <code>0c24765b6d4daa745e38b09f46382d1a457966e1c128265b87dc2b5a3fd16280</code>
      </td>
      <td>First notarization containing malicious duplicate state roots</td>
    </tr>
    <tr>
      <td>
        <code>f5f0d9056163edaa8497857226dd0905e10f044063ba77cedc3fc7589d3bf10c</code>
      </td>
      <td>Second notarization containing malicious duplicate state roots</td>
    </tr>
    <tr>
      <td>
        <code>5b5043febfd7f7c089e976d11d0f87a904881266bb96dd118b3d69b0e02aab52</code>
      </td>
      <td>Attacker's approximately 0.01 VRSC export request</td>
    </tr>
    <tr>
      <td>
        <code>86ed26828ce450fbac300c9f9c561190f08fb61942ba0e3f769e63992ff80359</code>
      </td>
      <td>Converter processing of the export request</td>
    </tr>
    <tr>
      <td>
        <code>7c4fc207ff2c005acf870b5ae2b3dffac61450d629acfdc4b2b1d589dcd52d76</code>
      </td>
      <td>Actual cross-chain transfer emission</td>
    </tr>
    <tr>
      <td>
        <code>e26e270d33543520abf4948980edbe62adf85564e512f43cc6da0808ca4e09a6</code>
      </td>
      <td>Batch transfer through LuckPool</td>
    </tr>
    <tr>
      <td>
        <code>0c5843f87f3ef1c9ea31ec4b6c601101eec8592ec476a03a53dd6e400df05c6e</code>
      </td>
      <td>Third notarization containing malicious state roots</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Loss and Fund-Flow Estimates</h2>

<p>
  Public reporting contains materially different fund-flow totals.
</p>

<table>
  <thead>
    <tr>
      <th align="left">Source</th>
      <th align="left">Reported loss</th>
      <th align="left">Reported ETH conversion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CertiK</td>
      <td>Approximately $7.44 million</td>
      <td>2,778.8662 ETH swapped through Relay</td>
    </tr>
    <tr>
      <td>Blockaid-related reporting</td>
      <td>Approximately $7.54 million</td>
      <td>Approximately 3,916.1 ETH after conversion</td>
    </tr>
  </tbody>
</table>

<p>
  These figures may represent different observation times, asset subsets,
  swap routes, gross withdrawals, or final consolidation totals.
</p>

<blockquote>
  <p>
    Preserve both figures with source attribution. Do not average them or
    describe either one as definitively final without additional
    transaction-level reconciliation.
  </p>
</blockquote>

<hr>

<h2>Relationship to the May 2026 Exploit</h2>

<p>
  The July incident used the same bridge contract, entry path, and general
  vulnerability class reported in the May 2026 attack.
</p>

<p>
  Blockaid-related reporting stated that the July exploit involved a
  different attacker and a new wallet set.
</p>

<ul>
  <li>Do not merge the July wallet cluster into the May cluster by default.</li>
  <li>
    Preserve separate case directories and address datasets for each
    incident.
  </li>
  <li>
    Merge or cross-reference clusters only after transaction-level evidence
    demonstrates shared control, funding, infrastructure, or laundering.
  </li>
</ul>

<hr>

<h2>Analyst Classification</h2>

<ul>
  <li>
    <strong>Primary execution seed:</strong>
    <code>0xBda71b58cEc0b1C20A8f87cCD52FA0679747855c</code>
  </li>
  <li>
    <strong>Highest-priority profit and laundering seed:</strong>
    <code>0xCFd0A20703cD11E0b9f665e1C3F1Ef989C142D54</code>
  </li>
  <li>
    <strong>Verus-side direct-watch seed:</strong>
    <code>RXo2PqXjgRVJ8w8QVDErVqVLavz4TToyuu</code>
  </li>
  <li>
    <strong>Victim infrastructure:</strong>
    Verus–Ethereum Bridge contract
  </li>
  <li>
    <strong>Technical pivot:</strong>
    VerusProof contract
  </li>
  <li>
    <strong>Laundering infrastructure:</strong>
    Tornado Cash router
  </li>
  <li>
    <strong>Named actor:</strong>
    none identified
  </li>
</ul>

<hr>

<h2>Attribution Boundaries</h2>

<ul>
  <li>
    The three attacker addresses identified by CertiK are suitable for
    direct monitoring.
  </li>
  <li>
    The bridge contract is compromised victim infrastructure, not an
    attacker wallet.
  </li>
  <li>
    The VerusProof contract is a vulnerable technical component, not an
    attacker-controlled contract.
  </li>
  <li>
    The Tornado Cash router is laundering infrastructure and should not be
    labeled as the exploiter.
  </li>
  <li>
    Depositors, relayers, swap routers, pools, token contracts, bridges,
    and counterparties should not be automatically threat-labeled.
  </li>
  <li>
    No named individual or organization has been publicly attributed.
  </li>
  <li>
    The May and July wallet clusters should remain separate unless stronger
    evidence establishes common control.
  </li>
</ul>

<hr>

<h2>Sources</h2>

<ul>
  <li>
    <a href="https://www.certik.com/blog/verus-incident-analysis">
      CertiK - Verus Incident Analysis
    </a>
  </li>
  <li>
    <a href="https://www.theblock.co/post/409489/new-verus-ethereum-bridge-attack">
      The Block - New Verus–Ethereum bridge attack
    </a>
  </li>
  <li>
    <a href="https://etherscan.io/address/0x71518580f36FeCEFfE0721F06bA4703218cD7F63">
      Etherscan - Verus Ethereum Bridge
    </a>
  </li>
  <li>
    <a href="https://etherscan.io/address/0xd90e2f925DA726b50C4Ed8D0Fb90Ad053324F31b">
      Etherscan - Tornado Cash router
    </a>
  </li>
</ul>
