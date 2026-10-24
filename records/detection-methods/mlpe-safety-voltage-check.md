---
id: method:mlpe-safety-voltage-check
type: DetectionMethod
name: MLPE string safety voltage check
aliases:
- open-air DC measurement
- safety voltage 1V per optimizer
- 1 Vdc per module reference voltage
- 1 Vdc per device check
- verify voltage across each PV panel/TS4 assembly
- safety voltage testing
- 1 V per optimizer
- string voltage verification
- Measure DC (open air)
- 1V safety voltage
- standby voltage
claims:
- claim_id: c1
  rel: produces
  target: meas:string-safety-voltage-high
  note: Measured string voltage exceeds the expected value for the number of optimizers. Causes include
    an extra optimizer in the string or a module wired in without an optimizer. The sources call a deviation
    of plus or minus 1% per string reasonable.
  cite:
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=18
    h: be3988d02f18
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: tbl=12.r1
    h: 3de003f378a5
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: tbl=12
    h: 4914ccee6efe
  - src: src:solaredge-solaredge-hd-wave-setapp-installation-guide-na-man-01-00541
    loc: tbl=14.r4
    h: c771fc0be7c6
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:string-safety-voltage-low
  note: Applies when the inverter AC is off (shutdown state). For TS4-F the expected value is 0.6 V per
    unit and for JMS-F about 1 to 2 V per device. A lower reading leads to halving the string to find
    the faulty device.
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  review: drafted
- claim_id: c3
  rel: produces
  target: meas:optimizer-safety-voltage-missing
  note: Found by disconnecting the string and measuring each optimizer on its own. A malfunctioning unit
    does not output the 1 V safety voltage.
  cite:
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=18
    h: be3988d02f18
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: tbl=12.r1
    h: 3de003f378a5
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: tbl=12
    h: 4914ccee6efe
  - src: src:solaredge-solaredge-hd-wave-setapp-installation-guide-na-man-01-00541
    loc: tbl=14.r4
    h: c771fc0be7c6
  review: drafted
- claim_id: c4
  rel: produces
  target: meas:negative-polarity-reading
  note: String polarity is checked with a voltmeter during the safety voltage check.
  cite:
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: tbl=12.r4
    h: 89a10e59cdfb
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: sec=h91
    h: bf1e86d0665b
  review: drafted
  review_note: 'support check: partial - Passages say polarity is checked with a voltmeter, but nothing
    states a negative reading symptom or that it arises in the safety voltage check as such.'
---
This check measures the DC voltage of a string built with module-level power electronics while the inverter is off or disconnected. In that state each optimizer or rapid shutdown device outputs only a small safety voltage instead of the full module voltage. For SolarEdge optimizers the string should read about 1 V for each optimizer in series. Other devices have different standby values, for example 0.6 V per TS4-F unit, about 1 V per JMS-F device, and roughly 0.6 to 0.7 V per APS device. Measure each string on its own before connecting it to other strings or to the inverter. Use a voltmeter accurate to at least 0.1 V, check polarity at the same time, and make sure the modules are in sunlight so the optimizers switch on. A string voltage that is too high points to wiring errors, such as an extra optimizer in the string or a module connected without an optimizer, and means the installation may not have a safe low voltage. To find a power optimizer failure, disconnect the string and measure each optimizer to locate the one without its safety voltage. To find a rapid shutdown device failure, keep halving the string until the faulty unit turns up. A correct safety voltage does not prove every device works. Devices stuck in bypass may only show up as a low operating voltage once the system is running, so also compare the voltage with the system active. Only qualified electrical workers should do this check. Strings can carry lethal voltage in sunlight, so wear protective equipment and confirm cables are dead before you touch them.

<!-- review notes
- sentence 7: support check: partial - Passages cover qualified persons, lethal voltage in sunlight, PPE, and checking cables voltage-free, but the qualified-persons warning comes from a different procedure and not this check specifically.
-->
