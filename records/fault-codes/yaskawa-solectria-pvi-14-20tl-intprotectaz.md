---
id: fc:yaskawa-solectria-pvi-14-20tl-intprotectaz
type: FaultCode
name: Yaskawa Solectria PVI-14-20TL IntProtectA~Z
aliases:
- IntProtectA~Z
- intprotectaz
- Yaskawa Solectria IntProtectA~Z
- Internal problem within the inverter
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-14-20tl
family_name: Solectria PVI 14/20TL
code: IntProtectA~Z
code_key: intprotectaz
display_message: Internal problem within the inverter
vendor_severity: Protection
page: 51
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r3
    h: e56bad3e4745
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r4
    h: 1a7d21381ce9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r3
    h: e56bad3e4745
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r4
    h: 1a7d21381ce9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r3
    h: e56bad3e4745
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r4
    h: 1a7d21381ce9
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r3
    h: e56bad3e4745
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r3
    h: e56bad3e4745
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: May clear on its own within 10 minutes; if not, contact service
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r3
    h: e56bad3e4745
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r4
    h: 1a7d21381ce9
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the alarm persists
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r4
    h: 1a7d21381ce9
  review: drafted
---
