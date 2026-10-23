---
id: fm:dc-link-capacitor-failure
type: FailureMode
name: DC link capacitor failure
aliases:
- Bulk Cap Fail
- Cap. Fault
claims:
- claim_id: c1
  rel: affects
  target: comp:dc-link-capacitor
  note: Manuals describe it as a breakdown or fault on the bulk capacitors inside the inverter.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r2
    h: d4397ea50b07
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r9
    h: 46f1f27a4794
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r3
    h: a644b87ba56c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r8
    h: 2458486027cd
  review: drafted
- claim_id: c2
  rel: presents_as
  target: symptom:internal-device-fault
  note: The error is internal to the inverter and cannot be checked from outside. Reported as E015 with
    a yellow or alarm LED.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r2
    h: d4397ea50b07
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r9
    h: 46f1f27a4794
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r3
    h: a644b87ba56c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r8
    h: 2458486027cd
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:inverter-display-check
  note: Error code E015 is shown as 'Bulk Cap Fail' or 'Cap. Fault' on ABB/FIMER inverters.
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r3
    h: a644b87ba56c
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r2
    h: d4397ea50b07
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r9
    h: 46f1f27a4794
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r8
    h: 2458486027cd
  review: drafted
  review_note: 'support check: partial - Passages show E015 displayed as Bulk Cap Fail/Cap. Fault, but
    don''t name ABB/FIMER or describe display checking as a detection method.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  note: Turn the inverter off and on again to see whether the error persists.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r2
    h: d4397ea50b07
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r9
    h: 46f1f27a4794
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r3
    h: a644b87ba56c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r8
    h: 2458486027cd
  review: drafted
  review_note: 'support check: partial - Passages say to switch off and on and see if the problem persists,
    but a restart is a check, not stated to mitigate or fix the failure.'
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the error persists after a restart, contact customer assistance.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r2
    h: d4397ea50b07
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r9
    h: 46f1f27a4794
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r3
    h: a644b87ba56c
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r8
    h: 2458486027cd
  review: drafted
---
A DC link capacitor failure is a breakdown of the bulk capacitors inside the inverter. On ABB and FIMER string inverters it shows as error E015, labelled Bulk Cap Fail or Cap. Fault, with a yellow or alarm LED. The fault is inside the inverter and cannot be checked from outside. Switch the inverter off and back on. If the error comes back, contact the manufacturer's customer assistance. Before opening the inverter, wait for the internal capacitor to discharge. Then use a voltage detector to confirm there is no voltage on the bulk capacitor.

<!-- review notes
- sentence 2: support check: partial - E015, Bulk Cap Fail/Cap. Fault and yellow/alarm LED are stated, but the passages don't name ABB/FIMER or string inverters.
- sentence 5: support check: partial - Passages say to wait for the internal capacitor to discharge and to check absence of voltage on the bulk capacitor with a voltage detector after opening the cover, but the order relative to opening is only loosely implied and the 'before opening' wait isn't clearly stated.
-->
