---
id: mit:inverter-restart
type: Mitigation
name: Inverter restart
aliases:
- Force Restart
- force reboot
---
An inverter restart is a power cycle. You switch both the AC and DC switches off, wait for the stored energy to discharge, and then switch both back on. The manuals give a wait of 5 minutes for most of these codes. For the CPLD fault and the bus hardware overcurrent fault, the wait is 1 minute. After a fault shutdown, the inverter's Control Command menu also offers a Force Restart. It allows one forced reboot. If an inverter is not running even though production conditions are good, a common reason is that it did not restart after a grid fault or an isolation fault. A restart is the first corrective action listed, followed by replacing defective components and updating the software. If the restart does not clear the fault, the manuals say to replace the inverter, or for some codes the control board or filter board. If a restart fails or the fault keeps coming back, a service team usually has to find the cause. Restart the inverter only after any fault that affects safety has been removed.

<!-- review notes
- sentence 2: support check: partial - 5 min for Fault0020/0100 and 1 min for CPLD and bus overcurrent are stated, but 'most of these codes' is loosely framed since other codes (0090, 0110) have no wait.
-->
