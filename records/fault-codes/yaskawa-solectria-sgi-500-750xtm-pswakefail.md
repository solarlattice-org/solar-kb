---
id: fc:yaskawa-solectria-sgi-500-750xtm-pswakefail
type: FaultCode
name: Yaskawa Solectria SGI-XTM PS Wake Fail
aliases:
- PS Wake Fail
- pswakefail
- Yaskawa Solectria PS Wake Fail
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: PS Wake Fail
code_key: pswakefail
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r8
    h: 41e6b2ab4a53
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:power-stage-fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r8
    h: 41e6b2ab4a53
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r8
    h: 41e6b2ab4a53
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Power stage fails during wake up, so the inverter does not start.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r8
    h: 41e6b2ab4a53
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; service if the problem persists.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r8
    h: 41e6b2ab4a53
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r8
    h: 41e6b2ab4a53
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r8
    h: 41e6b2ab4a53
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
