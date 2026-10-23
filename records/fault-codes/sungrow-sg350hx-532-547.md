---
id: fc:sungrow-sg350hx-532-547
type: FaultCode
name: Sungrow SG350HX 532-547
aliases:
- 532-547
- Sungrow 532-547
- PV Reverse Connection Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: 532-547
code_key: 532-547
code_from: 532
code_to: 547
display_message: PV Reverse Connection Alarm
page: 89
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=31.r3
    h: e686ceb2bfaa
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r1
    h: d532e40e88ef
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r1
    h: d532e40e88ef
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r3
    h: e686ceb2bfaa
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r1
    h: d532e40e88ef
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r1
    h: d532e40e88ef
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r3
    h: e686ceb2bfaa
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r1
    h: d532e40e88ef
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r1
    h: d532e40e88ef
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r3
    h: e686ceb2bfaa
  review: drafted
  review_note: 'support check: partial - Checking whether the string has reverse polarity is stated but
    no explicit measurement method.'
- claim_id: c5
  rel: mitigated_by
  target: mit:polarity-correction
  note: Correct only with DC switch open and string current below 0.5 A.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r1
    h: d532e40e88ef
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r1
    h: d532e40e88ef
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r3
    h: e686ceb2bfaa
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r1
    h: d532e40e88ef
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r1
    h: d532e40e88ef
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r3
    h: e686ceb2bfaa
  review: drafted
---
