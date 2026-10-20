---
id: fc:yaskawa-solectria-xgi-1500-crit6
type: FaultCode
name: Yaskawa Solectria XGI-1500 CRIT-6
aliases:
- CRIT-6
- crit6
- Yaskawa Solectria CRIT-6
- Critical Over Temperature
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: CRIT-6
code_key: crit6
display_message: Critical Over Temperature
vendor_severity: Critical
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19
    h: 5cef408e7946
  review: drafted
  review_note: code printed in the table header line
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19
    h: 5cef408e7946
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18
    h: bd286dd80521
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19
    h: 5cef408e7946
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19
    h: 5cef408e7946
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19
    h: 5cef408e7946
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c6
  rel: mitigated_by
  target: mit:fan-replacement
  note: Applies when the external fans are not operating.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19
    h: 5cef408e7946
  review: drafted
---
