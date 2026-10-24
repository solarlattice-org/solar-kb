---
id: fc:chint-sca-25ktl-208-fault130
type: FaultCode
name: CPS SCA25KTL-208 Fault0130
aliases:
- Fault0130
- fault130
- CPS Fault0130
- Bus over total voltage
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: Fault0130
code_key: fault130
display_message: Bus over total voltage
vendor_severity: Fault
page: 129
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r2
    h: 23e93731d517
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r2
    h: 23e93731d517
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  note: One manual labels this code as a grid relay fault instead.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r2
    h: 23e93731d517
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=61.r1
    h: 5570ca8fd045
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r1
    h: a87d89b7e17a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r1
    h: 3ffbc9c492c2
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r1
    h: a87d89b7e17a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r1
    h: e6b83208a466
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r2
    h: 23e93731d517
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=61.r1
    h: 5570ca8fd045
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r1
    h: a87d89b7e17a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r1
    h: 3ffbc9c492c2
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r1
    h: 170cc36d5adc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r1
    h: a87d89b7e17a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r1
    h: e6b83208a466
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if a power cycle does not clear the fault.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r2
    h: 23e93731d517
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=61.r1
    h: 5570ca8fd045
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r1
    h: a87d89b7e17a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r1
    h: 3ffbc9c492c2
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r1
    h: 170cc36d5adc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r1
    h: a87d89b7e17a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r1
    h: e6b83208a466
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; replace inverter if the fault persists.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r2
    h: 23e93731d517
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=61.r1
    h: 5570ca8fd045
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=38.r1
    h: a87d89b7e17a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=34.r1
    h: 3ffbc9c492c2
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=44.r1
    h: 170cc36d5adc
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=29.r1
    h: a87d89b7e17a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=36.r1
    h: e6b83208a466
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-25ktl-208
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=54.r2
    h: 23e93731d517
  review: drafted
---
