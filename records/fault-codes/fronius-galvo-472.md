---
id: fc:fronius-galvo-472
type: FaultCode
name: Fronius Galvo 472
aliases:
- '472'
- Fronius 472
- Fuse for solar module ground is defective
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '472'
code_key: '472'
display_message: Fuse for solar module ground is defective
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r17
    h: 21a2fd000df8
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h21
    h: a5ea6671c1aa
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:ground-fuse-failure
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r17
    h: 21a2fd000df8
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ground-fuse
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r17
    h: 21a2fd000df8
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:ground-fuse-replacement
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r17
    h: 21a2fd000df8
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r17
    h: 21a2fd000df8
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r17
    h: 21a2fd000df8
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:service-required
  note: Fuse must be replaced; contact the installer if the code keeps recurring.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r17
    h: 21a2fd000df8
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r17
    h: 21a2fd000df8
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h21
    h: a5ea6671c1aa
  review: drafted
---
