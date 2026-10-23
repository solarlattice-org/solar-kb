---
id: fc:yaskawa-solectria-sgi-500-750xtm-filterconterr
type: FaultCode
name: Yaskawa Solectria SGI-XTM Filter Cont. Err
aliases:
- Filter Cont. Err
- filterconterr
- Yaskawa Solectria Filter Cont. Err
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Filter Cont. Err
code_key: filterconterr
vendor_severity: Informative
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r11
    h: ba58bd4c1521
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:filter-malfunction
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r11
    h: ba58bd4c1521
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:filter-contactor
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r11
    h: ba58bd4c1521
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  note: Listed as informative; condition flagged while AC output continues.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r11
    h: ba58bd4c1521
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
  review_note: 'support check: partial - Row says condition exists while AC continues and u3 says informative
    messages, but ''Warning'' class isn''t stated (informative rather than warning).'
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r11
    h: ba58bd4c1521
  review: drafted
  review_note: 'support check: partial - AC power still produced, but the LC filter is not working; ''no
    production effect'' is implied but not stated.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; service by authorized provider if it persists.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r11
    h: ba58bd4c1521
  review: drafted
  review_note: 'support check: partial - Corrective action is turning DC/AC off and restarting (operator
    restart), with service if it persists; reset type is implied, not…'
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r11
    h: ba58bd4c1521
  review: drafted
---
