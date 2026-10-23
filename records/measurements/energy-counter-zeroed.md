---
id: meas:energy-counter-zeroed
type: Measurement
name: Energy counter drop to zero
aliases:
- Clear Energy
- Reset Energy Data
- Reset Energy
- Meter Energy Reset
signals:
- point: model_103.WH
  unit: unit:W-HR
  pattern: Stored or partial energy total suddenly returns to zero instead of rising steadily
---
The signature is an inverter or meter energy total that falls back to zero, rather than continuing to accumulate. Inverter menus include a function that clears the stored historical yield and sets it back to zero. On an inverter status display, the daily and lifetime energy fields, E-Today and E-Total in kWh, then read 0.0. Revenue meters can show the date and time of the last energy reset, so you can check whether a zeroed counter matches a deliberate reset. Only maintenance personnel should use the clear function, because using it wrongly can stop the inverter from working properly. Programmable meter counters can also be set to reset to zero by a logic equation, and a status bit turns on when the counter value equals zero.

<!-- review notes
- sentence 1: support check: partial - Passages describe functions that reset energy to zero but do not describe the signature of a total falling back to zero instead of accumulating.
- sentence 3: support check: partial - E-Today and E-Total rows show 0.0 kWh, but nothing ties this to a 'then' condition (after reset) in the passages.
- sentence 4: support check: partial - Meters display date/time of last energy reset, but the stated purpose of checking a zeroed counter against a deliberate reset isn't in the passages.
- sentence 1: review: partial - The passages describe inverter functions that reset historical yield or energy data to zero, but they never frame this as a signature of a total falling back instead of accumulating, and neither cited passage mentions a meter.
- sentence 4: review: partial - The passages show the meter displays the date/time of the last energy reset, but the stated purpose (checking whether a zeroed counter matches a deliberate reset) is an inference not in the passages.
-->
