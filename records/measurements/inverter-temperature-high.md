---
id: meas:inverter-temperature-high
type: Measurement
name: High inverter internal temperature
aliases:
- Internal Air Temperature
- OverTemp
- OV-TEM
- Critical Over Temperature
- Temp derating
- temperature derating
signals:
- point: model_103.TmpCab
  unit: unit:DEG_C
  pattern: cabinet temperature runs high or keeps rising during high-load, hot periods
- point: model_103.TmpSnk
  unit: unit:DEG_C
  pattern: heat sink temperature high compared with normal operation
---
Inverters report an internal air temperature value, and you can read it on the display or in the monitoring data. When the internal or ambient temperature gets too high, the inverter cuts its output power. Monitoring may show this as a temperature derating message or a derating state. Some manuals say derating starts at about 45 °C. One model reduces output in a straight line up to 60 °C and then shuts down to protect itself. If the temperature keeps rising, the inverter may stop producing power completely and show an overtemperature protection alarm or a critical overtemperature fault. Inverters do not always report the power reduction. To confirm derating, check a plot of power against irradiance. Common causes are poor installation or spacing, fan failure, dust or debris blocking cooling or vents, direct sunlight, high ambient temperature and wrong inverter settings. An abnormal temperature reading can also come from a poorly contacting internal temperature sensor, so compare the displayed value with the actual conditions before blaming overheating.

<!-- review notes
- sentence 1: support check: partial - Passages list Internal Air Temperature as inverter information and mention a display reading, but don't explicitly say it can be read on the display or in monitoring data.
- sentence 7: support check: partial - Poor sensor contact and verifying the displayed reading are stated, but not explicitly to compare with actual conditions before blaming overheating.
-->
