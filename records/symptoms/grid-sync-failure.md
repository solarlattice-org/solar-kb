---
id: symptom:grid-sync-failure
type: Symptom
name: Grid synchronization failure
aliases:
- Grid failure
- Grid Abnormal
- Grid Uncompliant
- Grid incident
claims:
- claim_id: c1
  rel: observed_as
  target: meas:zero-ac-grid-voltage
  note: 'The inverter reports that it is waiting for grid voltage, or reports a grid power outage. Causes
    named in the sources: the AC breaker is open, the AC cable is miswired or loose, or the grid itself
    is out.'
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h252
    h: 0d3c0d95a150
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h169
    h: 0d3c0d95a150
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r3
    h: c338b4abeef8
  review: drafted
  review_note: 'support check: partial - Waiting for grid voltage, grid power outage, breaker and cable
    causes are stated, but zero AC voltage as a measurement is not explicit and the passages don''t say
    the AC breaker is open.'
- claim_id: c2
  rel: observed_as
  target: meas:grid-voltage-reading-out-of-limit
  note: Over- or undervoltage measured beyond the protection trip thresholds blocks connection.
  cite:
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=88.r13
    h: 559b8ecfd60c
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=79.r6
    h: 559b8ecfd60c
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=95.r13
    h: 559b8ecfd60c
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=176.r1
    h: 14b129a5c9bc
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r5
    h: 3c84a7b77032
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:grid-frequency-reading-out-of-limit
  note: Over- or underfrequency, or a very large change in frequency, causes a disconnect.
  cite:
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=88.r13
    h: 559b8ecfd60c
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=79.r6
    h: 559b8ecfd60c
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=95.r13
    h: 559b8ecfd60c
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=176.r1
    h: 14b129a5c9bc
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h159
    h: 00db0741c1e5
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:zero-sequence-imbalance
  note: The Grid Uncompliant point includes zero-sequence overvoltage beyond the hardware trip thresholds.
  cite:
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=88.r13
    h: 559b8ecfd60c
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=79.r6
    h: 559b8ecfd60c
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=95.r13
    h: 559b8ecfd60c
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=176.r1
    h: 14b129a5c9bc
  review: drafted
- claim_id: c5
  rel: observed_as
  target: meas:zero-ac-output
  note: The inverter does not restart after a grid fault, even though production conditions are good.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=34.r1
    h: 20455651a3a5
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=53.r1
    h: 20455651a3a5
  review: drafted
  review_note: 'support check: partial - Passages say the inverter not working despite good production
    conditions often reflects no restart after grid faults, but the specific zero-power and irradiance
    signal values are not stated.'
---
The inverter does not connect to the utility grid, or drops off it, and shows a message such as waiting for grid voltage, grid failure, grid abnormal or grid incident. In monitoring data, AC output stays at zero even though production conditions are good, often because the inverter did not restart after a grid fault; the display or the data log shows the fault code. If the grid itself is the cause, the measured voltage or frequency is outside the trip limits, a zero-sequence overvoltage is present, or the frequency changes very sharply. Usually the inverter reconnects by itself once the grid is back to normal; if the fault keeps coming back, measure the actual grid and contact the utility if its values are outside the set range. Check on site first: is the AC circuit breaker closed, is the AC cable firmly connected to the correct terminals, and does the grid supply power reliably. If the grid is within limits and the wiring is sound, suspect the configuration: a wrong country data set can also prevent connection. If a restart does not clear the fault, or the fault keeps recurring, a service team usually has to find the cause; software issues may be fixed by a firmware update.

<!-- review notes
- sentence 2: support check: partial - The passage supports good conditions, lack of restart after grid faults and fault codes in display or data log, but not explicitly 'AC output stays at zero' or 'often'.
- sentence 6: support check: partial - A wrongly configured country data set is mentioned as a cause, but the ordering ('if grid within limits and wiring sound') is not stated.
-->
