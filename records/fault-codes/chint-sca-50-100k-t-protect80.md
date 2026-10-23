---
id: fc:chint-sca-50-100k-t-protect80
type: FaultCode
name: CPS SCA50-100K-T Protect0080
aliases:
- Protect0080
- protect80
- CPS Protect0080
- Grid Phase Vrms OutLim
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0080
code_key: protect80
display_message: Grid Phase Vrms OutLim
vendor_severity: Protection
page: 131
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r4
    h: c622dd8f1082
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r4
    h: c622dd8f1082
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-voltage-out-of-range
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r4
    h: c622dd8f1082
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=49.r4
    h: c622dd8f1082
  review: drafted
---
