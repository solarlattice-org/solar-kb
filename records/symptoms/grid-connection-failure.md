---
id: symptom:grid-connection-failure
type: Symptom
name: Grid connection failure
aliases:
- Grid conn. fault
- Grid connection installation failure
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-indicator
  note: The yellow LED on PVS models, or the alarm LED on UNO-DM models, comes on with W046.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r1
    h: 9205e4e0b34b
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r6
    h: a8b1ee8ba45c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r2
    h: 89f7284ff292
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 89f7284ff292
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: observed_as
  target: meas:zero-ac-grid-voltage
  note: One logged cause of W046 is a missing grid during the connection sequence. SMA inverters report
    a similar event as waiting for grid voltage.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r1
    h: 9205e4e0b34b
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r6
    h: a8b1ee8ba45c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r2
    h: 89f7284ff292
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 89f7284ff292
  review: drafted
  review_note: 'support check: partial - Missing grid is a logged cause of W046, but the passages give
    no voltage/power signal patterns or SMA ''waiting for grid voltage'' link (that''s in other passages
    not cited here).; review: partial - The rows support Missing grid as a logged cause of W046, but nothing
    in the cited passages backs the SMA ''waiting for grid voltage'' sentence.'
- claim_id: c3
  rel: observed_as
  target: meas:low-dc-input-voltage
  note: An input undervoltage (Input UV) error during the grid connection sequence also logs W046.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r1
    h: 9205e4e0b34b
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r6
    h: a8b1ee8ba45c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r2
    h: 89f7284ff292
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r2
    h: 89f7284ff292
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: observed_as
  target: meas:grid-voltage-reading-out-of-limit
  note: 'SMA: the connection is refused when the grid voltage or frequency is outside the valid country-specific
    thresholds.'
  cite:
  - src: src:sma-doc-278742
    loc: sec=h830
    h: f302b756ffef
  - src: src:sma-doc-259761
    loc: tbl=11.r1
    h: ed0d1d5925de
  - src: src:sma-doc-278742
    loc: tbl=9.r5
    h: ed0d1d5925de
  review: drafted
  review_note: 'support check: partial - Passages say voltage outside valid thresholds prevents connection
    and grid failure includes country-specific voltage/frequency deviation, but don''t explicitly say
    SMA refuses connection or tie to this fault''s frequency.; review: partial - The SMA passage says
    connection is not possible when the voltage is outside the valid thresholds, but the cited passages
    don''t tie the frequency part of the note, or the word ''country-specific'', to refusing connection;
    those words only appear in…'
---
A grid connection failure means the inverter tried to connect to the utility grid and did not succeed, so it is not feeding power. On FIMER/ABB string inverters this shows as warning W046 'Grid conn. fault', with the yellow or alarm LED lit. The manuals list three causes: no grid present, DC input undervoltage, or someone manually disconnecting the inverter during the connection sequence. SMA inverters report similar events ('Waiting for grid voltage' or 'Grid connection installation failure') and tell you to check the grid and fuses. To tell the causes apart, measure the AC grid voltage and frequency and compare them with the connection thresholds, and check the DC input voltage for an undervoltage condition. The inverter retries on its own. If the fault persists after several attempts, switch the inverter off and on again, and contact customer assistance if it still does not connect.

<!-- review notes
- sentence 1: support check: partial - Passages state the connection to the grid was unsuccessful, but not explicitly that the inverter is not feeding power.
- sentence 4: support check: partial - Event messages listed include those phrases and 'Check grid and fuses', but the passages don't identify them as SMA or as similar to this event.
- sentence 5: support check: partial - Passages give causes (threshold deviations, Input UV) but don't prescribe measuring AC voltage/frequency and DC voltage as a diagnostic procedure.
-->
