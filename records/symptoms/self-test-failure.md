---
id: symptom:self-test-failure
type: Symptom
name: Self-test failure
aliases:
- Open-loop self-check failure
- Abort self-test
---
A self-test failure means a device's built-in check of its own critical subsystems found a condition outside tolerance. First, restart the inverter: turn both the AC and DC switches off, wait for the energy to discharge, then turn both back on. The manuals give 1 minute for Protect0230 and 5 minutes for Fault0150. If the fault does not clear after the restart, the CPS manuals say to replace the inverter. On SMA STP inverters, a failed self-test of the arc-fault circuit interrupter must be investigated by Service. An aborted grid self-test (Italy only) calls for checking the AC connection and running the self-test again.

<!-- review notes
- sentence 4: support check: partial - Arc-fault self-test error requiring Service and the Italy-only abort with AC connection check are supported; 'running the self-test again' comes only from an unattributed 'Restart the self-test' passage (u27) not tied to event 9007, and 'must' and 'STP' are not explicit.
-->
