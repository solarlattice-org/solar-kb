---
id: symptom:current-sensor-calibration-timeout
type: Symptom
name: Current sensor calibration timeout
aliases:
- Timeout current sensor calibration
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On Fronius Symo UL inverters this shows as status code 314. Grid feed-in stops briefly, then the
    inverter goes back to its startup phase.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r13
    h: c13abd994ee5
  review: drafted
---
On a Fronius Symo inverter this symptom shows as status code 314, which reports that current sensor calibration timed out. The inverter stops feeding the grid for a short time and then returns to its startup phase, so monitoring data show a brief drop in AC power followed by a restart. The same manual lists a separate code, 315, for an AC current sensor fault. If that code also appears, the problem is more likely the sensor itself than a single calibration timeout. Other inverter makers report similar problems as a failed current sensor offset calibration, or as a current sensor that is not connected, not available or defective. When a calibration error keeps coming back, the manufacturer's service team has to find the cause, so contact service instead of trying to repair the sensor in the field.

<!-- review notes
- sentence 3: support check: partial - Code 315 as AC current sensor fault is listed, but the inference that it indicates the sensor itself is more likely the problem is not in the passage.
- sentence 5: support check: partial - Passages say the cause must be determined by Service and to contact Service, but nothing about recurring errors or not repairing the sensor in the field.
-->
