---
id: concept:reactive-power
type: Concept
name: Reactive power
aliases:
- kvar
- VAr
- Q
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:apparent-power
  note: Reactive power is the imaginary part of complex apparent power.
  cite:
  - src: src:man-sel-synchrowave-application-guides-testing-power-elements-in-the-sel-351s-sel-421-and-sel-700g
    loc: sec=h5
    h: 3fed7bd11260
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285
    loc: sec=h98
    h: 8a0d3daeea45
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:active-power
  note: Active power is the real part and reactive power the imaginary part of apparent power.
  cite:
  - src: src:man-sel-synchrowave-application-guides-testing-power-elements-in-the-sel-351s-sel-421-and-sel-700g
    loc: sec=h5
    h: 3fed7bd11260
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285
    loc: sec=h98
    h: 8a0d3daeea45
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:power-factor
  note: Changing the power factor setpoint changes the inverter's reactive power output.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.2.1
    h: 3eed03bbd339
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285
    loc: sec=h98
    h: 8a0d3daeea45
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c4
  rel: explains
  target: concept:voltage-rise
  note: Injecting reactive power raises voltage at the point of injection; absorbing it lowers voltage.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.2.1
    h: 3eed03bbd339
  review: drafted
- claim_id: c5
  rel: related_to
  target: func:constant-reactive-power
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.2.2.2
    h: 7f80beaf616f
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.5.2
    h: 6a065d90b256
  review: drafted
- claim_id: c6
  rel: related_to
  target: func:constant-power-factor
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.2.1
    h: 3eed03bbd339
  review: drafted
- claim_id: c7
  rel: related_to
  target: func:volt-var
  note: Volt-VAr curve points are set as reactive power percentages; one vendor limits output to 60% of
    nameplate.
  cite:
  - src: src:eq-equip-inverters-chint-modbus-maps-modbus-comm-user-manual
    loc: sec=h28
    h: b059d5d98e72
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=21.r14
    h: 90b18f19d4f5
  - src: src:eq-equip-inverters-chint-100-125-kw-inverter-cps-sch100-125ktl-do-us-600-480-manual-aug-2021-1
    loc: tbl=20.r14
    h: 90b18f19d4f5
  review: drafted
  review_note: 'support check: partial - Q(U) points as percentages and 60% nameplate limit are stated,
    but the 60% limit is not attributed to one vendor and curve-point wording is implicit.'
---
Reactive power, written Q and measured in VAr, is the imaginary part of complex apparent power, while active power in watts is the real part; together they form the power triangle. Injecting reactive power raises voltage at the connection point and absorbing it lowers voltage, so an inverter running at an absorbing power factor can offset the voltage rise caused by exporting real power. In constant VAr mode the inverter generates or absorbs a fixed amount of reactive power on command, much like utility switched capacitors; if the inverter's MVA rating would be exceeded, reactive output is capped without cutting active power. Large PV plants may be told by grid operators to absorb or supply reactive power at the grid connection point to help regulate voltage and stabilize the grid. Inverters and plant controllers expose reactive power as both a measured value and a setpoint, for example manual VAr setpoints, maximum reactive power limits, and Volt-VAr curve points set in percent under each grid code setting.
