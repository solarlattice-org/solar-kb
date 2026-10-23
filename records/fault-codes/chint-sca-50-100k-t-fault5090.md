---
id: fc:chint-sca-50-100k-t-fault5090
type: FaultCode
name: CPS SCA50-100K-T Fault5090
aliases:
- Fault5090
- fault5090
- CPS Fault5090
- DC Pair Plug Terminal Warning
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault5090
code_key: fault5090
display_message: DC Pair Plug Terminal Warning
vendor_severity: Fault
page: 147
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r3
    h: 91196e19e720
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r3
    h: 91196e19e720
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:connector-abnormal
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r3
    h: 91196e19e720
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r3
    h: 91196e19e720
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r3
    h: 91196e19e720
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=65.r3
    h: 91196e19e720
  review: drafted
---
