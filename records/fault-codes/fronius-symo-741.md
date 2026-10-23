---
id: fc:fronius-symo-741
type: FaultCode
name: Fronius Symo 741
aliases:
- '741'
- Fronius 741
- Error when recording logging data
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '741'
code_key: '741'
display_message: Error when recording logging data
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r15
    h: d30ab03d2784
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:data-storage-failure
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r15
    h: d30ab03d2784
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:usb-flash-drive
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r15
    h: d30ab03d2784
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:storage-drive-check
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r15
    h: d30ab03d2784
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:usb-drive-replacement
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r15
    h: d30ab03d2784
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r15
    h: d30ab03d2784
  review: drafted
---
