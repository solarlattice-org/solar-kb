---
id: fc:yaskawa-solectria-sgi-500-750xtm-dcvolthigh
type: FaultCode
name: Yaskawa Solectria SGI-XTM DC Volt High
aliases:
- DC Volt High
- dcvolthigh
- Yaskawa Solectria DC Volt High
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: DC Volt High
code_key: dcvolthigh
vendor_severity: Informative
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r5
    h: 2ea8480829ae
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r5
    h: 2ea8480829ae
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
  review_note: 'support check: partial - Informative section defines the category but the row''s membership
    is only implied; the row''s corrective action requires array adjustment.'
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r5
    h: 2ea8480829ae
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r5
    h: 2ea8480829ae
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r5
    h: 2ea8480829ae
  review: drafted
---
