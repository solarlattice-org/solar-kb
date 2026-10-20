---
id: meas:afci-self-test-fault
type: Measurement
name: AFCI self-test fault result
aliases:
- interference level too high
- interference level too low
---
This signature is an error the inverter reports when its arc-fault circuit interrupter fails its own self-test. The self-test checks whether the inverter's arc detection function, which watches the DC cabling for arcs, is working normally. On some inverters the test is started by hand from the display menu. When it passes, the display shows a pass message, the inverter shuts down and then starts up again. On SMA inverters, a failed self-test is logged as an event saying the interference level was too high or too low. For event 8209, the SMA manuals say to contact the Service, because only the Service can find the cause. Some manuals include a figure showing the AFCI test result screen, which tells you whether the test passed.

<!-- review notes
- sentence 4: support check: partial - The messages say interference level too high/low, but the passages shown do not explicitly name SMA, and only 8209 (too low) has an event number.
- sentence 6: support check: partial - Figure captions for AFCI test result exist, but nothing says the screen shows whether the test passed.
-->
