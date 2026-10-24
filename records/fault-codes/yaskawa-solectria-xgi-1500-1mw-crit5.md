---
id: fc:yaskawa-solectria-xgi-1500-1mw-crit5
type: FaultCode
name: Yaskawa Solectria XGI-1500-1MW CRIT-5
aliases:
- CRIT-5
- crit5
- Yaskawa Solectria CRIT-5
- AC Contactor Failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-1mw
family_name: Yaskawa Solectria XGI 1500-1MW
code: CRIT-5
code_key: crit5
display_message: AC Contactor Failure
vendor_severity: Critical
page: 64
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r4
    h: 50c72cf98570
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r4
    h: 50c72cf98570
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19
    h: d43f92f17c78
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:switch-status-fault
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r5
    h: ee59ec31ba64
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r5
    h: ee59ec31ba64
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r4
    h: 50c72cf98570
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r4
    h: 50c72cf98570
  review: drafted
  review_note: 'support check: partial - The AC contactor failure is stated, but the passages do not say
    it is a switch status fault. It is…'
- claim_id: c4
  rel: indicates
  target: fm:relay-failure
  note: Grid contactor may fail open or closed.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r5
    h: ee59ec31ba64
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r5
    h: ee59ec31ba64
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r4
    h: 50c72cf98570
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r4
    h: 50c72cf98570
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-contactor
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r5
    h: ee59ec31ba64
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r5
    h: ee59ec31ba64
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r4
    h: 50c72cf98570
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r4
    h: 50c72cf98570
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r5
    h: ee59ec31ba64
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r5
    h: ee59ec31ba64
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r4
    h: 50c72cf98570
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r4
    h: 50c72cf98570
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; technical support if error persists.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r5
    h: ee59ec31ba64
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r5
    h: ee59ec31ba64
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r4
    h: 50c72cf98570
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r4
    h: 50c72cf98570
  review: drafted
  review_note: 'support check: partial - Power cycle then support is stated, but clearing by manual reset
    is only implied.'
- claim_id: c8
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500-1mw
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r4
    h: 50c72cf98570
  review: drafted
---
