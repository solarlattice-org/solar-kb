---
id: fc:schneider-electric-conext-cl125-39
type: FaultCode
name: Schneider Electric CL125 039
aliases:
- '039'
- '39'
- Schneider Electric 039
- Inverter insulation resistance event (ISO-flt)
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '039'
code_key: '39'
display_message: Inverter insulation resistance event (ISO-flt)
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r4
    h: de1c37f1f982
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r4
    h: 7c22df9d7d73
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r4
    h: de1c37f1f982
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r4
    h: 7c22df9d7d73
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r4
    h: de1c37f1f982
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r4
    h: 7c22df9d7d73
  review: drafted
  review_note: 'support check: partial - Passages say to test wiring insulation as a remedy, not that
    the event is detected by insulation resistance testing.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Implied by the instruction to wait for the inverter to recover.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r4
    h: de1c37f1f982
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r4
    h: 7c22df9d7d73
  review: drafted
  review_note: 'review: partial - ''Wait for the inverter to recover automatically'' suggests the inverter
    stopped, but no passage says production stops.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Then test wiring insulation; contact technical support if the event persists.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r4
    h: de1c37f1f982
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r4
    h: 7c22df9d7d73
  review: drafted
---
