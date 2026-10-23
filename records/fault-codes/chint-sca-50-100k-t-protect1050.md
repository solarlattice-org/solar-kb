---
id: fc:chint-sca-50-100k-t-protect1050
type: FaultCode
name: CPS SCA50-100K-T Protect1050
aliases:
- Protect1050
- protect1050
- CPS Protect1050
- Core Hardware Ver Abn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect1050
code_key: protect1050
display_message: Core Hardware Ver Abn
vendor_severity: Protection
page: 144
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r2
    h: c09a497e44ef
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r2
    h: c09a497e44ef
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r2
    h: c09a497e44ef
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r2
    h: c09a497e44ef
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle AC and DC first; service if alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r2
    h: c09a497e44ef
  review: drafted
---
