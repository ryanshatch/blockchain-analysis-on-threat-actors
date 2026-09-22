# FomoPeek — Malicious iOS Releases and Wallet-Credential Theft

| Field | Assessment |
|---|---|
| Public disclosure | September 19, 2026; joint SlowMist and OKX investigation |
| Payload introduction | September 9, 2026, version 1.1 / build 105 |
| Affected releases | Version 1.1 / build 105 and version 1.2 / build 110 |
| Classification | Malicious App Store application; kernel-exploit-assisted credential theft |
| Ecosystems | Marketed for Solana, Ethereum, and TRON; device-accessible secrets may extend beyond these chains |
| Impact | Multiple asset-theft/private-key-exposure reports; aggregate loss and victim count not publicly established |
| Wallet ingestion | Zero; no complete, sufficiently attributed proceeds cluster in the reviewed reporting |
| Confidence | High for reported malicious functionality and campaign linkage; operator identity unknown |
| Evidence cutoff | September 19–21 reporting; source checks September 22, 2026 |

[SlowMist's alert](https://x.com/SlowMist_Team/status/2101211432541192615) and [OKX's corroborating announcement](https://x.com/OKXWallet_CN/status/2101213182253740536), reproduced in [The Crypto Times](https://www.cryptotimes.io/2026/09/19/slowmist-warns-fomopeek-ios-versions-may-expose-crypto-wallet-keys/), describe two hidden modules unrelated to the app's advertised tracking features. One contained an iOS kernel-exploitation framework with eight methods selected according to device and OS version.

If successful, that exploitation could escape the app sandbox, access/decrypt Keychain material, and read other applications' files. Potentially exposed information includes private keys, seed phrases, account credentials, messages, and files. Investigators also reported remote-command communications and captured plaintext configuration showing that exploitation was enabled for periodic execution. This establishes malicious capability and reported deployment, not proof that every installation succeeded in compromising its device.

## Release History

| Version | Build | Reported release | Package findings |
|---|---|---|---|
| 1.0 | Not retained | Earlier release | The two malicious frameworks were not found in the historical comparison |
| 1.1 | 105 | September 9 | Malicious modules first introduced |
| 1.2 | 110 | September 12 | Both modules retained |
| 1.3 | Not retained | September 17 | Both frameworks removed |

The [reported historical-package comparison](https://crypto.news/binance-warns-iphone-users-of-fomopeek-malware-targeting-crypto-wallets/) concerns official App Store releases, not merely sideloaded or re-signed packages. The four version records are preserved in [releases.csv](./releases.csv). Absence of these modules in one version is not a general safety certification, and removing them does not revoke secrets previously exposed.

The framework declares coverage across **iOS 12.0–18.7.x and 26.0–26.1**. This is a code-level compatibility claim, not evidence that every device/build in those ranges is exploitable. The supplied reporting does not provide a verified method-to-CVE mapping, so this case assigns no guessed CVE identifiers.

## Attribution and Monitoring

This is distinct from the [August FOMO iOS allegation](../August-2026-Security-Sweep/), whose verified transfer did not establish app causation. Similar branding is not evidence of common ownership. FomoPeek is a malicious application campaign rather than a Solana protocol exploit and is excluded from the single-incident Solana count.

Retain the release identifiers and investigative findings while awaiting published wallet addresses, transaction evidence, a defensible loss total, and clearer operator attribution. Reports of key exposure should be assessed against the specific device and installation history. SlowMist and OKX advised affected users to generate replacement credentials on a trusted device that never had the app installed and preserve relevant evidence.

No malicious application, executable framework, exploit implementation, or live command-server payload is included in this repository.

## Sources

- [SlowMist — original September 19 alert](https://x.com/SlowMist_Team/status/2101211432541192615)
- [OKX Wallet — joint-investigation confirmation](https://x.com/OKXWallet_CN/status/2101213182253740536)
- [The Crypto Times — reproduced researcher findings and operating behavior](https://www.cryptotimes.io/2026/09/19/slowmist-warns-fomopeek-ios-versions-may-expose-crypto-wallet-keys/)
- [crypto.news — build and release timeline](https://crypto.news/binance-warns-iphone-users-of-fomopeek-malware-targeting-crypto-wallets/)
- [CCN — credential exposure and declared OS coverage](https://www.ccn.com/news/crypto/fomopeek-ios-malware-steals-crypto-wallet-seed-phrases/)
