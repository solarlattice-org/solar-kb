---
id: symptom:clock-time-lost
type: Symptom
name: System clock time lost
aliases:
- Time lost
- Clock Fail
- Invalid system time
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Fronius Galvo, Primo and Symo show status code 751 'Time lost' as a warning on the inverter display.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r12
    h: b25992d57ac3
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r12
    h: b25992d57ac3
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r19
    h: b65c42fb684e
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:clock-reset-to-default-date
  note: After a full AC and DC shutdown and restart, the date and time come back as 01/01/2000 instead
    of the correct value. This points to a failed clock backup battery.
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r3
    h: 521d4f5ca817
  review: drafted
  review_note: 'support check: partial - FIMER W013 mentions reset to 01/01/2000 after restart and battery
    replacement, but it is a Clock Fail alarm and doesn''t explicitly say the cause is a failed backup
    battery as a diagnosis of time lost.'
- claim_id: c3
  rel: observed_as
  target: meas:inaccurate-timestamps
  note: Recorded time stamps are wrong. Causes include an unsynced clock, a backup supercap drained during
    a long power loss, or a real-time clock module running in emergency mode.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=9.r7
    h: a4d4792734d8
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r21
    h: b024f9819b36
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r24
    h: 5ab079e92f2b
  review: drafted
---
The inverter has lost its date and time. On Fronius units this shows up as status code 751, a warning on the display. A wrong system time directly corrupts data logging and the reported power generation values, so a monitoring record with odd time stamps can be the first sign of it. The usual cause is the clock's backup store running flat during a long power outage. Eaton names a drained supercap for this, and FIMER names the clock battery. Separate a simple time loss from a real-time clock failure by the code. A 751 warning only needs the time reset. A 758 means the clock module is in emergency mode and feed-in continues normally. A 757 is a clock hardware error, and the inverter stops feeding the grid. Check first by resetting the date and time on the inverter. If the code keeps coming back, contact a trained service technician. On a FIMER inverter, switch it fully off on both AC and DC, wait, and restart it. If the clock has gone back to 01/01/2000, replace the battery with the unit fully off and the polarity correct. Where the device supports it, use SNTP time sync to keep the clock right. Only move the time back when you have to, because that can overwrite system data already recorded.

<!-- review notes
- sentence 2: support check: partial - u19 says wrong system time directly affects data logging and power generation value, but the claim that a monitoring record with odd time stamps is the first sign is an inference not stated.
- sentence 3: support check: partial - Eaton's drained supercap and FIMER's battery replacement appear, but 'usual cause' and the flat-backup-during-outage cause for FIMER aren't stated.
- sentence 7: support check: partial - SNTP use is supported by u4, and u30 warns against changing time since it may overwrite data, but u30 is about Cluster Controller, not a general device claim.
-->
