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
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r1
    h: 344b1ae4ad3d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grounding-cable-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r1
    h: 344b1ae4ad3d
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r1
    h: 344b1ae4ad3d
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r2
    h: 4b55ebede240
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r1
    h: 344b1ae4ad3d
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r1
    h: 344b1ae4ad3d
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r2
    h: 4b55ebede240
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r1
    h: 344b1ae4ad3d
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r1
    h: 344b1ae4ad3d
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r2
    h: 4b55ebede240
  review: drafted
  review_note: 'support check: partial - Checking insulation between ground cable and live wire is stated,
    but not insulation resistance testing specifically.'
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r1
    h: 344b1ae4ad3d
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r1
    h: 344b1ae4ad3d
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r2
    h: 4b55ebede240
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=54.r1
    h: 344b1ae4ad3d
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=40.r1
    h: 344b1ae4ad3d
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=33.r2
    h: 4b55ebede240
  review: drafted
---
