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
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20
    h: 01dd772813e8
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20
    h: 01dd772813e8
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the error does not clear by itself
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20
    h: 01dd772813e8
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears on its own; escalate to service if persistent
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=20
    h: 01dd772813e8
  review: drafted
---
