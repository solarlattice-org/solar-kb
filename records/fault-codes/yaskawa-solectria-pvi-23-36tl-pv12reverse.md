---
id: fc:yaskawa-solectria-pvi-23-36tl-pv12reverse
type: FaultCode
name: Yaskawa Solectria PVI-TL PV1 (2) Reverse
aliases:
- PV1 (2) Reverse
- pv12reverse
- Yaskawa Solectria PV1 (2) Reverse
- DC inputs connected with incorrect polarities
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: PV1 (2) Reverse
code_key: pv12reverse
display_message: DC inputs connected with incorrect polarities
vendor_severity: Protection
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r2
    h: 0199c95676db
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r2
    h: 0199c95676db
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r2
    h: 0199c95676db
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r9
    h: 0cd413e87041
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r2
    h: 0199c95676db
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r9
    h: 0cd413e87041
  review: drafted
  review_note: 'support check: partial - Passages say verify DC polarity but do not state detection by
    polarity measurement.'
- claim_id: c5
  rel: mitigated_by
  target: mit:polarity-correction
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r2
    h: 0199c95676db
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r9
    h: 0cd413e87041
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the error persists with correct polarity.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r2
    h: 0199c95676db
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r10
    h: aeb5300bd1ed
  review: drafted
---
