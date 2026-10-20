---
id: symptom:ac-overcurrent
type: Symptom
name: AC overcurrent
aliases:
- AC instantaneous overcurrent
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ac-instantaneous-overcurrent-event
  note: Reported as an inverter fault code (Sungrow code 007) when the AC output current goes above the
    inverter's upper current limit.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r3
    h: c8a06567896b
  review: drafted
  review_note: 'support check: partial - Code 007 and the current-exceeds-limit description are stated,
    but the passage says nothing about the current signal''s waveform or about power dropping to zero
    and returning (only reconnection after the grid recovers).'
---
AC overcurrent is an inverter fault that is reported when the AC output current goes above the inverter's upper current limit. In monitoring data, it appears as an inverter fault code for an instantaneous AC overcurrent, and the inverter stops feeding the grid. The inverter usually reconnects to the grid by itself once the grid is back to normal, so a single event often needs no action. If the fault keeps coming back, record how often it happens and contact the inverter manufacturer. A revenue meter may stop logging peak demand, maximum values and energy while its overcurrent elements are active, so meter records can leave out the event itself.

<!-- review notes
- sentence 2: support check: partial - The fault code is stated, but the passage doesn't say the inverter stops feeding the grid (only implied by reconnection).
- sentence 3: support check: partial - Reconnection after the grid returns to normal is stated, but the passage doesn't say no action is needed for a single event.
- sentence 4: support check: partial - Contacting SUNGROW if the fault repeats is stated, but recording how often it occurs is not.
- sentence 5: support check: partial - The SEL-735 doesn't record peak demand, maximum metering, energy or crest factors while overcurrent elements are asserted, but the passage is specific to that meter and doesn't say records may omit the event.
-->
