---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-fault90
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Fault0090
aliases:
- Fault0090
- fault90
- Yaskawa Solectria Fault0090
- Static leakage current high
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Fault0090
code_key: fault90
display_message: Static leakage current high
vendor_severity: Fault
page: 83
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r4
    h: c89080c5443d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r4
    h: c89080c5443d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r4
    h: c89080c5443d
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r1
    h: 3255ffd71855
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r4
    h: c89080c5443d
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r1
    h: 3255ffd71855
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r4
    h: c89080c5443d
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r1
    h: 3255ffd71855
  review: drafted
  review_note: 'support check: partial - Tracing wiring of faulted string for leakage is stated, but DC
    cable is not explicitly named.'
- claim_id: c6
  rel: detected_by
  target: method:fault-localization
  note: Reconnect strings one at a time to find the one triggering the alarm.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r4
    h: c89080c5443d
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r1
    h: 3255ffd71855
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Trace faulted string wiring for leakage to earth.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=38.r4
    h: c89080c5443d
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=39.r1
    h: 3255ffd71855
  review: drafted
---
