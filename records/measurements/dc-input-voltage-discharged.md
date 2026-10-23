---
id: meas:dc-input-voltage-discharged
type: Measurement
name: DC input voltage discharged
aliases:
- Rapid Shutdown successful
signals:
- point: model_103.DCV
  unit: unit:V
  pattern: Inverter DC input voltage collapses to a low safe level shortly after initiation
- point: model_160.DCV
  unit: unit:V
  pattern: MPPT input voltages fall to a low level on all inputs at the same time
---
This signature means the voltage at the inverter DC inputs has been brought down after a rapid shutdown. The inverter logs it as event 9035, Rapid Shutdown successful, and the AC output voltage is discharged at the same time. It comes after event 9033, which says the inverter detected that a rapid shutdown was triggered. Either of two things starts the discharge: the AC side of the inverter is disconnected, or an external rapid shutdown initiator is activated. While this is happening, the PV inputs are shown as discharging. On models with a battery, the PV inputs are discharged and the battery is also switched off. Most manual versions say the AC side was disconnected when event 9033 was logged. One version says it was connected, so check the wording for your firmware and manual. Before working on the inverter, check that no voltage is present. Use a measuring device rated for the inverter's maximum DC and AC voltage, and a current clamp to confirm that no current is flowing.

<!-- review notes
- sentence 2: support check: partial - Event 9033 content is stated, but the passages do not say 9035 comes after 9033 (sequence is implied only).
- sentence 6: support check: partial - Passages list a meter for max AC/DC voltage and a current clamp to verify no current, but don't state the 'before working' instruction explicitly; the rated range is described slightly differently.
-->
