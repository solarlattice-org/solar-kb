---
id: symptom:dc-voltage-at-minimum
type: Symptom
name: DC voltage pinned at minimum
aliases:
- voltage flooring
- voltage-floor events
claims:
- claim_id: c1
  rel: observed_as
  target: meas:dc-voltage-pinned-at-minimum
  note: Rule out outages, curtailment, clipping, soiling and sensor faults before blaming the voltage
    floor.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:operating-voltage-above-iv-vmp
  note: A voltage-floor event is supported when the inverter runs above the array maximum power point
    and harvests less power than the IV-derived Pmp.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
  review_note: 'support check: partial - Operating voltage above IV Vmp and power below Pmp are stated,
    but the high module temperature signal is only implied by the high-temperature mention in the loss
    mechanism.'
- claim_id: c3
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring in summer 2025 at a 100 MW PV plant in
    California, per a field poster
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
---
In SCADA data the inverter DC voltage stays at or near its minimum operating threshold while output is lower than the irradiance would support. The inverter stays online and looks available, but it cannot track the array's true maximum power point, so power is left on the DC side. This pattern points to inverter voltage floor losses: array Vmp has dropped below the inverter's minimum DC input voltage because of high temperature, degraded modules, a tight string design margin or reactive power operation. It shows up most during hot periods, because module voltage falls as cell temperature rises. It can look like clipping or general underperformance, so first rule out outages, curtailment, clipping, soiling and sensor faults. To confirm it, compare the operating voltage with an independent Vmp estimate from in-situ or string IV sweeps or a temperature-corrected module model. The case is supported when the operating voltage stays above Vmp and the power stays below Pmp. Fixes include checking inverter settings, coordinating tap or voltage setpoint changes, reviewing reactive power requirements, and retesting MPPT recovery in hot weather.
