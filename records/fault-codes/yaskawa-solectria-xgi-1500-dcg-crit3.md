---
id: fc:yaskawa-solectria-xgi-1500-dcg-crit3
type: FaultCode
name: Yaskawa Solectria XGI-1500-DCG CRIT-3
aliases:
- CRIT-3
- crit3
- Yaskawa Solectria CRIT-3
- Internal Communication 2 Failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-dcg
family_name: Yaskawa Solectria XGI 1500-DCG
code: CRIT-3
code_key: crit3
display_message: Internal Communication 2 Failure
vendor_severity: Critical
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r3
    h: 2ba4661036f5
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16
    h: 3a195da0c10b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r3
    h: 2ba4661036f5
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:firmware-update
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r3
    h: 2ba4661036f5
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r3
    h: 2ba4661036f5
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Firmware update and power cycle first; technical support if it persists.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r3
    h: 2ba4661036f5
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r3
    h: 2ba4661036f5
  review: drafted
  review_note: 'support check: partial - Power cycle and firmware update are stated, but clearing by manual
    reset is only implied.'
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500-dcg
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16.r3
    h: 2ba4661036f5
  review: drafted
---
