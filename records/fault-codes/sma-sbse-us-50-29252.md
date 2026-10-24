---
id: fc:sma-sbse-us-50-29252
type: FaultCode
name: SMA SBSE-US-50 29252
aliases:
- '29252'
- SMA 29252
- Backup operation not possible
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '29252'
code_key: '29252'
display_message: Backup operation not possible
page: 121
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.81
    h: 7c0020ee8351
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h811
    h: c36ebb05aba4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:backup-mode-unavailable
  note: Backup mode does not start while the grid connection remains active.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h811
    h: c36ebb05aba4
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h812
    h: fbfc4453c9d0
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-settings-review
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h813
    h: 699a4a33d802
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.81
    h: 7c0020ee8351
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h811
    h: c36ebb05aba4
  review: drafted
---
