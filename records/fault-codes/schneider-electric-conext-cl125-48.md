---
id: fc:schneider-electric-conext-cl125-48
type: FaultCode
name: Schneider Electric CL125 048
aliases:
- '048'
- '48'
- Schneider Electric 048
- Phase-Rcurrent samplingchannel event
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '048'
code_key: '48'
display_message: Phase-Rcurrent samplingchannel event
page: 128
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r4
    h: 5d91dae4e7a5
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r2
    h: e17817788c3a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r4
    h: 5d91dae4e7a5
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r2
    h: e17817788c3a
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: If the event persists, escalate to technical support.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=52.r4
    h: 5d91dae4e7a5
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r2
    h: e17817788c3a
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
