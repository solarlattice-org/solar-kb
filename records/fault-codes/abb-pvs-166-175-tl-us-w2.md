---
id: fc:abb-pvs-166-175-tl-us-w2
type: FaultCode
name: ABB / FIMER PVS-166-175-TL W002
aliases:
- W002
- w2
- ABB / FIMER W002
- Input UV
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: W002
code_key: w2
display_message: Input UV
vendor_severity: Warning
page: 136
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=49.r6
    h: 118e69d98d4c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=49.r6
    h: 118e69d98d4c
  review: drafted
- claim_id: c3
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
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
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
---
