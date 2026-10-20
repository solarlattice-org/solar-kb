---
id: mit:mppt-recovery-retest
type: Mitigation
name: Post-change MPPT verification
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring, summer 2025, at a 100 MW California
    PV plant (Leeward Renewable Energy / OTT HydroMet poster)
  note: This is the loss the corrective changes aim to recover. The poster estimates that voltage or setting
    adjustments could recover a large share of it.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
  review_note: 'support check: partial - The ~1.2% summer 2025 average loss at the 100 MW California plant
    is stated, but the passages say nothing about a ''typical power loss'' for post-change verification
    beyond that, and ''a large share'' recoverable is only loosely noted.'
---
Post-change MPPT verification means retesting whether the inverter tracks the array maximum power point again after corrective changes for inverter voltage floor losses. It applies when array Vmp has dropped below the inverter's minimum DC input voltage, which forces the inverter to run above the maximum power point and leaves energy unused on the DC side. Typical changes that need this check are a transformer tap adjustment, an inverter parameter change, a revised voltage control strategy, or a string design change. After the change, compare the recovered operating points with Vmp and Pmp derived from IV curves, for example from in-situ IV tracers, string IV sweeps or a temperature-corrected module model. Run the retest under high-temperature operating conditions, because that is when array Vmp is lowest and voltage flooring shows up. Also confirm that the plant still meets its reactive power obligations after the change, since reactive power demand and AC voltage behaviour shift the inverter's effective operating window. Validate the changes and the retest results with the inverter supplier and the plant electrical engineer. Record any change in the plant SCADA and monitoring systems so the data stays continuous and you can check that the change was configured correctly.

<!-- review notes
- sentence 5: support check: partial - Retest under high-temperature conditions is stated, and high temperature is listed as pushing Vmp below the window, but the explicit claim that Vmp is lowest then is not stated outright.
- sentence 7: support check: partial - Mitigation is to be validated with the inverter supplier and plant electrical engineer, but the passages do not say the retest results themselves must be validated with them.
- sentence 8: support check: partial - The O&M guidance says changes should be reflected in SCADA/monitoring for data continuity and to verify correct configuration, but it is generic and not tied to this voltage-floor retest, and it focuses on device replacement.
-->
