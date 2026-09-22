# ether.fi Legacy AtomicQueue — Full Identifier Resolved

| Field | Assessment |
|---|---|
| Incident | September 11, 2026, Ethereum |
| Classification | Legacy queue authorization failure; abuse of outstanding ERC-20 approvals |
| Reported impact | Approximately 15.4536 ETH from eleven user wallets |
| Attacker | `0xa5cc6e490bce9185fa47b421f2eac677a83b64ea` |
| Treatment | High-confidence P1 direct watch and graph expansion |
| Vulnerable queue | `0xd45884b592e316eb816199615a95c182f75dea07` — victim/protocol infrastructure only |
| Identifier verification | September 22, 2026 |

The submitted September 11 scan withheld this case because its visible attacker representation was truncated. The [article's explorer link](https://www.cryptotimes.io/2026/09/11/ether-fi-loses-15-45-eth-in-legacy-atomicqueue-exploit-ceo-pledges-full-user-reimbursement/) now resolves the complete address. Reproduced [SlowMist](https://w.twstalker.com/SlowMist_Team) and [ExVul](https://mobile.twstalker.com/exvulsec) alerts identify the same attacker. This supersedes the earlier exclusion without guessing missing characters.

The complete transaction is [`0x7cbe0b4349513fed6d03ba8bf9ed708e10e07a501d10b5f344a25ae10595599b`](https://eth.blockscout.com/tx/0x7cbe0b4349513fed6d03ba8bf9ed708e10e07a501d10b5f344a25ae10595599b). Blockscout independently returns success, the same initiating EOA, and **September 11 at 07:20:11 UTC**. This verifies the transaction/initiator relationship; the aggregate loss and underlying mechanism remain attributed to the cited incident analyses.

[SlowMist's original alert](https://x.com/SlowMist_Team/status/2098344499923784048) attributes the flaw to insufficient authorization of the caller-supplied solver, permitting abuse of victims' existing allowances. The reported Tornado Cash routing does not make mixer infrastructure attacker-controlled. The victim queue, current ether.fi vaults, and users whose approvals were exploited must not receive attacker labels.

[addresses.csv](./addresses.csv) contains one attacker seed and one victim queue. [transactions.csv](./transactions.csv) records the exploit initiator and reported aggregate loss, explicitly distinguishing those from an individual token-transfer leg. No named actor is established. A still-truncated exploit-contract representation is not ingested.
