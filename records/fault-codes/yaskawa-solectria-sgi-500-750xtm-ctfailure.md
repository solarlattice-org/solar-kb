---
id: fc:yaskawa-solectria-sgi-500-750xtm-ctfailure
type: FaultCode
name: Yaskawa Solectria SGI-XTM CT Failure
aliases:
- CT Failure
- ctfailure
- Yaskawa Solectria CT Failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: CT Failure
code_key: ctfailure
vendor_severity: Critical
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r2
    h: c73f998bb2b6
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:current-sensor-fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r2
    h: c73f998bb2b6
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r2
    h: c73f998bb2b6
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r2
    h: c73f998bb2b6
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r2
    h: c73f998bb2b6
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; authorized service if it persists.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r2
    h: c73f998bb2b6
  review: drafted
  review_note: 'support check: partial - Restart is the corrective action, but clearing by it isn''t explicitly
    stated.'
---
