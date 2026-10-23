---
id: fc:fronius-symo-581
type: FaultCode
name: Fronius Symo 581
aliases:
- '581'
- Fronius 581
- Setup "Special Purpose Utility-Interactive" (SPUI) is activated
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '581'
code_key: '581'
display_message: Setup "Special Purpose Utility-Interactive" (SPUI) is activated
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r18
    h: ca9a756700ef
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:anti-islanding-disabled
  note: Special grid setup turns off islanding protection and changes frequency and voltage limits.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r18
    h: ca9a756700ef
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  note: Vendor says this is not an error; it is a configuration status.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r18
    h: ca9a756700ef
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Operator acknowledges the code on the display.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r18
    h: ca9a756700ef
  review: drafted
---
