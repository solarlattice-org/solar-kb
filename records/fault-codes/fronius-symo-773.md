---
id: fc:fronius-symo-773
type: FaultCode
name: Fronius Symo 773
aliases:
- '773'
- Fronius 773
- Software update group 0 (invalid country setup)
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '773'
code_key: '773'
display_message: Software update group 0 (invalid country setup)
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r31
    h: 0103336e07e8
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  note: Country setup is invalid for the software update group.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r31
    h: 0103336e07e8
  review: drafted
---
