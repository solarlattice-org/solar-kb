---
id: symptom:leakage-current-measurement-error
type: Symptom
name: Leakage current measurement error
aliases:
- Error Meas Ileak
- E030
- Internal error
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: FIMER/ABB inverters show code E030, with message Error Meas Ileak or Internal error depending
    on model.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=48.r8
    h: ac127ae8067a
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r3
    h: 14bb49350fa0
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r3
    h: 14bb49350fa0
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=40.r1
    h: cbdbc4d77bf8
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=55.r7
    h: 14123f919578
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r6
    h: 428110b38501
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=55.r6
    h: 428110b38501
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
The inverter shows code E030, labelled Error Meas Ileak or Internal error, and lights the yellow or alarm LED. The code means the inverter's internal check of DC-side (PV generator) leakage current to ground failed while it was connected to the grid. This leakage current is measured twice, by two independent circuits, to give the redundancy that regulations require, so E030 points to a fault in the measurement inside the inverter, not to a confirmed leakage on the array. The manufacturer says the fault is inside the inverter and cannot be checked from outside it. First switch the inverter off and back on, and contact customer assistance if the code comes back. Do not confuse it with E019 (Ileak sense.fail). E019 comes from the leakage sensor self-test, which forces a known current through the sensor, and it can only appear before the inverter connects to the grid. Genuine leakage current alarms tend to come with wet weather, damaged cable insulation or poor grounding. If an alarm follows that pattern, check the array insulation and grounding.

<!-- review notes
- sentence 3: support check: partial - Two independent circuits for redundancy and an internal error are stated, but the passages don't say it is not a confirmed array leakage; the alarm is even titled 'High leakage current'.
-->
