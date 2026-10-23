---
id: meas:ac-output-voltage-high
type: Measurement
name: High AC output voltage
aliases:
- AC overvoltage
- Over Grid Voltage
- OV-G-V
- AC Voltage High
- Vac High
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC phase voltage rises well above nominal before the warning or fault
---
The inverter measures an AC line voltage above its high-voltage setting for longer than the allowed clearing time, and it trips off the grid with an AC voltage high fault. Once the inverter disconnects, the voltage falls. The inverter does not reconnect until the line voltage drops below a separate reconnect setting and the reconnection time has passed. After reconnecting, the voltage climbs again as power flows and the wires heat up. The next trip can come seconds or minutes later, or even longer, which gives a repeating trip-and-reconnect pattern. Typical causes are high grid resistance compared with the PV peak capacity connected nearby, or too much resistance in the wiring between the inverter and the grid connection. To check, first switch the DC side off and measure AC at the inverter. If it is already high, the upper limit may only be raised with permission from the utility. Then run the inverter at full power with DC on, measure AC at the inverter test points and compare it with the display. If the voltage is high only now, the cables to the interconnection point are too small, so review the ampacity and voltage drop calculations. Inverter AC voltage readings on several models are only accurate to about 2 percent, so confirm a borderline reading with an independent meter.

<!-- review notes
- sentence 7: support check: partial - The passages give a 2% voltage measurement accuracy on several models, but they don't say to confirm borderline readings with an independent meter.
-->
