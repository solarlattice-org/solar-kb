---
id: fc:sungrow-sg-cx-us-71
type: FaultCode
name: Sungrow SG-CX-US 071
aliases:
- '071'
- '71'
- Sungrow 071
- AC-side SPD alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '071'
code_key: '71'
display_message: AC-side SPD alarm
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r6
    h: ffc90862e4ba
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r6
    h: ffc90862e4ba
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:spd-alarm
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r6
    h: ffc90862e4ba
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r6
    h: ffc90862e4ba
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:surge-protection-device
  note: AC-side surge protector.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r6
    h: ffc90862e4ba
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r6
    h: ffc90862e4ba
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:spd-replacement
  note: If inspection shows the SPD is exhausted.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r6
    h: ffc90862e4ba
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r6
    h: ffc90862e4ba
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:warning
  note: Labelled as an alarm.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r6
    h: ffc90862e4ba
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r6
    h: ffc90862e4ba
  review: drafted
  review_note: 'support check: partial - Labelled alarm, but no statement of device continuing operation;
    warning is implied only by label.'
- claim_id: c7
  rel: applies_to
  target: prod:sungrow-sg-cx-us
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r6
    h: ffc90862e4ba
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r6
    h: ffc90862e4ba
  review: drafted
---
