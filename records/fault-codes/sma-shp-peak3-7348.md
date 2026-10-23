---
id: fc:sma-shp-peak3-7348
type: FaultCode
name: SMA PEAK3-US 7348
aliases:
- '7348'
- SMA 7348
- Incorrect file format
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '7348'
code_key: '7348'
display_message: Incorrect file format
page: 66
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.24
    h: 7223324b4373
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h390
    h: 9c35d2b262b7
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
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
