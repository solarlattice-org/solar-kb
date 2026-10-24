---
id: fc:sma-stp-tl-us-3901-3902
type: FaultCode
name: SMA STP-TL-US 3901-3902
aliases:
- 3901-3902
- SMA 3901-3902
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 3901-3902
code_key: 3901-3902
code_from: 3901
code_to: 3902
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r2
    h: 751ce4fac423
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:insufficient-irradiance
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h216
    h: 4c08e1cc039f
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h217
    h: 25763edab45d
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r2
    h: 751ce4fac423
  review: drafted
  review_note: 'support check: partial - Passages say start conditions not met and wait for higher irradiation,
    but don''t explicitly name insufficient irradiance as the symptom…'
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h217
    h: 25763edab45d
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Applies when the message recurs frequently in the morning.
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h217
    h: 25763edab45d
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r2
    h: 751ce4fac423
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h217
    h: 25763edab45d
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r2
    h: 751ce4fac423
  review: drafted
  review_note: 'support check: partial - Waiting for higher irradiation implies it resolves once conditions
    are met, but auto-reset is not explicitly stated.'
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r2
    h: 751ce4fac423
  review: drafted
---
