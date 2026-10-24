---
id: fc:yaskawa-solectria-xgi-1500-1mw-crit6
type: FaultCode
name: Yaskawa Solectria XGI-1500-1MW CRIT-6
aliases:
- CRIT-6
- crit6
- Yaskawa Solectria CRIT-6
- Critical Over Temperature
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-1mw
family_name: Yaskawa Solectria XGI 1500-1MW
code: CRIT-6
code_key: crit6
display_message: Critical Over Temperature
vendor_severity: Critical
page: 64
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r5
    h: 16f90f507007
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r5
    h: 16f90f507007
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19
    h: d43f92f17c78
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r5
    h: 16f90f507007
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r5
    h: 7e267fe7e807
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17
    h: 2977d7d89391
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r5
    h: 16f90f507007
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r5
    h: 7e267fe7e807
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17
    h: 2977d7d89391
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r5
    h: 16f90f507007
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r5
    h: 7e267fe7e807
  review: drafted
  review_note: 'support check: partial - Checking that the fans are operating is a troubleshooting step,
    not a detection method for the fault.'
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r5
    h: 16f90f507007
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r5
    h: 7e267fe7e807
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:fan-replacement
  note: When external fans are not operating.
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r5
    h: 16f90f507007
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17
    h: 2977d7d89391
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500-1mw
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r5
    h: 16f90f507007
  review: drafted
---
