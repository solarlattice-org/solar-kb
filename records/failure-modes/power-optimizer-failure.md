---
id: fm:power-optimizer-failure
type: FailureMode
name: Power optimizer failure
aliases:
- Failing optimizer
- defective power optimizer
- defective optimizer
- malfunctioning power optimizer
- optimizer not connected to the PV module
- optimizer not outputting safety voltage
- optimizer down
- Power optimizer(s) malfunction
- non reporting optimizer
claims:
- claim_id: c1
  rel: affects
  target: comp:power-optimizer
  cite:
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: tbl=12.r6
    h: bcad92bf266a
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=18.r3
    h: d2b40070159d
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=18
    h: be3988d02f18
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: tbl=12.r1
    h: 3de003f378a5
  review: drafted
- claim_id: c2
  rel: presents_as
  target: symptom:optimizer-not-reporting
  note: The monitoring platform raises alerts such as no communication with power optimizer; one or two
    non-contiguous optimizers show no production while the others produce.
  cite:
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h9
    h: 340119fa6bbd
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h15
    h: bdb6f66b1bba
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h12
    h: f22f27581a43
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:string-voltage-high
  note: String voltage higher than the number of optimizers in the string can point to a malfunctioning
    optimizer, once extra optimizers or directly connected modules are ruled out.
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
  review: drafted
- claim_id: c4
  rel: presents_as
  target: symptom:string-down
  note: A string that goes down may be caused by an optimizer, but wiring is the more likely cause.
  cite:
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h12
    h: f22f27581a43
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:mlpe-safety-voltage-check
  note: Disconnect the wires between the optimizers in the string and measure each optimizer's output.
    The faulty unit is the one that does not output the 1V safety voltage.
  cite:
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: tbl=12.r6
    h: bcad92bf266a
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=18.r3
    h: d2b40070159d
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=18
    h: be3988d02f18
  - src: src:solaredge-solaredge-system-installation-guide-na-v4-3-unbound-mirror
    loc: tbl=12.r1
    h: 3de003f378a5
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Measure the DC voltage of both the optimizer and the module on site.
  cite:
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h9
    h: 340119fa6bbd
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h12
    h: f22f27581a43
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h17
    h: 5ed399c8170f
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:performance-monitoring
  note: Monitoring platform alerts and the time of the last measurement help find non-reporting optimizers.
  cite:
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h9
    h: 340119fa6bbd
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h15
    h: bdb6f66b1bba
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h12
    h: f22f27581a43
  review: drafted
  review_note: 'support check: partial - Monitoring alerts and last-measurement time are mentioned, but
    the passages do not call this performance monitoring; the claim is a reasonable paraphrase though.'
- claim_id: c8
  rel: mitigated_by
  target: mit:optimizer-replacement
  note: Bring a spare optimizer to site. Record the new serial number so the monitoring layout can be
    updated.
  cite:
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: tbl=12.r6
    h: bcad92bf266a
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=18.r3
    h: d2b40070159d
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h12
    h: f22f27581a43
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h17
    h: 5ed399c8170f
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:wiring-terminal-check
  note: Check the optimizer's connections, polarity, module and voltage.
  cite:
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: tbl=12.r6
    h: bcad92bf266a
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=18.r3
    h: d2b40070159d
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h9
    h: 340119fa6bbd
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: tbl=12.r6
    h: bcad92bf266a
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=18.r3
    h: d2b40070159d
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: If the malfunction cannot be resolved, leave out the faulty optimizer and connect a shorter string.
  cite:
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: tbl=12.r6
    h: bcad92bf266a
  - src: src:solaredge-solaredge-three-phase-synergy-installation-guide-na-v1-5
    loc: tbl=18.r3
    h: d2b40070159d
  review: drafted
- claim_id: c12
  rel: mitigated_by
  target: mit:optimizer-pairing
  note: Remote pairing may restore production, but keep monitoring the string. If wiring changes the resistance,
    the string will likely go down again.
  cite:
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h12
    h: f22f27581a43
  review: drafted
- claim_id: c13
  rel: distinguished_from
  target: fm:cable-defect
  by: method:dc-voltage-measurement
  note: A string that is down is more often a wiring issue. Check the string DC voltage at ground level
    and inspect the junction boxes first. Only on-site checks of optimizer and module voltage confirm
    the optimizer as the cause.
  cite:
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h12
    h: f22f27581a43
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h9
    h: 340119fa6bbd
  review: drafted
---
A power optimizer failure is a malfunction of the module-level DC optimizer in a string, so that the unit no longer works properly. In monitoring it usually appears as one or two optimizers that stop reporting and produce nothing while the others in the string keep producing. It can also show up as a string voltage higher than the number of optimizers, or as a whole string going down, although wiring and junction boxes are the more common causes of a dead string. To confirm it, disconnect the wires between the optimizers and measure each optimizer's output to find the one that does not give the safety voltage. On site, lift the panel, check the connections, and measure the DC voltage of both the optimizer and the module. Check the faulty unit's connections, polarity, module and voltage, then contact the manufacturer and replace the optimizer. If it cannot be fixed, bypass it with a shorter string. Bring a spare optimizer to site and record the new serial number so the monitoring layout can be updated.
