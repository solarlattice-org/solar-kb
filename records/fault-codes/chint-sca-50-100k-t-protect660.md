---
id: fc:chint-sca-50-100k-t-protect660
type: FaultCode
name: CPS SCA50-100K-T Protect0660
aliases:
- Protect0660
- protect660
- CPS Protect0660
- Arc Board Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0660
code_key: protect660
display_message: Arc Board Fault
vendor_severity: Protection
page: 140
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r1
    h: 03dfc1d11f10
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r1
    h: 03dfc1d11f10
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-detector-failure
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r1
    h: 03dfc1d11f10
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r1
    h: 03dfc1d11f10
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r1
    h: 03dfc1d11f10
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation if the alarm persists after restart.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r1
    h: 03dfc1d11f10
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle AC and DC first; service if the alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r1
    h: 03dfc1d11f10
  review: drafted
---
