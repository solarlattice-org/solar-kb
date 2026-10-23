---
id: fc:chint-sca-50-100k-t-fault5030
type: FaultCode
name: CPS SCA50-100K-T Fault5030
aliases:
- Fault5030
- fault5030
- CPS Fault5030
- DC Bulkhead Connector Temperature Sensor Abnormal
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault5030
code_key: fault5030
display_message: DC Bulkhead Connector Temperature Sensor Abnormal
vendor_severity: Fault
page: 148
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r5
    h: 0c59f97bb8e0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r5
    h: 0c59f97bb8e0
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r5
    h: 0c59f97bb8e0
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r5
    h: 0c59f97bb8e0
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r5
    h: 0c59f97bb8e0
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Connection check first; service if the alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r5
    h: 0c59f97bb8e0
  review: drafted
---
