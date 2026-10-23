---
id: meas:low-dc-input-voltage
type: Measurement
name: Low DC input voltage
aliases:
- Vdc-Low
- Low DC Voltage
- DC low
signals:
- point: model_103.DCV
  unit: unit:V
  pattern: near zero or well below normal while the status LEDs are dark
- point: model_160.DCV
  unit: unit:V
  pattern: MPPT input voltage absent or low
---
The inverter reports that the DC input voltage from the PV array is too low to feed power into the grid. On several string inverters this shows as a flashing green LED. The inverter is either waiting for enough DC voltage or still checking the utility grid. When this happens at startup, no action is needed. The inverter starts on its own once the DC voltage is high enough and the grid conditions are met. Some central inverters raise this as a major fault. With the unit in Stop mode, compare the DC voltage on the display with a voltage you measure yourself. If the two readings disagree, check the DC side for short circuits or wiring mistakes. Some inverters do not stop at low input voltage but reduce their output power automatically. Inverter voltage floor losses produce a related pattern. The array's maximum power point voltage falls below the inverter's minimum input voltage, so the inverter stays online but cannot track the true maximum power point. Voltage floor losses are most likely in hot periods, because module voltage drops as cells heat up. To confirm them, review DC voltage, AC voltage, reactive power and the Vmp from IV curves together.

<!-- review notes
- sentence 6: support check: partial - u21 says power is automatically reduced when input voltage is too high or too low, but it doesn't state that the inverter does not stop, nor that this applies to only some inverters.
-->
