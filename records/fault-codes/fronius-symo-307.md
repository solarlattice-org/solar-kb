---
id: fc:fronius-symo-307
type: FaultCode
name: Fronius Symo 307
aliases:
- '307'
- Fronius 307
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '307'
code_key: '307'
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r7
    h: 58762101bb0c
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-undervoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r7
    h: 58762101bb0c
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r12
    h: dd8fb706a82b
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  note: Appears naturally at dawn and dusk from low irradiance; manual states it is not a fault.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r7
    h: 58762101bb0c
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r12
    h: dd8fb706a82b
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17
    h: 2e256223844f
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes automatically; installer only if it recurs with sufficient irradiance.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r7
    h: 58762101bb0c
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r12
    h: dd8fb706a82b
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17
    h: 2e256223844f
  review: drafted
  review_note: 'support check: partial - The passages say 307 appears naturally and Class 3 codes resume
    automatically, but no row gives the installer note for…'
- claim_id: c5
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r7
    h: 58762101bb0c
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
---
