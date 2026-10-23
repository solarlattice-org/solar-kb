---
id: fc:abb-uno-dm-6-0-plus-us-e5
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS E005
aliases:
- E005
- e5
- ABB / FIMER E005
- Comm.Error
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: E005
code_key: e5
display_message: Comm.Error
vendor_severity: Error
page: 124
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r11
    h: e4659b85aec4
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r1
    h: 9987d3d32146
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r11
    h: e4659b85aec4
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r1
    h: 9987d3d32146
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r1
    h: ab73e682c967
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r3
    h: c7caa7328b83
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r11
    h: 49b3171d4ab4
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r11
    h: e4659b85aec4
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r1
    h: 9987d3d32146
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r5
    h: 5d3cf7b751cb
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: affects
  target: comp:control-board
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r1
    h: ab73e682c967
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r3
    h: c7caa7328b83
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r11
    h: 49b3171d4ab4
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r11
    h: e4659b85aec4
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r1
    h: 9987d3d32146
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r5
    h: 5d3cf7b751cb
  review: drafted
  review_note: 'support check: partial - The passages mention control devices inside the inverter but
    never name a control board.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r1
    h: ab73e682c967
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r3
    h: c7caa7328b83
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r11
    h: 49b3171d4ab4
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r11
    h: e4659b85aec4
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r1
    h: 9987d3d32146
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r5
    h: 5d3cf7b751cb
  review: drafted
  review_note: 'support check: partial - Switching off and on is a step before contacting assistance;
    the passages do not say it resolves the error.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the error persists.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r1
    h: ab73e682c967
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r3
    h: c7caa7328b83
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r11
    h: 49b3171d4ab4
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r11
    h: e4659b85aec4
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r1
    h: 9987d3d32146
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r5
    h: 5d3cf7b751cb
  review: drafted
  review_note: 'support check: partial - A power cycle is listed, but the passages do not say a manual
    reset clears the error.'
---
