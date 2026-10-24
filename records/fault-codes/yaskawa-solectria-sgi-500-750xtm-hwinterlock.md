---
id: fc:yaskawa-solectria-sgi-500-750xtm-hwinterlock
type: FaultCode
name: Yaskawa Solectria SGI-XTM Hw Interlock
aliases:
- Hw Interlock
- hwinterlock
- Yaskawa Solectria Hw Interlock
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Hw Interlock
code_key: hwinterlock
vendor_severity: Informative
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r13
    h: 1ec1f6ad7fc8
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-undervoltage
  note: Alternatively the hardware safety interlock is not satisfied.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r13
    h: 1ec1f6ad7fc8
  review: drafted
  review_note: 'support check: partial - Description says interlock not satisfied or DC voltage too low
    to connect; DC undervoltage is one alternative only.'
- claim_id: c3
  rel: affects
  target: comp:pv-disconnect-switch
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r13
    h: 1ec1f6ad7fc8
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r13
    h: 1ec1f6ad7fc8
  review: drafted
  review_note: 'support check: partial - Corrective action says verify DC voltage, but the passage doesn''t
    say the fault is detected by DC voltage measurement.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Inverter cannot connect.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r13
    h: 1ec1f6ad7fc8
  review: drafted
  review_note: 'support check: partial - ''Too low to connect'' implies the inverter doesn''t connect
    (not feeding in), but trip is not explicitly stated.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Check switch and DC voltage, then power-cycle; persistent case points to array sizing.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r13
    h: 1ec1f6ad7fc8
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r13
    h: 1ec1f6ad7fc8
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r13
    h: 1ec1f6ad7fc8
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
