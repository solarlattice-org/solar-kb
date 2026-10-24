---
id: fc:yaskawa-solectria-xgi-1500-crit11
type: FaultCode
name: Yaskawa Solectria XGI-1500 CRIT-11
aliases:
- CRIT-11
- crit11
- Yaskawa Solectria CRIT-11
- Operational Self Check Failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: CRIT-11
code_key: crit11
display_message: Operational Self Check Failure
vendor_severity: Critical
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r5
    h: 2ea826cbedaa
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
  cite:
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=19.r5
    h: 2ea826cbedaa
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=16.r5
    h: 2ea826cbedaa
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r5
    h: 2ea826cbedaa
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18
    h: bd286dd80521
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=19.r5
    h: 2ea826cbedaa
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=18
    h: 0ec887918da1
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=16.r5
    h: 2ea826cbedaa
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15
    h: bd286dd80521
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r3
    h: 76890d978352
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r8
    h: c327bc55c79a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r3
    h: 76890d978352
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r8
    h: c327bc55c79a
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r3
    h: 76890d978352
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r8
    h: c327bc55c79a
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; description states service is required if the error does not clear.
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r3
    h: 76890d978352
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r8
    h: c327bc55c79a
  review: drafted
  review_note: 'support check: partial - Power cycle is an operator action implying manual reset, but
    the row does not explicitly state the clearing mechanism.'
- claim_id: c9
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r5
    h: 2ea826cbedaa
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=19.r5
    h: 2ea826cbedaa
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=16.r5
    h: 2ea826cbedaa
  review: drafted
---
