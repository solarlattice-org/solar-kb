---
id: fc:chint-sca-50-100k-t-protect850
type: FaultCode
name: CPS SCA50-100K-T Protect0850
aliases:
- Protect0850
- protect850
- CPS Protect0850
- MPPT5 CurrHigh
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0850
code_key: protect850
display_message: MPPT5 CurrHigh
vendor_severity: Protection
page: 143
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r1
    h: f15bb2d076f6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r1
    h: f15bb2d076f6
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r1
    h: f15bb2d076f6
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear on its own within minutes; service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r1
    h: f15bb2d076f6
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r1
    h: f15bb2d076f6
  review: drafted
---
