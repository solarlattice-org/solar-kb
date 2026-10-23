---
id: fc:fronius-primo-425
type: FaultCode
name: Fronius Primo 425
aliases:
- '425'
- Fronius 425
- Communication with the power module is not possible
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '425'
code_key: '425'
display_message: Communication with the power module is not possible
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r11
    h: 2414b6a9d1da
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h20
    h: 45088a5d7149
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r12
    h: 2414b6a9d1da
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r11
    h: 2414b6a9d1da
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r8
    h: b276fe8f7024
  review: drafted
---
