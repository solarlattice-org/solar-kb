---
id: fc:yaskawa-solectria-xgi-1500-dcg-warn13
type: FaultCode
name: Yaskawa Solectria XGI-1500-DCG WARN-13
aliases:
- WARN-13
- warn13
- Yaskawa Solectria WARN-13
- AC Very High Voltage 2 Detected
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-dcg
family_name: Yaskawa Solectria XGI 1500-DCG
code: WARN-13
code_key: warn13
display_message: AC Very High Voltage 2 Detected
vendor_severity: Warning
page: 57
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r6
    h: 7c3b9865858a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r6
    h: 7c3b9865858a
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=18
    h: fc50119e7e7e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r6
    h: 7c3b9865858a
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r6
    h: 7c3b9865858a
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r6
    h: 7c3b9865858a
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r6
    h: 7c3b9865858a
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r6
    h: 7c3b9865858a
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r6
    h: 7c3b9865858a
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when measured voltage differs from the inverter reading by more than 2 percent.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r6
    h: 7c3b9865858a
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r6
    h: 7c3b9865858a
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r6
    h: 7c3b9865858a
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r6
    h: 7c3b9865858a
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes once grid conditions improve; service only if measurement discrepancy exists.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r6
    h: 7c3b9865858a
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
---
