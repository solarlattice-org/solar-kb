---
id: fc:yaskawa-solectria-xgi-1500-warn7
type: FaultCode
name: Yaskawa Solectria XGI-1500 WARN-7
aliases:
- WARN-7
- warn7
- Yaskawa Solectria WARN-7
- AC High Frequency 1 Detected
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: WARN-7
code_key: warn7
display_message: AC High Frequency 1 Detected
vendor_severity: Warning
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r7
    h: c09c57d5b97b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
  cite:
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=20.r7
    h: c09c57d5b97b
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r7
    h: c09c57d5b97b
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r7
    h: c09c57d5b97b
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20
    h: fc50119e7e7e
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=20.r7
    h: c09c57d5b97b
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=20
    h: a7be798a92ad
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r7
    h: c09c57d5b97b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17
    h: a7be798a92ad
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r7
    h: c09c57d5b97b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r7
    h: c09c57d5b97b
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r7
    h: c09c57d5b97b
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r7
    h: c09c57d5b97b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r7
    h: c09c57d5b97b
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r7
    h: c09c57d5b97b
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h151
    h: b0c738d81358
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Wait for the grid to recover; service if measurement differs by more than 2 percent
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r7
    h: c09c57d5b97b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r7
    h: c09c57d5b97b
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r7
    h: c09c57d5b97b
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h151
    h: b0c738d81358
  review: drafted
- claim_id: c8
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r7
    h: c09c57d5b97b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r7
    h: c09c57d5b97b
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18.r7
    h: c09c57d5b97b
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r7
    h: c09c57d5b97b
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=20.r7
    h: c09c57d5b97b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17.r7
    h: c09c57d5b97b
  review: drafted
---
