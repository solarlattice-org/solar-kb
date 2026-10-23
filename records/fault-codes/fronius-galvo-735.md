---
id: fc:fronius-galvo-735
type: FaultCode
name: Fronius Galvo 735
aliases:
- '735'
- Fronius 735
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '735'
code_key: '735'
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r7
    h: 5e3b87908888
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h23
    h: 8efd8641166b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  note: Update is canceled because file is wrong for device or outdated.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r10
    h: 297b42096d4f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r7
    h: 5e3b87908888
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r7
    h: 5e3b87908888
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:update-file-check
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r10
    h: 297b42096d4f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r7
    h: 5e3b87908888
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r7
    h: 5e3b87908888
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:update-file-redownload
  note: Download the correct file if check fails; service if code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r10
    h: 297b42096d4f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r7
    h: 5e3b87908888
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r7
    h: 5e3b87908888
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r10
    h: 297b42096d4f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r7
    h: 5e3b87908888
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r7
    h: 5e3b87908888
  review: drafted
---
