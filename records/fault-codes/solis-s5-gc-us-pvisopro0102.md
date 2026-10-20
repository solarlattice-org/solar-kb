---
id: fc:solis-s5-gc-us-pvisopro0102
type: FaultCode
name: Solis S5-GC PV ISO-PRO 01/02
aliases:
- PV ISO-PRO 01/02
- pvisopro0102
- Solis PV ISO-PRO 01/02
- Ground Protect ion
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: PV ISO-PRO 01/02
code_key: pvisopro0102
display_message: Ground Protect ion
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c3
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:insulation-loss
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Solution says physically check cables, implying DC cables, but
    the cable type isn''t specified as the affected component.'
- claim_id: c6
  rel: detected_by
  target: method:insulation-resistance-test
  note: Repeat in the same weather as when the alarm occurred.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15
    h: cb7b6f9ed265
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Listed in the ''Fault messages'' table, but the row doesn''t
    state the device behavior; classification only implied by table title.'
- claim_id: c9
  rel: has_recovery
  target: ec:manual-reset
  note: Reset after inspection; replace inverter if insulation checks normal and fault persists.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Solution includes reset inverter and replace inverter, but the
    passage doesn''t say reset is required to clear it or that…'
---
