---
id: symptom:internal-overcurrent-overvoltage
type: Symptom
name: Internal overcurrent or overvoltage
aliases:
- OV-BUS
claims:
- claim_id: c1
  rel: observed_as
  target: meas:dc-bus-voltage-high
  note: 'Solis OV-BUS alarm: the inverter detects excessive voltage on its internal DC bus. Listed causes
    are internal damage or a wire that came loose during shipping. Confirm by measuring DC and AC voltages
    and comparing them with the LCD readings.'
  quote: Inverter detects High DC Voltage on internal bus
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r4
    h: 980abe97f48c
  review: drafted
---
Inverters have built-in protection functions, including DC overvoltage and overcurrent protection, that flag abnormal internal electrical conditions. One typical alarm is a DC bus overvoltage (OV-BUS), raised when the inverter detects too much voltage on its internal DC bus. The listed causes are internal damage to the inverter or a wire that came loose during shipping. Check first by measuring the DC and AC voltages yourself and comparing them with the values on the inverter display. If the measured voltages are normal but the alarm stays, treat it as internal damage: the inverter should be replaced. Revenue meters can also report a severe out-of-tolerance internal operating condition as a status failure, and then go into a disabled state.

<!-- review notes
- sentence 5: support check: partial - Replace Inverter and internal damage are listed, but the passage does not state the conditional logic that normal measured voltages with persistent alarm means internal damage.
-->
