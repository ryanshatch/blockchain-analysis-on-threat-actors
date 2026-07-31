<div align="center">

<h1>Across Protocol Solana Relayer Exploit</h1>

<p>
  <strong>
    Forged Solana deposit events, off-chain parser failure,
    cross-chain relayer payouts, and fund-recovery analysis
  </strong>
</p>

</div>

<hr>

<h2>Incident Summary</h2>

<p>
  On <strong>July 17, 2026</strong>, an attacker exploited a validation
  weakness in off-chain Solana event-reading software used by a relayer
  operated by <strong>Risk Labs</strong>, the foundation supporting
  Across Protocol.
</p>

<p>
  The attacker generated instruction data that resembled legitimate
  Across <code>FundsDeposited</code> events. The off-chain parser accepted
  these representations as real deposits and caused the Risk Labs relayer
  to advance its own assets to attacker-controlled or attacker-linked
  recipients on destination chains.
</p>

<p>
  No corresponding funded deposits existed on Solana. The relayer therefore
  paid destination-chain funds for deposits that had never actually
  occurred.
</p>

<table>
  <tbody>
    <tr>
      <td><strong>Incident date</strong></td>
      <td>July 17, 2026</td>
    </tr>
    <tr>
      <td><strong>Reported attack window</strong></td>
      <td>Approximately 05:07–06:14 UTC</td>
    </tr>
    <tr>
      <td><strong>Initial public alert</strong></td>
      <td>Approximately 05:30 UTC</td>
    </tr>
    <tr>
      <td><strong>Origin network</strong></td>
      <td>Solana</td>
    </tr>
    <tr>
      <td><strong>Destination scope</strong></td>
      <td>18 reported destination chains</td>
    </tr>
    <tr>
      <td><strong>Affected component</strong></td>
      <td>Risk Labs-operated off-chain relayer and event-reader software</td>
    </tr>
    <tr>
      <td><strong>Incident type</strong></td>
      <td>
        Forged-deposit event acceptance / off-chain provenance and
        type-validation failure
      </td>
    </tr>
    <tr>
      <td><strong>Gross relayer payout</strong></td>
      <td>Approximately $4.5 million</td>
    </tr>
    <tr>
      <td><strong>Initial reported net loss</strong></td>
      <td>Below $4 million</td>
    </tr>
    <tr>
      <td><strong>User losses</strong></td>
      <td>None reported</td>
    </tr>
    <tr>
      <td><strong>Named attacker</strong></td>
      <td>None publicly identified</td>
    </tr>
    <tr>
      <td><strong>Incident confidence</strong></td>
      <td>High</td>
    </tr>
    <tr>
      <td><strong>Address-linkage confidence</strong></td>
      <td>High</td>
    </tr>
    <tr>
      <td><strong>Individual-control confidence</strong></td>
      <td>
        Medium to high — addresses were publicly tracked in connection
        with the attack, but no person or organization has been attributed
      </td>
    </tr>
  </tbody>
</table>

<hr>

<h2>What Was Actually Exploited</h2>

<p>
  This was not primarily an on-chain smart-contract drain. Public
  post-incident analysis indicates that the Solana and EVM contracts
  generally performed their programmed functions.
</p>

<p>
  The security failure occurred in off-chain software responsible for
  reading Solana transactions and deciding whether a valid Across deposit
  had occurred.
</p>

<p>
  Across uses an intent-based system. A user deposits assets on an origin
  chain, and a relayer advances its own liquidity to the recipient on the
  destination chain. The relayer is reimbursed later through Across
  settlement.
</p>

<p>
  The Risk Labs event reader reportedly failed to verify the complete
  identity and provenance of a purported Anchor event before acting on it.
  In particular, it did not properly validate the event's eight-byte
  Anchor discriminator.
</p>

<blockquote>
  <p>
    The system verified that attacker-controlled data looked like a
    deposit event, but it did not adequately prove that the data was a
    genuine, funded Across deposit event.
  </p>
</blockquote>

<hr>

<h2>Anchor Event Discriminators</h2>

<p>
  Anchor uses an eight-byte discriminator to identify the instruction,
  account, or event type represented by serialized data.
</p>

<p>
  A secure event consumer must verify that the discriminator matches the
  exact expected event before decoding the remainder of the payload and
  treating it as authoritative.
</p>

<p>
  The Across parser reportedly decoded attacker-supplied data shaped like
  a <code>FundsDeposited</code> event without adequately proving that it
  originated from the correct event type and execution path.
</p>

<hr>

<h2>Simplified Attack Flow</h2>

<h3>Normal Across Flow</h3>

<ol>
  <li>A user deposits USDC through the Across SpokePool on Solana.</li>
  <li>The legitimate deposit changes on-chain state and transfers assets.</li>
  <li>Relayer software detects and validates the deposit.</li>
  <li>
    A relayer advances its own funds to the recipient on a destination
    chain.
  </li>
  <li>
    The relayer later receives reimbursement through Across settlement.
  </li>
</ol>

<h3>Fraudulent Flow</h3>

<ol>
  <li>The attacker executed a wrapper program on Solana.</li>
  <li>
    The wrapper performed a cross-program invocation into the Across
    SpokePool.
  </li>
  <li>
    The invocation called the read-only helper
    <code>get_unsafe_deposit_id</code>.
  </li>
  <li>
    The attacker appended serialized data resembling a legitimate
    <code>FundsDeposited</code> event.
  </li>
  <li>
    The off-chain Risk Labs parser accepted the forged representation as
    a real deposit.
  </li>
  <li>
    The Risk Labs relayer advanced real funds on destination chains.
  </li>
  <li>
    No legitimate Solana deposit or matching asset transfer backed the
    payment.
  </li>
</ol>

<p>
  The attacker was not directly withdrawing funds from an Across smart
  contract. The attacker deceived software controlling a relayer wallet
  into paying destination-chain assets.
</p>

<hr>

<h2>Role of get_unsafe_deposit_id</h2>

<p>
  The <code>get_unsafe_deposit_id</code> helper was not, by itself, the
  vulnerability.
</p>

<p>
  Public post-incident reporting describes it as a harmless, read-only
  helper that provided a convenient instruction path through which the
  attacker could carry forged serialized data.
</p>

<table>
  <tbody>
    <tr>
      <td><strong>Carrier</strong></td>
      <td><code>get_unsafe_deposit_id</code></td>
    </tr>
    <tr>
      <td><strong>Root failure</strong></td>
      <td>
        Missing event-type authentication, discriminator verification,
        provenance validation, and funded-state confirmation
      </td>
    </tr>
  </tbody>
</table>

<p>
  Describing the incident only as an exploitation of an “unsafe deposit
  function” would therefore be incomplete.
</p>

<hr>

<h2>Technical Root-Cause Classification</h2>

<table>
  <thead>
    <tr>
      <th align="left">Validation category</th>
      <th align="left">Failure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Input validation</td>
      <td>
        The off-chain service decoded attacker-controlled serialized
        instruction data.
      </td>
    </tr>
    <tr>
      <td>Type validation</td>
      <td>
        The exact eight-byte Anchor event discriminator was not adequately
        verified.
      </td>
    </tr>
    <tr>
      <td>Provenance validation</td>
      <td>
        The parser did not adequately prove that the data came from a
        genuine Across deposit-event path.
      </td>
    </tr>
    <tr>
      <td>State validation</td>
      <td>
        The relayer acted without independently proving that a funded
        deposit and corresponding state transition existed.
      </td>
    </tr>
    <tr>
      <td>Asset validation</td>
      <td>
        The relayer did not require independent confirmation of the
        corresponding token transfer or escrow balance increase.
      </td>
    </tr>
  </tbody>
</table>

<p>
  The cleanest technical description is:
</p>

<blockquote>
  <p>
    The Across attacker forged Solana deposit events that satisfied an
    incomplete off-chain parser, causing a Risk Labs relayer to pay
    destination-chain funds for deposits that never actually occurred.
  </p>
</blockquote>

<hr>

<h2>Scale of the Attack</h2>

<table>
  <thead>
    <tr>
      <th align="left">Metric</th>
      <th align="left">Reported value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Fabricated deposit events</td>
      <td>1,627</td>
    </tr>
    <tr>
      <td>Single-use Solana wallets</td>
      <td>1,627</td>
    </tr>
    <tr>
      <td>Destination chains targeted</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Nominal value of fabricated deposits</td>
      <td>Approximately $41.7 million</td>
    </tr>
    <tr>
      <td>Fraudulent requests filled</td>
      <td>581</td>
    </tr>
    <tr>
      <td>Gross Risk Labs relayer payout</td>
      <td>Approximately $4.5 million</td>
    </tr>
    <tr>
      <td>Initially trapped attacker funds</td>
      <td>Approximately $500,000</td>
    </tr>
    <tr>
      <td>Initial net-loss description</td>
      <td>Below $4 million</td>
    </tr>
    <tr>
      <td>Later returned amount</td>
      <td>331.8 ETH</td>
    </tr>
  </tbody>
</table>

<h3>Why Loss Estimates Differ</h3>

<p>
  Public figures around $3.35 million, $3.6 million, $4 million, and
  $4.5 million may describe different accounting categories:
</p>

<ul>
  <li>Gross amount advanced by the relayer</li>
  <li>Assets successfully consolidated by the attacker</li>
  <li>Assets trapped or frozen</li>
  <li>Assets subsequently recovered</li>
  <li>Net unrecovered loss at a particular time</li>
</ul>

<p>
  These figures should not be treated as interchangeable.
</p>

<hr>

<h2>Direct Incident-Watch Seeds</h2>

<p>
  Across publicly stated that it was tracking the following addresses
  with SEAL 911.
</p>

<table>
  <thead>
    <tr>
      <th align="left">Network</th>
      <th align="left">Address</th>
      <th align="left">Classification</th>
      <th align="left">Monitoring</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Solana</td>
      <td>
        <a href="https://solscan.io/account/8bkoZToaTBBtAPczgHqD4XVxWtvBkiy4crtexEtYDYSL">
          <code>8bkoZToaTBBtAPczgHqD4XVxWtvBkiy4crtexEtYDYSL</code>
        </a>
      </td>
      <td>
        Incident-linked Solana investigation and orchestration seed
      </td>
      <td>
        Watch directly and use for source-transaction and program-call
        expansion
      </td>
    </tr>
    <tr>
      <td>EVM — exact network role requires transaction-level review</td>
      <td>
        <a href="https://etherscan.io/address/0xa0C0e9f307b5A26cA3FB5891c19154fc7A02BeF7">
          <code>0xa0C0e9f307b5A26cA3FB5891c19154fc7A02BeF7</code>
        </a>
      </td>
      <td>Incident-linked EVM investigation seed</td>
      <td>Watch directly and use for destination-fill and proceeds tracing</td>
    </tr>
    <tr>
      <td>EVM — exact network role requires transaction-level review</td>
      <td>
        <a href="https://etherscan.io/address/0xA6fb971F3B7a9b9F76EdA76bc89268fe26560189">
          <code>0xA6fb971F3B7a9b9F76EdA76bc89268fe26560189</code>
        </a>
      </td>
      <td>Incident-linked EVM investigation seed</td>
      <td>Watch directly and use for destination-fill and proceeds tracing</td>
    </tr>
  </tbody>
</table>

<h3>Address-Attribution Limits</h3>

<ul>
  <li>
    The three addresses are high-confidence incident-linked tracking seeds.
  </li>
  <li>
    No named individual or organization has been publicly attributed as
    the attacker.
  </li>
  <li>
    The precise role of each EVM address should be confirmed through
    transaction-level review before assigning a narrower label.
  </li>
  <li>
    Do not apply the attacker label to every counterparty of these
    addresses.
  </li>
</ul>

<hr>

<h2>Fund-Recovery Update</h2>

<p>
  On <strong>July 28, 2026</strong>, PeckShield reported that an
  Across-exploiter-linked address returned <strong>331.8 ETH</strong>,
  worth approximately <strong>$624,000</strong> at the time of reporting,
  to the Across Hub Pool Owner multisig.
</p>

<table>
  <tbody>
    <tr>
      <td><strong>Recovery date</strong></td>
      <td>July 28, 2026</td>
    </tr>
    <tr>
      <td><strong>Network</strong></td>
      <td>Ethereum</td>
    </tr>
    <tr>
      <td><strong>Returned amount</strong></td>
      <td>331.8 ETH</td>
    </tr>
    <tr>
      <td><strong>Reported USD value</strong></td>
      <td>Approximately $624,000</td>
    </tr>
    <tr>
      <td><strong>Destination</strong></td>
      <td>
        <a href="https://etherscan.io/address/0xB524735356985D2f267FA010D681f061DfF03715">
          <code>0xB524735356985D2f267FA010D681f061DfF03715</code>
        </a>
      </td>
    </tr>
    <tr>
      <td><strong>Destination classification</strong></td>
      <td>Across Protocol Hub Pool Owner multisig</td>
    </tr>
    <tr>
      <td><strong>Recovery confidence</strong></td>
      <td>High for the reported transfer; transaction hash pending capture</td>
    </tr>
  </tbody>
</table>

<blockquote>
  <p>
    The Across Hub Pool Owner multisig is a recovery destination and
    protocol-controlled Safe. It must not be threat-labeled.
  </p>
</blockquote>

<p>
  This recovery event reduces the unrecovered amount, but a definitive
  updated net-loss statement from Risk Labs should be recorded only if
  Risk Labs or Across publishes one.
</p>

<hr>

<h2>Why User Funds Were Safe</h2>

<p>
  Across relayers advance their own destination-chain liquidity before
  later reimbursement.
</p>

<p>
  The forged-event parser caused the Risk Labs relayer to make fraudulent
  fills using relayer capital. It did not permit the attacker to withdraw
  directly from legitimate user deposits.
</p>

<p>
  Across stated that legitimate transfers were completed or refunded and
  that the financial loss was confined to the Risk Labs-operated relayer.
</p>

<p>
  This architecture limited the immediate blast radius. However, a relayer
  with greater available liquidity or weaker exposure controls could have
  filled substantially more of the approximately $41.7 million in
  fabricated requests.
</p>

<hr>

<h2>What Should Have Prevented the Attack</h2>

<p>
  A defensive Solana event consumer should validate all of the following
  before releasing destination-chain funds:
</p>

<ul>
  <li>Expected Solana program ID</li>
  <li>Exact event-authority PDA</li>
  <li>Expected cross-program invocation structure</li>
  <li>Exact eight-byte Anchor event discriminator</li>
  <li>Expected serialization version</li>
  <li>Expected payload length</li>
  <li>Successful transaction execution</li>
  <li>Canonical instruction and account relationships</li>
  <li>Corresponding on-chain deposit state</li>
  <li>Actual token transfer or escrow-balance increase</li>
  <li>Unique deposit identifier</li>
  <li>Replay protection</li>
  <li>Per-wallet, per-route, and per-period exposure limits</li>
  <li>Rate limits and anomaly detection for newly created wallets</li>
</ul>

<blockquote>
  <p>
    Events are notifications. Authenticated state transitions and verified
    asset movement are evidence.
  </p>
</blockquote>

<hr>

<h2>Analyst Classification</h2>

<ul>
  <li>
    <strong>Attack class:</strong>
    forged deposit-event acceptance by an off-chain relayer parser.
  </li>
  <li>
    <strong>Primary failure:</strong>
    missing event-type, provenance, state, and asset validation.
  </li>
  <li>
    <strong>Origin:</strong>
    Solana.
  </li>
  <li>
    <strong>Operational impact:</strong>
    fraudulent relayer fills across multiple destination chains.
  </li>
  <li>
    <strong>Direct-watch seeds:</strong>
    one Solana address and two EVM addresses published by Across.
  </li>
  <li>
    <strong>User-loss assessment:</strong>
    no user losses reported.
  </li>
  <li>
    <strong>Named attacker:</strong>
    none identified.
  </li>
  <li>
    <strong>Recovery status:</strong>
    partial recovery reported, including 331.8 ETH returned on July 28.
  </li>
</ul>

<hr>

<h2>Attribution Boundaries</h2>

<ul>
  <li>
    The three published addresses are incident-linked monitoring seeds.
  </li>
  <li>
    No named actor attribution should be assigned.
  </li>
  <li>
    The Risk Labs relayer is the affected victim infrastructure, not
    attacker-controlled infrastructure.
  </li>
  <li>
    The Across Hub Pool Owner multisig is a recovery destination and must
    not be threat-labeled.
  </li>
  <li>
    Across SpokePool contracts and event-authority accounts should be
    treated as protocol infrastructure.
  </li>
  <li>
    Destination-chain SpokePools, token contracts, bridges, DEX routers,
    liquidity pools, exchanges, and unrelated counterparties must not be
    automatically threat-labeled.
  </li>
  <li>
    Interaction with an incident-linked address does not independently
    prove common control, knowledge, or malicious intent.
  </li>
</ul>

<hr>

<h2>Sources</h2>

<ul>
  <li>
    <a href="https://x.com/AcrossProtocol">
      Across Protocol — Initial incident disclosure and SEAL 911 tracking
      addresses
    </a>
  </li>
  <li>
    <a href="https://mobile.twstalker.com/SEAL_911">
      SEAL 911 — Archived Across incident disclosure
    </a>
  </li>
  <li>
    <a href="https://docs.across.to/guides/concepts/intents-architecture">
      Across Documentation — Intent architecture and relayer model
    </a>
  </li>
  <li>
    <a href="https://en.cryptonomist.ch/2026/07/24/across-solana-relayer-attack/">
      The Cryptonomist — Technical post-incident analysis
    </a>
  </li>
  <li>
    <a href="https://hacked.slowmist.io/">
      SlowMist Hacked — Across Solana incident entry
    </a>
  </li>
  <li>
    <a href="https://blockchain.news/flashnews/across-protocol-exploiter-refunds-331-8-eth">
      Blockchain.News — PeckShield fund-recovery update
    </a>
  </li>
  <li>
    <a href="https://etherscan.io/address/0xB524735356985D2f267FA010D681f061DfF03715">
      Etherscan — Across Protocol Hub Pool Owner multisig
    </a>
  </li>
</ul>
