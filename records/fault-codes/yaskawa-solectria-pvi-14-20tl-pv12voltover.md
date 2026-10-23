---
id: fc:yaskawa-solectria-pvi-14-20tl-pv12voltover
type: FaultCode
name: Yaskawa Solectria PVI-14-20TL PV1 (2) VoltOver
aliases:
- PV1 (2) VoltOver
- pv12voltover
- Yaskawa Solectria PV1 (2) VoltOver
- DC input voltage exceeds the specified value
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-14-20tl
family_name: Solectria PVI 14/20TL
code: PV1 (2) VoltOver
code_key: pv12voltover
display_message: DC input voltage exceeds the specified value
vendor_severity: Protection
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r4
    h: 690b78cb6b4c
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r5
    h: 762159c58c71
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r6
    h: 7d553801c797
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r7
    h: eece10593da6
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r8
    h: 994417da0769
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r4
    h: 690b78cb6b4c
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r5
    h: 762159c58c71
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r6
    h: 7d553801c797
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r7
    h: eece10593da6
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r8
    h: 994417da0769
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r1
    h: 77d009cbbe67
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r4
    h: 690b78cb6b4c
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:voc-measurement
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r1
    h: 77d009cbbe67
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r5
    h: 762159c58c71
  review: drafted
  review_note: 'support check: partial - Passages say verify DC open circuit voltage is within range,
    but not that detection is by Voc measurement.'
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Final escalation if the alarm persists after restart.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r1
    h: 77d009cbbe67
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r8
    h: 994417da0769
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Watch for automatic clearing first; then verify Voc, power cycle; then service.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r1
    h: 77d009cbbe67
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r4
    h: 690b78cb6b4c
  review: drafted
---
