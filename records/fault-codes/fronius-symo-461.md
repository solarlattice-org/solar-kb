---
id: fc:fronius-symo-461
type: FaultCode
name: Fronius Symo 461
aliases:
- '461'
- Fronius 461
- Error in DSP data memory
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '461'
code_key: '461'
display_message: Error in DSP data memory
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r32
    h: 6be95aa710d5
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:memory-error
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r32
    h: 6be95aa710d5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r30
    h: 6be95aa710d5
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:digital-signal-processor
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r32
    h: 6be95aa710d5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r30
    h: 6be95aa710d5
  review: drafted
---
