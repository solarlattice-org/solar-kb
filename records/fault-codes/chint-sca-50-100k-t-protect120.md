---
id: fc:chint-sca-50-100k-t-protect120
type: FaultCode
name: CPS SCA50-100K-T Protect0120
aliases:
- Protect0120
- protect120
- CPS Protect0120
- Grid Phase Abn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0120
code_key: protect120
display_message: Grid Phase Abn
vendor_severity: Protection
page: 132
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=50.r3
    h: 3214e8e06ca9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=50.r3
    h: 3214e8e06ca9
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:auto-reset
  note: Observe first; then power-cycle, then contact service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=50.r3
    h: 3214e8e06ca9
  review: drafted
---
