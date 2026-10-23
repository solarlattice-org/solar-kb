---
id: fc:fronius-galvo-731
type: FaultCode
name: Fronius Galvo 731
aliases:
- '731'
- Fronius 731
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '731'
code_key: '731'
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r3
    h: 8b211e171c09
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h23
    h: 8efd8641166b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:unsupported-storage-drive
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r6
    h: 57eda22c1714
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r3
    h: 8b211e171c09
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r3
    h: 8b211e171c09
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:usb-flash-drive
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r6
    h: 57eda22c1714
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r3
    h: 8b211e171c09
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r3
    h: 8b211e171c09
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r6
    h: 57eda22c1714
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r3
    h: 8b211e171c09
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r3
    h: 8b211e171c09
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:storage-drive-check
  note: Check the drive and its file system first; contact service if the code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r6
    h: 57eda22c1714
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r3
    h: 8b211e171c09
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r3
    h: 8b211e171c09
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:usb-drive-replacement
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r6
    h: 57eda22c1714
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r3
    h: 8b211e171c09
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r3
    h: 8b211e171c09
  review: drafted
---
