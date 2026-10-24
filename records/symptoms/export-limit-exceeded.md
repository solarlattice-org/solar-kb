---
id: symptom:export-limit-exceeded
type: Symptom
name: Feed-in above export limit
aliases:
- Supplied power has exceeded the permitted value
- zero feed-in control deviation
- Inverter does not respond to active power limitation
- Exporting at night
- Export limit exceeded
- phase feeding into the grid despite zero export
- control deviations of 1-2 kW
claims:
- claim_id: c1
  rel: observed_as
  target: meas:export-power-above-limit
  note: Export control monitoring shows a red status bar when power exported at the point of connection
    is over the export limit; a brief red bar after a positive load step is normal, and a red bar is a
    trigger for a fallback plan.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h57
    h: d6e8f90be636
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h24
    h: 84577b17004f
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: 'support check: partial - Red bar over export limit, normal brief red after load step,
    and fallback trigger are stated, but the ''derating off / inverter not curtailed'' condition is not
    stated as such.'
- claim_id: c2
  rel: observed_as
  target: meas:export-limit-exceeded-event
  note: SMA Sunny Home Manager event 10520 logged when power fed in exceeded the permitted value several
    times although active power limitation is enabled.
  cite:
  - src: src:sma-doc-246498
    loc: sec=h470
    h: e6d2bb229353
  - src: src:sma-kb-event-10520-and-message-supplied-power-has-exceeded-the-permitted-value-several-tim
    loc: sec=h1
    h: f30e7546c662
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: observed_as
  target: meas:inverter-ignores-power-limit-event
  note: 'SMA event 10525: at least one inverter does not respond to active power limitation; the controller
    curtails the remaining inverters harder to keep within the limit.'
  cite:
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r85
    h: 4829bdfc7fab
  - src: src:sma-doc-246498
    loc: sec=h476
    h: e2c0f6371b26
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
This symptom means more active power is fed into the grid at the point of connection than the export limit allows, even though export limitation is switched on. It shows in the system logbook as a message that supplied power has exceeded the permitted value several times, or that an inverter does not respond to active power limitation. On export control monitoring screens, a red status bar means exported power is above the limit, while yellow means it is inside the guard band below the limit. A short exceedance after a sudden load change is normal because the control cannot fully prevent it, but it is limited in time; repeated or lasting exceedance points to an export control fault. Check the feed-in or energy meter first: confirm it works and is wired correctly, since a failed or wrongly installed meter breaks the control loop. If the meter is fine and the message keeps coming back, check the inverter active power operating mode so it follows the external or system control setpoint. If an inverter does not respond to limitation, the controller curtails the other inverters harder to stay within the limit; if the exceedance message also appears on the same day, there is a real fault. Check the guard band or negative limit settings too: they give the control a safety margin against load steps and meter inaccuracy.

<!-- review notes
- sentence 3: support check: partial - Red over the limit is stated, and yellow is in the guard band between set point and limit, but the guard band is not stated as 'below the limit' in those exact words (it is between set point and limit, which implies below).
- sentence 4: support check: partial - Short exceedance after load change being normal and time-limited is stated, but 'repeated or lasting exceedance points to an export control fault' is only supported for the SMA repeated message case, not generally.
- sentence 5: support check: partial - Checking the meter works and is correctly connected is stated, but 'first' ordering and the claim that a failed meter breaks the control loop are not stated.
- sentence 8: support check: partial - Guard band as safety margin including measurement accuracy and negative value for load steps are stated, but the passages don't frame it as a troubleshooting check, and meter inaccuracy applies to the guard band only.
- sentence 4: review: partial - The FIMER note supports that a short exceedance after a sudden load change cannot be fully avoided and is time-constrained by the control, but the general claim that repeated or lasting exceedance points to a fault rests only on the…
-->
