---
id: symptom:grid-loss
type: Symptom
name: Grid loss
aliases:
- Grid outage
- Grid Meter Offline
claims:
- claim_id: c1
  rel: observed_as
  target: meas:zero-ac-grid-voltage
  note: PowerTrack moves downtime loss into the Grid Meter Offline category when the meter linked to the
    inverter reads zero AC voltage. Downtime loss and grid meter offline loss cannot both apply at the
    same time.
  cite:
  - src: src:alsoenergy-kb-pv-model-losses
    loc: sec=front
    h: 10001d881d82
  review: drafted
  review_note: 'support check: partial - Passage supports that zero meter AC voltage moves downtime to
    Grid Meter Offline and that both can''t coexist, but says nothing about grid loss being observed as
    zero AC grid voltage or the phase-voltage/power signal patterns.'
- claim_id: c2
  rel: observed_as
  target: meas:zero-power-at-irradiance
  note: Downtime loss is flagged when irradiance is high enough for the inverter to run but output is
    zero or below. Early-morning and evening data are filtered out.
  cite:
  - src: src:alsoenergy-kb-pv-model-losses
    loc: sec=front
    h: 10001d881d82
  review: drafted
  review_note: 'support check: partial - Downtime loss definition (enough irradiance, power ≤ 0, early/late
    filtering) is stated, but the passage never links it to grid loss as an observation.'
---
Check the AC voltage at the grid meter first: if the meter tied to the inverter reads zero volts, the loss counts as grid meter offline, not as inverter downtime. Failure-detection schemes list grid outage as its own failure pattern, separate from a defective inverter or defective control devices. To tell them apart, look at daily and hourly energy loss, how long the event lasted, and whether neighbouring systems went down at the same time. Do not confuse grid loss with grid curtailment: curtailment holds output at a flat, controlled level below available power, and the equipment still looks available. Some inverters wait for the grid to return to normal before reconnecting. If the grid fault keeps coming back, measure the actual grid and contact the utility if the readings are outside the set range. Contact the inverter manufacturer only after grid causes have been ruled out and the fault continues.

<!-- review notes
- sentence 1: support check: partial - Passage states that zero AC voltage on the associated meter makes the loss Grid Meter Offline rather than Downtime, but does not say to check it first (ordering/procedure).
- sentence 3: support check: partial - The table lists daily/hourly energy loss, duration and spatial dimension as analyzed aspects for all failures, but doesn't say these distinguish grid outage or that neighbours going down simultaneously is the test.
- sentence 4: support check: partial - Passage gives the flat controlled output below available power with normal availability for curtailment, but doesn't contrast it with grid loss or give the 'do not confuse' instruction.
- sentence 5: support check: partial - Repeated-fault advice to measure the grid and contact the utility if out of range is stated, but the evidence is truncated and only implies waiting for grid return to normal ('grid after the grid returns to normal').
-->
