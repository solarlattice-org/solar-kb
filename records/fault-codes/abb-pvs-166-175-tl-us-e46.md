---
id: fc:abb-pvs-166-175-tl-us-e46
type: FaultCode
name: ABB / FIMER PVS-166-175-TL E046
aliases:
- E046
- e46
- ABB / FIMER E046
- Str. test failed
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: E046
code_key: e46
display_message: Str. test failed
vendor_severity: Error
page: 143
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r5
    h: 3b1b26d47aed
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r5
    h: 3b1b26d47aed
  review: drafted
- claim_id: c3
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
- claim_id: c4
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
- claim_id: c5
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
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
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
- claim_id: c7
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
- claim_id: c8
  rel: applies_to
  target: prod:abb-pvs-166-175-tl-us
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r5
    h: 3b1b26d47aed
  review: drafted
---
