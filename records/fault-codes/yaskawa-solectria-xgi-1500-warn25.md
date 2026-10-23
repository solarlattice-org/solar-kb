---
id: fc:yaskawa-solectria-xgi-1500-warn25
type: FaultCode
name: Yaskawa Solectria XGI-1500 WARN-25
aliases:
- WARN-25
- warn25
- Yaskawa Solectria WARN-25
- Communication 1 Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: WARN-25
code_key: warn25
display_message: Communication 1 Fault
vendor_severity: Warning
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r8
    h: 3aba5cfd6070
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
  cite:
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=21.r8
    h: 3aba5cfd6070
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r8
    h: 3aba5cfd6070
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r8
    h: 3aba5cfd6070
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20
    h: fc50119e7e7e
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=21.r8
    h: 3aba5cfd6070
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=20
    h: a7be798a92ad
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r8
    h: 3aba5cfd6070
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17
    h: a7be798a92ad
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r8
    h: 3aba5cfd6070
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r8
    h: 3aba5cfd6070
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r8
    h: 3aba5cfd6070
  review: drafted
  review_note: 'support check: partial - Communication processor initialization fault implies an internal
    fault, but ''internal device fault'' is not explicitly stated.'
- claim_id: c6
  rel: affects
  target: comp:communication-processor
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r8
    h: 3aba5cfd6070
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r8
    h: 3aba5cfd6070
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r8
    h: 3aba5cfd6070
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r8
    h: 3aba5cfd6070
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r8
    h: 3aba5cfd6070
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r8
    h: 3aba5cfd6070
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r8
    h: 3aba5cfd6070
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the error persists.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r8
    h: 3aba5cfd6070
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=18.r8
    h: 3aba5cfd6070
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=19.r8
    h: 3aba5cfd6070
  review: drafted
  review_note: 'support check: partial - Power cycle is an operator action, but the row doesn''t say the
    warning clears that way; the general text says…'
---
