---
id: fc:fronius-symo-601
type: FaultCode
name: Fronius Symo 601
aliases:
- '601'
- Fronius 601
- CAN bus is full
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '601'
code_key: '601'
display_message: CAN bus is full
vendor_severity: Class 6
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r1
    h: f1f5dec6cab3
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h24
    h: 4242ab97920a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-communication-failure
  note: Internal CAN bus is overloaded.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r1
    h: f1f5dec6cab3
  review: drafted
  review_note: 'support check: partial - CAN bus full matches internal communication failure, but the
    passage doesn''t say ''internal'' CAN bus or ''overloaded''.'
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r1
    h: f1f5dec6cab3
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h24
    h: 4242ab97920a
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r1
    h: f1f5dec6cab3
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:firmware-update
  note: Contact a trained service technician if the code persists after the update.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r1
    h: f1f5dec6cab3
  review: drafted
  review_note: 'support check: partial - Firmware update is stated, but the contact-technician-after-update
    note is not in the row.'
---
