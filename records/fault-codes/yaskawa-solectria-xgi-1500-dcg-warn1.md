---
id: fc:yaskawa-solectria-xgi-1500-dcg-warn1
type: FaultCode
name: Yaskawa Solectria XGI-1500-DCG WARN-1
aliases:
- WARN-1
- warn1
- Yaskawa Solectria WARN-1
- Internal Over Current/ Over Voltage
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-dcg
family_name: Yaskawa Solectria XGI 1500-DCG
code: WARN-1
code_key: warn1
display_message: Internal Over Current/ Over Voltage
vendor_severity: Warning
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r1
    h: 97295ce050bd
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r1
    h: 97295ce050bd
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18
    h: fc50119e7e7e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-overcurrent-overvoltage
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r1
    h: 97295ce050bd
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r1
    h: 97295ce050bd
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r1
    h: 97295ce050bd
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Warning events stop AC production; the row says production is temporarily affected
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r1
    h: 97295ce050bd
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r1
    h: 97295ce050bd
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r1
    h: 97295ce050bd
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
    loc: tbl=20.r1
    h: 97295ce050bd
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r1
    h: 97295ce050bd
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r1
    h: 97295ce050bd
  review: drafted
  review_note: 'support check: partial - Power cycle is advised, but warnings can also self-recover; manual
    reset clearing is only implied.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r1
    h: 97295ce050bd
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r1
    h: 97295ce050bd
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r1
    h: 97295ce050bd
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500-dcg
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r1
    h: 97295ce050bd
  review: drafted
---
