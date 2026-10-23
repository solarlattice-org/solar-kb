---
id: meas:ac-line-thd-high
type: Measurement
name: High AC line harmonic distortion
aliases:
- THD
- THDi
- Total harmonic distortion
- Current Harmonic Distortion
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: Distorted or unsteady AC phase voltage at the inverter terminals
- point: model_103.A
  unit: unit:A
  pattern: Abnormally high or distorted AC current reported alongside the alarm
---
This signature is a total harmonic distortion reading on the AC line that sits above what the connected inverter normally produces or tolerates. For reference, several inverter datasheets give output current distortion below 3 percent per IEEE 519 in normal operation. One manufacturer states its below 3 percent current distortion figure only when the AC voltage distortion is under 2 percent and output is above half of rated power, so check the operating point before you compare readings. Some units specify tighter output distortion limits, for example below 1 percent or below 1.5 percent, and grid-forming or battery inverters list voltage distortion limits of their own. Revenue and power quality meters can report total harmonic distortion as a harmonics quantity, which lets you trend it from monitoring data. When an inverter raises a grid-unstable alarm such as GRID-INTF, test the AC line for distortion twice, once with the DC switch off and once with it on. If distortion is high, you can switch off one of several inverters to see whether the reading changes, adjust impedance matching, and check for internal damage or a wire that came loose in shipping.

<!-- review notes
- sentence 1: support check: partial - The u13 alarm says to test the AC line for THD on grid instability and the datasheets give normal THD values, but no passage says the signature is a THD reading above what the inverter normally produces or tolerates.
- sentence 4: support check: partial - Passages show THD below 1% and below 1.5%, and a grid-forming voltage THD limit, but nothing about battery inverters, and the 'grid-forming or battery inverters' wording is only partly backed (u12 lists output voltage THD for SI models without saying they are battery inverters).
- sentence 5: support check: partial - The passages show a meter-style point named Total Harmonic Distortion, but nothing about revenue or power quality meters specifically or about trending it from monitoring data.
- sentence 1: review: partial - The passages give normal THD specs of under 3% and say to test the AC line for THD on a GRID-INTF alarm, but none defines the signature as a reading above what the inverter normally produces or tolerates.
- sentence 4: review: partial - The <1% and <1.5% limits and a grid-forming voltage THD limit are quoted, but no passage identifies the SI models (or any unit) as battery inverters.
-->
