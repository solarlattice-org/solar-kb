---
id: fc:yaskawa-solectria-xgi-1500-warn28
type: FaultCode
name: Yaskawa Solectria XGI-1500 WARN-28
aliases:
- WARN-28
- warn28
- Yaskawa Solectria WARN-28
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: WARN-28
code_key: warn28
vendor_severity: Warning
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20
    h: fc50119e7e7e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:network-connection-check
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Self-recovers per section once the network connection is restored.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
---
