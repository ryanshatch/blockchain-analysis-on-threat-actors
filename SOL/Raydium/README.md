<div align="center" style="text-align: center;">
<h1>New SOL Threat-Wallet Alert</h1>
<h2>Raydium Legacy AMM V3 Exploit</h2>
</div>

<table>
  <thead>
    <tr><th align="left">Field</th><th align="left">Details</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Origin chain</strong></td><td>Solana</td></tr>
    <tr><td><strong>Proceeds chain</strong></td><td>Ethereum</td></tr>
    <tr><td><strong>Incident</strong></td><td>Fake LP-mint validation bypass against Raydium's deprecated AMM V3 program</td></tr>
    <tr><td><strong>Incident date</strong></td><td>June 10, 2026</td></tr>
    <tr><td><strong>Source type</strong></td><td>Raydium statements, security-research reporting, PeckShield fund-flow alerts, Solana and Ethereum explorer evidence</td></tr>
    <tr><td><strong>Confidence</strong></td><td>High for the incident, root-cause class, affected legacy pools, Solana attacker address, Ethereum proceeds address, and reported laundering path</td></tr>
    <tr><td><strong>Estimated loss</strong></td><td>Approximately $1.34 million: about 150,177 RAY, 5,603 SOL, and 893,700 USDC</td></tr>
    <tr><td><strong>Why it matters</strong></td><td>The legacy withdrawal instruction used the LP mint supplied by the caller without proving it matched the pool's authentic LP mint. The attacker created a counterfeit mint with a supply they controlled, causing the program's share calculation to treat fake LP tokens as ownership of the real pool reserves.</td></tr>
  </tbody>
</table>

<h2>Incident Summary</h2>

<p>
On June 10, 2026, an attacker targeted five inactive Raydium liquidity pools attached to the deprecated AMM V3 program. The program had been phased out in 2021 and was no longer reachable through Raydium's current interface or SDK, but the old on-chain program and residual pool reserves remained callable.
</p>

<p>
The attacker created a counterfeit SPL token mint, minted the fake LP token supply to an attacker-controlled account, and passed that mint into the legacy withdrawal instruction. Because the program did not strictly compare the caller-supplied LP mint with the immutable LP mint assigned to each pool, the fake token supply was used in the withdrawal proportion calculation.
</p>

<p>
By controlling both the amount held and the total supply of the counterfeit mint, the attacker made the program calculate a 100% liquidity share and release real assets from the affected pools. The stolen assets were consolidated on Solana, converted and bridged to Ethereum, after which approximately 810 ETH was reported deposited into Tornado Cash and 7 ETH was sent to FixedFloat.
</p>

<h2>Direct Incident-Watch Seeds</h2>

<h3>Primary Solana Attacker Address</h3>
<p><a href="https://solscan.io/account/4WnPebowR4HHfumvNPaDjG6Pa5Hi1jxLm6xmmBq33QVk"><code>4WnPebowR4HHfumvNPaDjG6Pa5Hi1jxLm6xmmBq33QVk</code></a></p>
<p>Publicly identified as the primary attacker wallet used to drain the deprecated Raydium pools and consolidate stolen assets.</p>
<p><strong>Recommended use:</strong> Highest-priority direct-watch seed. Expand initial KuCoin funding, exploit calls, counterfeit mint creation, swaps, peel-chain activity, and bridge preparation.</p>

<h3>Ethereum Proceeds Address</h3>
<p><a href="https://etherscan.io/address/0x0EaBAAb9a56011c6158D4aA7f2E49A82fB34E609"><code>0x0EaBAAb9a56011c6158D4aA7f2E49A82fB34E609</code></a></p>
<p>Publicly linked to the bridged Raydium proceeds and subsequent Tornado Cash and FixedFloat movements.</p>
<p><strong>Recommended use:</strong> Watch directly for privacy-pool deposits, exchange or swap-service interactions, cross-chain reuse, and later fund returns.</p>

<h3>Solana Bridge-Preparation / Consolidation Address</h3>
<p><a href="https://solscan.io/account/2snHHreXbpJ7UwZxPe37gnUNf7Wx7wv6UKDSR2JckKuS"><code>2snHHreXbpJ7UwZxPe37gnUNf7Wx7wv6UKDSR2JckKuS</code></a></p>
<p>Independent forensic reporting identifies this address as a bridge-preparation hub after the stolen assets were converted into USDC.</p>
<p><strong>Recommended use:</strong> Graph-expansion seed. Confirm each inbound and outbound transfer before assigning direct attacker control.</p>

<h2>Affected Pools</h2>
<ul>
  <li>Sollet USDT–RAY</li>
  <li>Sollet ETH–RAY</li>
  <li>SRM–RAY</li>
  <li>USDC–RAY</li>
  <li>RAY–SOL</li>
</ul>

<blockquote>
The affected pools were deprecated infrastructure and victim liquidity sources. They should not be threat-labeled. Current Raydium programs, active pools, SDK routes, and ordinary users were not reported affected by this incident.
</blockquote>

<h2>Technical Root Cause</h2>

<ol>
  <li>The attacker created a new SPL token mint unrelated to the authentic LP mint of any affected pool.</li>
  <li>The attacker minted a controlled supply of counterfeit LP tokens.</li>
  <li>The legacy AMM V3 withdrawal instruction accepted the caller-supplied mint account without validating it against the pool's configured LP mint.</li>
  <li>The program calculated the withdrawal proportion using the counterfeit mint's held amount and total supply.</li>
  <li>Because the attacker controlled the full fake supply, the calculation represented the attacker as owning 100% of the pool.</li>
  <li>The program released real RAY, SOL, USDC, and legacy pool assets in exchange for fake LP tokens.</li>
  <li>The sequence was repeated across five deprecated pools.</li>
</ol>

<blockquote>
The attacker did not forge authentic Raydium LP tokens. The legacy program was tricked into treating an unrelated mint as the pool's LP token because it failed to bind the mint account to the pool configuration.
</blockquote>

<h2>Fund Flow</h2>

<pre>
Five deprecated Raydium AMM V3 pools
        ↓ counterfeit LP mint withdrawals
4WnPebowR4HHfumvNPaDjG6Pa5Hi1jxLm6xmmBq33QVk
        ↓ swaps and consolidation on Solana
2snHHreXbpJ7UwZxPe37gnUNf7Wx7wv6UKDSR2JckKuS
        ↓ Solana-to-Ethereum bridge
0x0EaBAAb9a56011c6158D4aA7f2E49A82fB34E609
        ├─ approximately 810 ETH → Tornado Cash
        └─ approximately 7 ETH → FixedFloat
</pre>

<h2>Classification</h2>
<ul>
  <li><strong>Primary classification:</strong> Solana smart-contract account-validation exploit</li>
  <li><strong>Vulnerability:</strong> Missing LP mint identity validation</li>
  <li><strong>Affected surface:</strong> Deprecated AMM V3 pools phased out of the UI and SDK in 2021</li>
  <li><strong>Direct-watch targets:</strong> primary Solana attacker and Ethereum proceeds wallet</li>
  <li><strong>Graph-expansion target:</strong> Solana bridge-preparation hub</li>
  <li><strong>Initial funding:</strong> public reporting states the attacker was funded from KuCoin; the exchange itself must not be threat-labeled</li>
  <li><strong>Named actor:</strong> none publicly identified</li>
</ul>

<h2>Impact and Response</h2>
<ul>
  <li>Approximately 150,177 RAY, 5,603 SOL, and 893,700 USDC were removed.</li>
  <li>Raydium stated that no current users or active mainnet programs were affected.</li>
  <li>The affected legacy pools were not available through the current Raydium dApp or SDK.</li>
  <li>Raydium committed to covering the losses from its treasury.</li>
  <li>The project initiated additional security review of current mainnet programs.</li>
  <li>No public attacker identity or confirmed recovery of the laundered proceeds was identified in the reviewed sources.</li>
</ul>

<h2>Monitoring Boundaries</h2>
<ul>
  <li>Do not threat-label KuCoin solely because it was reported as the initial funding source.</li>
  <li>Do not threat-label Tornado Cash contracts or every FixedFloat counterparty as attacker-controlled.</li>
  <li>Do not merge this case with Raydium's separate December 2022 authority-compromise incident.</li>
  <li>Preserve the distinction between deprecated AMM V3 code and Raydium's active programs.</li>
</ul>

<h2>Sources</h2>
<ul>
  <li><a href="https://www.theblock.co/post/404304/raydium-dex-1-34-million-exploit-retired-amm-program-treasury-cover-losses">Raydium incident confirmation and affected-pool scope</a></li>
  <li><a href="https://blog.autosec.dev/security-events/raydium-legacy-amm-v3-lp-mint-validation-exploit/">AUTOSEC — root cause, loss estimate, and reported attacker addresses</a></li>
  <li><a href="https://hacked.slowmist.io/?c=Solana">SlowMist Hacked — Raydium incident record</a></li>
  <li><a href="https://community.chainbounty.io/posts/019ec8ef-7235-711a-adfb-b196ac5dd2be">Independent cross-chain fund-flow analysis</a></li>
</ul>

<hr>
<h2>In other words:</h2>
<p>
Raydium's old program asked the caller which token mint represented the pool's LP shares, but it did not verify that answer against the pool's real LP mint. The attacker created a fake token with a supply they completely controlled and presented it as the LP token.
</p>
<p>
The program divided the attacker's fake holdings by the fake total supply, calculated that the attacker owned the entire pool, and released real assets from five retired pools.
</p>
<p><strong>TLDR:</strong> A missing LP-mint identity check let counterfeit tokens masquerade as genuine Raydium liquidity shares, draining approximately $1.34 million from deprecated Solana pools before the proceeds were bridged to Ethereum.</p>
