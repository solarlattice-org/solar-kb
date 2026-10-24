---
id: fc:yaskawa-solectria-pvi-23-36tl-intprotect10-260
type: FaultCode
name: Yaskawa Solectria PVI-TL IntProtect0010-0260
aliases:
- IntProtect0010-0260
- intprotect10-260
- Yaskawa Solectria IntProtect0010-0260
- Internal problem within the inverter
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: IntProtect0010-0260
code_key: intprotect10-260
code_from: 10
code_to: 260
display_message: Internal problem within the inverter
vendor_severity: Protection
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20
    h: 01dd772813e8
  review: drafted
  review_note: code printed in the table header line
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20
    h: 01dd772813e8
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20
    h: 01dd772813e8
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20
    h: 01dd772813e8
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the error does not clear automatically.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20
    h: 01dd772813e8
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Watch for automatic clearing first; then contact service.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20
    h: 01dd772813e8
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-pvi-23-36tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20
    h: 01dd772813e8
  review: drafted
---
