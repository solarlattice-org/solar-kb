---
id: fc:sungrow-sg-cx-us-532-547
type: FaultCode
name: Sungrow SG-CX-US 532-547
aliases:
- 532-547
- Sungrow 532-547
- String x reverse connection alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 532-547
code_key: 532-547
code_from: 532
code_to: 547
display_message: String x reverse connection alarm
page: 98
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r1
    h: d532e40e88ef
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r3
    h: 1c1583d51d6a
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r1
    h: d532e40e88ef
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r3
    h: 1c1583d51d6a
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r1
    h: d532e40e88ef
  review: drafted
  review_note: 'support check: partial - The passages say to check string polarity but don''t state how
    the alarm is detected.'
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r3
    h: 1c1583d51d6a
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r1
    h: d532e40e88ef
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Codes map to strings 1 to 16; service if the alarm persists.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r3
    h: 1c1583d51d6a
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r1
    h: d532e40e88ef
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r3
    h: 1c1583d51d6a
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r1
    h: d532e40e88ef
  review: drafted
---
