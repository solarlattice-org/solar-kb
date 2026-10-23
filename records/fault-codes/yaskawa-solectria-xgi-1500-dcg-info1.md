---
id: fc:yaskawa-solectria-xgi-1500-dcg-info1
type: FaultCode
name: Yaskawa Solectria XGI-1500-DCG INFO-1
aliases:
- INFO-1
- info1
- Yaskawa Solectria INFO-1
- Power Derating, Temperature
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-dcg
family_name: Yaskawa Solectria XGI 1500-DCG
code: INFO-1
code_key: info1
display_message: Power Derating, Temperature
vendor_severity: Info
page: 58
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21.r1
    h: 67ef32086053
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21.r1
    h: 67ef32086053
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21
    h: 76fe58efcf3b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r1
    h: 67ef32086053
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21.r1
    h: 67ef32086053
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r1
    h: 67ef32086053
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21.r1
    h: 67ef32086053
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r1
    h: 67ef32086053
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21.r1
    h: 67ef32086053
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:fan-replacement
  note: Only if external fans are found not operating.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r1
    h: 67ef32086053
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21.r1
    h: 67ef32086053
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r1
    h: 67ef32086053
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21.r1
    h: 67ef32086053
  review: drafted
---
