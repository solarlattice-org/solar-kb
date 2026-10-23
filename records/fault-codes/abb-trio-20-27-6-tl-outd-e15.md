---
id: fc:abb-trio-20-27-6-tl-outd-e15
type: FaultCode
name: ABB / FIMER TRIO-20.0-27.6-TL E015
aliases:
- E015
- e15
- ABB / FIMER E015
- Bulk Cap Fail
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: trio-20-27-6-tl-outd
family_name: TRIO-20.0/27.6-TL-OUTD(-US)
code: E015
code_key: e15
display_message: Bulk Cap Fail
vendor_severity: Error
page: 111
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r3
    h: a644b87ba56c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r3
    h: a644b87ba56c
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:dc-link-capacitor-failure
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r9
    h: 46f1f27a4794
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r2
    h: d4397ea50b07
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r8
    h: 2458486027cd
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r8
    h: 2458486027cd
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r10
    h: 8b415c7672ff
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r10
    h: 8b415c7672ff
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r3
    h: a644b87ba56c
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-link-capacitor
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r9
    h: 46f1f27a4794
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r2
    h: d4397ea50b07
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r8
    h: 2458486027cd
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r8
    h: 2458486027cd
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r10
    h: 8b415c7672ff
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r10
    h: 8b415c7672ff
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r3
    h: a644b87ba56c
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r9
    h: 46f1f27a4794
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r2
    h: d4397ea50b07
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r3
    h: a644b87ba56c
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r9
    h: 46f1f27a4794
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r2
    h: d4397ea50b07
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r3
    h: a644b87ba56c
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the fault persists afterwards.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r9
    h: 46f1f27a4794
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r2
    h: d4397ea50b07
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r8
    h: 2458486027cd
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r3
    h: a644b87ba56c
  review: drafted
  review_note: 'support check: partial - Power cycle then contact service is stated, but clearing by manual
    reset is not stated.'
---
