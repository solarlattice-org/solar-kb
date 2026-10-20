---
id: fc:solis-s5-gc-us-arcfault
type: FaultCode
name: Solis S5-GC ARC-FAULT
aliases:
- ARC-FAULT
- arcfault
- Solis ARC-FAULT
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: ARC-FAULT
code_key: arcfault
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c3
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: drafted
  review_note: 'support check: partial - Cables are to be checked, implying DC cable, but the passage
    doesn''t explicitly name it as affected.'
- claim_id: c4
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:junction-box
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: detected_by
  target: method:junction-box-inspection
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: drafted
- claim_id: c9
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15
    h: cb7b6f9ed265
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Listed in the ''Fault messages'' table, but the row doesn''t
    state device behavior; classification only implied by table title.'
- claim_id: c10
  rel: has_recovery
  target: ec:manual-reset
  note: Reset after DC circuit inspection; replace inverter if fault persists.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Reset inverter and replace inverter are listed in the solution,
    but the passage doesn''t say it clears by manual reset specifically.'
---
