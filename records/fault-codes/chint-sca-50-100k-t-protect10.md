---
id: fc:chint-sca-50-100k-t-protect10
type: FaultCode
name: CPS SCA50-100K-T Protect0010
aliases:
- Protect0010
- protect10
- CPS Protect0010
- Power Abn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0010
code_key: protect10
display_message: Power Abn
vendor_severity: Protection
page: 130
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48.r2
    h: 4ef914fab821
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48.r2
    h: 4ef914fab821
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48.r2
    h: 4ef914fab821
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; contact service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48.r2
    h: 4ef914fab821
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=48.r2
    h: 4ef914fab821
  review: drafted
---
