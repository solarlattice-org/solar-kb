---
id: fc:schneider-electric-conext-cl125-78
type: FaultCode
name: Schneider Electric CL125 078
aliases:
- '078'
- '78'
- Schneider Electric 078
- PV power event warning
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '078'
code_key: '78'
display_message: PV power event warning
page: 130
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r4
    h: dcf727f4472f
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=34.r2
    h: 8bad0403ce44
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:loose-cable-connection
  note: Likely cause is loose connections at the PV input terminals.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r4
    h: dcf727f4472f
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=34.r2
    h: 8bad0403ce44
  review: drafted
  review_note: 'support check: partial - The solution is to check for loose connections, but the event
    is described as a PV power event warning, not…'
- claim_id: c4
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r4
    h: dcf727f4472f
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=34.r2
    h: 8bad0403ce44
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c5
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Retighten the terminals to the specified torque.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r4
    h: dcf727f4472f
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=34.r2
    h: 8bad0403ce44
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: has_event_class
  target: ec:warning
  note: The vendor labels this event a warning.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r4
    h: dcf727f4472f
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=34.r2
    h: 8bad0403ce44
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r4
    h: dcf727f4472f
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=34.r2
    h: 8bad0403ce44
  review: drafted
---
