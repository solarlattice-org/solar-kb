---
id: fc:yaskawa-solectria-xgi-1500-info2
type: FaultCode
name: Yaskawa Solectria XGI-1500 INFO-2
aliases:
- INFO-2
- info2
- Yaskawa Solectria INFO-2
- Power Derating, Customer Command
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: INFO-2
code_key: info2
display_message: Power Derating, Customer Command
vendor_severity: Info
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r2
    h: 069df80c5ce8
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r2
    h: 069df80c5ce8
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23
    h: ae4d31cce1d2
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:remote-power-limit
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r2
    h: 069df80c5ce8
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:setpoint-dispatch-review
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r2
    h: 069df80c5ce8
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
  rel: has_production_effect
  target: ec:derate
  note: Contact support if no derate request was made.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r2
    h: 069df80c5ce8
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.3
    h: 4ce3b79bc3ed
  review: drafted
---
