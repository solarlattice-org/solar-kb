---
id: fc:fronius-symo-761-765
type: FaultCode
name: Fronius Symo 761-765
aliases:
- 761-765
- Fronius 761-765
- Provides information about the internal processor status
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: 761-765
code_key: 761-765
code_from: 761
code_to: 765
display_message: Provides information about the internal processor status
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r26
    h: c59056eb51c1
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r26
    h: c59056eb51c1
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r26
    h: c59056eb51c1
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
---
