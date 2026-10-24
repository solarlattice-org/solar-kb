---
id: fc:chint-sca-50-100k-t-fault7040
type: FaultCode
name: CPS SCA50-100K-T Fault7040
aliases:
- Fault7040
- fault7040
- CPS Fault7040
- PIDOverhigh voltage Warn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault7040
code_key: fault7040
display_message: PIDOverhigh voltage Warn
vendor_severity: Fault
page: 150
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r3
    h: a6da8ac351ac
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r3
    h: a6da8ac351ac
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:pid-module-overvoltage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r3
    h: a6da8ac351ac
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear on its own within minutes; if it persists, contact service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r3
    h: a6da8ac351ac
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=68.r3
    h: a6da8ac351ac
  review: drafted
---
