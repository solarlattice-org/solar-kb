---
id: symptom:parameter-download-failure
type: Symptom
name: Parameter download failure
aliases:
- Software Parameter Load Failure
---
This symptom shows up as an inverter event: the inverter reports that a remote download of its software parameters did not succeed. The same critical event table also has separate codes for internal communication failures, so check which code was logged before deciding on the cause. First, try updating the inverter firmware and then power cycle the inverter. If the event comes back, contact the manufacturer's technical support. On SMA STP inverters, a successful configuration load is logged as event 10118, Parameter upload complete, so that event shows the parameter transfer worked.

<!-- review notes
- sentence 4: support check: partial - The row says to contact Technical Support, but it does not make that conditional on the event recurring; it lists it as a step after the update and power cycle.
- sentence 5: support check: partial - The passages say event 10118 'Parameter upload complete' means the configuration file loaded successfully, but they don't name SMA STP inverters.
-->
