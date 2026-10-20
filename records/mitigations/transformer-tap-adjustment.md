---
id: mit:transformer-tap-adjustment
type: Mitigation
name: Transformer tap adjustment
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring in summer 2025 at a 100 MW California
    PV plant, before voltage or setting adjustments
  note: This is the loss the adjustment targets. Voltage or setting adjustments were estimated to recover
    a large share of it; no recovered percentage is given.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
---
Transformer tap adjustment changes the transformer winding tap to correct a deviation from nominal voltage. For PV plants, it is one of the candidate fixes for Inverter Voltage Floor Losses. It applies when degraded modules, high temperature, a thin string voltage margin or reactive power operation pull array Vmp below the inverter's minimum DC input voltage. The inverter then has to run above the maximum power point. Agree the tap or voltage setpoint change with the inverter supplier and the plant electrical engineer, and check the inverter settings and AC voltage behaviour first. Change taps only with the transformer de-energized, and grounded where the manual requires it. Set the handle or tap jumpers to a nameplate position, then lock or torque the connection. On three-phase units, every phase must be on the same tap. Never leave the tap changer between positions or in a position that is not marked on the nameplate. After re-energizing, check that the voltage is within the nameplate design range, typically +/-5% of nominal. Higher voltage can overheat the transformer and disturb the equipment it feeds. If the phases show different voltages or the ratio test does not match the nameplate, check that the tap changer is making good contact and that all phases are on the same position. At one plant, voltage or setting adjustments were estimated to recover a large share of the measured voltage-floor loss. After the change, retest MPPT recovery in hot conditions against Vmp and Pmp from IV curves, and confirm the plant still meets its reactive power obligations.

<!-- review notes
- sentence 2: support check: partial - Causes and forced operation above MPP are stated, but the passages say Vmp falls below the inverter's DC input voltage constraint/minimum without explicitly using 'thin string margin' wording; mostly matches, though minor.
- sentence 3: support check: partial - Validation with supplier and electrical engineer and verifying inverter settings/AC behavior are stated, but 'first' ordering is only implied by list order and the supplier/engineer validation is for mitigation generally.
-->
