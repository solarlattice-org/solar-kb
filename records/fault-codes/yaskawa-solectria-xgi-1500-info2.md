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
  rel: defined_in
  target: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
  cite:
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=23.r2
    h: 069df80c5ce8
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=20.r2
    h: 069df80c5ce8
  review: drafted
- claim_id: c4
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
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=23.r2
    h: 069df80c5ce8
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=23
    h: ae4d31cce1d2
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=20.r2
    h: 069df80c5ce8
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=20
    h: ae4d31cce1d2
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:remote-power-limit
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r2
    h: 069df80c5ce8
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21.r2
    h: 069df80c5ce8
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:setpoint-dispatch-review
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r2
    h: 069df80c5ce8
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21.r2
    h: 069df80c5ce8
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when no derate request was actually made.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r2
    h: 069df80c5ce8
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21.r2
    h: 069df80c5ce8
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r2
    h: 069df80c5ce8
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21.r2
    h: 069df80c5ce8
  review: drafted
---
