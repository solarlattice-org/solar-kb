---
id: fc:sungrow-sg-cx-us-39
type: FaultCode
name: Sungrow SG-CX-US 39
aliases:
- '39'
- Sungrow 39
- Low system insulation resistance
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '39'
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
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r1
    h: 6d164bcc8c14
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:insulation-loss
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r1
    h: 6d164bcc8c14
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  review: drafted
  review_note: 'support check: partial - Passages say to check resistance to ground of string/DC cable,
    but don''t state the fault is detected by insulation resistance…'
- claim_id: c5
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r1
    h: 6d164bcc8c14
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  review: drafted
  review_note: 'support check: partial - Passages say to check the ISO protection value setting, a troubleshooting
    step rather than a detection method; roughly implied.'
- claim_id: c6
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r1
    h: 6d164bcc8c14
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r1
    h: 6d164bcc8c14
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears itself; repeated occurrence leads to settings and insulation checks, then service.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r1
    h: 6d164bcc8c14
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r3
    h: 99f23921c8b9
  review: drafted
---
