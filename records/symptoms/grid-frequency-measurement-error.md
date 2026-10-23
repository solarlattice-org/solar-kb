---
id: symptom:grid-frequency-measurement-error
type: Symptom
name: Grid frequency measurement error
aliases:
- Error Meas F
- Internal error
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: ABB/FIMER inverters show code E028 on the display, labelled Error Meas F or Internal error.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r6
    h: 04b4732fc478
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r1
    h: a5a70a4f9522
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r5
    h: b84626e5e6ba
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=39.r9
    h: 2328009f7962
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r1
    h: a5a70a4f9522
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r4
    h: c4f7b5c4417b
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=55.r4
    h: c4f7b5c4417b
  review: drafted
---
The inverter reports code E028 on its display, shown as Error Meas F or Internal error, together with the yellow LED or the alarm LED. The code means the inverter's own grid frequency measurement failed. Regulations require two separate circuits to measure frequency for redundancy, and the error is tied to this check. The manuals say this is an error inside the inverter that cannot be checked from outside. The cause is in the inverter's measurement electronics, not in the grid itself. Do not confuse it with a grid over-frequency alarm. There, the grid frequency itself goes above the limit set by the operator, and you can check it both on the inverter and at the supply. For other brands' frequency alarms, the manuals say to measure frequency at the inverter test points and compare it with the display reading. A display reading that differs from the measurement may point to a bad measurement circuit. First, switch the inverter off and back on. If E028 comes back, contact customer assistance. A matching code, E027 (Error Meas V), covers the same redundant-measurement fault for grid voltage.

<!-- review notes
- sentence 3: support check: partial - The passages say it is an error inside the inverter that cannot be checked externally, but they don't say the cause is in the measurement electronics rather than the grid, though that is loosely implied.
-->
