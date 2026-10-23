---
id: fc:fronius-symo-438
type: FaultCode
name: Fronius Symo 438
aliases:
- '438'
- Fronius 438
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '438'
code_key: '438'
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r17
    h: 99124dc8e3e3
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:hardware-incompatibility
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r17
    h: 99124dc8e3e3
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r16
    h: 2711211cbc24
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:firmware-update
  note: Firmware update first; service technician if the code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r17
    h: 99124dc8e3e3
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r16
    h: 2711211cbc24
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r17
    h: 99124dc8e3e3
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
  review_note: 'support check: partial - The class 4 text is generic and does not tie 438 to class 4;
    the row says it self-retries.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Reconnects automatically if possible; service technician if it persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r17
    h: 99124dc8e3e3
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r16
    h: 2711211cbc24
  review: drafted
---
