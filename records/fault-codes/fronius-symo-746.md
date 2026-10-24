---
id: fc:fronius-symo-746
type: FaultCode
name: Fronius Symo 746
aliases:
- '746'
- Fronius 746
- Error occurred during the update
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '746'
code_key: '746'
display_message: Error occurred during the update
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r18
    h: c9ed61ead8c6
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  note: Update process is canceled.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r18
    h: c9ed61ead8c6
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:retry-update
  note: Retry after a short wait; service technician if code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r18
    h: c9ed61ead8c6
  review: drafted
  review_note: 'support check: partial - Restarting the update after 2 minutes is stated, but no service
    technician advice appears in the passage.'
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r18
    h: c9ed61ead8c6
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r18
    h: c9ed61ead8c6
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
---
