---
id: symptom:abnormal-temperature-reading
type: Symptom
name: Abnormal temperature reading
aliases:
- TempSensorErr
- Prompt detection of abnormal temperature
claims:
- claim_id: c1
  rel: observed_as
  target: meas:implausible-sensor-temperature
  note: One inverter manual lists a sensor reading of -25C as a possible cause of the TempSensorErr alarm.
    That points to a sensor or connector fault, not a real temperature.
  cite:
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=33.r2
    h: b4e0065cf5c2
  review: drafted
  review_note: 'support check: partial - u4 lists a -25C sensor reading as a possible cause of TempSensorErr,
    but the passage doesn''t say it is stuck/fixed, doesn''t follow ambient or load, or that it points
    to a sensor/connector fault (the heat sink signal isn''t mentioned).'
---
This symptom shows up as a TempSensorErr alarm on the inverter, meaning the unit has picked up an abnormal internal temperature reading. The listed causes both point to a temperature sensor fault: either the sensor's socket connector is making poor contact, or the sensor itself is damaged. One manual notes that the sensor may read -25C. A fixed value like that, which does not change, suggests a sensor or wiring problem rather than a real cold condition. First, check the temperature value on the inverter display and see whether it makes sense. Next, reboot the inverter. On some models you do this by switching the external AC disconnect off and back on. On others you switch the internal disconnects off and then turn the inverter back on. If the alarm comes back or does not clear, suspect a loose sensor connector or a damaged sensor, and contact the manufacturer's customer service.

<!-- review notes
- sentence 3: support check: partial - u4 says the sensor is reading -25C as a cause, but nothing says a fixed unchanging value implies a sensor or wiring problem rather than real cold.
- sentence 6: support check: partial - Causes (poor connector contact, damaged sensor) and contacting Solectria customer service if the error does not clear are stated, but not the 'comes back' condition, and the combined step reads as an inference.
-->
