---
id: fc:abb-pvs-60-tl-us-w17
type: FaultCode
name: ABB / FIMER PVS-60-TL W017
aliases:
- W017
- w17
- ABB / FIMER W017
- String Err.
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: W017
code_key: w17
display_message: String Err.
vendor_severity: Warning
page: 153
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:string-current-error
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r5
    h: 78e6287189be
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r5
    h: 78e6287189be
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r5
    h: dd59f3125797
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:string-fuse-failure
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r5
    h: 78e6287189be
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r5
    h: 78e6287189be
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r5
    h: dd59f3125797
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:string-fuse
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r5
    h: 78e6287189be
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r5
    h: 78e6287189be
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r5
    h: dd59f3125797
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:fuse-check
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r5
    h: 78e6287189be
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r5
    h: 78e6287189be
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r5
    h: dd59f3125797
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:fuse-replacement
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r5
    h: 78e6287189be
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r5
    h: 78e6287189be
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r5
    h: dd59f3125797
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: Used when no fuse is damaged but the alarm stays; check the configured input strings.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r5
    h: 78e6287189be
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r5
    h: 78e6287189be
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r5
    h: dd59f3125797
  review: drafted
---
