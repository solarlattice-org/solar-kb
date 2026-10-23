---
id: fc:abb-uno-dm-6-0-plus-us-e56
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS E056
aliases:
- E056
- e56
- ABB / FIMER E056
- Over Temp. (from external box)
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: E056
code_key: e56
display_message: Over Temp. (from external box)
vendor_severity: Error
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r2
    h: 303e18b961e9
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r8
    h: 129daf3e629b
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r2
    h: 303e18b961e9
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r8
    h: 129daf3e629b
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r1
    h: 18005e07fa44
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r2
    h: 4c81ecedd060
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r2
    h: 303e18b961e9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r8
    h: 129daf3e629b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r8
    h: 129daf3e629b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r1
    h: fa309d5be880
  review: drafted
  review_note: 'support check: partial - E056 is excessive temperature measured in the external wiring
    box, not specifically inverter overtemperature.'
- claim_id: c5
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r1
    h: 18005e07fa44
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r2
    h: 4c81ecedd060
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r2
    h: 303e18b961e9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r8
    h: 129daf3e629b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r8
    h: 129daf3e629b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r1
    h: fa309d5be880
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Clears once the unit cools down; contact service if it persists with ambient back in range.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r1
    h: 18005e07fa44
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r2
    h: 4c81ecedd060
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r2
    h: 303e18b961e9
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r8
    h: 129daf3e629b
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r8
    h: 129daf3e629b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=41.r1
    h: fa309d5be880
  review: drafted
  review_note: 'support check: partial - Waiting for cool down and the contact-service-if-persists are
    stated, but auto-reset is only implied.'
---
