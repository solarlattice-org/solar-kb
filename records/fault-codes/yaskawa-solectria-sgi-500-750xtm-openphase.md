---
id: fc:yaskawa-solectria-sgi-500-750xtm-openphase
type: FaultCode
name: Yaskawa Solectria SGI-XTM Open Phase
aliases:
- Open Phase
- openphase
- Yaskawa Solectria Open Phase
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Open Phase
code_key: openphase
vendor_severity: Critical
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r8
    h: c8f6b700404a
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:phase-loss
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r8
    h: c8f6b700404a
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r8
    h: c8f6b700404a
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
  review_note: 'support check: partial - Critical messages are displayed as errors, but the row does not
    state whether the device stops; the fault class is…'
- claim_id: c4
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r8
    h: c8f6b700404a
  review: drafted
---
