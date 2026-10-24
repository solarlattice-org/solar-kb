---
id: fc:sungrow-sg-cx-us-76
type: FaultCode
name: Sungrow SG-CX-US 076
aliases:
- '076'
- '76'
- Sungrow 076
- Device anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '076'
code_key: '76'
display_message: Device anomaly
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r8
    h: 07b2c8eb2e45
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r8
    h: 3831f14e4750
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r8
    h: 07b2c8eb2e45
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r8
    h: 3831f14e4750
  review: drafted
  review_note: 'support check: partial - Device anomaly maps loosely to internal device fault; plausible
    but generic.'
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r8
    h: 07b2c8eb2e45
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r8
    h: 3831f14e4750
  review: drafted
  review_note: 'support check: partial - Row says device anomaly requiring restart/service, fault class
    implied but not explicit.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: First wait for self-recovery; then power cycle restart; then manufacturer service if persistent.
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r8
    h: 3831f14e4750
  review: drafted
  review_note: 'support check: partial - Waiting for recovery is stated but power cycle and service steps
    make auto-reset only partially accurate.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r8
    h: 3831f14e4750
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r8
    h: 07b2c8eb2e45
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r8
    h: 3831f14e4750
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:sungrow-sg-cx-us
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r8
    h: 07b2c8eb2e45
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=38.r8
    h: 3831f14e4750
  review: drafted
---
