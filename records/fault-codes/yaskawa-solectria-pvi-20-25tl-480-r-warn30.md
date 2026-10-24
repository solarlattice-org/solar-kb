---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-warn30
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R WARN-30
aliases:
- WARN-30
- warn30
- Yaskawa Solectria WARN-30
- EepromErr
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: WARN-30
code_key: warn30
display_message: EepromErr
vendor_severity: Warning
page: 79
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r1
    h: 56bd14b8774e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r1
    h: 56bd14b8774e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:unauthorized-access-attempt
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r4
    h: 30fada4483b8
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r4
    h: 30fada4483b8
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r4
    h: 30fada4483b8
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Based on section statement that all warning events cease AC production.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r4
    h: 30fada4483b8
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:yaskawa-solectria-pvi-20-25tl-480-r
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r1
    h: 56bd14b8774e
  review: drafted
---
