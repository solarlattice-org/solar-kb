---
id: fc:abb-trio-20-27-6-tl-outd-w9
type: FaultCode
name: ABB / FIMER TRIO-20.0-27.6-TL W009
aliases:
- W009
- w9
- ABB / FIMER W009
- Empty Table
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: trio-20-27-6-tl-outd
family_name: TRIO-20.0/27.6-TL-OUTD(-US)
code: W009
code_key: w9
display_message: Empty Table
vendor_severity: Warning
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r10
    h: 0673884d3afd
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r10
    h: 0673884d3afd
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  note: Applies only to wind models whose generator characterisation table is missing
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r10
    h: 0673884d3afd
  review: drafted
  review_note: 'support check: partial - Characterisation board not compiled for WIND models is stated,
    but ''configuration error'' is a loose label.'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r10
    h: 0673884d3afd
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  note: Only for wind models
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r10
    h: 0673884d3afd
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:abb-trio-20-27-6-tl-outd
  cite:
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: tbl=35.r10
    h: 0673884d3afd
  review: drafted
---
