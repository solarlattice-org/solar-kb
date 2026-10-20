---
id: meas:dc-power-voltage-change
type: Measurement
name: Abrupt DC power and voltage change
signals:
- point: model_103.DCW
  unit: unit:W
  pattern: sudden change in mean DC power
- point: model_103.DCV
  unit: unit:V
  pattern: sudden change in mean DC voltage
---
If the inverter's ground fault circuit detects leakage current from the PV array, it raises an alarm and the inverter stops operating, so output changes abruptly instead of drifting down. CPS inverters report this condition as a high leakage current fault, such as Fault0090 for dynamic leakage current or GFCIErr. To find the faulty string, isolate all strings, then reconnect them one at a time and restart the inverter until the alarm comes back. Trace that string for leakage to earth ground. Measure leakage to ground to confirm a DC ground fault. A DC arc fault is a sudden high-power discharge between conductors. Arcs are brief and hard to catch, so they are usually detected by spectrum analysis of the current and voltage waveforms. Snow on the modules can also cause an abrupt drop in production after a snowfall, followed by a gradual recovery as it melts or slides off. Rule this out before looking for an electrical fault.

<!-- review notes
- sentence 1: support check: partial - Passage states leakage detection, alarm and ceasing operation, but not the claim that output changes abruptly rather than drifting down.
- sentence 5: support check: partial - Definition and transience are stated, but spectrum analysis is only one of the current methods (also AFCIs), not 'usually' the method.
- sentence 6: support check: partial - Abrupt drop after snowfall and gradual melt/slide-off recovery are stated, but not the advice to rule it out before looking for an electrical fault.
-->
