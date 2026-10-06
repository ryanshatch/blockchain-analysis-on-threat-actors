# Contributing evidence

Open an issue using the existing intelligence or attribution-correction template before a large case addition. Include primary or reproducible sources, full network-specific identifiers, dates with their exact meaning, observed transaction IDs where available, and the uncertainty in actor control. Do not upload stolen data, keys, personal doxxing, malware binaries, or live phishing links that facilitate harm.

For a dedicated case, update its README and `addresses.csv` together. The CSV role should distinguish direct attacker control, exploit proceeds, malicious infrastructure, victim/recovery assets, service hops and unconfirmed counterparties. Use `threat_label=false` for addresses that must not inherit an attacker label. Do not infer a named actor, a loss amount, a transaction date, or a common controller from mere contact with a suspicious wallet. Preserve historical corrections and state what changed.

Before proposing a change, run:

```sh
python -m threatintel validate
python -m unittest discover -s tests -v
python scripts/check_docs.py
```

The validator currently skips older CSV schemas, reporting each file. If you change one of those cases, review it manually and add an adapter or schema mapping rather than forcing fields into a misleading form. The [data model](docs/data-model.md) describes the generated index and current guardrails. Repository content is subject to its existing [license](LICENSE); discuss substantial contribution or reuse permissions with the maintainer.
