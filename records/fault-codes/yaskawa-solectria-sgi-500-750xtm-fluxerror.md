---
id: fc:yaskawa-solectria-sgi-500-750xtm-fluxerror
type: FaultCode
name: Yaskawa Solectria SGI-XTM Flux Error
aliases:
- Flux Error
- fluxerror
- Yaskawa Solectria Flux Error
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Flux Error
code_key: fluxerror
vendor_severity: Informative
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r12
    h: bdde4bf47fdf
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-sync-failure
  note: Internal phase lock loop failure.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r12
    h: bdde4bf47fdf
  review: drafted
  review_note: 'support check: partial - Internal phase lock loop failure is stated, which relates to
    grid sync, but ''grid synchronization failure'' is an inference.'
- claim_id: c3
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; service by authorized provider if it persists.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r12
    h: bdde4bf47fdf
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r12
    h: bdde4bf47fdf
  review: drafted
---
