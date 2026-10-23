---
id: fc:chint-sca-50-100k-t-fault5020
type: FaultCode
name: CPS SCA50-100K-T Fault5020
aliases:
- Fault5020
- fault5020
- CPS Fault5020
- AC Bulkhead Connector Temperature Sensor Abnormal
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault5020
code_key: fault5020
display_message: AC Bulkhead Connector Temperature Sensor Abnormal
vendor_severity: Fault
page: 148
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r6
    h: f12501e70c0e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r6
    h: f12501e70c0e
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r6
    h: f12501e70c0e
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-connector
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r6
    h: f12501e70c0e
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r6
    h: f12501e70c0e
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Connection check first; service if the alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r6
    h: f12501e70c0e
  review: drafted
---
