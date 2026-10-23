---
id: fc:yaskawa-solectria-sgi-500-750xtm-softshutdown
type: FaultCode
name: Yaskawa Solectria SGI-XTM Soft Shutdown
aliases:
- Soft Shutdown
- softshutdown
- Yaskawa Solectria Soft Shutdown
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Soft Shutdown
code_key: softshutdown
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r15
    h: a1afea6f5374
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:remote-shutdown
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r15
    h: a1afea6f5374
  review: drafted
  review_note: 'support check: partial - Inverter disabled by soft shutdown function; ''remote shutdown''
    is implied via Modbus command but not explicitly stated.'
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r15
    h: a1afea6f5374
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Operator turns inverter on via UI.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r15
    h: a1afea6f5374
  review: drafted
---
