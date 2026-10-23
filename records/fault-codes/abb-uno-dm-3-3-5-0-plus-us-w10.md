---
id: fc:abb-uno-dm-3-3-5-0-plus-us-w10
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS W010
aliases:
- W010
- w10
- ABB / FIMER W010
- Fan Fail
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: W010
code_key: w10
display_message: Fan Fail
vendor_severity: Warning
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r6
    h: 42b90af91b1b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r6
    h: e6003e990f3d
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r6
    h: 42b90af91b1b
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r6
    h: e6003e990f3d
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r6
    h: f68c18540d32
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r6
    h: 42b90af91b1b
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r6
    h: 42b90af91b1b
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r6
    h: e6003e990f3d
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r6
    h: e6003e990f3d
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r1
    h: a45581a188f9
  review: drafted
- claim_id: c5
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r6
    h: f68c18540d32
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r6
    h: 42b90af91b1b
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r6
    h: 42b90af91b1b
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r6
    h: e6003e990f3d
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r6
    h: e6003e990f3d
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r1
    h: a45581a188f9
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r6
    h: f68c18540d32
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r6
    h: 42b90af91b1b
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r6
    h: 42b90af91b1b
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r6
    h: e6003e990f3d
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r6
    h: e6003e990f3d
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r1
    h: a45581a188f9
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r6
    h: f68c18540d32
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r6
    h: 42b90af91b1b
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r6
    h: 42b90af91b1b
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r6
    h: e6003e990f3d
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r6
    h: e6003e990f3d
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r1
    h: a45581a188f9
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:service-required
  note: Internal fault that cannot be checked externally; call service if the alarm keeps repeating.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=43.r6
    h: f68c18540d32
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r6
    h: 42b90af91b1b
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=34.r6
    h: 42b90af91b1b
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=50.r6
    h: e6003e990f3d
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=45.r6
    h: e6003e990f3d
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=36.r1
    h: a45581a188f9
  review: drafted
  review_note: 'support check: partial - Internal error that can''t be checked externally and contact
    assistance if repeating are stated, though ''clears by service required'' is…'
---
