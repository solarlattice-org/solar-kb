---
id: symptom:optimizer-not-reporting
type: Symptom
name: Power optimizer not reporting
aliases:
- No Communication with Power Optimizer
- No String Communication
- non reporting optimizer
- string down
claims:
- claim_id: c1
  rel: observed_as
  target: meas:zero-power-at-irradiance
  note: 'Typical non-reporting case: a monitoring alert plus no production from one or two non-contiguous
    optimizers while the other optimizers keep producing.'
  cite:
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h9
    h: 340119fa6bbd
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:optimizer-paired-count-low
  note: The inverter status screen shows P_OK xxx/yyy where the first number is smaller than the second.
    The missing optimizers can be identified on the LCD.
  cite:
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: sec=h210
    h: 4450763dce6f
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: sec=h253
    h: ae31bc2b5499
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:zero-dc-voltage
  note: A string voltage of 0V points to a disconnected power optimizer output.
  cite:
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: tbl=11.r2
    h: fecee5e83d43
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=17.r2
    h: fecee5e83d43
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: tbl=12.r2
    h: 1c0d0a76f145
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: tbl=11
    h: 2c6603d5788e
  review: drafted
  review_note: 'support check: partial - Passages say 0V string voltage means optimizer output disconnected,
    but do not link it to a non-reporting optimizer or to the specific signal.'
- claim_id: c4
  rel: observed_as
  target: meas:string-voltage-below-optimizer-count
  note: String voltage is above 0V but lower than the number of optimizers. Possible causes are an optimizer
    not connected in the string, a module not connected to an optimizer input, or reversed string polarity.
  cite:
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: tbl=12.r3
    h: b7d481fe4a28
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: tbl=11.r3
    h: 412c65f91086
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=17.r3
    h: 412c65f91086
  - src: src:solaredge-solaredge-hd-wave-setapp-installation-guide-na-man-01-00541
    loc: tbl=14.r3
    h: 68c5dcae89c8
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=17
    h: 2c6603d5788e
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: tbl=11
    h: 2c6603d5788e
  review: drafted
- claim_id: c5
  rel: observed_as
  target: meas:optimizer-safety-voltage-missing
  note: With the string wires disconnected, a faulty optimizer is the one whose output does not show the
    1V safety voltage.
  cite:
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: tbl=12.r6
    h: bcad92bf266a
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: tbl=12.r1
    h: 3de003f378a5
  review: drafted
  review_note: 'support check: partial - The passage describes finding the optimizer lacking 1V safety
    voltage with wires disconnected, but frames it as a malfunction under high string voltage, not as
    a non-reporting observation.'
---
The monitoring platform raises this alert, not the inverter, when it gets no communication from one power optimizer or from a whole string of them. On the inverter, the status screen shows fewer reporting optimizers than installed ones in the P_OK count, and the LCD can identify which optimizers are missing. If only one or two scattered optimizers have no production while the rest produce, likely causes are the connections, the module or a power optimizer failure. Lift the panel, check the connections and measure the DC voltage of the optimizer and the module. Before sending anyone to site, check the logical layout in the portal. The optimizer may already have been replaced without its serial number being updated, or it may never have been assigned to a string. If a whole string is down, a wiring fault is more likely than the optimizer. Measure the string DC voltage at ground level, then start the roof inspection at the junction boxes and connectors. A string voltage of 0V points to a disconnected optimizer output. A voltage above zero but below the optimizer count points to an optimizer missing from the string, a module not connected to its optimizer, or reversed polarity. To find a faulty optimizer, disconnect the string and measure each optimizer output. The one without a 1V safety voltage is the suspect, and its connections, polarity and module should be checked. Remote pairing may bring the optimizers back, but a wiring fault that changes resistance can take the string down again, so bring a spare optimizer to site.

<!-- review notes
- sentence 1: support check: partial - Passage says the two alerts are generated by the monitoring platform, not the inverter, but doesn't say they fire for one optimizer vs. a whole string explicitly (names imply it).
-->
