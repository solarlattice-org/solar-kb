---
id: fc:yaskawa-solectria-xgi-1500-dcg-crit7
type: FaultCode
name: Yaskawa Solectria XGI-1500-DCG CRIT-7
aliases:
- CRIT-7
- crit7
- Yaskawa Solectria CRIT-7
- Ground Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-dcg
family_name: Yaskawa Solectria XGI 1500-DCG
code: CRIT-7
code_key: crit7
display_message: Ground Fault
vendor_severity: Critical
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r1
    h: 7b61827d0a62
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r1
    h: 7b61827d0a62
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16
    h: 3a195da0c10b
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
---
