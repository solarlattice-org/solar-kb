---
id: fc:chint-sca-50-100k-t-protect1070
type: FaultCode
name: CPS SCA50-100K-T Protect1070
aliases:
- Protect1070
- protect1070
- CPS Protect1070
- SPI Comm Abn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect1070
code_key: protect1070
display_message: SPI Comm Abn
vendor_severity: Protection
page: 144
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r1
    h: '396717034e15'
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r1
    h: '396717034e15'
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r1
    h: '396717034e15'
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Verify grid connection first; service if alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r1
    h: '396717034e15'
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r1
    h: '396717034e15'
  review: drafted
---
