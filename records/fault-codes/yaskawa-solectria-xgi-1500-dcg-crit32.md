---
id: fc:yaskawa-solectria-xgi-1500-dcg-crit32
type: FaultCode
name: Yaskawa Solectria XGI-1500-DCG CRIT-32
aliases:
- CRIT-32
- crit32
- Yaskawa Solectria CRIT-32
- Reserved
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500-dcg
family_name: Yaskawa Solectria XGI 1500-DCG
code: CRIT-32
code_key: crit32
display_message: Reserved
vendor_severity: Critical
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r6
    h: 38ba84e7e160
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r6
    h: 38ba84e7e160
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=16
    h: 3a195da0c10b
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:yaskawa-solectria-xgi-1500-dcg
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=17.r6
    h: 38ba84e7e160
  review: drafted
---
