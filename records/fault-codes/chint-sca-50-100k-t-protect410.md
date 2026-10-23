---
id: fc:chint-sca-50-100k-t-protect410
type: FaultCode
name: CPS SCA50-100K-T Protect0410
aliases:
- Protect0410
- protect410
- CPS Protect0410
- MPPT1RevCo nnect
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0410
code_key: protect410
display_message: MPPT1RevCo nnect
vendor_severity: Protection
page: 138
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=56.r2
    h: e534e7a8937b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=56.r2
    h: e534e7a8937b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=56.r2
    h: e534e7a8937b
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=56.r2
    h: e534e7a8937b
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=56.r2
    h: e534e7a8937b
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Correct the reversed string on MPPT1; contact service if the alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=56.r2
    h: e534e7a8937b
  review: drafted
---
