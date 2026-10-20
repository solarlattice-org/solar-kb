---
id: mit:inverter-parameter-change
type: Mitigation
name: Inverter parameter adjustment
aliases:
- inverter parameter changes
- Changing Operating Parameters
- Parameter configuration
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring in summer 2025 at a 100 MW PV plant in
    California; this is the loss that voltage or setting adjustments target
  note: The source says voltage or setting adjustments were estimated to recover a large share of this
    loss. The loss is about 1.2%.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
This action changes the inverter's operating parameters, which are set to default values at the factory, to make the inverter perform better. It is one of the candidate fixes for inverter voltage floor losses. These losses happen when array Vmp drops below the inverter's minimum DC input voltage, so the inverter is held above the maximum power point. Do not mix this up with inverter clipping. Clipping is a power ceiling, while voltage flooring is an MPPT constraint, and the two need different fixes. On SMA units, log into the user interface as Installer, open Device parameters, edit and set the parameter, then save all settings. Sungrow units let you set parameters through the App. Some grid-sensitive parameters can only be changed by qualified people using a Grid Guard code. Wrong settings can cause an inverter exception. Agree on the change with the inverter supplier and the plant electrical engineer. It may need to be coordinated with transformer tap or voltage setpoint changes. After the change, compare the recovered operation with Vmp and Pmp taken from IV curves. Retest MPPT recovery in high-temperature operation and confirm that reactive power obligations are still met. At one plant, adjusting voltage or settings was estimated to recover a large share of the measured voltage floor loss.
