---
id: fc:fronius-symo-242
type: FaultCode
name: Fronius Symo 242
aliases:
- '242'
- Fronius 242
- Arc detected
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '242'
code_key: '242'
display_message: Arc detected
vendor_severity: Class 2
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r9
    h: 8e9f6d1cc072
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h20
    h: b46d8cafebc3
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r9
    h: 8e9f6d1cc072
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r7
    h: e10fae29d087
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r9
    h: 8e9f6d1cc072
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r7
    h: e10fae29d087
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
  review_note: 'support check: partial - Code 242 needs an Enter reset and is an arc event, but the passages
    don''t state a fault classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Feed-in resumes only after acknowledgement, implying it is interrupted until then.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r9
    h: 8e9f6d1cc072
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r7
    h: e10fae29d087
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - The passages say the inverter restarts feeding after the reset,
    which implies feed-in was interrupted, but they don''t say so explicitly.'
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: If it keeps recurring, contact the installer.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r9
    h: 8e9f6d1cc072
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r7
    h: e10fae29d087
  review: drafted
---
