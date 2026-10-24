---
id: fc:abb-trio-20-27-6-tl-outd-w18
type: FaultCode
name: ABB / FIMER TRIO-20.0-27.6-TL W018
aliases:
- W018
- w18
- ABB / FIMER W018
- SPD DC Err
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: trio-20-27-6-tl-outd
family_name: TRIO-20.0/27.6-TL-OUTD(-US)
code: W018
code_key: w18
display_message: SPD DC Err
vendor_severity: Warning
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r6
    h: 0fa2e4f35b89
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r6
    h: 0fa2e4f35b89
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:spd-alarm
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r5
    h: fce7cbf479d8
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r6
    h: 56f4c661497a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r6
    h: 0296a6930509
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r6
    h: 0296a6930509
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r6
    h: 0fa2e4f35b89
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:surge-protector-exhausted
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r5
    h: fce7cbf479d8
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r6
    h: 56f4c661497a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r6
    h: 0296a6930509
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r6
    h: 0296a6930509
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r6
    h: 0fa2e4f35b89
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:surge-protection-device
  note: DC-side surge arresters, models with monitored SPD
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r5
    h: fce7cbf479d8
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r6
    h: 56f4c661497a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r6
    h: 0296a6930509
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r6
    h: 0296a6930509
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r6
    h: 0fa2e4f35b89
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  note: Red inspection window means damaged arrester
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r5
    h: fce7cbf479d8
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r6
    h: 56f4c661497a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r6
    h: 0296a6930509
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r6
    h: 0296a6930509
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r6
    h: 0fa2e4f35b89
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:spd-replacement
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r5
    h: fce7cbf479d8
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r6
    h: 56f4c661497a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r6
    h: 0296a6930509
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r6
    h: 0296a6930509
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r6
    h: 0fa2e4f35b89
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:service-required
  note: Cartridge replacement; service if alarm persists with green windows
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r5
    h: fce7cbf479d8
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r6
    h: 56f4c661497a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r6
    h: 0296a6930509
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r6
    h: 0296a6930509
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r6
    h: 0fa2e4f35b89
  review: drafted
  review_note: 'support check: partial - Cartridge replacement and contact customer assistance are stated,
    but service-required classification applies mainly to the persistent case; replacement is an…'
- claim_id: c9
  rel: applies_to
  target: prod:abb-trio-20-27-6-tl-outd
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r6
    h: 0fa2e4f35b89
  review: drafted
---
