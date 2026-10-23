---
id: fc:fronius-symo-768
type: FaultCode
name: Fronius Symo 768
aliases:
- '768'
- Fronius 768
- Power limit different in the hardware modules
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '768'
code_key: '768'
display_message: Power limit different in the hardware modules
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r29
    h: 5547f93b88eb
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  note: Power limit settings differ between hardware modules.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r29
    h: 5547f93b88eb
  review: drafted
---
