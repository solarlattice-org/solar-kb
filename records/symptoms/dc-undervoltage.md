---
id: symptom:dc-undervoltage
type: Symptom
name: DC undervoltage
---
In analytical monitoring, the voltage at the PV array output is logged as a parameter in volts, symbol VDC. This is the channel to watch for DC undervoltage. Monitoring guidance looks at DC voltage together with module temperature, so read a low DC voltage alongside the temperature data. One inverter manual shows a curve of output derating against DC voltage, so input voltage can limit output. In the field, field instructions include checking whether DC voltage is present at the inverter input terminals and on the DC MOV board. Before you troubleshoot further, use a multimeter to confirm the DC inputs have the right polarity, because reversed inputs can damage the inverter.

<!-- review notes
- sentence 1: support check: partial - The passage gives the parameter, symbol VDC and unit V, but doesn't say it is the channel to watch for DC undervoltage.
- sentence 2: support check: partial - The passage is only a section heading pairing DC voltage and module temperature, so it doesn't say to read low DC voltage alongside temperature data.
- sentence 3: support check: partial - The figure title shows a derating-with-DC-voltage curve, but the passage doesn't state that input voltage limits output.
- sentence 4: support check: partial - The figure captions refer to checking for absence of DC voltage at the input terminals and on the DC MOV board, but they don't state these are field instructions.
- sentence 5: support check: partial - The passage supports checking DC input polarity with a multimeter because wrong polarity may damage the inverter, but not that it should be done before further troubleshooting, and it says 'may cause' damage.
-->
