---
id: fc:sungrow-sg250hx-564-579
type: FaultCode
name: Sungrow SG250HX 564-579
aliases:
- 564-579
- Sungrow 564-579
- PV Reverse Con-nection Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: 564-579
code_key: 564-579
code_from: 564
code_to: 579
display_message: PV Reverse Con-nection Alarm
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r3
    h: 1c1583d51d6a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r3
    h: 1c1583d51d6a
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r3
    h: 1c1583d51d6a
  review: drafted
  review_note: 'support check: partial - The passage gives no detection method, only a check of the string
    polarity.'
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r3
    h: 1c1583d51d6a
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Codes map to strings 17 to 32; service if the alarm persists.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r3
    h: 1c1583d51d6a
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=40.r3
    h: 1c1583d51d6a
  review: drafted
---
