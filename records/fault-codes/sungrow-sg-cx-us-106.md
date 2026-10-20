---
id: fc:sungrow-sg-cx-us-106
type: FaultCode
name: Sungrow SG-CX-US 106
aliases:
- '106'
- Sungrow 106
- Grounding cable fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '106'
code_key: '106'
display_message: Grounding cable fault
page: 97
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r1
    h: 344b1ae4ad3d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grounding-cable-fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r2
    h: bb5f80409564
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r1
    h: 344b1ae4ad3d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r1
    h: 344b1ae4ad3d
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:insulation-resistance-test
  note: Insulation between ground cable and live conductor is checked.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r2
    h: bb5f80409564
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r1
    h: 344b1ae4ad3d
  review: drafted
  review_note: 'support check: partial - Insulation between ground cable and live wire is checked, but
    no insulation resistance test is stated.'
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r1
    h: 344b1ae4ad3d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only after wiring and insulation causes are ruled out.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r2
    h: bb5f80409564
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r1
    h: 344b1ae4ad3d
  review: drafted
---
