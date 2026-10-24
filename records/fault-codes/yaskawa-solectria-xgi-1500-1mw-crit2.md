---
id: fc:yaskawa-solectria-xgi-1500-1mw-crit2
type: FaultCode
name: Yaskawa Solectria XGI-1500-1MW CRIT-2
aliases:
- CRIT-2
- crit2
- Yaskawa Solectria CRIT-2
- Internal Communication 1 Failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-1mw
family_name: Yaskawa Solectria XGI 1500-1MW
code: CRIT-2
code_key: crit2
display_message: Internal Communication 1 Failure
vendor_severity: Critical
page: 64
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r2
    h: 19341281f673
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19
    h: d43f92f17c78
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r2
    h: 19341281f673
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:firmware-update
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r2
    h: 19341281f673
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r2
    h: 19341281f673
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Firmware update and power cycle first; technical support if it persists.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r2
    h: 19341281f673
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r2
    h: 19341281f673
  review: drafted
  review_note: 'support check: partial - Power cycle and firmware update are stated, but clearing by manual
    reset is only implied.'
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500-1mw
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r2
    h: 19341281f673
  review: drafted
---
