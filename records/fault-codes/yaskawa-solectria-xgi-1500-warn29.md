---
id: fc:yaskawa-solectria-xgi-1500-warn29
type: FaultCode
name: Yaskawa Solectria XGI-1500 WARN-29
aliases:
- WARN-29
- warn29
- Yaskawa Solectria WARN-29
- Software Update Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: WARN-29
code_key: warn29
display_message: Software Update Fault
vendor_severity: Warning
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r3
    h: d1c666db0e5b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
  cite:
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=22.r3
    h: d1c666db0e5b
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r3
    h: d1c666db0e5b
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r3
    h: d1c666db0e5b
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20
    h: fc50119e7e7e
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=22.r3
    h: d1c666db0e5b
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=20
    h: a7be798a92ad
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r3
    h: d1c666db0e5b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17
    h: a7be798a92ad
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r3
    h: d1c666db0e5b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r3
    h: d1c666db0e5b
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r3
    h: d1c666db0e5b
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:communication-processor
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r3
    h: d1c666db0e5b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r3
    h: d1c666db0e5b
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r3
    h: d1c666db0e5b
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r3
    h: d1c666db0e5b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r3
    h: d1c666db0e5b
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r3
    h: d1c666db0e5b
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r3
    h: d1c666db0e5b
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
    loc: tbl=22.r3
    h: d1c666db0e5b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r3
    h: d1c666db0e5b
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r3
    h: d1c666db0e5b
  review: drafted
  review_note: 'support check: partial - A power cycle and then contacting support matches a manual reset,
    but section 9.1.2 also says warnings can self-recover, so…'
- claim_id: c10
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r3
    h: d1c666db0e5b
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=22.r3
    h: d1c666db0e5b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r3
    h: d1c666db0e5b
  review: drafted
---
