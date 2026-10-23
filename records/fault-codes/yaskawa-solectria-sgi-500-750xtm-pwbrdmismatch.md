---
id: fc:yaskawa-solectria-sgi-500-750xtm-pwbrdmismatch
type: FaultCode
name: Yaskawa Solectria SGI-XTM Pw Brd Mismatch
aliases:
- Pw Brd Mismatch
- pwbrdmismatch
- Yaskawa Solectria Pw Brd Mismatch
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Pw Brd Mismatch
code_key: pwbrdmismatch
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r9
    h: ecedecd53baf
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r9
    h: ecedecd53baf
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r9
    h: ecedecd53baf
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r9
    h: ecedecd53baf
  review: drafted
---
