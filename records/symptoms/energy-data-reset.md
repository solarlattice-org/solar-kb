---
id: symptom:energy-data-reset
type: Symptom
name: Energy counter reset
aliases:
- Energy data reset
- Energy Reset
claims:
- claim_id: c1
  rel: observed_as
  target: meas:energy-counter-zeroed
  note: On FIMER inverters the stored statistical energy data in EEPROM is zeroed and warning W024 is
    raised with no LED. On revenue meters, a confirmed reset sets the energy data to zero.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r10
    h: f0568d967008
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r10
    h: 608e5eecba01
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r10
    h: 608e5eecba01
  - src: src:sel-735-im-20250228
    loc: sec=h203
    h: 2bd11b3f0c18
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:energy-reset-event-log
  note: The FIMER inverter saves the reset only in its historic event record. Meters log an Energy Reset
    event category and keep the time and date of the last reset.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r10
    h: f0568d967008
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r10
    h: 608e5eecba01
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r10
    h: 608e5eecba01
  - src: src:sel-735-im-20250228
    loc: tbl=199.r4
    h: 1ac874da52a0
  - src: src:sel-735-im-20250228
    loc: sec=h468
    h: 6e85041cbaef
  - src: src:sel-735-im-20250228
    loc: tbl=138.r2
    h: b05f20f92260
  review: drafted
---
An energy counter reset means the stored production or energy totals suddenly go back to zero. On FIMER PVS and UNO-DM inverters it shows up as warning W024, Energy data reset, with no LED lit. The manuals say this is not an error. The customer or installer zeroes the partial energy values on purpose, through the internal webserver or the advanced configuration software. The same warning can also appear after someone replaces the memory card that holds the production statistics. On TRIO inverters, holding the ENTER button for more than three seconds in the Partial statistics menu resets the partial time, energy and peak power counters. The inverter records the reset only in its historic event log, so check that log first to see when the reset happened. Energy meters also let you reset the energy registers. They log the reset as an event and store the time and date of the last reset, which helps you line it up with gaps in the monitoring data. If nobody has a record of resetting the counters, ask the installer or owner, and find out whether the memory card was swapped recently.

<!-- review notes
- sentence 1: support check: partial - W024 Energy data reset with no LED is stated, but the passages don't name PVS or UNO-DM models, nor say totals 'suddenly' go to zero.
- sentence 4: support check: partial - Passage says pressing ENTER over 3 seconds resets all counters in the Partial sub-menu (time, energy, peak power), but doesn't mention TRIO.
- sentence 5: support check: partial - Passages say the information is only saved in the historic event record, but the advice to check that log first to find the time is not stated.
- sentence 6: support check: partial - Meters reset energy, log an Energy Reset event and display the last reset time/date, but the link to aligning with monitoring data gaps is not stated.
- sentence 7: support check: partial - Passages say the reset is done by customer/installer and may occur on memory card replacement, but don't state the advice to ask the installer or owner.
-->
