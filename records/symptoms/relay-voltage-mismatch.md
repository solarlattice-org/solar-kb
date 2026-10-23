---
id: symptom:relay-voltage-mismatch
type: Symptom
name: Relay voltage mismatch
aliases:
- Error Read V
- Output relay damaged
- Relay plausibility error
---
The inverter measures the voltage on both sides of its grid connection relay. When the input and output sides differ by too much, it reports a relay voltage mismatch. On ABB/FIMER inverters this shows as code E031 with the yellow or alarm LED lit. The manufacturer describes the cause as a damaged output relay. ABB/FIMER says this error is internal to the inverter and cannot be checked from outside. Switch the inverter off and on again, and contact customer assistance if the error comes back. KACO advises switching off both AC and DC for at least 5 minutes. If the fault occurs again after that, treat it as a device fault. On Solis inverters a related relay check fault is linked to a stuck relay. Before blaming the relay there, check the AC connector terminals, loose AC wiring and earthing, and measure the AC voltages at the inverter AC gland.
