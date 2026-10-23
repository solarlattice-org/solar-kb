---
id: fc:abb-uno-dm-3-3-5-0-plus-us-e46
type: FaultCode
name: ABB / FIMER UNO-DM-3.3-5.0-PLUS E046
aliases:
- E046
- e46
- ABB / FIMER E046
- String self test fail
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-3-3-5-0-plus-us
family_name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US
code: E046
code_key: e46
display_message: String self test fail
vendor_severity: Error
page: 131
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r10
    h: cfabca3d10ea
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r2
    h: 7071c88636b1
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r10
    h: cfabca3d10ea
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=56.r2
    h: 7071c88636b1
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:reverse-polarity
  note: Inverted string found during string self-test
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r5
    h: 3b1b26d47aed
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r6
    h: 8ca1a43bdeae
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r10
    h: cfabca3d10ea
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r2
    h: 7071c88636b1
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r5
    h: 3b1b26d47aed
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r6
    h: 8ca1a43bdeae
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r10
    h: cfabca3d10ea
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r2
    h: 7071c88636b1
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r5
    h: 3b1b26d47aed
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r6
    h: 8ca1a43bdeae
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r10
    h: cfabca3d10ea
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r2
    h: 7071c88636b1
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:polarity-correction
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r5
    h: 3b1b26d47aed
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r6
    h: 8ca1a43bdeae
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r10
    h: cfabca3d10ea
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r2
    h: 7071c88636b1
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Reactivate after correcting strings; contact service if it persists
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r5
    h: 3b1b26d47aed
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=49.r6
    h: 8ca1a43bdeae
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=41.r10
    h: cfabca3d10ea
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r2
    h: 7071c88636b1
  review: drafted
  review_note: 'support check: partial - Reactivating the system after correcting strings and contacting
    assistance are stated, but manual-reset classification is only implied.'
---
