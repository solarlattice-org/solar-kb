---
id: fc:yaskawa-solectria-sgi-500-750xtm-vsenseerror
type: FaultCode
name: Yaskawa Solectria SGI-XTM Vsense Error
aliases:
- Vsense Error
- vsenseerror
- Yaskawa Solectria Vsense Error
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Vsense Error
code_key: vsenseerror
vendor_severity: Critical
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r11
    h: 251d0aca9ea4
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r11
    h: 251d0aca9ea4
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
  review_note: 'support check: partial - Critical messages are displayed as errors and the row describes
    an internal failure needing service, but the fault class is…'
- claim_id: c3
  rel: indicates
  target: fm:voltage-sensor-fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r11
    h: 251d0aca9ea4
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r11
    h: 251d0aca9ea4
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r11
    h: 251d0aca9ea4
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r11
    h: 251d0aca9ea4
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
---
