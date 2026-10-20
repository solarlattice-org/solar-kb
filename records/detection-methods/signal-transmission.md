---
id: method:signal-transmission
type: DetectionMethod
name: Signal transmission method
aliases:
- STM
- Signal Transmission Device
- STD
claims:
- claim_id: c1
  rel: produces
  target: meas:stm-no-signal-at-ribbon
  note: The receiver cannot pick up the test signal at the point where a single cell interconnect ribbon
    is disconnected, but still picks it up on ribbons that are connected.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.6
    h: abaa389f3b5e
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=24.r1
    h: fa856767e325
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:stm-no-signal-on-submodule
  note: Seen when every interconnect ribbon of one cell, or a string interconnect, is disconnected. The
    signal then goes through the bypass diode, so it cannot be found anywhere on that submodule.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.6
    h: abaa389f3b5e
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=24.r2
    h: efef0762eda5
  review: drafted
- claim_id: c3
  rel: produces
  target: meas:stm-signal-on-shaded-submodule
  note: Points to an open-circuit bypass diode. The submodule is shaded on purpose (for example with a
    rubber sheet), and the signal is still found on it instead of passing through the diode.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.6
    h: abaa389f3b5e
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=24.r3
    h: af88837daede
  review: drafted
---
The signal transmission method uses a small, light, low-cost device with two parts. A transmitter injects a small alternating test current into the circuit, and a receiver senses the magnetic flux that current creates. The device was first made for general electrical work, such as finding earth-leakage points and tracing wires inside walls. Applied to the DC circuit of a PV array, it can find interconnect ribbon disconnections and open-circuit bypass diodes. Stop the PV system first. Then connect the transmitter to the target string at the combiner box and move the receiver along the interconnect ribbons on the front or back of each module. For Cell Interconnection Failure: if one ribbon is disconnected, there is no signal at the break. If all ribbons of a cell are disconnected, there is no signal anywhere on that submodule, because the current goes through its bypass diode. To check for Bypass Diode Failure, shade one submodule with something like a rubber sheet so its diode turns on. A healthy diode carries the signal around the submodule, so if the signal still shows up on the shaded submodule, the diode is open-circuit. In one field example, the results of this method fully matched an EL image showing two cells with disconnected ribbons. Compared with EL imaging, which is mostly done indoors and costs a lot, this method is cheap and easy to use in the field, and the modules stay installed.
