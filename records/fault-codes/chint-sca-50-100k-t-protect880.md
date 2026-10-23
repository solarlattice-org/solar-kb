---
id: fc:chint-sca-50-100k-t-protect880
type: FaultCode
name: CPS SCA50-100K-T Protect0880
aliases:
- Protect0880
- protect880
- CPS Protect0880
- MPPT6 CurrHigh
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0880
code_key: protect880
display_message: MPPT6 CurrHigh
vendor_severity: Protection
page: 143
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r4
    h: d781b0c7f29e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r4
    h: d781b0c7f29e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r4
    h: d781b0c7f29e
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear on its own within minutes; service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r4
    h: d781b0c7f29e
  review: drafted
  review_note: 'support check: partial - Row says observe 5 minutes for automatic elimination, implying
    auto-clear, but not that it is expected, and service if persists…'
---
