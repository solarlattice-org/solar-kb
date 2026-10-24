---
id: fc:yaskawa-solectria-xgi-1500-crit7
type: FaultCode
name: Yaskawa Solectria XGI-1500 CRIT-7
aliases:
- CRIT-7
- crit7
- Yaskawa Solectria CRIT-7
- Ground Fault, Excessive Leakage Current
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: CRIT-7
code_key: crit7
display_message: Ground Fault, Excessive Leakage Current
vendor_severity: Critical
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r1
    h: 8cc7b04502b0
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
  cite:
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=19.r1
    h: 8cc7b04502b0
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=16.r1
    h: 8cc7b04502b0
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r1
    h: 8cc7b04502b0
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18
    h: bd286dd80521
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=19.r1
    h: 8cc7b04502b0
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=18
    h: 0ec887918da1
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=16.r1
    h: 8cc7b04502b0
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=15
    h: bd286dd80521
  review: drafted
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
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
- claim_id: c8
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
- claim_id: c9
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r1
    h: 8cc7b04502b0
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=19.r1
    h: 8cc7b04502b0
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=16.r1
    h: 8cc7b04502b0
  review: drafted
---
