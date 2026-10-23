---
id: fc:sma-stp-core1-us-3803
type: FaultCode
name: SMA CORE1-US 3803
aliases:
- '3803'
- SMA 3803
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '3803'
code_key: '3803'
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r4
    h: 93c2d6ff802b
  review: drafted
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
  rel: detected_by
  target: method:pv-current-measurement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r12
    h: 561137c8e396
  review: drafted
  review_note: 'support check: partial - Says to check DC input current, but no explicit detection by
    PV current measurement.'
- claim_id: c7
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
- claim_id: c8
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
- claim_id: c9
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
---
