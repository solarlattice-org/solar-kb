---
id: symptom:periodic-grid-disconnection
type: Symptom
name: Scheduled periodic grid disconnection
aliases:
- Periodic GridOff
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Warning code W048 with the message 'Periodic GridOff'. It is raised when the inverter disconnects
    and reconnects on its own to run the Riso (insulation resistance) test.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r8
    h: 1c552187e7fa
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r4
    h: c89977a731af
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r4
    h: c89977a731af
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r3
    h: c86bbae59d8b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r5
    h: ed6a6728cb2f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r5
    h: ed6a6728cb2f
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
When the inverter reaches the grid connection time limit set by the grid standard, it disconnects from the grid by itself and then reconnects. The disconnection is there so the inverter can run its Riso insulation resistance test. The manuals say this alarm is not an error, because safety regulations require the automatic disconnection. Check first how often the event happens: if the inverter disconnects sooner than the expected interval, contact the manufacturer's customer assistance.

<!-- review notes
- sentence 4: support check: partial - The contact-assistance advice for disconnections shorter than expected is stated, but the passages don't say to check frequency first or give an expected interval.
- sentence 4: review: partial - Contacting customer assistance when the inverter disconnects sooner than expected is stated, but the instruction to check frequency first is not.
-->
