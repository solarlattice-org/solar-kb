---
id: fc:fronius-symo-314
type: FaultCode
name: Fronius Symo 314
aliases:
- '314'
- Fronius 314
- Timeout current sensor calibration
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '314'
code_key: '314'
display_message: Timeout current sensor calibration
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r13
    h: c13abd994ee5
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:current-sensor-calibration-timeout
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r13
    h: c13abd994ee5
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r13
    h: c13abd994ee5
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r13
    h: c13abd994ee5
  review: drafted
  review_note: 'support check: partial - The row describes a short interruption of feed-in, which suggests
    a trip, but doesn''t call it a fault.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r13
    h: c13abd994ee5
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes automatically; service technician if persistent.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r13
    h: c13abd994ee5
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when the code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r13
    h: c13abd994ee5
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
  review_note: 'support check: partial - The remedy marker ''*)'' maps to ''if status code persists: contact
    a Fronius-trained service technician'', but the passages never link…'
---
