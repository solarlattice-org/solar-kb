---
id: fc:abb-uno-dm-6-0-plus-us-w2
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS W002
aliases:
- W002
- w2
- ABB / FIMER W002
- Input UV
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: W002
code_key: w2
display_message: Input UV
vendor_severity: Warning
page: 121
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=33.r7
    h: ed85ff32322f
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=44.r7
    h: 7e047f719311
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=33.r7
    h: ed85ff32322f
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=44.r7
    h: 7e047f719311
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:insufficient-irradiance
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=42.r8
    h: 44d5f8dc6501
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=33.r7
    h: ed85ff32322f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=49.r7
    h: 7e047f719311
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=44.r7
    h: 7e047f719311
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r8
    h: 397eafc39e02
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:dc-undervoltage
  note: Low PV input voltage at switch-off
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=42.r8
    h: 44d5f8dc6501
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=33.r7
    h: ed85ff32322f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=49.r7
    h: 7e047f719311
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=44.r7
    h: 7e047f719311
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r8
    h: 397eafc39e02
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=42.r8
    h: 44d5f8dc6501
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=33.r7
    h: ed85ff32322f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=49.r7
    h: 7e047f719311
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=44.r7
    h: 7e047f719311
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r8
    h: 397eafc39e02
  review: drafted
  review_note: 'support check: partial - Cause cites incorrect PV generator configuration, but no explicit
    statement that the code affects the PV array component.'
- claim_id: c7
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Compare input voltage against Vstart
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=42.r8
    h: 44d5f8dc6501
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=33.r7
    h: ed85ff32322f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=49.r7
    h: 7e047f719311
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=44.r7
    h: 7e047f719311
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r8
    h: 397eafc39e02
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: If input stays below Vstart; if above Vstart, contact service
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=42.r8
    h: 44d5f8dc6501
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=33.r7
    h: ed85ff32322f
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=49.r7
    h: 7e047f719311
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=44.r7
    h: 7e047f719311
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r8
    h: 397eafc39e02
  review: drafted
  review_note: 'support check: partial - Check of correct system composition is stated, but string configuration
    correction is not explicit.'
- claim_id: c9
  rel: applies_to
  target: prod:abb-uno-dm-6-0-plus-us
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=33.r7
    h: ed85ff32322f
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=44.r7
    h: 7e047f719311
  review: drafted
---
