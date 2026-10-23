---
id: fc:fronius-symo-701-704
type: FaultCode
name: Fronius Symo 701-704
aliases:
- 701-704
- Fronius 701-704
- Provides information about the internal processor status
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: 701-704
code_key: 701-704
code_from: 701
code_to: 704
display_message: Provides information about the internal processor status
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r1
    h: 814a3dfe09bf
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r1
    h: 814a3dfe09bf
  review: drafted
---
