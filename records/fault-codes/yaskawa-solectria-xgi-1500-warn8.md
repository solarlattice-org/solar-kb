---
id: fc:yaskawa-solectria-xgi-1500-warn8
type: FaultCode
name: Yaskawa Solectria XGI-1500 WARN-8
aliases:
- WARN-8
- warn8
- Yaskawa Solectria WARN-8
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: WARN-8
code_key: warn8
vendor_severity: Warning
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r1
    h: bcb675936799
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r1
    h: bcb675936799
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20
    h: fc50119e7e7e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r1
    h: bcb675936799
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r1
    h: bcb675936799
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Wait for grid to recover; support only if measured frequency disagrees with inverter reading.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r1
    h: bcb675936799
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r1
    h: bcb675936799
  review: drafted
---
