---
id: fc:yaskawa-solectria-sgi-500-750xtm-nameplatelimits
type: FaultCode
name: Yaskawa Solectria SGI-XTM Nameplate Limits
aliases:
- Nameplate Limits
- nameplatelimits
- Yaskawa Solectria Nameplate Limits
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Nameplate Limits
code_key: nameplatelimits
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32
    h: bcd67f31434e
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
  review_note: code printed in the table header line
- claim_id: c2
  rel: reports
  target: symptom:flat-capped-output
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32
    h: bcd67f31434e
  review: drafted
  review_note: 'support check: partial - Power limited by nameplate rating suggests capped output, but
    ''flat'' capping is not stated.'
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32
    h: bcd67f31434e
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
  review_note: 'support check: partial - Row says no action needed and u3 describes informative messages,
    but the row isn''t explicitly labelled informational.'
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: Limited to nameplate rating; no number stated.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32
    h: bcd67f31434e
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32
    h: bcd67f31434e
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
