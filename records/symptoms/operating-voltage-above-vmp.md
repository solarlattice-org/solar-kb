---
id: symptom:operating-voltage-above-vmp
type: Symptom
name: Operating voltage above Vmp
aliases:
- voltage flooring
claims:
- claim_id: c1
  rel: observed_as
  target: meas:operating-voltage-above-iv-vmp
  note: Voltage flooring is supported when the measured operating voltage stays above the Vmp from an
    IV curve or a temperature-corrected model, and operating power stays below IV-derived Pmp.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:dc-voltage-pinned-at-minimum
  note: Look for intervals where inverter DC voltage sits at or near the minimum operating threshold while
    output is lower than irradiance would support.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:high-reactive-power-during-floor
  note: High reactive power demand or AC voltage hysteresis can shift the effective inverter operating
    window. Check these at the same timestamps.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h4
    h: 7023830f6e10
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: drafted
- claim_id: c4
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring in summer 2025 at a 100 MW PV plant in
    California (field poster)
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
---
When this happens, the inverter keeps the array at a DC voltage above the array's true maximum power point voltage, so it harvests less than the available DC power. It is the typical sign of inverter voltage floor losses: array Vmp has dropped below the inverter's minimum DC input voltage, which can be caused by high module temperature, degraded modules, tight string design margin or reactive power operation. Watch for it during hot periods, because module voltage falls as cell temperature rises. The inverter stays online and irradiance looks normal. Start by finding intervals where the inverter DC voltage is at or close to its minimum threshold while output is lower than irradiance would support. First rule out outages, curtailment, clipping, soiling and sensor faults. To confirm it, compare the operating voltage with an independent Vmp estimate from in-situ or string IV sweeps or a temperature-corrected module model. Voltage flooring is supported when the operating voltage stays above Vmp and the power stays below Pmp. Do not mistake it for clipping. Clipping is a power ceiling, while this is an MPPT limit set by the DC voltage window. Also check AC voltage and reactive power dispatch at the same timestamps, because the root cause may be plant voltage control, transformer tap position or inverter settings rather than module degradation.
