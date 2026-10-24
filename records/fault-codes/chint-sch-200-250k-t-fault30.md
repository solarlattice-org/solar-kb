---
id: fc:chint-sch-200-250k-t-fault30
type: FaultCode
name: CPS SCH200-250K-T Fault0030
aliases:
- Fault0030
- fault30
- CPS Fault0030
- Bus over voltage hardware
category: Inverters
make: chint
make_name: CPS
model_family: sch-200-250k-t
family_name: CPS SCH200K-T-US-480 / SCH250K-T-US-600
code: Fault0030
code_key: fault30
display_message: Bus over voltage hardware
vendor_severity: Fault
page: 107
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r4
    h: 89bcee8573d1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r4
    h: 89bcee8573d1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r4
    h: 89bcee8573d1
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Hardware fault needing an inverter power cycle implies production has stopped
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r4
    h: 89bcee8573d1
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; replace the inverter if the fault persists
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r4
    h: 89bcee8573d1
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r4
    h: 89bcee8573d1
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r4
    h: 89bcee8573d1
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:chint-sch-200-250k-t
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r4
    h: 89bcee8573d1
  review: drafted
---
