---
id: fc:chint-sca-50-100k-t-protect440
type: FaultCode
name: CPS SCA50-100K-T Protect0440
aliases:
- Protect0440
- protect440
- CPS Protect0440
- MPPT3 VoltHigh
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0440
code_key: protect440
display_message: MPPT3 VoltHigh
vendor_severity: Protection
page: 139
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r1
    h: 626db0c0bece
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r1
    h: 626db0c0bece
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r1
    h: 626db0c0bece
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r1
    h: 626db0c0bece
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Open-circuit PV voltage must stay below 1000 V; contact service if the alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r1
    h: 626db0c0bece
  review: drafted
  review_note: 'support check: partial - Passage says to measure DC terminal voltage and keep open-circuit
    PV voltage under 1000 V, but ''detected by'' DC voltage…'
- claim_id: c6
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r1
    h: 626db0c0bece
  review: drafted
---
