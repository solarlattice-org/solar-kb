---
id: fc:yaskawa-solectria-xgi-1500-1mw-warn2
type: FaultCode
name: Yaskawa Solectria XGI-1500-1MW WARN-2
aliases:
- WARN-2
- warn2
- Yaskawa Solectria WARN-2
- Phase Lock Loop Failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-1mw
family_name: Yaskawa Solectria XGI 1500-1MW
code: WARN-2
code_key: warn2
display_message: Phase Lock Loop Failure
vendor_severity: Warning
page: 65
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=20.r2
    h: dbb8e24a7219
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=20.r2
    h: dbb8e24a7219
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=20
    h: 75af07aa9414
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-sync-failure
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r2
    h: dbb8e24a7219
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r2
    h: dbb8e24a7219
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r2
    h: dbb8e24a7219
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Warning events stop AC production; the row says production is temporarily affected
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r2
    h: dbb8e24a7219
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r2
    h: dbb8e24a7219
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r2
    h: dbb8e24a7219
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h151
    h: b0c738d81358
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact technical support if the error persists
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r2
    h: dbb8e24a7219
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r2
    h: dbb8e24a7219
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r2
    h: dbb8e24a7219
  review: drafted
  review_note: 'support check: partial - Power cycle advised, but manual reset as the clearing mode is
    only implied; warnings self-recover.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r2
    h: dbb8e24a7219
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r2
    h: dbb8e24a7219
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r2
    h: dbb8e24a7219
  review: drafted
---
