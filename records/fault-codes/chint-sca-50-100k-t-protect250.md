---
id: fc:chint-sca-50-100k-t-protect250
type: FaultCode
name: CPS SCA50-100K-T Protect0250
aliases:
- Protect0250
- protect250
- CPS Protect0250
- Grid Volt Unbalance Abn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0250
code_key: protect250
display_message: Grid Volt Unbalance Abn
vendor_severity: Protection
page: 136
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r2
    h: 088e1c8952e5
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r2
    h: 088e1c8952e5
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:phase-imbalance
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r2
    h: 088e1c8952e5
  review: drafted
  review_note: 'support check: partial - Grid Voltage Unbalance corresponds to phase imbalance, but this
    is a loose mapping.'
- claim_id: c4
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r2
    h: 088e1c8952e5
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r2
    h: 088e1c8952e5
  review: drafted
---
