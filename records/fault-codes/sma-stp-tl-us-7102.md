---
id: fc:sma-stp-tl-us-7102
type: FaultCode
name: SMA STP-TL-US 7102
aliases:
- '7102'
- SMA 7102
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '7102'
code_key: '7102'
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r1
    h: 5ddb92ae453d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:parameter-download-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r3
    h: 6022b2728800
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r3
    h: 6022b2728800
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r3
    h: 6022b2728800
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r1
    h: 5ddb92ae453d
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h362
    h: cfb3a4f04fb7
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h363
    h: 6b6402ed30f5
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:reload-parameter-file
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r3
    h: 6022b2728800
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r3
    h: 6022b2728800
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r3
    h: 6022b2728800
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r1
    h: 5ddb92ae453d
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h364
    h: cbdd760c8efa
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r3
    h: 6022b2728800
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r3
    h: 6022b2728800
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r3
    h: 6022b2728800
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r1
    h: 5ddb92ae453d
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h363
    h: 6b6402ed30f5
  review: drafted
  review_note: 'support check: partial - Passages say the inverter continues to feed in despite the failure,
    which implies a warning, but the class is not…'
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r3
    h: 6022b2728800
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r3
    h: 6022b2728800
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r3
    h: 6022b2728800
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r1
    h: 5ddb92ae453d
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h363
    h: 6b6402ed30f5
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r1
    h: 5ddb92ae453d
  review: drafted
---
