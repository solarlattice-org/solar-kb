---
id: fc:sma-stp-core1-us-7348
type: FaultCode
name: SMA CORE1-US 7348
aliases:
- '7348'
- SMA 7348
- Incorrect file format
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7348'
code_key: '7348'
display_message: Incorrect file format
page: 51
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h273
    h: a1fc113b5482
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h274
    h: 7dd1ba2d9012
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h190
    h: a1fc113b5482
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h191
    h: 7dd1ba2d9012
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h275
    h: a1fc113b5482
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h276
    h: 7dd1ba2d9012
  review: drafted
- claim_id: c4
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
- claim_id: c5
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
---
