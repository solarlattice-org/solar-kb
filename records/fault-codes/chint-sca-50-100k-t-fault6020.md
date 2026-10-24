---
id: fc:chint-sca-50-100k-t-fault6020
type: FaultCode
name: CPS SCA50-100K-T Fault6020
aliases:
- Fault6020
- fault6020
- CPS Fault6020
- DC Bulkhead Connector OverTempera tureFault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault6020
code_key: fault6020
display_message: DC Bulkhead Connector OverTempera tureFault
vendor_severity: Fault
page: 149
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r7
    h: 64323385ffdc
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r7
    h: 64323385ffdc
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:connector-overtemperature
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r7
    h: 64323385ffdc
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r7
    h: 64323385ffdc
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the alarm persists after the observation period.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r7
    h: 64323385ffdc
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear by itself within minutes; service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r7
    h: 64323385ffdc
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r7
    h: 64323385ffdc
  review: drafted
---
