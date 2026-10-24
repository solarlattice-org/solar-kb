---
id: method:backup-transition-test
type: DetectionMethod
name: Backup transition test
aliases:
- Test Backup Transition
- simulated grid outage test
- main breaker off test
- Testing automatic backup operation
- Test backup operation
- Test Island Mode
claims:
- claim_id: c1
  rel: produces
  target: meas:zero-ac-grid-voltage
  note: With the main breaker off, the line (grid) side of the backup interface should read 0 VAC across
    L1-L2, L1-N and L2-N, which confirms the grid is isolated.
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-08-backup-interface-installation-and-wiring
    loc: sec=h6
    h: 6eba64aae6ab
  review: drafted
  review_note: 'review: partial - The passage gives 0 VAC on the line side for L1-L2, L1-N and L2-N with
    the Main breaker off, but it never says this confirms the grid is isolated.'
- claim_id: c2
  rel: produces
  target: meas:backup-load-voltage-present
  note: The load side of the backup interface should show normal split-phase voltage. All loads on the
    backup circuit should be powered once the configured grid-fault delay has passed.
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-08-backup-interface-installation-and-wiring
    loc: sec=h6
    h: 6eba64aae6ab
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: sec=h85
    h: d64eb21249a5
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c3
  rel: produces
  target: meas:transfer-switch-audible-click
  note: An audible click means the automatic transfer switching device has changed over, both into backup
    operation and back to grid-parallel operation.
  cite:
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: sec=h85
    h: d64eb21249a5
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
A backup transition test simulates a grid outage to confirm that a battery-backed system moves its backed-up loads onto backup power and later returns to the grid. To start it, switch off the main breaker, the pre-meter fuse or the breaker feeding the transfer switch, then wait for the configured grid-fault delay. After the wait, measure AC voltage at the backup interface: the line side should read zero, and the load side should show normal line-to-line and line-to-neutral voltage. The transfer switch should click as it changes over, and every load on the backup circuit should be powered. When the grid breaker is switched back on, it should click again as it returns to grid-parallel operation. Before the test, check that islanding is enabled, that the number of transfer switches is set correctly, that the protected loads breaker is on, and that a backup-capable system mode is selected. The test shows the owner how the system will behave in a real outage, reveals backed-up load demand that is too high, and confirms the system works properly. Electrical layouts vary from site to site, so the operator must adapt the procedure to each one. After the test the inverter may wait several minutes before it reconnects to the grid. For anti-islanding checks, switch off the solar backfeed breaker or the solar AC disconnect so that absence of voltage can be measured correctly.
