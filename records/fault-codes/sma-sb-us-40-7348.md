---
id: fc:sma-sb-us-40-7348
type: FaultCode
name: SMA SB-US-40 7348
aliases:
- '7348'
- SMA 7348
- Incorrect file format
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-40
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP/1TP-US-40)
code: '7348'
code_key: '7348'
display_message: Incorrect file format
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-40-ba-en-13
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h221
    h: 14b76d13a164
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h222
    h: 7dd1ba2d9012
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h191
    h: 7dd1ba2d9012
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h222
    h: 7dd1ba2d9012
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h369
    h: a5f29b48f614
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h391
    h: a5f29b48f614
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:config-file-verification
  note: Verify format and integrity, then retry the import.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h275
    h: 2024a52bf518
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h192
    h: 2024a52bf518
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h223
    h: 2024a52bf518
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h370
    h: 2024a52bf518
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h392
    h: 2024a52bf518
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sb-us-40
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h221
    h: 14b76d13a164
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h222
    h: 7dd1ba2d9012
  review: drafted
---
