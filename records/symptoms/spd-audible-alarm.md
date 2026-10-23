---
id: symptom:spd-audible-alarm
type: Symptom
name: SPD audible alarm
claims:
- claim_id: c1
  rel: observed_as
  target: meas:spd-red-status-led
  note: The audible alarm sounds when a phase or neutral/ground LED on the SPD display turns red, which
    means protection is lost on that mode.
  cite:
  - src: src:eaton-eaton-spd
    loc: sec=3.2
    h: 413badbb96aa
  - src: src:eaton-eaton-spd
    loc: tbl=7.r8
    h: e5d6e169f09a
  - src: src:eaton-eaton-spd
    loc: tbl=7.r4
    h: 0296e9cdc4cc
  - src: src:eaton-eaton-spd
    loc: tbl=7.r6
    h: 4f67694d74a3
  - src: src:eaton-eaton-spd
    loc: tbl=8.r3
    h: 6ac33fcf20dc
  - src: src:eaton-eaton-spd
    loc: tbl=8.r4
    h: 28c46d3ae071
  - src: src:eaton-eaton-spd
    loc: tbl=7.r7
    h: '019039e56176'
  - src: src:eaton-eaton-spd
    loc: tbl=7.r5
    h: 5c6573ea8467
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:spd-alarm-status-register
  note: On Power Xpert SPD units, a read-only alarm status value reports protection status, and one enumerated
    value means the alarm has been silenced.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=16.r17
    h: d7bbaba2d6d8
  - src: src:eaton-eaton-spd
    loc: tbl=17.r19
    h: a855b7fd3550
  review: drafted
  review_note: 'support check: partial - Passages show a Power Xpert alarm status UINT8 RO with value
    9 ''Alarm silenced'', but ''one enumerated value'' is fine; the link to the audible alarm is implied,
    though not fully explicit.'
---
The SPD gives an audible alarm on units fitted with one, and it sounds when any LED on the display panel turns red. A red LED means that phase or mode has lost protection. Look at the display first. A red phase LED with the alarm on points to lost phase protection, often after a significant surge event, and the fix is to replace the SPD. If every phase LED is red, the SPD rating may be below the system voltage, or there may be an extended temporary overvoltage. Fix the overvoltage source or fit the correct voltage model before you replace the unit. A red neutral-to-ground LED with the alarm on means neutral-to-ground protection is compromised. The SPD should be replaced. If the alarm sounds while all phase LEDs stay green, the likely cause is low voltage reaching the SPD power supply rather than an exhausted surge protector. A red LED with no alarm usually means someone pressed the silence button. If the fault is still there when power is cycled, the alarm comes back on. In normal operation the alarm is off and the form C normally closed contact stays closed. Power Xpert units also report alarm status, including a silenced state, through a status register.

<!-- review notes
- sentence 3: support check: partial - Causes (rating below system voltage, extended TOV) are stated, but the solution says replace SPD, check TOV sources, or replace with the correct model; 'before you replace the unit' ordering is not stated.
- sentence 5: support check: partial - Cause is insufficient voltage to the power supply, but the passage's solution is replace SPD and 'rather than exhausted surge protector' and 'likely' are not stated.
-->
