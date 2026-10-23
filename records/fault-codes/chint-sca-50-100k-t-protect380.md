---
id: fc:chint-sca-50-100k-t-protect380
type: FaultCode
name: CPS SCA50-100K-T Protect0380
aliases:
- Protect0380
- protect380
- CPS Protect0380
- PV abnormal connection failure
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0380
code_key: protect380
display_message: PV abnormal connection failure
vendor_severity: Protection
page: 137
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r5
    h: ccfd925a7cc1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r5
    h: ccfd925a7cc1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:pv-input-abnormal
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r5
    h: ccfd925a7cc1
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r5
    h: ccfd925a7cc1
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Contact service if the alarm persists after checking.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r5
    h: ccfd925a7cc1
  review: drafted
---
