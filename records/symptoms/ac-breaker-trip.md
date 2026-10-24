---
id: symptom:ac-breaker-trip
type: Symptom
name: AC circuit breaker tripping
aliases:
- AC Trip
- AC MCB tripping
- RCBO tripping
claims:
- claim_id: c1
  rel: observed_as
  target: meas:zero-ac-grid-voltage
  note: When the AC breaker opens, the inverter loses its grid connection. It may then show a NO-GRID
    code (Solis 1015) or a 'Waiting for grid voltage / Grid failure' message that tells you to check the
    AC circuit breaker (SMA).
  cite:
  - src: src:kb-solis-44002485766-1015-no-grid-ac-mcb-tripping
    loc: sec=front
    h: df67875747d5
  - src: src:kb-solis-44001815757-ac-breaker-trips-steps-to-diagnose-and-resolve-issues
    loc: sec=h1
    h: 07a99f956f58
  - src: src:kb-solis-44002485766-1015-no-grid-ac-mcb-tripping
    loc: sec=h1
    h: 33303fa86332
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h169
    h: 0d3c0d95a150
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h252
    h: 0d3c0d95a150
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h254
    h: 0d3c0d95a150
  review: drafted
  review_note: 'support check: partial - Passages support the NO-GRID 1015 code and SMA ''Grid failure
    > Check AC circuit breaker'' message, but nothing states that phase voltage or frequency reads zero
    when the breaker trips.'
- claim_id: c2
  rel: observed_as
  target: meas:zero-ac-output
  note: The trip cuts the connection between the inverter and the grid, so the inverter cannot feed any
    power into the grid.
  cite:
  - src: src:kb-solis-44001815757-ac-breaker-trips-steps-to-diagnose-and-resolve-issues
    loc: sec=h1
    h: 07a99f956f58
  review: drafted
  review_note: 'support check: partial - Passage says the trip cuts the inverter-grid connection, which
    implies no feed-in, but it doesn''t state power or current falling to zero.'
- claim_id: c3
  rel: observed_as
  target: meas:ac-breaker-status-open
  note: On Tesla Megapack, the AC Breaker Status point reads 1 when the breaker is closed and 0 when it
    is open.
  cite:
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=88.r7
    h: 0b5cb225f0fe
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=78.r7
    h: 0b5cb225f0fe
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=95.r7
    h: 0b5cb225f0fe
  review: drafted
---
An AC trip happens when the AC circuit breaker between the inverter and the grid opens, which disconnects the inverter from the grid. In monitoring this usually shows up as a no-grid or grid-failure alarm on the inverter, with a prompt to check the AC circuit breaker. On some storage systems a breaker status point changes from closed to open. Note when the trip happens: at grid connection, during startup, while generating power, at random, or at a set time. This helps narrow down the cause. One test is to see whether it still trips with power limited to 10% and then 20%. Check the breaker rating first. A breaker that is too small or has built-in current protection can cause nuisance tripping. The rating should be 1.2 times the inverter's maximum AC output current. If the correctly sized breaker still trips, it may have degraded over time. Replace it with a new one of the correct rating to rule out a hardware fault. Inspect the breaker terminals, AC connector, AC distribution board and meter side for loose or damaged wiring. Measure phase-to-phase, phase-to-neutral and neutral-to-earth voltages at the inverter AC gland, so you can catch AC wiring errors such as shorted phases. If the inverter keeps reporting grid failure, the AC cable may be connected wrongly or the country data set may be configured wrongly. This points to a wiring error or a grid code setting problem rather than a breaker fault.

<!-- review notes
- sentence 6: support check: partial - Inspection of terminals, AC connector, ACDB and meter side and the voltage measurements at the AC gland are stated, but 'shorted phases' is only loosely backed by the note about customers shorting 2 phases to 3.
- sentence 7: support check: partial - The wrong AC cable connection or country data set cause is stated, but the conclusion that this points away from a breaker fault is not.
-->
