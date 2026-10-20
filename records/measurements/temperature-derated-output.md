---
id: meas:temperature-derated-output
type: Measurement
name: Temperature-linked output derating
aliases:
- Temperature derating
- Power Derating, Temperature
- Active power limit Temperature
- Derating en température
- Derating running
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power reduced below expected output while temperature is high
- point: model_307.TmpAmb
  unit: unit:DEG_C
  pattern: ambient temperature high when the power reduction occurs
- point: model_103.TmpSnk
  unit: unit:DEG_C
  pattern: heat sink temperature high while power is reduced
- point: model_103.TmpCab
  unit: unit:DEG_C
  pattern: High cabinet temperature at the same time as the stepwise power reduction
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: plane-of-array irradiance stays high while power is reduced
---
In this signature, the inverter lowers its output power, or shuts off, to keep its components from overheating. Manufacturer derating curves show full output up to an ambient threshold, around 45 C on several models. Above that point the output drops, and on one model it falls linearly until the inverter shuts down at 60 C. Some inverters log a dedicated event when the internal operating temperature cuts the power. SMA units log one once the reduction has lasted more than 10 minutes. Inverters do not always report a derating or power-reduction status. Check their behaviour by plotting power against irradiance. The failure mode behind this pattern is inverter overheating. Check that all external fans are running and that the ambient temperature is within the normal operating range. Replace any failed fans. If you run a performance ratio regression on grid-side power, it also picks up thermal losses in the inverter. Use array-side power to separate these losses from module temperature effects.

<!-- review notes
- sentence 2: support check: partial - 45 °C onset for CPS SCA and linear derating to shutdown at 60 °C for PVI 23-28TL are stated, but 'full output up to threshold on several models' is only supported for two models and the 45 °C CPS passage says only 'begin to derate'.
-->
