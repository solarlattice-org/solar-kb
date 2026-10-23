---
id: method:phase-current-measurement
type: DetectionMethod
name: Phase current measurement
aliases:
- Secondary Current Measurement
claims:
- claim_id: c1
  rel: produces
  target: meas:negative-sequence-current-imbalance
  note: Negative-sequence current is the listed way to find two crossed phases, and one of the listed
    ways to find a CT wired to the wrong tap.
  cite:
  - src: src:sel-acselerator-quickset-instruction-manual
    loc: tbl=47
    h: 6ad65973ecf9
  - src: src:sel-acselerator-quickset-instruction-manual
    loc: tbl=47.r2
    h: 5e78d8aee3e3
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:phase-angle-deviation
  note: Incorrect CT polarity is found by comparing the angle of each phase with a reference phase.
  cite:
  - src: src:sel-acselerator-quickset-instruction-manual
    loc: tbl=47
    h: 6ad65973ecf9
  review: drafted
- claim_id: c3
  rel: produces
  target: meas:current-magnitude-mismatch
  note: Comparing the expected current with the measured current magnitude points to a CT wired to the
    wrong tap.
  cite:
  - src: src:sel-acselerator-quickset-instruction-manual
    loc: tbl=47
    h: 6ad65973ecf9
  review: drafted
---
Phase current measurement records the current in each AC phase through current transformer secondary inputs. Each phase, A, B and C, has its own in and out terminals. A metering relay manual lists phase current checks for finding errors in the operating current: magnitude, negative-sequence current and phase angle. A high negative-sequence current points to two crossed phases. If the measured current magnitude does not match the expected value, or negative-sequence current appears, the CT may be connected to the wrong tap. To find incorrect CT polarity, compare the angle of each phase against one reference phase. The magnitude check also shows when the load current is too low for a valid test. Inverter readings are less precise than a dedicated meter. One inverter reports AC current as a three-phase average. Stated accuracy is 1 percent of AC current for one inverter family and plus or minus 3 percent for another.

<!-- review notes
- sentence 3: support check: partial - Table pairs two crossed phases with negative-sequence measurement but does not explicitly say a high value indicates it.
- sentence 7: support check: partial - Passages give three-phase average current and 1% vs ±3% accuracies, but the claim that inverter readings are less precise than a dedicated meter is not stated.
-->
