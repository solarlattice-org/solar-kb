---
id: method:fan-supply-voltage-check
type: DetectionMethod
name: Fan supply voltage measurement
claims:
- claim_id: c1
  rel: produces
  target: meas:fan-supply-voltage-low
  note: Measured between the red and black wire pins at the external fan connector of a non-spinning fan.
    A reading below 6 VDC means the inverter is not supplying the fan, so the manual calls for replacing
    the inverter.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=55.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2
    h: e78dae227e3f
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31
    h: e78dae227e3f
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:fan-supply-voltage-normal
  note: If a fan is not spinning but its connector reads above 6 V, the supply is present and the fan
    itself has failed. The manual calls for replacing the fan.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=55.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2
    h: e78dae227e3f
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31
    h: e78dae227e3f
  review: drafted
---
First, see whether the fan is turning. If the fan spins while the warning is active, the fan-sensing circuit is at fault and the inverter should be replaced. If the fan is not spinning, remove the six bolts that hold the two external fans. Then open the white snap-on connector and measure the voltage between the pins on the red and black wires. A reading below 6 VDC means the inverter is not supplying the fan, and the inverter should be replaced. A reading above 6 V means the fan itself has failed and should be replaced. The same alarm can also come from a blocked fan, a fan at the end of its service life, or poor contact at the fan socket connector. Check for foreign objects on the blades before taking measurements. Before taking the fans apart, the manual suggests watching for 5 minutes to see if the alarm clears by itself. If it does not, switch the external AC disconnect off and back on to reboot. Contact post-sales service if the fault remains.

<!-- review notes
- sentence 3: support check: partial - Replace-inverter below 6VDC and replace-fan above 6V are stated, but the interpretation that the inverter is not supplying the fan or that the fan has failed is not stated explicitly.
- sentence 5: support check: partial - The 5-minute observation, AC disconnect reboot, and contacting post-sales service are listed, but the passages do not say these come before taking the fans apart, and the reboot step is not conditioned on the alarm failing to clear (it follows the foreign-object check).
-->
