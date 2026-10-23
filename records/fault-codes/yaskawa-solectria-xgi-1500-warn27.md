---
id: fc:yaskawa-solectria-xgi-1500-warn27
type: FaultCode
name: Yaskawa Solectria XGI-1500 WARN-27
aliases:
- WARN-27
- warn27
- Yaskawa Solectria WARN-27
- Communication 3 Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: WARN-27
code_key: warn27
display_message: Communication 3 Fault
vendor_severity: Warning
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r1
    h: 1114cf32932e
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
  cite:
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=22.r1
    h: 1114cf32932e
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r1
    h: 1114cf32932e
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r1
    h: 1114cf32932e
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20
    h: fc50119e7e7e
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=22.r1
    h: 1114cf32932e
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=20
    h: a7be798a92ad
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r1
    h: 1114cf32932e
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17
    h: a7be798a92ad
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r1
    h: 1114cf32932e
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r1
    h: 1114cf32932e
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r1
    h: 1114cf32932e
  review: drafted
  review_note: 'support check: partial - Communication processor hardware fault implies an internal fault,
    but ''internal device fault'' is not explicit.'
- claim_id: c6
  rel: affects
  target: comp:communication-processor
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r1
    h: 1114cf32932e
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r1
    h: 1114cf32932e
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r1
    h: 1114cf32932e
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r1
    h: 1114cf32932e
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r1
    h: 1114cf32932e
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r1
    h: 1114cf32932e
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r1
    h: 1114cf32932e
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
    loc: tbl=22.r1
    h: 1114cf32932e
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r1
    h: 1114cf32932e
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r1
    h: 1114cf32932e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
