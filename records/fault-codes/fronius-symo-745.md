---
id: fc:fronius-symo-745
type: FaultCode
name: Fronius Symo 745
aliases:
- '745'
- Fronius 745
- Update file defective
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '745'
code_key: '745'
display_message: Update file defective
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r17
    h: 6693eb36d662
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
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
- claim_id: c6
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r17
    h: 6693eb36d662
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
---
