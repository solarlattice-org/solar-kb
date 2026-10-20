---
id: fc:yaskawa-solectria-xgi-1500-warn30
type: FaultCode
name: Yaskawa Solectria XGI-1500 WARN-30
aliases:
- WARN-30
- warn30
- Yaskawa Solectria WARN-30
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: WARN-30
code_key: warn30
vendor_severity: Warning
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r4
    h: 30fada4483b8
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r4
    h: 30fada4483b8
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20
    h: fc50119e7e7e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:unauthorized-access-attempt
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r4
    h: 30fada4483b8
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r4
    h: 30fada4483b8
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r4
    h: 30fada4483b8
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
  review_note: 'support check: partial - Warnings can self-recover if conditions cease, but nothing in
    the row says this particular event auto-clears.'
---
