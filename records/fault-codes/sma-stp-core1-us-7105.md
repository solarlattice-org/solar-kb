---
id: fc:sma-stp-core1-us-7105
type: FaultCode
name: SMA CORE1-US 7105
aliases:
- '7105'
- SMA 7105
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7105'
code_key: '7105'
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r4
    h: b52d03895a68
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r4
    h: b52d03895a68
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r4
    h: b52d03895a68
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:parameter-change-rejected
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r4
    h: b52d03895a68
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r4
    h: b52d03895a68
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r4
    h: b52d03895a68
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r6
    h: 16f5c7fa5db0
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-settings-review
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r4
    h: b52d03895a68
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r4
    h: b52d03895a68
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r4
    h: b52d03895a68
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r6
    h: 16f5c7fa5db0
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:enter-access-code
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r4
    h: b52d03895a68
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r4
    h: b52d03895a68
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r4
    h: b52d03895a68
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r6
    h: 16f5c7fa5db0
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r4
    h: b52d03895a68
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r4
    h: b52d03895a68
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r4
    h: b52d03895a68
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r6
    h: 16f5c7fa5db0
  review: drafted
  review_note: 'support check: partial - The inverter continues feeding after a failed parameter setting,
    which implies a warning, but the class is not stated.'
- claim_id: c8
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r4
    h: b52d03895a68
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r4
    h: b52d03895a68
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r4
    h: b52d03895a68
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r6
    h: 16f5c7fa5db0
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c9
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r4
    h: b52d03895a68
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r4
    h: b52d03895a68
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
