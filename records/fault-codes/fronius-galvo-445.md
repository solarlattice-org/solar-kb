---
id: fc:fronius-galvo-445
type: FaultCode
name: Fronius Galvo 445
aliases:
- '445'
- Fronius 445
- Limit value setting not permitted
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '445'
code_key: '445'
display_message: Limit value setting not permitted
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r9
    h: 9da719b8b35f
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h21
    h: a5ea6671c1aa
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:hardware-incompatibility
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r19
    h: f3e2b584d37a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r19
    h: f3e2b584d37a
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r18
    h: f6c30ff3550e
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r9
    h: 9da719b8b35f
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:firmware-update
  note: Firmware update first; service technician if the code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r19
    h: f3e2b584d37a
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r18
    h: f6c30ff3550e
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r9
    h: 9da719b8b35f
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r19
    h: f3e2b584d37a
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
  review_note: 'support check: partial - The class 4 text is generic and does not tie 445 to class 4;
    the row states the inverter does…'
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r19
    h: f3e2b584d37a
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r18
    h: f6c30ff3550e
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r9
    h: 9da719b8b35f
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r9
    h: 9da719b8b35f
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h21
    h: a5ea6671c1aa
  review: drafted
---
