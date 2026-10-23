---
id: fc:yaskawa-solectria-sgi-500-750xtm-desaterror
type: FaultCode
name: Yaskawa Solectria SGI-XTM Desat Error
aliases:
- Desat Error
- desaterror
- Yaskawa Solectria Desat Error
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Desat Error
code_key: desaterror
vendor_severity: Critical
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r4
    h: 3e3a774d0e4a
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r4
    h: 3e3a774d0e4a
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r4
    h: 3e3a774d0e4a
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r4
    h: 3e3a774d0e4a
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; authorized service if it persists.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r4
    h: 3e3a774d0e4a
  review: drafted
  review_note: 'support check: partial - Restart is the corrective action, but clearing by it isn''t explicitly
    stated.'
---
