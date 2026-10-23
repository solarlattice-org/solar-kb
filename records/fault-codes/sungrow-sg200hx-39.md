---
id: fc:sungrow-sg200hx-39
type: FaultCode
name: Sungrow SG200HX 039
aliases:
- '039'
- '39'
- Sungrow 039
- Low System Insulation Resistance
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: '039'
code_key: '39'
display_message: Low System Insulation Resistance
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r4
    h: 85cfb0a3dd33
  review: drafted
- claim_id: c2
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
- claim_id: c3
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
  review: drafted
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
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
  review: drafted
  review_note: 'support check: partial - Passages say to check the resistance to ground of the string
    and DC cable and the ISO protection value, but…'
- claim_id: c7
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
- claim_id: c8
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
- claim_id: c9
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
---
