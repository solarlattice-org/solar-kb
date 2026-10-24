---
id: concept:cease-to-energize
type: Concept
name: Cease to energize
aliases:
- momentary cessation
category: Grid
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: req:ieee-1547-2018-4-5
  scope:
    standard: std:ieee-1547-2018
  quote: In the cease to energize state, the DER shall not deliver active power during steady-state or
    transient conditions.
  quote_source: IEEE 1547-2018 §4.5
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=4.5
    h: 0558bd01f897
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=4.r16
    h: 23d824c79f06
  review: drafted
- claim_id: c2
  rel: related_to
  target: std:ieee-1547-2018
  note: Defines the cease to energize state and the optional momentary cessation parameters.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=4.5
    h: 0558bd01f897
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h198
    h: 83456634f8d4
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=43.r2
    h: 79cd25c57bc0
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=10.6.11
    h: ded63491f0a8
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h108
    h: a44acf481535
  review: drafted
- claim_id: c3
  rel: related_to
  target: func:disable-permit-service
  scope:
    standard: std:ieee-1547-2018
  note: Setting Permit service to disabled directs the DER to cease to energize and trip.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=10.6.11
    h: ded63491f0a8
  review: drafted
- claim_id: c4
  rel: related_to
  target: func:voltage-ride-through
  scope:
    standard: std:ieee-1547-2018
  note: For Category III DER, voltage inside the momentary cessation region requires ceasing to energize
    without tripping, then restoring output.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h108
    h: a44acf481535
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=43.r2
    h: 79cd25c57bc0
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:ieee-1547-performance-categories
  note: Momentary cessation behavior is specified for Category III DER.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h108
    h: a44acf481535
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:area-eps
  note: Cease to energize may alternatively be met by disconnecting the Local EPS from the Area EPS; the
    Area EPS operator may request the remaining reactive susceptance.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=4.5
    h: 0558bd01f897
  - src: src:eq-equip-inverters-chint-cps-lost-application-note-012126
    loc: sec=4.5
    h: 03d015c97643
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:local-electric-power-system
  note: Reactive exchange limits depend on aggregate DER rating of the Local EPS; the DER may keep supplying
    a disconnected portion of the Local EPS.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=4.5
    h: 0558bd01f897
  - src: src:eq-equip-inverters-chint-cps-lost-application-note-012126
    loc: sec=4.5
    h: 03d015c97643
  review: drafted
- claim_id: c8
  rel: related_to
  target: method:cease-to-energize-test
  scope:
    standard: std:ieee-1547-2003
  note: Operate a load interrupting device, verify output terminals de-energize and do not reconnect for
    the required delay; test each phase individually.
  cite:
  - src: src:std-standards-ieee-ieee1547
    loc: sec=5.4.2
    h: 1992054d53f1
  - src: src:std-manuals-utility-first-energy-corp-commissioning-test-requirements
    loc: tbl=6
    h: 1992054d53f1
  review: drafted
  review_note: 'support check: partial - The test content matches, but the passages do not show it belongs
    to IEEE 1547-2003; the references (4.1.4, 4.2.x, 4.4.1) are not tied to the edition in the passages.'
- claim_id: c9
  rel: related_to
  target: comp:battery-storage
  note: An energy storage system that ceases to energize may continue charging; some battery systems report
    a cease-to-energize status flag over Modbus.
  cite:
  - src: src:ref-standards-ieee-ieee-1547-2018-highlights
    loc: sec=h33
    h: a83696c99ca7
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=119.r23
    h: 1332337963c2
  review: drafted
---
Cease to energize is a DER state in which the unit delivers no active power at its point of connection, whether conditions are steady or transient. During this state the DER may still import power and exchange reactive power, but only to keep its housekeeping and auxiliary loads supplied, and any reactive exchange must come solely from passive devices. The requirement can also be met by disconnecting the Local EPS, or the part of it that holds the DER, from the Area EPS, and the DER may keep supplying that isolated part. Momentary cessation is a related ride-through behavior: for Category III DER, when voltage falls into the momentary cessation region, the DER ceases to energize without tripping and then restores its output. Setting Permit service to disabled directs a DER to cease to energize and trip, and an energy storage system that has ceased to energize may keep charging. In the field, the function is verified by operating a load interrupting device, confirming that the output terminals are de-energized and do not reconnect before the required delay, and repeating this on each phase.

<!-- review notes
- sentence 2: support check: partial - Import of active power and reactive exchange is permitted only for housekeeping and auxiliary loads, and reactive exchange must result from passive devices, but the passages do not limit the passive-only requirement to those loads; they also set the 10%/3% limits.
-->
