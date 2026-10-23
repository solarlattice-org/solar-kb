---
id: meas:zero-dc-voltage
type: Measurement
name: Zero DC voltage reading
aliases:
- Absence of DC voltage
signals:
- point: model_103.DCV
  unit: unit:V
  pattern: DC voltage at zero while the DC switch is on
---
This signature is a DC voltage of zero. The inverter measurement data screen shows the DC input voltage (Vdc) as 0.0 V. Inverters report DC input voltage in volts as a standard measurement point, so the zero shows up both on the display and in monitoring data. In the field, measure at the inverter DC input terminals to confirm that DC voltage is really absent. For this check and for measuring the DC link, use a meter with a DC input range of at least 1000 V, and a current clamp to confirm that no current is flowing. On some central inverters, the DC voltage register shows a special value of 32768 when the DC contactors are open. This means no DC voltage measurement is available, not that the voltage is zero. Compare your meter reading at the DC terminals with the inverter display. If the two do not agree, the inverter's measurement circuit may be faulty.

<!-- review notes
- sentence 2: support check: partial - Passages show DC Voltage (V) is a measurement point, but don't state it appears in both display and monitoring data as such (though both are suggested).
- sentence 3: support check: partial - Figure caption mentions absence of DC voltage at input terminals but doesn't state the instruction to measure there to confirm.
- sentence 4: support check: partial - Equipment list gives a ≥1000 V DC range meter and current clamp for verifying no current, but the passage also allows an AC 690 V alternative and doesn't tie it specifically to this check with 'at least 1000 V' only.
- sentence 5: support check: partial - The register description states 32768 means DC contactors open and no measurement available, but 'some central inverters' is not stated and 'not zero' is only implied.
- sentence 6: support check: partial - Passages say compare meter to display and a bad measurement circuit may be the cause, with a 2% tolerance, but this is in the context of an overvoltage alarm, not zero-voltage.
- sentence 1: review: partial - The rows show Vdc(V) as 0.0, but the cited table rows do not identify a measurement data screen or frame zero DC voltage as a signature.
-->
