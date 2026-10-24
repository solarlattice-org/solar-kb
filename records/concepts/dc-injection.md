---
id: concept:dc-injection
type: Concept
name: DC injection
aliases:
- DC component in grid current
- DC current injection
- DC injection current
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: std:firstenergy-commissioning-test-requirements
  note: Commissioning requirement 4.3.1 repeats the 0.5% of full rated output current DC injection limit
    at the point of DR connection.
  cite:
  - src: src:std-manuals-utility-first-energy-corp-commissioning-test-requirements
    loc: tbl=4.r1
    h: 23d0578b3ad4
  - src: src:std-manuals-utility-first-energy-corp-commissioning-test-requirements
    loc: tbl=4
    h: d89458914140
  review: drafted
- claim_id: c2
  rel: related_to
  target: method:dc-injection-measurement
  note: A conformance test checks that an inverter-based system stays within the IEEE 1547 DC injection
    limit.
  cite:
  - src: src:ref-standards-ieee-ieee-1541-1-overview
    loc: sec=h23
    h: 9b7b343c25fa
  review: drafted
- claim_id: c3
  rel: related_to
  target: func:dc-injection-limitation
  note: Inverters provide settable DC injection protection, e.g. enable flags, trip value and trip time.
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=26.r7
    h: 817b65631b5c
  - src: src:eq-equip-inverters-chint-100-125-kw-inverter-cps-sch100-125ktl-do-us-600-480-manual-aug-2021-1
    loc: tbl=25.r6
    h: 1a0d21f378e8
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=44.r1
    h: d528d200b666
  - src: src:eq-equip-inverters-delta-dc1-controller-20191024-dc1
    loc: sec=h87
    h: 2c77f11e479b
  review: drafted
- claim_id: c4
  rel: related_to
  target: symptom:dc-injection-high
  note: Delta inverters report per-phase and total DC injection faults (F01-F04).
  cite:
  - src: src:eq-equip-inverters-delta-delta-modbus-definition-ul-v01-10-20190523
    loc: tbl=54.r3
    h: 956bc28188dc
  - src: src:eq-equip-inverters-delta-delta-modbus-definition-ul-v01-10-20190523
    loc: tbl=54.r2
    h: 5348373bfff3
  - src: src:eq-equip-inverters-delta-delta-modbus-definition-ul-v01-10-20190523
    loc: tbl=54.r1
    h: 0fa294d978a9
  review: drafted
---
DC injection is direct current that an inverter puts into the AC grid along with its normal AC output. Inverter datasheets usually list a DC current injection figure, for example below 0.5% of nominal output current on Sungrow central and string inverters. Many inverters include settable DC injection protection with a mode, a trip value and a trip time, and these can be turned on or off for each grid code. When the limit is exceeded the inverter logs a DC injection fault, which may be reported for each phase or as a total. Conformance testing checks the inverter against the IEEE 1547 limit, so check the DC injection settings during commissioning against the grid code that applies.

<!-- review notes
- sentence 1: support check: partial - Passages give only the limit on DC current injected, not a definition of DC injection as direct current added to the AC output.
- sentence 2: support check: partial - Specific Sungrow figures below 0.5% are shown, but 'usually listed' across inverter datasheets and 'central and string' are not established.
- sentence 3: support check: partial - Mode/trip value/trip time and per-grid-code enable flags are shown, but 'many inverters' is not established and the per-grid-code columns just list default values, not independent toggling.
- sentence 4: support check: partial - Per-phase and total DC injection faults exist, but the passages do not say they are logged when the limit is exceeded.
- sentence 5: support check: partial - IEEE 1547 conformance test is stated, but the commissioning advice to check settings against the applicable grid code is not in the passages.
-->
