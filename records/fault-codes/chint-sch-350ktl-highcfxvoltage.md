---
id: fc:chint-sch-350ktl-highcfxvoltage
type: FaultCode
name: CPS SCH350KTL High CFx voltage
aliases:
- High CFx voltage
- highcfxvoltage
- CPS High CFx voltage
- x=1, 2…30
category: Inverters
make: chint
make_name: CPS
model_family: sch-350ktl
family_name: CPS SCH350KTL-DO/US-800
code: High CFx voltage
code_key: highcfxvoltage
display_message: x=1, 2…30
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r8
    h: 896c26094d2a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: Listed in the protection faults table.
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r8
    h: 896c26094d2a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34
    h: 05a4f42b1d19
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: sec=7.2.2
    h: 2c8a3dd026dc
  review: drafted
  review_note: 'support check: partial - The row appears in the Protection Faults table, but ''Fault''
    class is implied by the table, not stated directly.'
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: A protection fault stops the inverter until it is restarted.
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r8
    h: 896c26094d2a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: sec=7.2.2
    h: 2c8a3dd026dc
  review: drafted
  review_note: 'support check: partial - Requires power cycle implying stop, but passages don''t explicitly
    say production stops.'
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle the inverter first; replace the inverter if the fault persists.
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r8
    h: 896c26094d2a
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r8
    h: 896c26094d2a
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if a restart does not clear the fault.
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r8
    h: 896c26094d2a
  review: drafted
---
