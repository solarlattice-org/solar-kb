---
id: fc:fronius-symo-604
type: FaultCode
name: Fronius Symo 604
aliases:
- '604'
- Fronius 604
- DC module temperature sensor faulty
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '604'
code_key: '604'
display_message: DC module temperature sensor faulty
vendor_severity: Class 6
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r3
    h: 08c050bc6e48
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h24
    h: 4242ab97920a
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r3
    h: 08c050bc6e48
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:temperature-sensor
  note: DC module sensor.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r3
    h: 08c050bc6e48
  review: drafted
---
