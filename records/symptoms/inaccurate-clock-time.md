---
id: symptom:inaccurate-clock-time
type: Symptom
name: Inaccurate clock time
aliases:
- Time stamps inaccurate
- Inaccurate time
- Clock Fail
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inaccurate-timestamps
  note: 'Eaton SPD: time stamps go wrong when the clock is not synced or the supercap has drained during
    a long power loss.'
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=9.r7
    h: a4d4792734d8
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: observed_as
  target: meas:clock-reset-to-default-date
  note: 'FIMER UNO-DM: after a full AC and DC shutdown and restart, the date and time may come back as
    01/01/2000. This points to the clock backup battery.'
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r3
    h: 521d4f5ca817
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r3
    h: 521d4f5ca817
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Reset to 01/01/2000 after full shutdown/restart is stated and
    battery replacement is the remedy, but ''may come back'' as a symptom is okay; the passage doesn''t
    explicitly say the battery is the cause beyond replacing it, and the ''inaccurate clock time'' link
    is implied.'
- claim_id: c3
  rel: observed_as
  target: meas:inverter-fault-indicator
  note: FIMER W013 Clock Fail flashes the alarm LED. It triggers when the displayed time differs from
    the microprocessor's internal time by more than 1 minute.
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r3
    h: 521d4f5ca817
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r3
    h: 521d4f5ca817
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Fronius status code 758, and 753 on the Symo, means the real-time clock module is in emergency
    mode. Time may be inaccurate or lost, but feeding power into the grid continues normally.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r15
    h: '761e75330970'
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r15
    h: '761e75330970'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r21
    h: b024f9819b36
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r24
    h: 5ab079e92f2b
  review: drafted
---
The inverter or device shows a wrong date or time, and logged events carry inaccurate time stamps. On Fronius Galvo, Primo and Symo inverters, status code 758 (753 on the Symo) means the real-time clock module is in emergency mode, while feeding power into the grid continues normally. Tell this apart from code 757, a hardware error in the real-time clock module: with 757 the inverter stops feeding current into the grid, and if the code persists a Fronius-trained technician is needed. Other causes include a clock that was never synced, or a backup supercap that drained during an extended power loss. On FIMER inverters, the Clock Fail alarm flashes the alarm LED when the displayed time drifts from the internal microprocessor time, which indicates a fault in the clock circuit. First reset the date and time on the inverter, and where the device supports it, use network time sync (SNTP) to keep it accurate. On FIMER inverters, if the date returns to a default value after a full AC and DC shutdown and restart, replace the clock battery with the inverter fully isolated, and keep the polarity correct. Correct the time quickly, because a wrong system time directly corrupts data logging and the recorded power generation values.

<!-- review notes
- sentence 2: support check: partial - Code 758/753 meaning is stated, but the passages given don't name Galvo, Primo, Symo models in the text.
- sentence 5: support check: partial - W013 flashes alarm LED and indicates clock circuit malfunction, but the trigger is a difference over 1 minute, not just any drift.
- sentence 8: support check: partial - Passage says wrong system time directly affects data logging and power generation value, but doesn't say 'corrupts' or urge correcting quickly.
-->
