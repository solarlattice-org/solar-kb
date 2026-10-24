---
id: fc:yaskawa-solectria-xgi-1500-crit9
type: FaultCode
name: Yaskawa Solectria XGI-1500 CRIT-9
aliases:
- CRIT-9
- crit9
- Yaskawa Solectria CRIT-9
- Critical Internal Hardware Failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: CRIT-9
code_key: crit9
display_message: Critical Internal Hardware Failure
vendor_severity: Critical
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r3
    h: 9ff3688aa2a9
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
  cite:
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=19.r3
    h: 9ff3688aa2a9
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=16.r3
    h: 9ff3688aa2a9
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r3
    h: 9ff3688aa2a9
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18
    h: bd286dd80521
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=19.r3
    h: 9ff3688aa2a9
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=18
    h: 0ec887918da1
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=16.r3
    h: 9ff3688aa2a9
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15
    h: bd286dd80521
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r2
    h: d2629351cf52
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r7
    h: 2731f0fff08f
  review: drafted
- claim_id: c6
  rel: indicates
  target: fm:power-stage-fault
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r2
    h: d2629351cf52
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r7
    h: 2731f0fff08f
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r2
    h: d2629351cf52
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r7
    h: 2731f0fff08f
  review: drafted
  review_note: 'support check: partial - The failure is in the powertrain, but the inverter bridge is
    not named.'
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r2
    h: d2629351cf52
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r7
    h: 2731f0fff08f
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; technical support if error persists.
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r2
    h: d2629351cf52
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r7
    h: 2731f0fff08f
  review: drafted
  review_note: 'support check: partial - Power cycle then support is stated, but clearing by manual reset
    is only implied.'
- claim_id: c10
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r3
    h: 9ff3688aa2a9
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=19.r3
    h: 9ff3688aa2a9
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=16.r3
    h: 9ff3688aa2a9
  review: drafted
---
