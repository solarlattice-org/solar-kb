---
id: fc:fronius-symo-772
type: FaultCode
name: Fronius Symo 772
aliases:
- '772'
- Fronius 772
- Memory unit unavailable
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '772'
code_key: '772'
display_message: Memory unit unavailable
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r30
    h: 79f2721b17d9
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:memory-unit
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r30
    h: 79f2721b17d9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:memory-error
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r30
    h: 79f2721b17d9
  review: drafted
---
