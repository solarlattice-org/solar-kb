---
id: symptom:inverter-overload
type: Symptom
name: Inverter overload
aliases:
- Output overload
- Self-diagnosis > Overload
---
Inverter overload is an inverter event reported on the display or in the monitoring event log, not something you can see on the hardware. On Sungrow string inverters it appears as fault code 016, output overload. On SMA Sunny Tripower inverters it appears as event 6603, listed under self-diagnosis as overload. Sungrow says the cause is PV module power on the inverter that is too large for its normal operating range, so the first check is how much array power is connected compared with the inverter rating. Sungrow's instruction is to wait for the inverter to recover on its own and to contact the manufacturer if the fault persists. To tell overload apart from other output problems, record inverter DC voltage and current separately, because these logs support root cause analysis. Also log inverter internal temperature so you can check ventilation and rule out overheating.

<!-- review notes
- sentence 1: support check: partial - Passages show overload as a fault code/event number (016, 6603), but nothing says it is reported only on display/log or not visible on hardware.
- sentence 4: support check: partial - Cause (configured module power too large for the inverter's normal range) is stated, but the 'first check' of array power versus inverter rating is an inference, not stated.
- sentence 6: support check: partial - The passage says DC voltage and current should be stored separately for root cause analysis, but not specifically to distinguish overload from other output problems.
- sentence 7: support check: partial - Recording inverter temperature to assess ventilation and identify overheating is supported, but not specifically in the context of overload diagnosis.
-->
