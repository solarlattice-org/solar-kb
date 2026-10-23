---
id: fc:yaskawa-solectria-xgi-1500-1mw-info2
type: FaultCode
name: Yaskawa Solectria XGI-1500-1MW INFO-2
aliases:
- INFO-2
- info2
- Yaskawa Solectria INFO-2
- Power Derating, Customer Command
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-1mw
family_name: Yaskawa Solectria XGI 1500-1MW
code: INFO-2
code_key: info2
display_message: Power Derating, Customer Command
vendor_severity: Info
page: 67
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=23.r2
    h: 069df80c5ce8
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=23.r2
    h: 069df80c5ce8
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=23
    h: 22e0cd33fa72
  review: drafted
- claim_id: c3
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
- claim_id: c4
  rel: detected_by
  target: method:setpoint-dispatch-review
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23.r2
    h: 069df80c5ce8
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=21.r2
    h: 069df80c5ce8
  review: drafted
- claim_id: c5
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
- claim_id: c6
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
