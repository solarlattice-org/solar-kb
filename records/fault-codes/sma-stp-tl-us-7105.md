---
id: fc:sma-stp-tl-us-7105
type: FaultCode
name: SMA STP-TL-US 7105
aliases:
- '7105'
- SMA 7105
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '7105'
code_key: '7105'
page: 51
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r6
    h: 16f5c7fa5db0
  review: drafted
- claim_id: c2
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
- claim_id: c3
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
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
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
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r6
    h: 16f5c7fa5db0
  review: drafted
---
