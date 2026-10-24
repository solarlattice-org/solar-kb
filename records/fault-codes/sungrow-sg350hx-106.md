---
id: fc:sungrow-sg350hx-106
type: FaultCode
name: Sungrow SG350HX 106
aliases:
- '106'
- Sungrow 106
- Grounding Cable Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '106'
code_key: '106'
display_message: Grounding Cable Fault
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=33.r2
    h: 4b55ebede240
  review: drafted
- claim_id: c2
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
  review: drafted
- claim_id: c3
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
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
  rel: applies_to
  target: prod:sungrow-sg350hx
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=33.r2
    h: 4b55ebede240
  review: drafted
---
