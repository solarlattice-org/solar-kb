---
id: fc:yaskawa-solectria-xgi-1500-1mw-warn31
type: FaultCode
name: Yaskawa Solectria XGI-1500-1MW WARN-31
aliases:
- WARN-31
- warn31
- Yaskawa Solectria WARN-31
- Invalid Configuration Request
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-1mw
family_name: Yaskawa Solectria XGI 1500-1MW
code: WARN-31
code_key: warn31
display_message: Invalid Configuration Request
vendor_severity: Warning
page: 67
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=22.r5
    h: a82464b1d23a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=22.r5
    h: a82464b1d23a
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=20
    h: 75af07aa9414
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:parameter-change-rejected
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r5
    h: a82464b1d23a
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r5
    h: a82464b1d23a
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r5
    h: a82464b1d23a
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Re-enter a value within allowable limits.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r5
    h: a82464b1d23a
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r5
    h: a82464b1d23a
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r5
    h: a82464b1d23a
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Based on section statement that all warning events cease AC production.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r5
    h: a82464b1d23a
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500-1mw
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=22.r5
    h: a82464b1d23a
  review: drafted
---
