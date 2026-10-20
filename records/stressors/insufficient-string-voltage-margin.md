---
id: stressor:insufficient-string-voltage-margin
type: Stressor
name: Insufficient string voltage margin
aliases:
- string design margin
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Summer 2025 average energy loss from inverter voltage flooring at a 100 MW California PV
    plant. String design margin was one of several listed contributors.
  note: This loss covers voltage flooring as a whole. The source does not separate out the share caused
    by string margin alone. It says voltage or setting adjustments were estimated to recover a large part
    of the measured loss.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
---
Insufficient string voltage margin means the strings are designed with too little room between their operating voltage and the inverter's DC input voltage window. When the margin is too small, array Vmp can drop below the inverter's minimum input voltage. The inverter then has to run above the maximum power point, and available DC power goes unharvested. This is the failure mode called Inverter Voltage Floor Losses. The problem is most likely in hot periods, because module voltage falls as cell temperature rises. Degraded modules and high reactive power demand can make it worse. At the other extreme, low ambient temperatures raise string voltage and can damage the inverter. If a measured string Voc is close to the inverter's maximum, check the string length. When sizing strings, use the NEC 690.7 temperature factors or the module maker's temperature coefficient. This keeps string voltage below the inverter limit at the minimum design temperature. A string with fewer modules than the others on the same inverter can cause a string current reflux fault. The fix is to correct the module configuration. To reduce exposure, future string designs should keep voltage margin at both low and high temperatures. Any changes should be confirmed with the inverter supplier and checked against IV-derived Vmp.

<!-- review notes
- sentence 1: support check: partial - Passages list string design margin as a cause of Vmp falling below the inverter window, but never define insufficient margin as too little room between operating voltage and the window.
- sentence 6: support check: partial - Passage lists fewer modules than other strings as a check item for string current reflux and says to adjust configuration, but also lists other causes (shading, wiring, orientation), so it is not the sole fix.
-->
