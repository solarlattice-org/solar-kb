---
id: fc:yaskawa-solectria-xgi-1500-dcg-crit11
type: FaultCode
name: Yaskawa Solectria XGI-1500-DCG CRIT-11
aliases:
- CRIT-11
- crit11
- Yaskawa Solectria CRIT-11
- Operational Self Check Failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-dcg
family_name: Yaskawa Solectria XGI 1500-DCG
code: CRIT-11
code_key: crit11
display_message: Operational Self Check Failure
vendor_severity: Critical
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r3
    h: 76890d978352
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r3
    h: 76890d978352
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16
    h: 3a195da0c10b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r3
    h: 76890d978352
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r8
    h: c327bc55c79a
  review: drafted
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500-dcg
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r3
    h: 76890d978352
  review: drafted
---
