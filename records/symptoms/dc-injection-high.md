---
id: symptom:dc-injection-high
type: Symptom
name: High DC injection
aliases:
- DCI high
- DC current injection
- DC injection from AC output
---
High DC injection means the inverter's own monitoring has found too much DC current on its AC output. The manufacturer links it to transient conditions where impedance and voltage are unbalanced between the grid phases. First, raise the DCImax limit so the inverter has more room to adjust during transients. If the fault still does not clear after that, replace the inverter. Do not confuse it with Protect0180, a separate alarm for a DCI sampling offset. That one calls for recalibration if the inverter can start, and replacement if it keeps alarming and cannot start. Other inverter datasheets specify DC current injection as a small fraction of rated output current. Check the limit that applies to the unit you are working on.

<!-- review notes
- sentence 1: support check: partial - The passage lists monitoring of DC injection from AC output as a protection function, but doesn't state that high DC injection means the monitoring found too much DC current.
-->
