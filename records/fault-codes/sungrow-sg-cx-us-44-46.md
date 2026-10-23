---
id: fc:sungrow-sg-cx-us-44-46
type: FaultCode
name: Sungrow SG-CX-US 044-046
aliases:
- 044-046
- 44-46
- Sungrow 044-046
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 044-046
code_key: 44-46
code_from: 44
code_to: 46
display_message: Device anomaly
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r2
    h: 34ef19307761
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r2
    h: b9e2ca61bd34
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r2
    h: 34ef19307761
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r2
    h: b9e2ca61bd34
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r2
    h: 34ef19307761
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r2
    h: b9e2ca61bd34
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: First wait for self-recovery; then AC/DC power cycle restart; then manufacturer service if persistent.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r2
    h: 34ef19307761
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r2
    h: b9e2ca61bd34
  review: drafted
  review_note: 'support check: partial - The wait-then-power-cycle-then-service sequence is stated, but
    the manual power cycle contradicts a pure auto-reset classification.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r2
    h: 34ef19307761
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r2
    h: b9e2ca61bd34
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r2
    h: b9e2ca61bd34
  review: drafted
---
