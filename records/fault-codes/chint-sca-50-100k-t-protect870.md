---
id: fc:chint-sca-50-100k-t-protect870
type: FaultCode
name: CPS SCA50-100K-T Protect0870
aliases:
- Protect0870
- protect870
- CPS Protect0870
- MPPT6RevCo nnect
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0870
code_key: protect870
display_message: MPPT6RevCo nnect
vendor_severity: Protection
page: 143
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r3
    h: eb8e9d5bff8c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r3
    h: eb8e9d5bff8c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r3
    h: eb8e9d5bff8c
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r3
    h: eb8e9d5bff8c
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r3
    h: eb8e9d5bff8c
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Correct reversed string connection after isolation; service if alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r3
    h: eb8e9d5bff8c
  review: drafted
---
