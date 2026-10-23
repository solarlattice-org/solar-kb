---
id: fc:fronius-primo-738
type: FaultCode
name: Fronius Primo 738
aliases:
- '738'
- Fronius 738
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '738'
code_key: '738'
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r9
    h: 2637b7ea5d91
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h22
    h: 8efd8641166b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:data-storage-failure
  note: Drive may be full or write-protected.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r13
    h: 8ae82f05b06b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r9
    h: 2637b7ea5d91
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r9
    h: 2637b7ea5d91
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:usb-flash-drive
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r13
    h: 8ae82f05b06b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r9
    h: 2637b7ea5d91
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r9
    h: 2637b7ea5d91
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:storage-drive-check
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r13
    h: 8ae82f05b06b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r9
    h: 2637b7ea5d91
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r9
    h: 2637b7ea5d91
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:usb-drive-replacement
  note: Only if freeing memory and removing write protection do not help.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r13
    h: 8ae82f05b06b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r9
    h: 2637b7ea5d91
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r9
    h: 2637b7ea5d91
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r13
    h: 8ae82f05b06b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r9
    h: 2637b7ea5d91
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r9
    h: 2637b7ea5d91
  review: drafted
---
