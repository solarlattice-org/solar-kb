---
id: fc:chint-sca-50-100k-t-fault7010
type: FaultCode
name: CPS SCA50-100K-T Fault7010
aliases:
- Fault7010
- fault7010
- CPS Fault7010
- PID voltage stability alarm
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault7010
code_key: fault7010
display_message: PID voltage stability alarm
vendor_severity: Fault
page: 150
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r6
    h: 3af18e90a362
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r6
    h: 3af18e90a362
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:pid-voltage-instability
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r6
    h: 3af18e90a362
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear on its own within minutes; if it persists, contact service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r6
    h: 3af18e90a362
  review: drafted
---
