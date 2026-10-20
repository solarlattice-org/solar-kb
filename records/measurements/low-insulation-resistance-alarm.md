---
id: meas:low-insulation-resistance-alarm
type: Measurement
name: Low insulation resistance alarm
aliases:
- IsolationErr
- Insulation resistance low
- low insulation fault
- PV ISO-PRO 01/02
signals:
- point: model_103.W
  unit: unit:W
  pattern: inverter stops exporting while the insulation alarm is active
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: normal morning irradiance while the inverter stays offline
- point: model_307.RH
  unit: unit:PERCENT
  pattern: high humidity or dew at the time the inverter fails to start
---
The inverter raises a protection alarm when it detects low DC insulation resistance between the PV circuit and earth ground. It often shows up after rain or in the early morning when modules are wet with dew, and the inverter may switch off when the resistance falls below its limit. Bad module insulation cannot be seen by eye. Only an insulation resistance measurement confirms it, and testing in humid or wet conditions works better than testing dry. To find the faulted string, isolate all strings, then add them back one at a time and restart the inverter until the alarm returns. Then trace that string for leakage to ground. Note the weather when the alarm occurs. If a dry measurement looks normal, measure again in the same weather that triggered the alarm and check the cables physically. Broken module glass can cause insulation faults and moisture ingress. Aged backsheets can crack and lose their insulating properties. If a voltage measurement does not clearly show a ground fault, an insulation resistance measurement gives more exact results.

<!-- review notes
- sentence 3: support check: partial - Passage says not visible by eye and detection only via measurement, with dry or better humid/wet conditions; 'only measurement confirms' is close but it also says visual defects may allow deduction, and 'works better' is paraphrase.
-->
