# Expansion roadmap

The repository already contains many research cases. The goal is to improve reuse and reproducibility, not to create a larger file count or assign unsupported actor identities.

## Milestone 1 — queryable foundation (this PR)

- Preserve existing case CSVs as source of truth and index the compatible dedicated cases in a generated SQLite database.
- Keep chain-specific identifiers, case-specific roles, evidence URLs, control confidence and threat-label boundaries separate.
- Validate new compatible records and run unit tests on pull requests. Report legacy files not yet supported.
- Document the model, limitations and a reproducible local query workflow.

Acceptance: a clean checkout runs `python -m unittest discover -s tests -v`, `python -m threatintel validate`, and a build/query without credentials, network calls, or committed database files.

## Milestone 2 — legacy migration and richer observations

Map legacy address layouts case by case, with review of field meaning and source provenance. Add domains/social identifiers and dated transaction or fund-flow *events* as separate sourced records. Deduplicate sweep recaps without deleting narrative history. Provide a reconciliation report showing imported and excluded rows.

Acceptance: each adapter has fixtures, explicit lossless field mapping and no attacker-label promotion of victim, recovery or custodial infrastructure.

## Milestone 3 — optional, rate-limited collectors

Start with one chain and a public, documented API. Make credentials optional and scoped; implement bounded pagination, retries, caching, snapshot timestamps and raw-response provenance. Keep local/offline analysis functional. Add Ethereum, Solana, BNB Chain, Base, Polygon, Arbitrum and Avalanche separately only as source quality and maintenance permit.

Acceptance: mocked API tests cover errors, rate limits and reorg-sensitive data; no secrets or unverified labels enter committed datasets automatically.

## Milestone 4 — analysis and reports

Build evidence-backed timelines, transaction-level flow views and actor/campaign profiles. Show which links are direct transaction facts and which are hypotheses. Add holder/liquidity checks for relevant token cases and only then evaluate a transparent, calibrated risk model. Avoid assigning risk scores where observations are sparse.

Acceptance: generated reports can be recreated from pinned data snapshots and cite the evidence behind every assertion; reviewer approval remains required for attribution changes.

## Milestone 5 — maintenance and release quality

Add contribution and correction review templates, schema-versioned exports, migration tests, dependency/security checks if dependencies are introduced, and a changelog. Consider PostgreSQL only if concurrent writers or query scale justify it; SQLite is sufficient for the present read-only local workflow.
