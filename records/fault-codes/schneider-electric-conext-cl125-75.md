---
id: fc:schneider-electric-conext-cl125-75
type: FaultCode
name: Schneider Electric CL125 075
aliases:
- '075'
- '75'
- Schneider Electric 075
- Solar irradiation is not sufficient for inverter operation
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '075'
code_key: '75'
display_message: Solar irradiation is not sufficient for inverter operation
page: 130
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r2
    h: 263fa810db4b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r9
    h: 6f701d85f9af
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:insufficient-irradiance
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r2
    h: 263fa810db4b
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r9
    h: 6f701d85f9af
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Irradiance is too low for the inverter to operate.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r2
    h: 263fa810db4b
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r9
    h: 6f701d85f9af
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Insufficient irradiation for operation implies stop, but a trip
    is not explicitly stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears once there is enough sunlight; if it recurs in good irradiance, review the PV
    design.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r2
    h: 263fa810db4b
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r9
    h: 6f701d85f9af
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Only if the event recurs while irradiance is sufficient.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r2
    h: 263fa810db4b
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r9
    h: 6f701d85f9af
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=54.r2
    h: 263fa810db4b
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r9
    h: 6f701d85f9af
  review: drafted
---
