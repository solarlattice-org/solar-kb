---
id: fc:sma-sunny-central-cp-xt-3803
type: FaultCode
name: SMA SC-CP-XT 3803
aliases:
- '3803'
- SMA 3803
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3803'
code_key: '3803'
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r12
    h: 561137c8e396
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r12
    h: 561137c8e396
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r12
    h: 561137c8e396
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:pv-current-measurement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r12
    h: 561137c8e396
  review: drafted
  review_note: 'support check: partial - Says to check DC input current, but no explicit detection by
    PV current measurement.'
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Only when the message appears frequently.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r12
    h: 561137c8e396
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Brief interruption of feed-in.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Interruption is brief; resumes on its own.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  review: drafted
  review_note: 'support check: partial - Brief interruption implies resumption, but not explicit; R column
    is ''-''.'
- claim_id: c8
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r12
    h: 561137c8e396
  review: drafted
---
