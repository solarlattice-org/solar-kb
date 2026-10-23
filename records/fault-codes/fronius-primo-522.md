---
id: fc:fronius-primo-522
type: FaultCode
name: Fronius Primo 522
aliases:
- '522'
- Fronius 522
- DC low String 1
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '522'
code_key: '522'
display_message: DC low String 1
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r6
    h: fd63c26a438f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h21
    h: a6a4378aca92
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-undervoltage
  note: Low DC on string 1 input.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r9
    h: 0239235c5bc1
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r6
    h: fd63c26a438f
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r9
    h: 0239235c5bc1
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r6
    h: fd63c26a438f
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r9
    h: 0239235c5bc1
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Acknowledge by key press; if it recurs, contact the installer or service.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r9
    h: 0239235c5bc1
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
---
