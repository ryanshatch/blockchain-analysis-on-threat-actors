<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <div style="text-align: center;">
        <img
            alt="Header image"
            src="https://i0.wp.com/thegeorgiasun.com/wp-content/uploads/2021/12/shutterstock_1919690516-scaled.jpg?fit=2000%2C1333&quality=89&ssl=1"
        >
        <hr>
    </div>
    <div align="center">

# Blockchain Analysis on Threat Actors

**A defensive on-chain intelligence repository for tracking sanctioned wallets, threat actors, exploit flows, scams, rug pulls, and suspicious cryptocurrency activity.**

</div>

---

## Overview

This repository contains cryptocurrency addresses and transaction data collected through:

- Official government and law-enforcement disclosures
- Public blockchain explorers
- Security researchers and threat-intelligence providers
- Public reporting
- Personally encountered fraud and scam-baiting investigations
- Independent on-chain analysis

Entries range from **official, high-confidence attributions** to **provisional investigative leads**. Each case should be evaluated according to its listed source type, confidence level, and supporting evidence.

> Inclusion in this repository does not independently prove criminal activity. Addresses associated with active investigations, suspected incidents, or third-party reporting should be treated as provisional unless confirmed by an authoritative source.

---

## Repository Structure

### Analysis Directories

| Directory | Description |
|---|---|
| [`1VPNS/`](./1VPNS/) | OFAC-designated wallets associated with Dmytro Rashevskyi and First VPN Service / 1VPNS across BTC, ETH, and SOL. |
| [`FTX/`](./FTX/) | Historical FTX and Alameda Research wallet analysis, balances, addresses, and transaction activity. |
| [`HBAR/`](./HBAR/) | Hedera-to-Ethereum suspected theft and bridge-flow analysis. |
| [`HOPE/`](./HOPE/) | Analysis of the Solana-based HOPE token, wallet concentration, transfers, sales, and suspected rug activity. |
| [`Lazarus/`](./Lazarus/) | DPRK TraderTraitor / Lazarus Group wallets, including addresses connected to the Bybit theft and earlier incidents. |
| [`SOL/`](./SOL/) | Solana-specific threat-actor, governance, exploit, and suspicious-wallet investigations. |
| [`SOL/BonkDAO/`](./SOL/BonkDAO/) | Analysis of the BonkDAO governance attack and associated on-chain activity. |
| [`TRON/`](./TRON/) | TRON-specific sanctions, state-linked attribution, and threat-wallet investigations. |
| [`TRON/Central-Bank-of-Iran/`](./TRON/Central-Bank-of-Iran/) | OFAC attribution involving TRON addresses associated with the Central Bank of Iran. |


### Notable Subdirectories

| Directory | Description |
|---|---|
| [`parsing/`](./parsing/) | Transaction exports, CSV datasets, combined transfer records, parsing scripts, and analysis notes. |
| [`img/`](./img/) | Images and supporting visual evidence used by repository documentation. |
| [`parsing/sol tx history/`](./parsing/sol%20tx%20history/) | Raw and processed Solana transaction-history exports. |

### Root Files

| File | Purpose |
|---|---|
| [`readme.md`](./readme.md) | Main repository overview and navigation. |
| [`wallets.md`](./wallets.md) | General wallet index and individual wallet records. |
| [`scammer DB.html`](./scammer%20DB.html) | Legacy HTML-format scammer and wallet database. |
| [`.gitattributes`](./.gitattributes) | Git file-handling configuration. |

---

## Current Research Coverage

| Category | Examples |
|---|---|
| Sanctions intelligence | OFAC-designated infrastructure, state-linked wallets, and sanctioned actors |
| State-sponsored activity | DPRK TraderTraitor / Lazarus Group |
| Cybercrime infrastructure | First VPN Service / 1VPNS |
| Exchange and protocol incidents | FTX, Alameda Research, Bybit, and Hedera-related flows |
| Governance attacks | BonkDAO |
| Rug pulls and token manipulation | HOPE and other Solana ecosystem cases |
| Personally encountered fraud | Spear-phishing, impersonation, hacked-account, and payment scams |
| Transaction analysis | Wallet clustering, bridge activity, swaps, consolidation, and exchange deposits |

---

## Chain Coverage

| Chain | Coverage |
|---|---|
| Bitcoin | Sanctioned wallets, fraud payments, DPRK-linked addresses, and scam-related transfers |
| Ethereum and EVM chains | Theft flows, sanctioned wallets, bridge destinations, token swaps, and consolidation activity |
| Solana | Rug pulls, governance attacks, NFT-related fraud, token concentration, and scam wallets |
| TRON | Sanctions attribution and state-linked financial infrastructure |
| Hedera | Suspected exploit and cross-chain bridge activity |

---

## Confidence Levels

| Confidence | Meaning |
|---|---|
| **High** | Official attribution from OFAC, FBI, DOJ, law enforcement, a court filing, or another authoritative source |
| **Medium** | Supported by multiple reputable researchers, security firms, blockchain records, or reporting sources |
| **Low** | Preliminary lead, personally encountered wallet, unconfirmed attribution, or incomplete transaction evidence |
| **Unknown** | Address retained for monitoring but attribution has not been sufficiently established |

Confidence describes the strength of the attribution, not the certainty that every transaction involving the address is malicious.

---

## Recommended Case Format

Each investigation directory should contain a `README.md` with the following information:

| Field | Description |
|---|---|
| Incident or actor | Name of the actor, organization, protocol, scam, or incident |
| Published date | Date the attribution or alert was published |
| Source type | OFAC, FBI, security researcher, public reporting, personal investigation, or other source |
| Confidence | High, medium, low, or unknown |
| Classification | Sanctioned wallet, theft address, bridge-flow wallet, scam wallet, exchange deposit, or another role |
| Chain | BTC, ETH, SOL, TRON, HBAR, or another supported network |
| Address | Complete blockchain address |
| Address role | Seed wallet, consolidation wallet, deposit address, theft wallet, intermediary, or suspected counterparty |
| Monitoring action | Recommended analytical or alerting use |
| Evidence | Source links, transaction hashes, screenshots, exports, or supporting notes |
| Limitations | Unresolved questions, conflicting evidence, or provisional assumptions |

---

## Research Workflow

1. Identify an address through an authoritative disclosure, reputable alert, public report, or direct investigation.
2. Confirm the address and chain using an appropriate blockchain explorer.
3. Record the original source and publication date.
4. Assign an attribution confidence level.
5. Document the address role without overstating unsupported conclusions.
6. Review direct counterparties, token transfers, bridge activity, swaps, and consolidation behavior.
7. Store raw transaction exports in [`parsing/`](./parsing/).
8. Add material attribution changes or newly discovered addresses to the relevant case directory.
9. Preserve previous findings when an attribution changes instead of silently replacing them.

---

## Common Monitoring Uses

Addresses in this repository may be useful for:

- Sanctions-exposure screening
- Wallet and counterparty monitoring
- Graph-expansion seeds
- Bridge-flow analysis
- Exchange-deposit detection
- Mixer-interaction analysis
- Theft-fund tracing
- Scam-pattern comparison
- Threat-intelligence enrichment
- Historical incident research

---

## Source Standards

Preferred sources include:

- U.S. Department of the Treasury and OFAC
- FBI and IC3
- U.S. Department of Justice
- Court filings and official seizure notices
- Blockchain explorers
- Established blockchain-security firms
- Reputable on-chain researchers
- Exchange-security disclosures
- Protocol postmortems
- Transaction-level evidence

Social-media posts, anonymous claims, and unverified community reports should be treated as leads rather than confirmed attribution.

---

## Data Handling

- Preserve addresses exactly as published.
- Record the correct blockchain for every address.
- Separate confirmed facts from analytical conclusions.
- Clearly identify provisional or disputed attribution.
- Avoid publishing unnecessary personally identifiable information.
- Link to original sources whenever possible.
- Do not assume every counterparty of a malicious wallet is also malicious.
- Reassess older entries when new attribution or transaction evidence becomes available.

---

## Disclaimer

This repository is maintained for defensive security research, fraud analysis, threat intelligence, education, and historical documentation.

The information may be incomplete, outdated, provisional, or dependent on third-party reporting. Users should independently verify addresses, transactions, and attribution before relying on the data for legal, compliance, enforcement, or financial decisions.
    <!-- <div align="center" style="text-align: center;">
        <h1>Wallet Database</h1>
        <p>This is a database of crypto wallets that include both public alerts (new addition to my research and parsing) along with all fraud related scammers that I encounter.<br></p>
        <p><strong>I consistently add, maintain, and or follow all of the data parsed into this repo.</strong></p>
        <hr>
    </div>
    <div style="text-align: center;">
        <p>
            <strong>Wallets currently under analysis:</strong><br>
            <h4>Local Spear phishing treat actor:</h4>
            <code>bc1qexnz95lqaj6dje92wrsevv9tljrgws8c79znfw</code>:<br>
            <br><p>Currently empty because of a failed attack. I still plan on keeping them under heavy surveilance due to how close to home this scammer is, chances are high they are local using a mule based out of Macon GA. I will release more details in time, currently keeping this as vague as possible.</p>
            <h3><strong>Related coverage: 3/20/2026 - 3/23/2026</strong></h3>
            <a href="https://theaugustapress.com/rcso-make-arrest-in-fraudulent-bail-payment-scheme/">The Augusta Press</a><br>
            <a href="https://thegeorgiasun.com/crime/scam-alert/augusta-woman-arrested-in-phone-scam-targeting-richmond-county-residents">The Georgia Sun</a><br>
            <a href="https://mylolowcountry.com/sullivan-s-island/arrest-made-in-phone-fraud-probe-in-richmond-county/">My Lowcountry</a><br>
            <a href="https://www.wrdw.com/2026/03/20/augusta-woman-arrested-jail-bond-phone-scam/">WRDW</a>
            <h4>Just a note that these attacks are getting more and more in depth by the day and closer and closer to home. If you are reading this, I want you to take this as a personal warning from one to another, I dont want to see ANYONE fall for any types of these scams. Whether they are impersonating real officers or officials, if you dont remember the incident chances are it isnt real. Javascript is just as real as BTC ATM's. It breaks my heart to see this database grow and for each wallet to have grown in txn history. Americans deserve the money they work for, please stay safe out there anon.</h4>
            <br><p>small update: Recieved a letter in the mail from Social Security about Scam Alerts. I'm beyond happy that this problem is finally being delivered to everyones doorsteps. Anyone who partakes in deciet and exploiting deserves no reconciliation and a life sentence.</p>
            <div style="text-align: center;">
                <img
                    alt="Sub Header Image"
                    src="https://github.com/ryanshatch/blockchain-analysis-on-threat-actors/blob/main/img/mail.png">
        </p>
        <hr>
        <p>
            @rovercrc aka Rover:
            <code>0x4472d6969c0750dd7ba8e387d2b007a80794802f</code>
        </p>
        <hr>
        <p>
            ENS: drewroberts.eth<br>
            <code>0xC6aa2f0FF6b8563EA418ec2558890D6027413699</code><br><br>
            <s><code>2GsFJ1JR1j8RAWuUfdJPXdjknq5VmKG9XSfoTZdqQeoR</code></s><br>
            <s><code>0xAAcE3E2dB13C372C74BDaE118f045D49daC8AE18</code></s><br>
            <s><code>6UWokqQxV4mcK7DeggjQGYMvLJ5HY6zH8AM1Bj6axPGw</code></s>
        </p>
    </div>
    <hr>
    <img
        alt="Solana"
        src="https://github.com/imaclone-sol/Rugger-Wallet-DB/blob/main/PamajjDAO%20burning.JPG"
    >
    <hr>
    <h3>Sam Bankman Fried - SBF</h3>
    <h4>Alameda Research 25: <code>0x84D34f4f83a87596Cd3FB6887cFf8F17Bf5A7B83</code></h4>
    <table cellspacing="0" cellpadding="0">
        <thead>
            <tr>
                <th></th>
                <th>A</th>
                <th>B</th>
                <th>C</th>
                <th>D</th>
                <th>E</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>1</th>
                <td>Address</td>
                <td>Label</td>
                <td>USD balance (Oct 1st 2021)</td>
                <td>USD balance (Nov 7th 2021)</td>
                <td>DIfference</td>
            </tr>
            <tr>
                <th>#25</th>
                <td>0x84d34f4f83a87596cd3fb6887cff8f17bf5a7b83</td>
                <td>Alameda Research</td>
                <td>$117,799</td>
                <td>$160,951</td>
                <td>$43,152</td>
            </tr>
        </tbody>
    </table>
    <ul>
        <li>$eth - <a href="https://etherscan.io/address/0x84d34f4f83a87596cd3fb6887cff8f17bf5a7b83">View on Etherscan</a></li>
        <li>All Chains - <a href="https://blockscan.com/address/0x84d34f4f83a87596cd3fb6887cff8f17bf5a7b83">View on Blockscan</a></li>
        <li>More detailed analysis on FTX wallets can be found in this subrepository - <a href="https://github.com/ryanshatch/Scam-Bait/tree/main/FTX">FTX Analysis</a></li>
    </ul>
    <hr>
    <h4>Fz Pamajj - $sol</h4>
    <ul>
        <li>Exchange.art account: <a href="https://exchange.art/fz-pamajj/nfts">View NFT Account</a></li>
        <li>Burner 2: <code>3LT9mkc7yQTofJVa3MSeEFg15Wehk4y7ZWwmfmUu7qvx</code> - <a href="https://solscan.io/account/3LT9mkc7yQTofJVa3MSeEFg15Wehk4y7ZWwmfmUu7qvx#solTransfers">Solscan</a></li>
        <li>Burner 1: <code>41tCXQbqaTDfkYzEPRQzkL1d8kVck7GgCXQsMcT7bnUk</code> - <a href="https://solscan.io/account/41tCXQbqaTDfkYzEPRQzkL1d8kVck7GgCXQsMcT7bnUk#solTransfers+splTokenTransfers">Solscan</a></li>
        <li>Main: <code>HSRjRJmTu9UVugqNea2X2WVFnb329SywgBGipJhMLKU5</code> - <a href="https://solscan.io/account/HSRjRJmTu9UVugqNea2X2WVFnb329SywgBGipJhMLKU5#solTransfers+splTokenTransfers">Solscan</a></li>
    </ul>
    <h4>Pamajj DAO:</h4>
    <ul>
        <li>solscan: <a href="https://solscan.io/collection/734599ad3777b5444f05482651a3d1e2193565b3c17d7f48ddf3fdf4a44b607d">Collection</a></li>
        <li>Magic Eden: <a href="https://magiceden.io/marketplace/pamajjdao_pass_">Marketplace</a></li>
        <li>Burned Token: <a href="https://solscan.io/token/8eBnBufXe5aDi2Zb68vhxQKmZdDFxndQcyaJre7fHgqk">Token Info</a></li>
    </ul>
    <hr>
    <h4>Alex Becker</h4>
    <ul>
        <li>Main: <code>0xaE4D837cAA0C53579f8a156633355Df5058B02f3</code> - <a href="https://etherscan.io/address/0xae4d837caa0c53579f8a156633355df5058b02f3">Etherscan</a></li>
        <li>USDC Cash Out: <code>0x907b322d33121a50a9f7bc5305761b0ca40c6113</code> - <a href="https://etherscan.io/tokentxns?a=0x907b322d33121a50a9f7bc5305761b0ca40c6113&ps=100&p=1">Etherscan</a></li>
    </ul>
    <hr>
    <h4>Kmoney - kmoney.sol</h4>
    <ul>
        <li>
            $sol - <code>7byBtWp7uW8eYNs1N4uDesGf5hw8gkCdbPUWi6ckyUNX</code>
            <ul>
                <li>solscan: <a href="https://solscan.io/account/7byBtWp7uW8eYNs1N4uDesGf5hw8gkCdbPUWi6ckyUNX">View on Solscan</a></li>
                <li>birdeye profile: <a href="https://birdeye.so/profile/7byBtWp7uW8eYNs1N4uDesGf5hw8gkCdbPUWi6ckyUNX?chain=solana">View Profile</a></li>
            </ul>
        </li>
    </ul>
    <hr>
    <h4>Dusting Attack wallet</h4>
    <p>$sol - <code>777vxoS8tWgLEgr6yMp5scadhnWxkksRKDMQFBJKD24N</code></p>
    <ul>
        <li>solscan: <a href="https://solscan.io/account/777vxoS8tWgLEgr6yMp5scadhnWxkksRKDMQFBJKD24N">View on Solscan</a></li>
        <li>dusting attack: when a small amount of crypto is sent to a large number of wallet addresses. The attackers then attempt to trace the transaction activity of these wallets in order to de-anonymize them.</li>
    </ul>
    <hr>
    <div style="text-align: center;">
        <p>
            FB Brooklynn Taylor Buff (Hacked acct) (changed to Faith Spires) - 
            <code>bc1q9etmuux673pkrtqsh6m3fratuqxw22nc70s2gu</code>
        </p>
        <a href="https://www.facebook.com/luhh.faithh">Facebook Profile</a> -
        <a href="https://blockchair.com/bitcoin/address/bc1q9etmuux673pkrtqsh6m3fratuqxw22nc70s2gu">Bitcoin Address</a>
    </div>
    <br>
    <hr>
    <div style="text-align: center;">
        <p>
            FB Brooklynn Taylor Buff (Hacked acct updated June 23) (changed to Faith Spires) -
            <code>3B8PAG1ynzghVixBNDfGAijfWthob8sgQo</code>
        </p>
        <a href="https://www.facebook.com/luhh.faithh">Facebook Profile</a> -
        <a href="https://blockchair.com/bitcoin/address/3B8PAG1ynzghVixBNDfGAijfWthob8sgQo">Bitcoin Address</a>
    </div>
    <br>
    <hr>
    <div style="text-align: center;">
        <p>
            FB Hollie Harvell hacked acct 9/3/2023 -
            <code>35jFVWx6fNUV8QA5vsVtw6iXE5XpBDFJet</code>
        </p>
        <a href="https://www.facebook.com/hollie.harvell.77">Facebook Profile</a> -
        <a href="https://blockchair.com/bitcoin/address/35jFVWx6fNUV8QA5vsVtw6iXE5XpBDFJet">Bitcoin Address</a>
    </div>
    <br>
    <hr>
    <div style="text-align: center;">
        <p>
            Luwizop ($sol Panic Station Pythons rugger) -
            <code>3YaGKXSuxwfvKiJ83V92hKRvh23w1RdYgrwY7C5CSNG6</code>
        </p>
        <ul style="display: inline-block; text-align: left;">
            <li>solscan: <a href="https://solscan.io/account/3YaGKXSuxwfvKiJ83V92hKRvh23w1RdYgrwY7C5CSNG6#portfolio">View Portfolio</a></li>
        </ul>
    </div> -->
</body>
</html>
