---
id: symptom:islanding-detected
type: Symptom
name: Islanding detected
aliases:
- island condition
- islanding condition
claims:
- claim_id: c1
  rel: observed_as
  target: meas:zero-ac-grid-voltage
  note: The manual treats an islanding condition as a loss of AC voltage at the inverter. Production stops
    until the event ends.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r3
    h: c2e7279a7a24
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
  review_note: 'support check: partial - The manual says islanding means no AC voltage and production
    ceases until the event ends, but the passage does not state power returns when the grid returns or
    specific signal behavior beyond that.'
- claim_id: c2
  rel: observed_as
  target: meas:islanding-breaker-open
  note: The Breaker Closed register reads 0 when the islanding breaker is open and the system is running
    off-grid.
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=116
    h: 7d574d783445
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=127
    h: 41aab1d799e4
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=116.r1
    h: 1b47d85da3b9
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=127.r6
    h: 1b47d85da3b9
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:grid-ok-flag-false
  note: Grid OK is a boolean that is true only when the grid voltage and frequency are inside the islanding
    controller's reconnect thresholds. When it is false, the grid is not yet fit for reconnection.
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=116.r2
    h: 7614f05ee8a8
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=61.r10
    h: dac1f80151b8
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=127.r7
    h: 7614f05ee8a8
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=60.r10
    h: dac1f80151b8
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=162.r3
    h: 398ba7f4657f
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=182.r6
    h: 398ba7f4657f
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=116
    h: 7d574d783445
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=127
    h: 41aab1d799e4
  review: drafted
  review_note: 'support check: partial - Grid OK is defined as voltage and frequency within reconnect
    thresholds, but the passages never link Grid OK false to an islanding detected event or to zero frequency
    readings.'
---
An islanding warning means the inverter has detected an islanding condition, and it stops producing power until the event is over. Systems with active anti-islanding, such as the Sandia Frequency Shift method, detect the island on their own, disconnect from the grid and report a trip. In monitoring data, an islanding controller shows this through its Breaker Closed flag, which reads 0 when the system is off-grid, and its Grid OK flag, which stays false until grid voltage and frequency are back inside the reconnect thresholds. The controller also reports grid-side and microgrid-side voltage and frequency, plus the phase difference used during reconnection, so you can see why reconnection is being held off. First, measure the AC voltage with a CAT III multimeter. If there is no AC voltage, check every AC fuse and breaker and inspect the AC conductors for damage. If AC voltage is present but the inverter still will not connect to the grid, contact the manufacturer's technical support.

<!-- review notes
- sentence 3: support check: partial - Breaker Closed = 0 means off-grid and Grid OK is defined by thresholds, but the passages don't say Grid OK stays false during islanding until thresholds are met, nor tie this to an islanding event.
- sentence 4: support check: partial - The registers for grid and microgrid voltage and frequency and the phase difference are listed, but the passages don't say they explain why reconnection is held off.
-->
