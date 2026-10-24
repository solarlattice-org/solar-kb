---
id: fc:chint-sch-350ktl-warn80
type: FaultCode
name: CPS SCH350KTL Warn0080
aliases:
- Warn0080
- warn80
- CPS Warn0080
- external heat exchanger fan error
category: Inverters
make: chint
make_name: CPS
model_family: sch-350ktl
family_name: CPS SCH350KTL-DO/US-800
code: Warn0080
code_key: warn80
display_message: external heat exchanger fan error
vendor_severity: Warning
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r5
    h: aca1ec83d74b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r5
    h: aca1ec83d74b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r5
    h: aca1ec83d74b
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:fan-failure
  note: Applies to the external heat exchanger fan.
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r5
    h: aca1ec83d74b
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r5
    h: aca1ec83d74b
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: The alarm is expected to clear by itself within about five minutes.
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r5
    h: aca1ec83d74b
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sch-350ktl
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r5
    h: aca1ec83d74b
  review: drafted
---
