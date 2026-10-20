---
id: mit:voltage-control-strategy
type: Mitigation
name: Revised voltage control strategy
aliases:
- voltage setpoint changes
- Voltage Control
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring at a 100 MW California PV plant in summer
    2025, before corrective voltage or setting adjustments
  note: The source estimates that voltage or setting adjustments could recover a large share of this loss;
    the recovered fraction is not quantified.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
  review_note: 'support check: partial - The passage gives about 1.2% summer 2025 average loss at a 100
    MW California plant, but it doesn''t state this as a loss for a ''revised voltage control strategy''
    (the quantity is the voltage-flooring loss), though the pre-correction condition is implied.'
---
A revised voltage control strategy changes how the plant regulates AC voltage so the inverter DC operating window no longer forces the array off its maximum power point. It addresses Inverter Voltage Floor Losses, where array Vmp drops below the inverter minimum DC input voltage and energy is left on the DC side. It applies when high reactive power demand or AC voltage hysteresis is found to narrow the effective inverter operating window, rather than module degradation alone. Voltage control regulates voltage toward a reference by injecting or absorbing reactive power, and its settings are project-dependent and come from modeling of the grid at the interconnection point. It is one candidate action alongside transformer tap adjustment, inverter parameter changes and string design changes, and should be validated with the inverter supplier and the plant electrical engineer. After the change, compare recovered operation against IV-derived Vmp and Pmp and retest MPPT recovery under high-temperature conditions. A key limit is that reactive power and grid support obligations must still be met after the strategy is revised. At one large California plant, voltage or setting adjustments were estimated to recover a large share of the measured voltage-floor loss.

<!-- review notes
- sentence 1: support check: partial - Revised voltage control strategy is listed as a candidate mitigation and AC voltage/reactive power can alter the operating window, but the passages don't explicitly describe it as changing AC voltage regulation so the array is no longer forced off MPP.
- sentence 3: support check: partial - The passage says high reactive power demand or AC voltage hysteresis can change the effective operating window and root cause may involve voltage control rather than module degradation alone, but it doesn't say the strategy 'applies when' this is found, and it says 'narrow' nowhere.
-->
