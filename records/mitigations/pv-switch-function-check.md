---
id: mit:pv-switch-function-check
type: Mitigation
name: PV switch function check
---
This action is a check that the SunSpec-compliant PV module switches or PV array disconnect switches actually work. SMA lists it as the corrective measure for event 9037, which appears when the switches did not connect the PV module or PV generator, so the inverter reports that the generator is not connected. If event 9038 appears, SMA Service must find the cause. A switch check done on site may not be enough to fix it. For the related Rapid Shutdown warning 9034, installers should confirm that the SunSpec shutdown devices on site appear in SMA's compatibility list and that the inverter runs the latest firmware. Event 9034 is often caused by the keep-alive signal from another inverter's strings that run close by or share a conduit. Updated firmware lets the inverter keep running, but the warning is still reported. More generally, switchgear in a PV system should be function-tested to confirm it works correctly and is properly mounted and connected.

<!-- review notes
- sentence 3: support check: partial - Passages say the cause of 9038 must be determined by the Service, but 'a switch check may not be enough' is an inference, though the row lists the check too.
-->
