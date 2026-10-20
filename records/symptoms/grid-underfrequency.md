---
id: symptom:grid-underfrequency
type: Symptom
name: Grid underfrequency
aliases:
- Underfrequency
claims:
- claim_id: c1
  rel: observed_as
  target: meas:grid-frequency-reading-out-of-limit
  note: Inverter reports grid underfrequency (e.g. fault code 9/009) when measured grid frequency is below
    its lower limit; storage systems may flag a Grid Uncompliant alert for over/underfrequency beyond
    hardware trip thresholds.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r2
    h: 097b3595b2db
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r2
    h: 22c6c28d3439
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=79.r6
    h: 559b8ecfd60c
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=127.r2
    h: 1b31052ab9d4
  review: drafted
  review_note: 'support check: partial - Fault 9 and Grid Uncompliant alert are supported, but the passages
    don''t state the inverter output drops while below a reconnection threshold or the specific ''configured
    trip threshold'' wording; the frequency reading is documented but not the pattern.'
---
The inverter raises a grid underfrequency fault when the grid frequency it measures drops below its configured lower limit. Look at the logged grid frequency reading and see if it fell below the underfrequency trip threshold before the event. First measure the actual grid frequency on site. If it is outside the set range, the cause is on the grid side, so contact the local utility. If the grid frequency looks normal, check in the app or on the LCD that the protection parameters are set correctly. Trip and reconnection thresholds can be changed, and default values differ by product, for example 58.5 Hz or 59.3 Hz. The inverter reconnects only after the frequency rises back above a separate underfrequency reconnection threshold. On some storage systems this condition shows up as a general Grid Uncompliant alert that covers both voltage and frequency excursions. If grid and settings causes are ruled out and the fault keeps coming back, contact the manufacturer's service.

<!-- review notes
- sentence 2: support check: partial - Passages give a grid frequency reading and underfrequency trip thresholds, but nothing states this diagnostic step of comparing the logged reading to the threshold before the event.
- sentence 5: support check: partial - A separate underfrequency reconnection threshold exists, but the passages do not explicitly state the inverter reconnects only after frequency rises back above it.
-->
