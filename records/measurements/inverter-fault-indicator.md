---
id: meas:inverter-fault-indicator
type: Measurement
name: Inverter fault indicator light
aliases:
- Fault status indication light
- fault indicator contact
- LED indicator
---
If the FAULT light on the inverter's LED panel stays on, the inverter has detected a fault. On some models a steady light means an internal fault. A slow flash on the FAULT light means an alarm. A fast flash means a protective action has been triggered, and the light stays active until the fault is cleared. If the FAULT light is off, there is either no fault or the inverter's power supply is not working, so check the POWER light as well. Grid problems usually show on a separate GRID light, which flashes while the AC voltage is outside its allowed range. Some inverters use a colour code instead. For example, a blinking red LED points to an isolation or RCD problem, a blinking green LED to high temperature, and a steady red LED to a detected arc. A ground fault in the array makes the inverter raise an alarm, stop operating and show an error until the fault is cleared. Reversed PV polarity also leaves the inverter in a fault or alarm state. When the light is on, read the message on the display or in the alarm menu, or check the monitoring data log, to find the specific fault. The inverter's multifunction relay can also drive an external warning light that shows either an error or normal operation.

<!-- review notes
- sentence 2: support check: partial - Slow flash = alarm and fast flash = protective action are stated, but the light staying on until the fault is cleared is stated for faults (blink quickly), not clearly as a property of protective action in the tables.
- sentence 3: support check: partial - Light off meaning no fault or power supply not working is stated, and the POWER light is described, but the advice to check the POWER light is not stated explicitly.
-->
