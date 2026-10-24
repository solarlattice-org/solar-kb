---
id: fc:sungrow-sg-cx-us-39
type: FaultCode
name: Sungrow SG-CX-US 039
aliases:
- '039'
- '39'
- Sungrow 039
- Low system insulation resistance
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '039'
code_key: '39'
display_message: Low system insulation resistance
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r3
    h: 99f23921c8b9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r4
    h: 85cfb0a3dd33
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:insulation-loss
  note: Unless caused by rainy or damp conditions.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r3
    h: 99f23921c8b9
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r4
    h: 85cfb0a3dd33
  review: drafted
  review_note: 'support check: partial - The row names it a fault code, but nothing explicitly classes
    it as a fault rather than a warning; the…'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: 'If repeated: check settings and insulation, then contact service.'
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r4
    h: 85cfb0a3dd33
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r1
    h: 64dee7ae617e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Passages say to check the resistance to ground of the string
    and DC cable and the ISO protection value, but…'
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: Verify insulation protection threshold complies with local rules.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r4
    h: 85cfb0a3dd33
  review: drafted
- claim_id: c9
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r1
    h: 64dee7ae617e
  review: drafted
- claim_id: c10
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r1
    h: 64dee7ae617e
  review: drafted
  review_note: 'support check: partial - The passages mention the module and the string only as a cause
    and a check target; the PV array is…'
- claim_id: c11
  rel: applies_to
  target: prod:sungrow-sg-cx-us
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=37.r3
    h: 99f23921c8b9
  review: drafted
---
