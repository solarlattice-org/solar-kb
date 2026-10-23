---
id: fc:chint-sca-50-100k-t-warn10
type: FaultCode
name: CPS SCA50-100K-T Warn0010
aliases:
- Warn0010
- warn10
- CPS Warn0010
- In Fan Abn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Warn0010
code_key: warn10
display_message: In Fan Abn
vendor_severity: Warning
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=46.r3
    h: 5e4100f1c608
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=46.r3
    h: 5e4100f1c608
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=46.r3
    h: 5e4100f1c608
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=46.r3
    h: 5e4100f1c608
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=46.r3
    h: 5e4100f1c608
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=46.r3
    h: 5e4100f1c608
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Observe for automatic clearing; then restart, then contact service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=46.r3
    h: 5e4100f1c608
  review: drafted
---
