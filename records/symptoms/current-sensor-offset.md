---
id: symptom:current-sensor-offset
type: Symptom
name: Current sensor offset
aliases:
- sampling offset of DCI
- DCI sampling offset
- DC current sensor C offset
- DC Input Current Offset Abnormal
- DCI Curr Offset Abn
- Inverter Current Offset Abnormal
- Current Sensor Offset Calibration Failed
---
This symptom shows up as an inverter protection code or event message saying the inverter's DC current (DCI) measurement has an offset. SMA inverters report it as event 8501, a DC current sensor C offset, and Yaskawa reports it as a failed current sensor offset calibration. For the CPS sampling offset alarm: if the inverter can still start up, recalibrate it. If the alarm keeps coming back and the inverter cannot start, replace the inverter. On SMA units, contact service if the offset message comes back.
