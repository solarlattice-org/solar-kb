---
id: fc:chint-sca-50-100k-t-protect800
type: FaultCode
name: CPS SCA50-100K-T Protect0800
aliases:
- Protect0800
- protect800
- CPS Protect0800
- MPPT4 VoltHigh
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0800
code_key: protect800
display_message: MPPT4 VoltHigh
vendor_severity: Protection
page: 141
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r5
    h: 264274534a2b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r5
    h: 264274534a2b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r5
    h: 264274534a2b
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r5
    h: 264274534a2b
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r5
    h: 264274534a2b
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation if the alarm persists after voltage verification.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r5
    h: 264274534a2b
  review: drafted
---
