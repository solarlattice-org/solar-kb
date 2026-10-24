---
id: fc:yaskawa-solectria-sgi-500-750xtm-rcmfault
type: FaultCode
name: Yaskawa Solectria SGI-XTM RCM Fault
aliases:
- RCM Fault
- rcmfault
- Yaskawa Solectria RCM Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: RCM Fault
code_key: rcmfault
vendor_severity: Critical
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r9
    h: fdcec88603e8
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r9
    h: fdcec88603e8
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r9
    h: fdcec88603e8
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
  review_note: 'support check: partial - Critical messages are displayed as errors, but the row does not
    state whether the device stops; the fault class is…'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r9
    h: fdcec88603e8
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  note: Qualified person must locate and repair the ground fault source.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r9
    h: fdcec88603e8
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r9
    h: fdcec88603e8
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
---
