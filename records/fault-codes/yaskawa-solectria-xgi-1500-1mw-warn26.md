---
id: fc:yaskawa-solectria-xgi-1500-1mw-warn26
type: FaultCode
name: Yaskawa Solectria XGI-1500-1MW WARN-26
aliases:
- WARN-26
- warn26
- Yaskawa Solectria WARN-26
- Communication 2 Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-1mw
family_name: Yaskawa Solectria XGI 1500-1MW
code: WARN-26
code_key: warn26
display_message: Communication 2 Fault
vendor_severity: Warning
page: 66
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=21.r9
    h: 8534a8b4965d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=21.r9
    h: 8534a8b4965d
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=20
    h: 75af07aa9414
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r9
    h: 8534a8b4965d
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r9
    h: 8534a8b4965d
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r9
    h: 8534a8b4965d
  review: drafted
  review_note: 'support check: partial - Communication processor application fault implies an internal
    fault, but ''internal device fault'' is not explicit.'
- claim_id: c4
  rel: affects
  target: comp:communication-processor
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r9
    h: 8534a8b4965d
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r9
    h: 8534a8b4965d
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r9
    h: 8534a8b4965d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r9
    h: 8534a8b4965d
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r9
    h: 8534a8b4965d
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r9
    h: 8534a8b4965d
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r9
    h: 8534a8b4965d
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the error persists.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r9
    h: 8534a8b4965d
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r9
    h: 8534a8b4965d
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r9
    h: 8534a8b4965d
  review: drafted
  review_note: 'support check: partial - Power cycle is an operator action, but the row doesn''t say the
    warning clears that way; the general text says…'
- claim_id: c8
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500-1mw
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=21.r9
    h: 8534a8b4965d
  review: drafted
---
