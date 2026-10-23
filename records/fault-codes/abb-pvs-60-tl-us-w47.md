---
id: fc:abb-pvs-60-tl-us-w47
type: FaultCode
name: ABB / FIMER PVS-60-TL W047
aliases:
- W047
- w47
- ABB / FIMER W047
- Update Incomplete
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: W047
code_key: w47
display_message: Update Incomplete
vendor_severity: Warning
page: 154
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r7
    h: 956cadd0c430
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r7
    h: 956cadd0c430
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r2
    h: 4ffd56f4dd30
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r7
    h: 956cadd0c430
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r3
    h: 0711ae43ba47
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r3
    h: 0711ae43ba47
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r4
    h: bf8c7b8719ad
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r4
    h: bf8c7b8719ad
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:retry-update
  note: Finish pending updates first, then restart, then contact support
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=52.r2
    h: 4ffd56f4dd30
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r7
    h: 956cadd0c430
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=38.r3
    h: 0711ae43ba47
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=36.r3
    h: 0711ae43ba47
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r4
    h: bf8c7b8719ad
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r4
    h: bf8c7b8719ad
  review: drafted
  review_note: 'support check: partial - Complete pending updates, restart, contact support are stated;
    ''retry'' is implied by completing the update.'
---
