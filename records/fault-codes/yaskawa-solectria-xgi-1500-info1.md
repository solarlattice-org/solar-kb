---
id: fc:yaskawa-solectria-xgi-1500-info1
type: FaultCode
name: Yaskawa Solectria XGI-1500 INFO-1
aliases:
- INFO-1
- info1
- Yaskawa Solectria INFO-1
- Power Derating, Temperature
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: INFO-1
code_key: info1
display_message: Power Derating, Temperature
vendor_severity: Info
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r1
    h: 67ef32086053
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r1
    h: 67ef32086053
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23
    h: ae4d31cce1d2
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r1
    h: 67ef32086053
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r1
    h: 67ef32086053
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:fan-replacement
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r1
    h: 67ef32086053
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r1
    h: 67ef32086053
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:derate
  note: No derate value stated.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r1
    h: 67ef32086053
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.3
    h: 4ce3b79bc3ed
  review: drafted
---
