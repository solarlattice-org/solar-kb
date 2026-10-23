---
id: meas:ambient-temperature-above-limit
type: Measurement
name: Ambient temperature above limit
aliases:
- Ambient Temp
- Temp. Ambient
signals:
- point: model_307.TmpAmb
  unit: unit:DEG_C
  pattern: ambient temperature near the inverter above the maximum permitted for the device
---
This signature is an ambient temperature reading that sits above the operating range the equipment manufacturer allows. The reading comes from an ambient temperature sensor or monitoring point, reported in degrees Celsius. One example is the Megapack, which measures air temperature inside its own enclosure and reports it only while in State Request On. Inverter datasheets give an ambient operating range up to +60°C and say output is derated above 45°C, so expect reduced power before the upper limit is reached. On a pad-mounted transformer, running in ambient air above the nameplate limit (usually -5°C to 40°C) lowers its nominal capability for each degree over the limit. Higher ambient temperature around a cable lowers its ampacity. On SMA battery systems, event 9314 reports a battery error when the upper limit of the battery manufacturer's approved temperature range is exceeded. The corrective action is to make sure the battery's ambient conditions are met. Some inverter manuals also give a maximum temperature rise above ambient for terminations and busbars, so ambient temperature is the baseline for judging component heating.

<!-- review notes
- sentence 1: support check: partial - Passages give manufacturer operating ranges (e.g., up to +60°C or +65°C) but none define a signature as an ambient reading above that range; the notion is only loosely implied.
- sentence 7: support check: partial - The table gives maximum temperature rise above ambient for terminations and busbars, but 'some inverter manuals' and the baseline-for-judging claim are an inference not explicitly stated.
-->
