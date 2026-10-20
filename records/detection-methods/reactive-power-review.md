---
id: method:reactive-power-review
type: DetectionMethod
name: AC voltage and reactive power review
claims:
- claim_id: c1
  rel: produces
  target: meas:high-reactive-power-during-floor
  note: High reactive power demand or AC voltage hysteresis can shift the effective inverter operating
    window. This points the root cause toward plant voltage control, transformer tap, inverter settings
    or grid support requirements.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h4
    h: 7023830f6e10
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: drafted
  review_note: 'support check: partial - Passages say to review AC voltage and reactive power at the same
    timestamps and that high reactive power or AC voltage hysteresis shifts the operating window, but
    they don''t state the specific signal patterns (high VAr, PF away from unity, AC voltage coinciding
    with pinned DC voltage).'
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average summer 2025 energy loss from inverter voltage flooring at a 100 MW California PV
    plant (Leeward Renewable Energy and OTT HydroMet field study)
  note: Voltage or setting adjustments were estimated to recover a large share of this loss.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
---
This method checks inverter AC voltage and reactive power dispatch at the same times as suspected inverter voltage floor events. First find intervals where the inverter DC voltage sits at or near its minimum operating threshold while output is lower than irradiance supports. Rule out outages, curtailment, clipping, soiling and sensor faults before blaming voltage flooring. Then look at AC voltage and reactive power at those same timestamps. High reactive power demand or AC voltage hysteresis can shift the inverter's effective operating window and push it above the array maximum power point. Use it together with DC voltage, module temperature and Vmp from IV curves, because the loss can otherwise look like clipping or general underperformance. Events are most likely during hot periods. Inverters report different sets of parameters, so check that AC voltage and reactive power are logged. Also allow for the inverter's measurement accuracy, which in one manual is 2 percent of AC voltage and 5 percent of nominal AC power for active and reactive power. Confirmed findings usually lead to checking inverter settings, changing transformer taps or voltage setpoints, reviewing reactive power requirements, and retesting MPPT recovery in hot conditions.

<!-- review notes
- sentence 3: support check: partial - Passages support reviewing AC voltage and reactive power at the same timestamps and that they can change the effective operating window, but not explicitly that this pushes the inverter above the array MPP (only the loss mechanism section hints that, and it isn't cited).
- sentence 5: support check: partial - The tables show that inverters report different parameter sets and that one manual gives 2% AC voltage accuracy and 5% nominal AC power accuracy for active/reactive power, but nothing says to check that AC voltage and reactive power are logged or to allow for measurement accuracy.
-->
