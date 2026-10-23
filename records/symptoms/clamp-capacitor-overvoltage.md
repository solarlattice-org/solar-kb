---
id: symptom:clamp-capacitor-overvoltage
type: Symptom
name: Clamp capacitor overvoltage
aliases:
- Clamp capacitance over-voltage event
---
Over Modbus, the same condition is reported as alarm code 030, or 0x001E in hex. The manufacturer's instruction is to wait for the inverter to recover by itself. Do not confuse it with code 031, which reports a clamp capacitance undervoltage, not an overvoltage. For further steps, the Modbus note points to the NOTE in its Section 5.
