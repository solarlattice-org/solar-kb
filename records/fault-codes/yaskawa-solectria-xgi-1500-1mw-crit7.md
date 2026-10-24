---
id: fc:yaskawa-solectria-xgi-1500-1mw-crit7
type: FaultCode
name: Yaskawa Solectria XGI-1500-1MW CRIT-7
aliases:
- CRIT-7
- crit7
- Yaskawa Solectria CRIT-7
- Ground Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-1mw
family_name: Yaskawa Solectria XGI 1500-1MW
code: CRIT-7
code_key: crit7
display_message: Ground Fault
vendor_severity: Critical
page: 64
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r6
    h: 54aa331e6877
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r6
    h: 54aa331e6877
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19
    h: d43f92f17c78
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r1
    h: 7b61827d0a62
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r6
    h: 54aa331e6877
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r1
    h: 7b61827d0a62
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r6
    h: 54aa331e6877
  review: drafted
  review_note: 'support check: partial - The PV array disconnect, combiners and panels are mentioned,
    but the passages do not state that the fault affects the…'
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r1
    h: 7b61827d0a62
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r6
    h: 54aa331e6877
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  note: Qualified person must locate and repair the ground fault; equipment must not be touched.
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r1
    h: 7b61827d0a62
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r6
    h: 54aa331e6877
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500-1mw
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=19.r6
    h: 54aa331e6877
  review: drafted
---
