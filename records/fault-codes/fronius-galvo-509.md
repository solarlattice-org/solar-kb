---
id: fc:fronius-galvo-509
type: FaultCode
name: Fronius Galvo 509
aliases:
- '509'
- Fronius 509
- No feed-in within the last 24 hours
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '509'
code_key: '509'
display_message: No feed-in within the last 24 hours
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r2
    h: f098c673c83b
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h22
    h: 6d24baf3261a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:no-feed-in-period
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r2
    h: 1e877d15227f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r2
    h: 0258f1217490
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r2
    h: f098c673c83b
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r2
    h: 1e877d15227f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r2
    h: 0258f1217490
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r2
    h: f098c673c83b
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Acknowledge code; if it persists, observe further status codes.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r2
    h: 1e877d15227f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r2
    h: 0258f1217490
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r2
    h: f098c673c83b
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r2
    h: f098c673c83b
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h22
    h: 6d24baf3261a
  review: drafted
---
