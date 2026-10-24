---
id: fc:abb-uno-dm-3-3-5-0-plus-us-e79
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS E079
aliases:
- E079
- e79
- ABB / FIMER E079
- Wrong Sequence
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: E079
code_key: e79
display_message: Wrong Sequence
vendor_severity: Error
page: 132
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r7
    h: 2d52397e1881
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r13
    h: 6aaace62c1df
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r7
    h: 2d52397e1881
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r13
    h: 6aaace62c1df
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:phase-sequence-error
  note: Three-phase models only
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r8
    h: 1249e4d55f82
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r7
    h: d56300e46d63
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r7
    h: 2d52397e1881
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r7
    h: 2d52397e1881
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r13
    h: 6aaace62c1df
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r13
    h: 6aaace62c1df
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r8
    h: 1249e4d55f82
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r7
    h: d56300e46d63
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r7
    h: 2d52397e1881
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r7
    h: 2d52397e1881
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r13
    h: 6aaace62c1df
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r13
    h: 6aaace62c1df
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:phase-sequence-correction
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r8
    h: 1249e4d55f82
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r7
    h: d56300e46d63
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r7
    h: 2d52397e1881
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r7
    h: 2d52397e1881
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r13
    h: 6aaace62c1df
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r13
    h: 6aaace62c1df
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:abb-uno-dm-3-3-5-0-plus-us
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r7
    h: 2d52397e1881
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r13
    h: 6aaace62c1df
  review: drafted
---
