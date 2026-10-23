---
id: fc:chint-sca-50-100k-t-protect270
type: FaultCode
name: CPS SCA50-100K-T Protect0270
aliases:
- Protect0270
- protect270
- CPS Protect0270
- Inv Curr Unbalance Abn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0270
code_key: protect270
display_message: Inv Curr Unbalance Abn
vendor_severity: Protection
page: 136
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r3
    h: 2bf2a273c8a9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r3
    h: 2bf2a273c8a9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:phase-imbalance
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r3
    h: 2bf2a273c8a9
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Observe first; then restart; persistent case needs service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r3
    h: 2bf2a273c8a9
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r3
    h: 2bf2a273c8a9
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r3
    h: 2bf2a273c8a9
  review: drafted
---
