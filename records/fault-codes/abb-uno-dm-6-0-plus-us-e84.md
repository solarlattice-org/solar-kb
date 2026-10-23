---
id: fc:abb-uno-dm-6-0-plus-us-e84
type: FaultCode
name: ABB / FIMER UNO-DM-6.0-PLUS E084
aliases:
- E084
- e84
- ABB / FIMER E084
- BackFeed OC
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: uno-dm-6-0-plus-us
family_name: UNO-DM-6.0-TL-PLUS-US
code: E084
code_key: e84
display_message: BackFeed OC
vendor_severity: Error
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r8
    h: e53a63aa377c
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
  cite:
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r2
    h: b0925e880dad
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r8
    h: e53a63aa377c
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r2
    h: b0925e880dad
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:string-reverse-current
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r9
    h: d72e0510a000
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r9
    h: 76f7a1a8cc76
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r8
    h: e53a63aa377c
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r8
    h: e53a63aa377c
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=57.r2
    h: b0925e880dad
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r2
    h: b0925e880dad
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r9
    h: d72e0510a000
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r9
    h: 76f7a1a8cc76
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r8
    h: e53a63aa377c
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r8
    h: e53a63aa377c
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=57.r2
    h: b0925e880dad
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r2
    h: b0925e880dad
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r9
    h: d72e0510a000
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r9
    h: 76f7a1a8cc76
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r8
    h: e53a63aa377c
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r8
    h: e53a63aa377c
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=57.r2
    h: b0925e880dad
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r2
    h: b0925e880dad
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Applies under good irradiance; at low irradiance it is a normal protection. If it persists after
    restart, contact service.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=57.r9
    h: d72e0510a000
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=50.r9
    h: 76f7a1a8cc76
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=42.r8
    h: e53a63aa377c
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=40.r8
    h: e53a63aa377c
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=57.r2
    h: b0925e880dad
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r2
    h: b0925e880dad
  review: drafted
  review_note: 'support check: partial - Restart under good irradiance and low-irradiance normal protection
    are stated, but ''manual reset'' clearing is only implied by the restart instruction.'
---
