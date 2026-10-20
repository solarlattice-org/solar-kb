---
id: method:inverter-settings-review
type: DetectionMethod
name: Inverter settings review
claims:
- claim_id: c1
  rel: produces
  target: meas:dc-voltage-pinned-at-minimum
  note: Look for intervals where inverter DC voltage sits at or near the minimum operating threshold while
    output is lower than irradiance supports. Rule out outages, curtailment, clipping, soiling and sensor
    faults first.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:operating-voltage-above-iv-vmp
  note: A voltage-floor event is supported when the measured operating voltage stays above the IV-derived
    Vmp and the operating power is below the IV-derived Pmp.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
- claim_id: c3
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring in summer 2025 at a 100 MW California
    PV plant (Leeward Renewable Energy / OTT HydroMet poster)
  note: The source gives this figure as approximate. The same source estimates that voltage or setting
    adjustments would recover a large share of the loss.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
---
An inverter settings review checks the inverter's DC voltage limits and other parameters against how the plant actually runs. It is used to confirm whether the inverter's minimum DC input voltage is stopping maximum power point tracking. Start by finding intervals where the inverter DC voltage sits at or near its minimum threshold while output is lower than the irradiance supports. Rule out outages, curtailment, clipping, soiling and sensor faults first. Compare the operating voltage with an independent Vmp estimate from in-situ IV tracers, string IV sweeps or a temperature-corrected module model. Operation above Vmp with power below Pmp points to inverter voltage floor losses. Do not mistake this for clipping. Clipping is a power ceiling, while voltage flooring is an MPPT limit set by the DC voltage window, and the two need different fixes. Monitor control settings on both the DC and AC sides, and set alarms that trigger when a parameter is changed wrongly or goes outside a set limit. Measure and store the input DC voltage and current separately so MPP-tracking problems can be analysed. Wrong parameter settings can cause inverter faults, so only qualified personnel should change settings. Agree any changes with the inverter supplier and the plant electrical engineer. After a change, compare the recovered operation with the IV-derived Vmp and Pmp. Also confirm the plant still meets its reactive power obligations.

<!-- review notes
- sentence 1: support check: partial - Passages cover comparing inverter DC voltage limits and settings during suspected events, but they never define a 'settings review' or say it checks parameters against how the plant actually runs.
- sentence 4: support check: partial - The passage says clipping is a power ceiling, flooring is an MPPT constraint from the DC voltage window, and the two need different mitigations, but it doesn't spell out the 'do not mistake' framing beyond that.
-->
