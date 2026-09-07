# Hamas / Al-Qassam Cryptocurrency Financing and Laundering Network

| Field | Assessment |
|---|---|
| Public disclosure | September 1, 2026 |
| Source | U.S. Department of Justice and FBI seizure-warrant affidavits |
| Networks represented here | TRON and BNB Smart Chain |
| Classification | Terrorist fundraising, consolidation, laundering, exchange conversion, and money-mule activity |
| Seized value reported by DOJ | Approximately $560,000 |
| Machine-readable records | 18 complete addresses |
| Confidence | High for official network linkage; role-specific ownership caveats preserved |

## Executive Assessment

On September 1, 2026, the U.S. Department of Justice announced the unsealing of cryptocurrency seizure warrants directed at infrastructure used by Hamas's Al-Qassam Brigades. DOJ said the FBI seized approximately $560,000 and that Hamas controlled the seized cryptocurrency-address infrastructure on behalf of its military wing.

This case ingests the complete on-chain identifiers in the June 25, 2025 warrant package, case `25-sz-34`, relevant to the supplied finding: fourteen TRON target-property addresses, two Binance-linked TRON user accounts, one BNB Smart Chain financier account, and one separate BSC laundering/exchange hop described in the affidavit. It does not treat transactional neighbors, exchange sweeps, token contracts, or service infrastructure as Hamas-controlled by proximity alone.

## Highest-Priority Seeds

| Network | Address | Role | Confidence | Treatment |
|---|---|---|---|---|
| TRON | [`TAZEkqkjuHkYznF3Q8g9PKbpRuUNtUbgCB`](https://tronscan.org/#/address/TAZEkqkjuHkYznF3Q8g9PKbpRuUNtUbgCB) | Hamas donation-consolidation and operational laundering wallet | High | P1 direct watch |
| BNB Smart Chain | [`0x0c78ab86e809e1f65374055610f9fcb5cd100734`](https://bscscan.com/address/0x0c78ab86e809e1f65374055610f9fcb5cd100734) | Financier and fiat-conversion network account; seizure target | High | P1 direct watch |
| TRON | [`TL192dbA29m2pyaug7m7gHCurzGbzFnLEx`](https://tronscan.org/#/address/TL192dbA29m2pyaug7m7gHCurzGbzFnLEx) | Downstream laundering and rapid Binance dispersal wallet | High | P1 direct watch |

The FBI identified `TAZEk...UbgCB` as a consolidation wallet for Hamas donations. The affidavit describes it receiving funds from multiple donation addresses and dispersing them downstream. `TL192...FnLEx` received approximately 43,700 USDT exclusively from that consolidation wallet and transferred nearly all of it to Binance-linked accounts within about 20 minutes.

The BSC address `0x0c78...00734` is Target Property 39. The affidavit describes the associated Binance account as belonging to a financier who enabled a virtual-currency exchange network Hamas used to obtain fiat.

## Donation and Financing Addresses

| Address | Evidentiary role | Treatment |
|---|---|---|
| `TA315GUGunjKDhv1ZL1YTvy7asPzJhAtL1` | Official TRON seizure target in the Hamas fundraising graph | Direct watch |
| `TS4toQBwagdM2oD1Q9eNqWoL8s7fMg5U2b` | Official TRON seizure target in the Hamas fundraising graph | Direct watch |
| `TWsomy6GFJqhswDjJcufPgTpMKGhwcVhdw` | Official TRON seizure target in the Hamas fundraising graph | Direct watch |
| `TVWRL9AY81gDdChuYiCfiNm5U39DNTyQwG` | Official TRON seizure target in the Hamas fundraising graph | Direct watch |
| `TYjWo3X1eFm8ufpb1jPQf8xv5bfriszGgq` | Official TRON seizure target in the Hamas fundraising graph | Direct watch |
| `TM1ywQ3ApL8ai2VTR6515fmzNdgFdKfa6J` | Official TRON seizure target in the Hamas fundraising graph | Direct watch |
| `TAbC5hoom3mktAGf3KZBNdxhEEujdUtpWG` | Official TRON seizure target in the Hamas fundraising graph | Direct watch |
| `TFBnvjWAjXkRAigJSPR5YqzowMNT85y1YZ` | Official TRON seizure target in the Hamas fundraising graph | Direct watch |
| `TDeBgBrQjgySyP9zPje3CRBCT2MQd13hy3` | Address supplied by the Al-Qassam fundraising email to a prospective donor | Direct watch |
| `TWE3K4dctpkdQgXG5VRHU4ND1ssh3HCCFg` | Address supplied by the Al-Qassam fundraising email to a prospective donor | Direct watch |
| `TCeCc94bcYiooTuGsHojDCUNbdneK2qgn3` | Address supplied by the Al-Qassam fundraising email to a prospective donor | Direct watch |
| `TL5Npc5AA2CuWcWzjzemGV1zBo3dadUgdF` | Address supplied by the Al-Qassam fundraising email to a prospective donor | Direct watch |

The direct email evidence is stronger than proximity-only clustering: investigators documented responses from the Al-Qassam fundraising email that supplied target addresses to prospective donors. All twelve addresses above are nevertheless stored with their precise official target-property role rather than with an unsupported real-person controller.

## Custodial and Exchange-Linked Accounts

| Network | Address | Role | Ownership boundary | Treatment |
|---|---|---|---|---|
| TRON | `TKmyTRdBaKXviN5MCJHD7nvfmoSTQ6zzmS` | Binance-linked likely money-mule account | Custodial user account, not a self-hosted wallet | Direct watch for historical and recurring exposure |
| TRON | `TYZwCibn8uH1jr9c7i9Vc46mPoGpS9cvsz` | Binance-linked likely money-mule account | Custodial user account, not a self-hosted wallet | Direct watch for historical and recurring exposure |
| BNB Smart Chain | `0x8a48E24D664f481e5B8b98f6efa4Af43DC765834` | Incident-linked cross-chain exchange and laundering hop | Affidavit describes it as unattributed; precise controller unresolved | Direct watch for incident flows and graph expansion |

The affidavit says the BSC hop received approximately 20,005 USDT after a Binance user moved funds from TRON to BSC and forwarded 29,880 USDT to the financier account about 30 minutes later. It is useful incident infrastructure, but the evidence does not establish that it shared a controller with Target Property 39.

## Attribution Boundaries

- The official filings support Hamas / Al-Qassam fundraising-network linkage and the address-specific roles recorded here. They do not establish one controller for all 18 records.
- Binance-linked TRON accounts are custodial user accounts. Exchange hot wallets and later Binance consolidation sweeps do not inherit the Hamas label.
- `0x8a48...5834` is an incident-linked but unattributed BSC exchange hop; its control confidence is deliberately lower than its transaction-path confidence.
- Token contracts, bridges, exchange infrastructure, routers, and ordinary counterparties remain graph pivots unless separately attributed.
- This directory is not an exhaustive ingestion of every address in all five warrant packages linked from the September 1 DOJ release.

## Withheld Pending Primary-Source Reconciliation

The following two syntactically valid TRON addresses appeared in the submitted finding but were not located in the DOJ release or the five linked warrant packages reviewed for this update:

- `TWQTTSqorX2dqVYmVn8j1WNNaKgmL7ShkV`
- `TYMRKshB4rMrr2UP3HF9AFM1PGjpFSKLHh`

They are not included in `addresses.csv` or the direct-watch index. A complete address is necessary, but not sufficient, for threat attribution.

## Sources

- [U.S. Department of Justice — September 1 disruption and seizure announcement](https://www.justice.gov/usao-dc/pr/justice-department-continues-disrupt-hamas-terrorist-financing-schemes-through-seizures)
- [U.S. Department of Justice — June 25, 2025 seizure warrant and affidavit, case 25-sz-34](https://www.justice.gov/usao-dc/media/1459826/dl?inline=)

---

## TLDR

The September 1 unsealing adds 18 complete, role-separated TRON and BSC monitoring records from the June warrant package. `TAZEk...UbgCB` and `0x0c78...00734` are the strongest P1 seeds. Donation addresses, a downstream laundering wallet, two custodial money-mule accounts, and an unattributed BSC exchange hop retain narrower labels. Two additional submitted TRON strings are withheld because they could not be reconciled to the reviewed DOJ filings.
