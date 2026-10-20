---
id: comp:inverter
type: Component
name: Inverter
aliases:
- PV inverter
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring in summer 2025 at a 100 MW PV plant in
    California, measured in field work
  note: The report estimated that adjusting voltage or settings would recover a large share of this loss.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
---
The IEA failure catalogue treats the inverter as one of the main PV system components, together with modules, cables and connectors, and mounting. Field surveys distinguish central inverters, string inverters and module inverters, each with or without a transformer. Failure modes listed for the inverter are overheating with temperature derating, incorrect installation, and complete failure where the unit stops operating. A complete inverter failure is usually found through monitoring, then confirmed with visual inspection, IV curves or open-circuit voltage checks. Inverter voltage floor losses happen when array Vmp drops below the inverter's minimum DC input voltage. The inverter stays online but cannot hold the array at its maximum power point. This voltage floor problem is most likely in hot weather and can get worse with high reactive power demand. Check DC voltage, AC voltage, reactive power and IV-derived Vmp together. Some inverters include an anti-PID or PID repair function that shifts the array potential relative to ground to suppress or reverse potential induced degradation.

<!-- review notes
- sentence 2: support check: partial - The inverter type list includes central, string (with/without trafo) and module inverters, but module inverter has no with/without trafo split, and the list contains other categories.
- sentence 4: support check: partial - Detection lists MON with VI, I-V, VOC in parentheses, but the passage doesn't say 'usually' or explicitly describe a monitoring-then-confirmation sequence.
- sentence 7: support check: partial - Passages describe anti-PID and PID repair by shifting the array potential relative to ground, but only for the Solis inverter and its optional module, not as a general feature of some inverters, and the details differ by panel type.
-->
