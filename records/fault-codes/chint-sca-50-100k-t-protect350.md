---
id: fc:chint-sca-50-100k-t-protect350
type: FaultCode
name: CPS SCA50-100K-T Protect0350
aliases:
- Protect0350
- protect350
- CPS Protect0350
- MPPT2 RevConnect
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0350
code_key: protect350
display_message: MPPT2 RevConnect
vendor_severity: Protection
page: 137
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r2
    h: f2f956f03110
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r2
    h: f2f956f03110
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r2
    h: f2f956f03110
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r2
    h: f2f956f03110
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r2
    h: f2f956f03110
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Correct the reversed string on MPPT2; contact service if the alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r2
    h: f2f956f03110
  review: drafted
---
