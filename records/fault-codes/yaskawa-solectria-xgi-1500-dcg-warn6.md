---
id: fc:yaskawa-solectria-xgi-1500-dcg-warn6
type: FaultCode
name: Yaskawa Solectria XGI-1500-DCG WARN-6
aliases:
- WARN-6
- warn6
- Yaskawa Solectria WARN-6
- AC Very Low Frequency 2 Detected
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-dcg
family_name: Yaskawa Solectria XGI 1500-DCG
code: WARN-6
code_key: warn6
display_message: AC Very Low Frequency 2 Detected
vendor_severity: Warning
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r6
    h: 52310e005d49
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r6
    h: 52310e005d49
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18
    h: fc50119e7e7e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r6
    h: 52310e005d49
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r6
    h: 52310e005d49
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r6
    h: 52310e005d49
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r6
    h: 52310e005d49
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r6
    h: 52310e005d49
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r6
    h: 52310e005d49
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h151
    h: b0c738d81358
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Wait for the grid to recover; service if measurement differs by more than 2 percent
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r6
    h: 52310e005d49
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r6
    h: 52310e005d49
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r6
    h: 52310e005d49
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h151
    h: b0c738d81358
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r6
    h: 52310e005d49
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r6
    h: 52310e005d49
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r6
    h: 52310e005d49
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500-dcg
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r6
    h: 52310e005d49
  review: drafted
---
