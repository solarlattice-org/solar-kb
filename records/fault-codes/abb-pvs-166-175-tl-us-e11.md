---
id: fc:abb-pvs-166-175-tl-us-e11
type: FaultCode
name: ABB / FIMER PVS-166-175-TL E011
aliases:
- E011
- e11
- ABB / FIMER E011
- Ramp Fault
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-166-175-tl-us
family_name: FIMER PVS-166/175-TL-US
code: E011
code_key: e11
display_message: Ramp Fault
vendor_severity: Error
page: 140
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r6
    h: cb755388b362
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r6
    h: cb755388b362
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:boost-startup-timeout
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r6
    h: cb755388b362
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r8
    h: 34cbad8eb4b1
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r4
    h: 8a6059f8af12
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r6
    h: 03142bf6ac7c
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r10
    h: 171e85f917c7
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:boost-converter
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r6
    h: cb755388b362
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r8
    h: 34cbad8eb4b1
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r4
    h: 8a6059f8af12
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r6
    h: 03142bf6ac7c
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r10
    h: 171e85f917c7
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r6
    h: cb755388b362
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r8
    h: 34cbad8eb4b1
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r4
    h: 8a6059f8af12
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r6
    h: 03142bf6ac7c
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r10
    h: 171e85f917c7
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the error persists.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r6
    h: cb755388b362
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r8
    h: 34cbad8eb4b1
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r4
    h: 8a6059f8af12
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r6
    h: 03142bf6ac7c
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=37.r10
    h: 171e85f917c7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Power cycle then contact service is stated, but the passages
    never say the error clears by manual reset.'
---
