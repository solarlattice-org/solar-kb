---
id: symptom:clock-battery-low
type: Symptom
name: Clock backup battery low
aliases:
- Batt. Low
- Batt. Flat
- Battery flat
- Buffer battery discharged
- LOWBAT
claims:
- claim_id: c1
  rel: observed_as
  target: meas:clock-reset-to-default-date
  note: After a full AC and DC power-down and restart, the date/time reverting to 01/01/2000 confirms
    the backup battery no longer holds the clock.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r1
    h: 298b1ff70174
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=51.r1
    h: 0c3813490b8a
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r2
    h: 8b477ccac24a
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r2
    h: 8b477ccac24a
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r3
    h: 078ce4c16243
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:inverter-fault-indicator
  note: Warning W012 shows with a flashing yellow LED or the alarm LED. On TRIO units the code does not
    appear on the display.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r1
    h: 298b1ff70174
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=51.r1
    h: 0c3813490b8a
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r2
    h: 8b477ccac24a
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r2
    h: 8b477ccac24a
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r3
    h: 078ce4c16243
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:clock-battery-voltage-low
  note: Some meters report the real-time clock battery voltage as a value and raise a low-battery warning
    bit from a self-test. The self-test limit is a device threshold, not a field value.
  cite:
  - src: src:sel-735-im-20250228
    loc: tbl=376.r4
    h: f669e98185eb
  - src: src:sel-735-im-20250228
    loc: tbl=345.r2
    h: af64f61ce53d
  - src: src:sel-735-im-20250228
    loc: tbl=227.r10
    h: 64ff3002d898
  review: drafted
---
This warning means the inverter has measured a voltage on its internal backup (buffer) battery that is too low. FIMER inverters report it as W012, labelled Batt. Low or Batt. Flat. The warning shows as a flashing yellow LED or the alarm LED. On some models the code is not shown on the display. When the buffer battery is low, the inverter cannot keep its time setting. First check that the date and time are correct, and set them if they are not. Then switch the inverter fully off on both the AC and DC side, wait a few minutes and restart it. If the clock has gone back to 01/01/2000, the battery needs replacing. Replace the battery only with the inverter fully isolated on both the AC and DC side, and keep the correct polarity. Some meters report the clock battery voltage directly and set a low-battery warning bit, which can confirm the problem remotely.

<!-- review notes
- sentence 1: support check: partial - Passages state W012 Batt. Low/Batt. Flat for a too-low buffer battery voltage, but do not name FIMER as the manufacturer.
- sentence 7: support check: partial - Passages show a clock battery voltage and a low-battery warning bit, but do not say this can confirm the problem remotely.
-->
