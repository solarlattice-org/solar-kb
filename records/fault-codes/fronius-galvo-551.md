---
id: fc:fronius-galvo-551
type: FaultCode
name: Fronius Galvo 551
aliases:
- '551'
- Fronius 551
- Fuse for solar module ground is defective
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '551'
code_key: '551'
display_message: Fuse for solar module ground is defective
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 17801abf0e61
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h22
    h: 6d24baf3261a
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:ground-fuse-failure
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 17801abf0e61
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ground-fuse
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 17801abf0e61
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:ground-fuse-replacement
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 17801abf0e61
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 17801abf0e61
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  note: Fuse must be replaced; contact the installer if the code keeps recurring.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 17801abf0e61
  review: drafted
---
