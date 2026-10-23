---
id: fc:sungrow-sg-cx-us-72
type: FaultCode
name: Sungrow SG-CX-US 072
aliases:
- '072'
- '72'
- Sungrow 072
- DC-side SPD alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '072'
code_key: '72'
display_message: DC-side SPD alarm
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r7
    h: d170ba4e2b2e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:spd-alarm
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r7
    h: d170ba4e2b2e
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:surge-protection-device
  note: DC-side surge protector.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r7
    h: d170ba4e2b2e
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  note: Labelled as an alarm.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r7
    h: d170ba4e2b2e
  review: drafted
  review_note: 'support check: partial - Labelled alarm; warning class only implied by label.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: First wait for self-recovery; otherwise AC/DC power cycle restart.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  review: drafted
  review_note: 'support check: partial - Wait for self-recovery is stated, then manual power cycle; auto-reset
    is only the first step.'
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  review: drafted
---
