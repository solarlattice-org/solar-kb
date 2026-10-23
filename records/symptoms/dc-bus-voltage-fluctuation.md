---
id: symptom:dc-bus-voltage-fluctuation
type: Symptom
name: DC bus voltage fluctuation
---
Monitoring systems that read the inverter over Modbus see the same condition as alarm code 026, which is 0x001A in hex. Bus voltage is the voltage between the positive and negative poles on the inverter's DC side, so check the inverter DC voltage reading for instability. The manufacturer's first step is to wait for the inverter to recover by itself, and to refer to the event-table note if the event does not clear.
