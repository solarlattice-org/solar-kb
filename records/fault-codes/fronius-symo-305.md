---
id: fc:fronius-symo-305
type: FaultCode
name: Fronius Symo 305
aliases:
- '305'
- Fronius 305
- No feed-in despite closed relay
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '305'
code_key: '305'
display_message: No feed-in despite closed relay
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r5
    h: 545163f75f61
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r5
    h: 545163f75f61
  review: drafted
  review_note: 'support check: partial - The description ''No feed-in despite closed relay'' implies the
    grid relay, but the passage does not name it as the…'
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r5
    h: 545163f75f61
  review: drafted
  review_note: 'support check: partial - The interruption is brief and the inverter restarts, so a fault
    class is only loosely implied, and the passage does…'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r5
    h: 545163f75f61
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Contact installer if it keeps recurring.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r5
    h: 545163f75f61
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
---
