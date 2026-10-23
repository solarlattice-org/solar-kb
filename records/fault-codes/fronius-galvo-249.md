---
id: fc:fronius-galvo-249
type: FaultCode
name: Fronius Galvo 249
aliases:
- '249'
- Fronius 249
- Arc detector defective
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '249'
code_key: '249'
display_message: Arc detector defective
vendor_severity: Class 2
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r10
    h: 98c4cff38cbc
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h19
    h: fe0fbaee5a2c
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:arc-detector-failure
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r12
    h: cf9c0ea866d2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r10
    h: 98c4cff38cbc
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r12
    h: cf9c0ea866d2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r10
    h: 98c4cff38cbc
  review: drafted
---
