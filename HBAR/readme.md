<h1>HBAR Threat Actors and Wallets</h1>

<h2>Hedera → Ethereum Theft Flow</h2>

<table>
  <thead>
    <tr>
      <th align="left">Field</th>
      <th align="left">Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Chains</strong></td>
      <td>Hedera and Ethereum</td>
    </tr>
    <tr>
      <td><strong>Addresses</strong></td>
      <td>
        <code>0x9A4966152F6e10b33Cb7a37975e8619816d6a494</code><br>
        <code>0xaf20D792A19fD42dCf697ceBa6100291D96dD93e</code>
      </td>
    </tr>
    <tr>
      <td><strong>Incident</strong></td>
      <td>Suspected Hedera ecosystem compromise</td>
    </tr>
    <tr>
      <td><strong>Published</strong></td>
      <td>July 11, 2026</td>
    </tr>
    <tr>
      <td><strong>Source type</strong></td>
      <td>On-chain researcher, corroborated by multiple reporting feeds</td>
    </tr>
    <tr>
      <td><strong>Confidence</strong></td>
      <td>Medium — live incident attribution; Hedera has not yet published a definitive postmortem</td>
    </tr>
    <tr>
      <td><strong>Reported amount</strong></td>
      <td>More than $3.7 million</td>
    </tr>
    <tr>
      <td><strong>Activity</strong></td>
      <td>
        Funds reportedly moved from Hedera through LayerZero to Ethereum and were being converted from WBTC into ETH.
      </td>
    </tr>
    <tr>
      <td><strong>Address role</strong></td>
      <td>
        Theft and bridge-flow addresses; the exact source-versus-destination role for each address remains provisional.
      </td>
    </tr>
    <tr>
      <td><strong>Monitoring action</strong></td>
      <td>
        Watch both addresses directly and use them as graph-expansion pivots for bridge counterparties, WBTC swaps, ETH consolidation wallets, and subsequent exchange or mixer deposits.
      </td>
    </tr>
  </tbody>
</table>

<h2>Addresses</h2>

<h3>Suspected Theft / Bridge-Flow Address</h3>

<p>
  <code>0x9A4966152F6e10b33Cb7a37975e8619816d6a494</code>
</p>

<p>
  Public reporting associates this address with the suspected movement of stolen funds from the Hedera ecosystem to Ethereum.
</p>

<p>
  <strong>Recommended use:</strong> Watch directly and use as a graph-expansion pivot for LayerZero bridge counterparties, token swaps, ETH consolidation, and downstream deposits.
</p>

<hr>

<h3>Suspected Theft / Bridge-Flow Address</h3>

<p>
  <code>0xaf20D792A19fD42dCf697ceBa6100291D96dD93e</code>
</p>

<p>
  Public reporting associates this address with the suspected Hedera-to-Ethereum theft flow and subsequent asset-conversion activity.
</p>

<p>
  <strong>Recommended use:</strong> Watch directly and use as a graph-expansion pivot for WBTC swaps, ETH transfers, exchange deposits, mixer interactions, and connected wallets.
</p>

<blockquote>
  The exact source-versus-destination role of each address remains provisional.
</blockquote>

<h2>Incident Summary</h2>

<p>
  On-chain researcher Specter first reported the active theft flow. Odaily subsequently published the two addresses and described more than $3.7 million moving from Hedera to Ethereum through LayerZero.
</p>

<p>
  Binance and KuCoin news feeds independently reproduced the same addresses and attribution.
</p>

<h2>Analyst Note</h2>

<blockquote>
  This incident should currently be labeled <strong>“suspected Hedera exploit — Specter attribution”</strong>, not as a confirmed compromise of the Hedera base network.
</blockquote>

<p>
  The public evidence establishes suspicious theft-related fund movement and provides usable wallet seeds for monitoring and graph expansion.
</p>

<p>
  The following details remain unconfirmed:
</p>

<ul>
  <li>The initial attack vector</li>
  <li>The affected application, protocol, or account</li>
  <li>Whether the Hedera base network itself was compromised</li>
  <li>The precise source-versus-destination role of each address</li>
  <li>The identity or number of actors controlling the addresses</li>
</ul>

<h2>Classification</h2>

<ul>
  <li>
    <strong>Direct-watch priority</strong>
    <ul>
      <li><code>0x9A4966152F6e10b33Cb7a37975e8619816d6a494</code></li>
      <li><code>0xaf20D792A19fD42dCf697ceBa6100291D96dD93e</code></li>
    </ul>
  </li>
  <li>
    <strong>Graph-expansion targets</strong>
    <ul>
      <li>LayerZero bridge counterparties</li>
      <li>WBTC swap routers and liquidity pools</li>
      <li>ETH consolidation wallets</li>
      <li>Exchange deposit addresses</li>
      <li>Mixer or privacy-service deposits</li>
    </ul>
  </li>
  <li>
    <strong>Current attribution</strong>
    <ul>
      <li>Suspected Hedera exploit — Specter attribution</li>
      <li>Corroborated by multiple reporting feeds</li>
    </ul>
  </li>
  <li>
    <strong>Do not claim</strong>
    <ul>
      <li>A confirmed compromise of the Hedera base network</li>
      <li>A confirmed initial attack vector</li>
      <li>A confirmed individual or threat-group identity</li>
      <li>A definitive role for either address</li>
    </ul>
  </li>
  <li>
    <strong>Confidence</strong>
    <ul>
      <li>Medium — attribution remains provisional while the incident is active and no definitive Hedera postmortem has been published</li>
    </ul>
  </li>
</ul>