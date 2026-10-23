---
id: fc:yaskawa-solectria-sgi-500-750xtm-waittorestart
type: FaultCode
name: Yaskawa Solectria SGI-XTM Wait to Restart
aliases:
- Wait to Restart
- waittorestart
- Yaskawa Solectria Wait to Restart
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Wait to Restart
code_key: waittorestart
vendor_severity: Informative
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r7
    h: fe3241768089
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r7
    h: fe3241768089
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: No feed-in during the grid reconnect countdown.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r7
    h: fe3241768089
  review: drafted
  review_note: 'support check: partial - A grid reconnect countdown implies the inverter is not feeding
    in. The row never states that production stops.'
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r7
    h: fe3241768089
  review: drafted
  review_note: 'support check: partial - A countdown with no action needed implies the state ends on its
    own. The row doesn''t explicitly say it clears automatically.'
---
