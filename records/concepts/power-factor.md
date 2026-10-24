---
id: concept:power-factor
type: Concept
name: Power factor
aliases:
- PF
- cos phi
- leading power factor
- lagging power factor
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:apparent-power
  note: Power factor is the ratio of active power to apparent power (kW / kVA).
  cite:
  - src: src:ref-reference-short-circuit-calcs-bussman-sht-ckt-curr-calcs
    loc: tbl=15.r9
    h: bc34e91cc30b
  - src: src:eq-equip-meters-veris-e51cx-full-i0e2
    loc: tbl=20.r24
    h: ac22841b3ba5
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285
    loc: sec=h98
    h: 8a0d3daeea45
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:active-power
  note: Active power is the numerator of the power factor ratio.
  cite:
  - src: src:ref-reference-short-circuit-calcs-bussman-sht-ckt-curr-calcs
    loc: tbl=15.r9
    h: bc34e91cc30b
  - src: src:eq-equip-meters-veris-e51cx-full-i0e2
    loc: tbl=20.r24
    h: ac22841b3ba5
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285
    loc: sec=h98
    h: 8a0d3daeea45
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:reactive-power
  note: Changing the power factor setpoint changes the inverter's reactive power output.
  cite:
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285
    loc: sec=h98
    h: 8a0d3daeea45
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.2.1
    h: 3eed03bbd339
  review: drafted
- claim_id: c4
  rel: related_to
  target: func:constant-power-factor
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.2.1
    h: 3eed03bbd339
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c5
  rel: related_to
  target: func:watt-power-factor
  note: In PF(P) curve mode the power factor follows the active power output.
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: sec=h89
    h: a3ffee754d58
  - src: src:eq-equip-inverters-chint-100-125-kw-inverter-cps-sch100-125ktl-do-us-600-480-manual-aug-2021-1
    loc: sec=h96
    h: a3ffee754d58
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=26.r3
    h: e90f2a4c3a12
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:voltage-rise
  note: Running PV at an absorbing power factor helps offset the voltage rise caused by real power injection.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.2.1
    h: 3eed03bbd339
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
Power factor is the cosine of the angle by which phase current leads or lags phase voltage in an AC circuit. It equals 1.0 when power flows into a purely resistive load. It can also be written as active power divided by apparent power, that is kW over kVA. Meters and protective relays report power factor for each phase and for all three phases together, with a flag showing whether it is leading or lagging. Inverter datasheets such as the Fronius Symo list an adjustable power factor range from 0 to 1, inductive or capacitive. Changing an inverter's power factor setpoint changes its reactive power output. Running PV at an absorbing power factor helps hold down the voltage rise that comes with more real power export. Other control options are power factor scheduling and the PF(P) curve mode, where the power factor changes as the active power changes. If the operating range is limited to 0.85 inductive through 0.85 capacitive, the inverter's MVA rating has to be based on the plant's maximum MW output at 0.85 power factor.

<!-- review notes
- sentence 3: support check: partial - The passages show per-phase and three-phase power factor with leading/lagging, and a lead/lag indication point, but they never say meters and protective relays report it, and a flag is only partly shown.
- sentence 4: support check: partial - The passages show 0-1 ind./cap., but they don't name the Fronius Symo or call the range adjustable (the footnote 3 is not given).
- sentence 4: review: partial - The Fronius Symo manual rows give '0-1 ind./cap.', but the passages do not say the range is adjustable (the footnote 3 is not quoted) and the source is an operating manual, not a datasheet.
-->
