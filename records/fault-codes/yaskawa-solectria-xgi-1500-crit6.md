---
id: fc:yaskawa-solectria-xgi-1500-crit6
type: FaultCode
name: Yaskawa Solectria XGI-1500 CRIT-6
aliases:
- CRIT-6
- crit6
- Yaskawa Solectria CRIT-6
- Critical Over Temperature
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: CRIT-6
code_key: crit6
display_message: Critical Over Temperature
vendor_severity: Critical
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19
    h: 5cef408e7946
  review: drafted
  review_note: code printed in the table header line
- claim_id: c2
  rel: defined_in
  target: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
  cite:
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=19
    h: 5cef408e7946
  review: drafted
  review_note: code printed in the table header line
- claim_id: c3
  rel: defined_in
  target: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=16
    h: 3b7264257d02
  review: drafted
  review_note: code printed in the table header line
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19
    h: 5cef408e7946
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18
    h: bd286dd80521
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=19
    h: 5cef408e7946
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=18
    h: 0ec887918da1
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=16
    h: 3b7264257d02
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15
    h: bd286dd80521
  review: drafted
- claim_id: c5
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
  review: drafted
- claim_id: c6
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
- claim_id: c7
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
- claim_id: c8
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r5
    h: 16f90f507007
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r5
    h: 7e267fe7e807
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c9
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
- claim_id: c10
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19
    h: 5cef408e7946
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=19
    h: 5cef408e7946
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=16
    h: 3b7264257d02
  review: drafted
---
