---
id: fc:chint-sca-50-100k-t-protect40
type: FaultCode
name: CPS SCA50-100K-T Protect0040
aliases:
- Protect0040
- protect40
- CPS Protect0040
- Inverter Soft start time out
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0040
code_key: protect40
display_message: Inverter Soft start time out
vendor_severity: Protection
page: 131
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r1
    h: 5e500bf557e7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r1
    h: 5e500bf557e7
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:auto-reset
  note: Observe first; then power-cycle, then contact service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r1
    h: 5e500bf557e7
  review: drafted
---
