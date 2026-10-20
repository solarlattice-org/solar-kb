---
id: meas:afci-self-test-pass
type: Measurement
name: AFCI self-test pass result
aliases:
- AFCI Test Pass!
---
A pass result means the inverter ran its arc fault self-test and found the internal arc detection circuit working. The test is started by hand: set the AFCI self-test mode in the inverter menu from disabled to enabled. On some inverters, a pass shows the message AFCI Test Pass! on the display, and then the inverter shuts down. After a pass, the mode setting goes back to disabled by itself. The inverter restarts and shows normal operation again. The short shutdown after a pass is expected and is not a fault. A failed self-test shows up as an error event instead, such as an interference level that is too high or too low. Its cause has to be found by the manufacturer's service.

<!-- review notes
- sentence 5: support check: partial - The shutdown and restart as part of a pass is described, but the passages never say it is expected or not a fault in those words (implied only).
-->
