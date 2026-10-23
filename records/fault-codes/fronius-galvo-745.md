---
id: fc:fronius-galvo-745
type: FaultCode
name: Fronius Galvo 745
aliases:
- '745'
- Fronius 745
- Update file defective
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '745'
code_key: '745'
display_message: Update file defective
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r11
    h: 428a9f4632bf
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h23
    h: 8efd8641166b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  note: Update is canceled due to a defective file.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r17
    h: 6693eb36d662
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r11
    h: 428a9f4632bf
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r11
    h: 428a9f4632bf
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:update-file-redownload
  note: Service technician if code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r17
    h: 6693eb36d662
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r11
    h: 428a9f4632bf
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r11
    h: 428a9f4632bf
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:storage-drive-check
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r17
    h: 6693eb36d662
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r17
    h: 6693eb36d662
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r11
    h: 428a9f4632bf
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r11
    h: 428a9f4632bf
  review: drafted
---
