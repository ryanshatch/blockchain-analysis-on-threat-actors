# Evidence-aware data model (v1)

The case `addresses.csv` files remain authoritative. `python -m threatintel build` produces a local SQLite index for searching them; the database is generated, not committed. It has no live-chain collector, enrichment feed, inference engine, or mutable address labels.

## Tables

| Table | Key | Meaning |
| --- | --- | --- |
| `cases` | `case_id` | Named incident or campaign, not automatically a known human/group. `case_file` points back to its README. |
| `indicators` | `(chain_id, address_key, indicator_type)` | Reusable chain-specific identifier. EVM address keys are lowercased for exact matching; the displayed address remains from the first source row. The same hex account on two chains is two identifiers. |
| `observations` | `(case_id, indicator_id)` | One case-specific role, confidence, monitoring treatment and source CSV line. This is the attribution unit; a shared identifier does not imply shared ownership. |
| `evidence` | `(observation_id, url)` | Source URLs attached to that particular case observation. |

Source CSV columns are preserved as case observation fields. `incident_date`, `disclosure_date`, or `observed_date` becomes `event_date`; its source meaning is not silently converted into first/last on-chain activity. A blank date stays null. The `chain_id_origin` field is `source` except for older COLDCARD Bitcoin rows with blank chain IDs, which are explicitly mapped from `network=Bitcoin` to `bitcoin-mainnet` and flagged `network_mapping`.

`source_confidence` and `control_confidence` stay as source text. They are not numeric probabilities. `threat_label` is an explicit, case-specific boolean; a `false` observation may still warrant monitoring as a proceeds or service pivot. `priority` is an operational label, not an objective risk score. Recovery/victim indicator types cannot be threat-labeled by the importer. Contracts and programs may be malicious infrastructure, but must not be described as proceeds wallets without evidence.

The validator checks column shape, ISO dates, required fields, complete address *syntax* for known networks, evidence URLs, duplicate case/network/indicator keys, and the recovery/victim guardrail. It does not prove a checksum, on-chain existence, current balance, source credibility, common control, or legal status. Unknown network identifiers receive only a conservative length/whitespace check; reviewers must verify them against a chain-specific source.

The current adapter reads dedicated case `addresses.csv` files in the 16-column layout and explicitly lists skipped legacy schemas and security-sweep recaps. Recaps often repeat dedicated-case rows and are not counted as independent cases. Do not treat importer totals as the repository's total investigative coverage.

## Extend the model without creating false precision

- Add separate, sourced event/transaction tables before introducing first/last activity, volumes, flows or related-wallet edges. A report date is not a chain-activity date, and a transfer is not proof of shared controller.
- Keep wallet, victim contract, recovery address, service hop, token mint, malicious program, domain and social indicator types distinct. Never propagate an attacker label through a graph edge automatically.
- Add an `actor_id` only when evidence supports a stable actor grouping. A case ID can represent an unidentified incident; do not manufacture 25–50 named actors from existing cases.
- A future risk score needs a published rubric, missing-data behavior, calibration and tests before it can be used operationally. Do not turn confidence wording or transaction volume into an unexplained 0–100 score.
- Keep observation history rather than replacing an older role when funds are returned or an attribution is corrected. The original CSV and dated case narrative must identify the evidence for each change.

## Local use

From the repository root with Python 3.12 or newer:

```sh
python -m threatintel validate
python -m threatintel build --output /tmp/threatintel.sqlite
python -m threatintel query --db /tmp/threatintel.sqlite --case NEAR-INTENTS-2026-10-01
python -m threatintel query --db /tmp/threatintel.sqlite --address 0x8F103B6A0aD705bcE6357842A5fefEB49e8D83Ef --threat-only
```

The build refuses to overwrite an existing output. Choose a new path for a refresh. Query results include source path/line, role, confidence fields and evidence URLs. They are JSON observations, not a blacklist or automated enforcement decision.
