---
id: fc:sungrow-sg-cx-us-53-56
type: FaultCode
name: Sungrow SG-CX-US 053-056
aliases:
- 053-056
- 53-56
- Sungrow 053-056
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 053-056
code_key: 53-56
code_from: 53
code_to: 56
display_message: Device anomaly
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r4
    h: 1e315c4e9ee2
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r4
    h: 1e315c4e9ee2
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r4
    h: 1e315c4e9ee2
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: First wait for self-recovery; then AC/DC power cycle restart; then manufacturer service if persistent.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r4
    h: 1e315c4e9ee2
  review: drafted
  review_note: 'support check: partial - The sequence is stated, but the manual power cycle means auto-reset
    is only partly supported.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r4
    h: 1e315c4e9ee2
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r4
    h: 1e315c4e9ee2
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r4
    h: 1e315c4e9ee2
  review: drafted
---
