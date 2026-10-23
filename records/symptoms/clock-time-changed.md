---
id: symptom:clock-time-changed
type: Symptom
name: Clock time changed
aliases:
- date/time changed
- Date/time mod.
- W023
- Time adjusted / new time
claims:
- claim_id: c1
  rel: observed_as
  target: meas:datetime-change-event-log
  note: Warning W023 has no LED. The date/time change is only written to the inverter's stored event history.
    It is made by the customer or installer through the web interface, the configuration software or the
    display.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r9
    h: 297e19e7a46b
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r9
    h: f948f5938c4c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r9
    h: f948f5938c4c
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=51.r8
    h: 0081a0ca8b5c
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r9
    h: e0a1f09213fe
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
Warning W023 is recorded when someone changes the inverter's date or time through the web interface, the advanced configuration software or the display. The manuals say this is not an error: no LED lights, and the change is only saved in the inverter's event history, so no repair is needed when the change was intended. Do not confuse it with W013 Clock Fail. W013 appears when the displayed time differs from the microprocessor's internal time by more than one minute, which points to a clock circuit malfunction (real-time clock failure); it comes with a flashing yellow or alarm LED. If the date reset, replace the clock battery with the inverter fully switched off, keeping the polarity correct; if the clock alarm keeps returning, contact customer assistance. On other devices, wrong timestamps can come from a clock that is not synchronized or from a backup supercap drained during a long power loss; set the clock and use SNTP to keep the time accurate.

<!-- review notes
- sentence 2: support check: partial - Not an error, no LED, and history-only are stated; 'no repair needed when intended' is implied but not explicitly stated.
-->
