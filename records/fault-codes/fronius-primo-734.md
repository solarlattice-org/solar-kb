---
id: fc:fronius-primo-734
type: FaultCode
name: Fronius Primo 734
aliases:
- '734'
- Fronius 734
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '734'
code_key: '734'
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r6
    h: e4025e56afcd
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h22
    h: 8efd8641166b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r9
    h: 0bb4905e4691
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r6
    h: e4025e56afcd
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r6
    h: e4025e56afcd
  review: drafted
  review_note: 'support check: partial - The update file is not detected or not available, which is not
    literally an update failure, though it is closely related.'
- claim_id: c3
  rel: mitigated_by
  target: mit:update-file-check
  note: Service technician only if the code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r9
    h: 0bb4905e4691
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r6
    h: e4025e56afcd
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r6
    h: e4025e56afcd
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r9
    h: 0bb4905e4691
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r6
    h: e4025e56afcd
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r6
    h: e4025e56afcd
  review: drafted
---
