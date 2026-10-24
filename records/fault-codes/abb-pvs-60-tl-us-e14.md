---
id: fc:abb-pvs-60-tl-us-e14
type: FaultCode
name: ABB / FIMER PVS-60-TL E014
aliases:
- E014
- e14
- ABB / FIMER E014
- Over Temp.
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: E014
code_key: e14
display_message: Over Temp.
vendor_severity: Error
page: 156
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r1
    h: d8e7479cf2dd
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r1
    h: d8e7479cf2dd
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r8
    h: 83e99572cea5
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r1
    h: d8e7479cf2dd
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r7
    h: 7103a2f82d0a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r9
    h: 15a67944b799
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r9
    h: 15a67944b799
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r2
    h: b316943180a1
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:ambient-temperature-check
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r8
    h: 83e99572cea5
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r1
    h: d8e7479cf2dd
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r7
    h: 7103a2f82d0a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r9
    h: 15a67944b799
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r9
    h: 15a67944b799
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r2
    h: b316943180a1
  review: drafted
  review_note: 'support check: partial - The passages say to check ambient temperature and sunlight, but
    do not say the error is detected by an ambient…'
- claim_id: c5
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r8
    h: 83e99572cea5
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r1
    h: d8e7479cf2dd
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r7
    h: 7103a2f82d0a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r9
    h: 15a67944b799
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r9
    h: 15a67944b799
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r2
    h: b316943180a1
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes after cooling; contact service if it persists once ambient is back in range.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=53.r8
    h: 83e99572cea5
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r1
    h: d8e7479cf2dd
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=39.r7
    h: 7103a2f82d0a
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=53.r9
    h: 15a67944b799
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=48.r9
    h: 15a67944b799
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=38.r2
    h: b316943180a1
  review: drafted
  review_note: 'support check: partial - The passages say to wait for the inverter to cool and contact
    service if the problem persists. They never say…'
- claim_id: c7
  rel: applies_to
  target: prod:abb-pvs-60-tl-us
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=47.r1
    h: d8e7479cf2dd
  review: drafted
---
