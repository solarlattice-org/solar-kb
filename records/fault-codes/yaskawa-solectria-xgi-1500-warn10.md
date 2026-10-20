---
id: fc:yaskawa-solectria-xgi-1500-warn10
type: FaultCode
name: Yaskawa Solectria XGI-1500 WARN-10
aliases:
- WARN-10
- warn10
- Yaskawa Solectria WARN-10
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: WARN-10
code_key: warn10
vendor_severity: Warning
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r3
    h: 90108db5968e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r3
    h: 90108db5968e
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20
    h: fc50119e7e7e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r3
    h: 90108db5968e
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r3
    h: 90108db5968e
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Wait for grid to recover; support only if measured voltage disagrees with inverter reading.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r3
    h: 90108db5968e
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r3
    h: 90108db5968e
  review: drafted
---
