<div align="center" style="text-align: center;">
<h1>New Multi-Chain Threat Campaign Alert</h1>
<h2>SpaceX / Grok / xAI and 2026 FIFA World Cup Wallet Drainers</h2>
</div>

<table>
  <thead>
    <tr><th align="left">Field</th><th align="left">Details</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Networks</strong></td><td>Solana and EVM ecosystems, with separate Bitcoin and Ethereum deposit-scam activity also observed in the broader campaign set</td></tr>
    <tr><td><strong>Campaign period</strong></td><td>Observed during May–July 2026; Blockaid published its analysis July 8, 2026</td></tr>
    <tr><td><strong>Classification</strong></td><td>Multi-victim wallet-drainer, malicious dApp, fake-token, impersonation, and authorized-push-payment scam campaign</td></tr>
    <tr><td><strong>Source type</strong></td><td>Primary threat-intelligence reporting by Blockaid</td></tr>
    <tr><td><strong>Confidence</strong></td><td>High for the campaign behavior, malicious dApp infrastructure, wallet targeting, and named drainer-kit families described by Blockaid</td></tr>
    <tr><td><strong>Estimated loss</strong></td><td>No defensible aggregate Solana loss figure published</td></tr>
    <tr><td><strong>Why it matters</strong></td><td>The campaign demonstrates rapidly re-themed commercial drainer infrastructure targeting Solana users through Phantom, Backpack, Solflare, OKX, and Coinbase-facing experiences while also operating across EVM ecosystems.</td></tr>
  </tbody>
</table>

<h2>Campaign Summary</h2>

<p>
Blockaid documented a wave of malicious dApps and investment scams that reused high-interest public narratives around SpaceX, Grok, xAI, and the 2026 FIFA World Cup. The campaigns used lookalike sites, fake token presales, deepfake or impersonation content, direct-deposit scams, and wallet-draining dApps.
</p>

<p>
The World Cup portion of the campaign included malicious dApps detected across Solana and EVM. Blockaid specifically reported sites targeting users of Phantom, Backpack, Solflare, OKX, and Coinbase and automatically flagged a malicious <code>$WCUP</code> token dApp.
</p>

<p>
This campaign should not be counted as a single Solana protocol exploit. It is a multi-victim social-engineering and malicious-dApp campaign whose infrastructure is designed to change domains, themes, tokens, and receiving addresses rapidly.
</p>

<h2>Reported Drainer Ecosystem</h2>

<p>Blockaid attributed the World Cup campaign wave primarily to established drainer operations and kits including:</p>
<ul>
  <li>AngelFerno</li>
  <li>Quark</li>
  <li>Rublevka</li>
  <li>Eleven</li>
  <li>Step</li>
</ul>

<blockquote>
These names describe drainer operations or commercial kits reported by Blockaid. They should not be treated as proof that every observed domain or wallet was controlled by one actor.
</blockquote>

<h2>Public Domain Indicators</h2>

<table>
  <thead>
    <tr><th align="left">Domain</th><th align="left">Reported presentation</th><th align="left">Handling</th></tr>
  </thead>
  <tbody>
    <tr><td><code>roobet-worldcup.vercel.app</code></td><td>World Cup-themed malicious dApp</td><td>Block / investigate; retain as campaign IOC</td></tr>
    <tr><td><code>worldcupvp.app</code></td><td>World Cup-themed malicious dApp</td><td>Block / investigate; retain as campaign IOC</td></tr>
    <tr><td><code>watchfifa2026.xyz</code></td><td>Fake tournament or streaming-themed infrastructure</td><td>Block / investigate; retain as campaign IOC</td></tr>
    <tr><td><code>vote-worldcuponpump.com</code></td><td>World Cup / token-themed malicious dApp</td><td>Block / investigate; retain as campaign IOC</td></tr>
    <tr><td><code>fifaworldc.com</code></td><td>World Cup impersonation infrastructure</td><td>Block / investigate; retain as campaign IOC</td></tr>
  </tbody>
</table>

<h2>Attack Pattern</h2>

<pre>
Trending event or impersonated brand
        ↓
Deepfake, hijacked social account, ad, message, or search traffic
        ↓
Lookalike site / fake presale / fake betting, voting, or streaming dApp
        ↓
Wallet connection, token interaction, signature, or direct deposit
        ↓
Malicious transaction or authorized victim transfer
        ↓
Fresh receiving address / drainer infrastructure
        ↓
Rapid domain and address rotation
</pre>

<h2>Why Address-Only Blocking Is Insufficient</h2>

<ul>
  <li>Blockaid reported that fresh scam addresses may be created for individual victims and have little or no prior on-chain history.</li>
  <li>Domains are machine-generated, short-lived, and replaced before manual blocklists catch up.</li>
  <li>Multiple independent drainer operators reuse the same event narrative, so there is no single universal attacker address.</li>
  <li>The same campaign family can combine wallet-draining dApps with direct-deposit investment scams.</li>
</ul>

<h2>Wallet and Address Status</h2>

<blockquote>
Blockaid's public report did not publish a definitive campaign-wide list of Solana attacker wallets suitable for direct insertion into the repository's threat-wallet index. No wallet addresses are invented or inferred in this case file.
</blockquote>

<p><strong>Monitoring action:</strong> Track the published domains, drainer-kit families, malicious token/dApp behavior, and any future addresses released by Blockaid or corroborated through transaction-level evidence.</p>

<h2>Classification</h2>
<ul>
  <li><strong>Primary classification:</strong> multi-chain wallet-drainer and impersonation campaign</li>
  <li><strong>Solana relevance:</strong> malicious dApps targeted Phantom, Backpack, Solflare, OKX, and Coinbase users and included a malicious <code>$WCUP</code> token dApp</li>
  <li><strong>Protocol exploit:</strong> no</li>
  <li><strong>Confirmed rug pull:</strong> no; fake and malicious tokens were part of the lure infrastructure</li>
  <li><strong>Aggregate loss:</strong> not quantified in the public source</li>
  <li><strong>Direct-watch wallet set:</strong> unresolved</li>
</ul>

<h2>Sources</h2>
<ul>
  <li><a href="https://www.blockaid.io/blog/wallet-drainers-and-investment-scams-impersonating-spacex-and-the-fifa-world-cup">Blockaid — Wallet Drainers and Investment Scams Impersonating SpaceX and the FIFA World Cup</a></li>
</ul>

<hr>
<h2>In other words:</h2>
<p>
The attackers did not need to discover a new Solana vulnerability. They packaged existing drainer tooling around whatever people were already paying attention to — SpaceX, Grok, xAI, and the World Cup — and pushed victims toward convincing fake sites.
</p>
<p>
Because the domains and receiving addresses rotate quickly, the useful intelligence is not just a wallet list. The campaign's behavioral pattern, drainer families, domain infrastructure, fake-token themes, and transaction behavior are the stronger long-term indicators.
</p>
<p><strong>TLDR:</strong> Blockaid identified a cross-chain scam wave using major 2026 events to deliver wallet drainers and fake-token dApps, including Solana-targeted sites and a malicious <code>$WCUP</code> dApp; no reliable aggregate loss or campaign-wide wallet list was publicly released.</p>
