---
id: fc:chint-sca-50-100k-t-protect790
type: FaultCode
name: CPS SCA50-100K-T Protect0790
aliases:
- Protect0790
- protect790
- CPS Protect0790
- Zero-to-ground voltage anomaly protection
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0790
code_key: protect790
display_message: Zero-to-ground voltage anomaly protection
vendor_severity: Protection
page: 141
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r4
    h: 77a352ec9d2e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r4
    h: 77a352ec9d2e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:neutral-ground-voltage-abnormal
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r4
    h: 77a352ec9d2e
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r4
    h: 77a352ec9d2e
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation if the alarm persists after checking the grid connection.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r4
    h: 77a352ec9d2e
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r4
    h: 77a352ec9d2e
  review: drafted
---
