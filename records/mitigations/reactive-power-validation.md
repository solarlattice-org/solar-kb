---
id: mit:reactive-power-validation
type: Mitigation
name: Reactive power requirement review
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring in summer 2025 at a 100 MW California
    PV plant. This is the loss the mitigation targets.
  note: The poster estimates that voltage or setting adjustments would recover a large share of this loss.
    The share is not given as a number.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
Reactive power requirement review means checking which reactive power duties the grid and the plant actually require. It is one of the listed corrective actions for inverter voltage floor losses. It applies when reactive power operation helps push array Vmp below the inverter's minimum DC input voltage. In that state the inverter runs above the maximum power point and leaves DC energy unharvested. Look at AC voltage and reactive power dispatch at the same timestamps as the voltage-floor events. High reactive power demand or AC voltage hysteresis can shift the inverter's effective operating window. Check every reactive power setting against the standard that applies. Some inverter manuals mark a power-dependent reactive power mode as not required by certain interconnection standards. Do this review together with an inverter settings check, coordinated transformer tap or voltage setpoint changes, and an MPPT recovery retest during hot weather. At one field site, voltage or setting adjustments were estimated to recover a large share of the measured voltage-floor loss. Reactive power may be only part of the cause. Degraded modules, high temperature and thin string voltage margin can also pull Vmp below the floor.

<!-- review notes
- sentence 1: support check: partial - Validating reactive power requirements is a listed mitigation, but the passages do not define it as checking which duties the grid and plant actually require.
- sentence 4: support check: partial - Passages show manuals marking the reac-power mode as not required by Rule21 and UL1741SA, but not the instruction to check every setting against the applicable standard.
-->
