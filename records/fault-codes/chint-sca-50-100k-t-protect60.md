---
id: fc:chint-sca-50-100k-t-protect60
type: FaultCode
name: CPS SCA50-100K-T Protect0060
aliases:
- Protect0060
- protect60
- CPS Protect0060
- MPPT1 CurrHigh
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0060
code_key: protect60
display_message: MPPT1 CurrHigh
vendor_severity: Protection
page: 131
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r2
    h: 487bc46b4a4d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r2
    h: 487bc46b4a4d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r2
    h: 487bc46b4a4d
  review: drafted
  review_note: 'support check: partial - The code is MPPT1 Current High, which implies DC overcurrent,
    but the passage only suggests checking PV polarity.'
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r2
    h: 487bc46b4a4d
  review: drafted
  review_note: 'support check: partial - The passage mentions checking the PV input polarity, so the PV
    input is implied, but the PV array is not named.'
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r2
    h: 487bc46b4a4d
  review: drafted
  review_note: 'support check: partial - The passage says to check the PV input polarity, but it does
    not say the fault is detected by polarity measurement.'
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r2
    h: 487bc46b4a4d
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r2
    h: 487bc46b4a4d
  review: drafted
---
