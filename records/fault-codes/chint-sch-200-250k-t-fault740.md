---
id: fc:chint-sch-200-250k-t-fault740
type: FaultCode
name: CPS SCH200-250K-T Fault0740
aliases:
- Fault0740
- fault740
- CPS Fault0740
- CPLD fault
category: Inverters
make: chint
make_name: CPS
model_family: sch-200-250k-t
family_name: CPS SCH200K-T-US-480 / SCH250K-T-US-600
code: Fault0740
code_key: fault740
display_message: CPLD fault
vendor_severity: Fault
page: 107
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r3
    h: 0c654a137519
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r3
    h: 0c654a137519
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r3
    h: 0c654a137519
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Hardware fault needing an inverter power cycle implies production has stopped
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r3
    h: 0c654a137519
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; replace the inverter if the fault persists
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r3
    h: 0c654a137519
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r3
    h: 0c654a137519
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r3
    h: 0c654a137519
  review: drafted
---
