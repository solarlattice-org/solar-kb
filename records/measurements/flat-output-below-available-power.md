---
id: meas:flat-output-below-available-power
type: Measurement
name: Flat output below available power
signals:
- point: model_103.W
  unit: unit:W
  pattern: flat or controlled level below irradiance-supported available power
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: irradiance would support higher output
- point: model_103.DCV
  unit: unit:V
  pattern: May move away from the MPP voltage while output is held down
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 0.05
    unit: unit:PERCENT
  conditions: Annual energy lost to inverter power limitation in one example PV system, estimated by PR
    extrapolation from measured data (PR 200-900 W/m² vs 900-1200 W/m²)
  note: Here the limitation shows up as output that stops rising above about 897 W/kWp. This is inverter
    clipping, not curtailment.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2.2
    h: baaa36bbb1c3
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 0.03
    unit: unit:PERCENT
  conditions: Simulated inverter limitation loss for the same example system at a PV-to-inverter ratio
    of 1.12
  note: This is a model estimate, not a measurement.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2.2
    h: baaa36bbb1c3
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions)
---
The signature is a production trace that stays flat, or at a controlled level, below the power the measured irradiance would support. Inverter and tracker availability can look normal while this happens. It is easy to log the loss as underperformance unless setpoints and dispatch signals are checked. Grid curtailment losses produce this pattern. The limit can come from grid operator dispatch, an interconnection constraint, a plant controller command, a response to negative prices, or a site export cap. To confirm it, compare plant setpoints, inverter active power limits, operator dispatch, meter output, irradiance-based available power, battery charging behavior and curtailment flags. Inverter clipping looks similar: output stops rising with irradiance once the inverter reaches its maximum output or another limit. Inverter voltage floor losses can also look like clipping or general underperformance. To tell them apart, review DC voltage, AC voltage, reactive power and the Vmp derived from IV curves together. Inverters can carry an active power limit set as a percentage of rated or nameplate power. Some also report the theoretically available power, which can be compared with actual output.

<!-- review notes
- sentence 7: support check: partial - Percent-of-rated power limit is supported, and one passage lists theoretically available power output, but 'some also report' and comparison with actual output are not stated.
-->
