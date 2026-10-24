---
id: fc:yaskawa-solectria-sgi-500-750xtm-movfault
type: FaultCode
name: Yaskawa Solectria SGI-XTM MOV Fault
aliases:
- MOV Fault
- movfault
- Yaskawa Solectria MOV Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: MOV Fault
code_key: movfault
vendor_severity: Critical
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r6
    h: 3c0aa4eb4ab6
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:surge-protector-exhausted
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r6
    h: 3c0aa4eb4ab6
  review: drafted
  review_note: 'support check: partial - The passage says the DC MOV is in fault condition, which is roughly
    an exhausted surge protector, but exhaustion isn''t stated.'
- claim_id: c3
  rel: affects
  target: comp:surge-protection-device
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r6
    h: 3c0aa4eb4ab6
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  note: Listed as critical, but the inverter keeps running.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r6
    h: 3c0aa4eb4ab6
  review: drafted
  review_note: 'support check: partial - The inverter keeps running, which fits a warning, but the passage
    doesn''t say it is classed as one and calls…'
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r6
    h: 3c0aa4eb4ab6
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  note: Site visit recommended, not urgent.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r6
    h: 3c0aa4eb4ab6
  review: drafted
  review_note: 'support check: partial - A site visit is recommended, but the passage doesn''t state that
    the fault clears by service.'
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r6
    h: 3c0aa4eb4ab6
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
---
