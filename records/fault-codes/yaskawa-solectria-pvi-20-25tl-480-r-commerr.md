---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-commerr
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R CommErr
aliases:
- CommErr
- commerr
- Yaskawa Solectria CommErr
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: CommErr
code_key: commerr
page: 78
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=32.r1
    h: 65d166fa39a6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: Listed in the alarm section
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=32.r1
    h: 65d166fa39a6
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h151
    h: 30c6969b9187
  review: drafted
  review_note: 'support check: partial - The passage shows only an "ALARM" heading (u11), which does not
    clearly tie CommErr to it, and the row itself…'
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=32.r1
    h: 65d166fa39a6
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:communication-cable-check
  note: Cause is poor contact at the internal communication wire terminals
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=32.r1
    h: 65d166fa39a6
  review: drafted
  review_note: 'support check: partial - The cause is poor contact at the internal communication wire
    terminals, but no communication cable check is recommended.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Observe for 5 minutes first; then power off the system; then after-sales service
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=32.r1
    h: 65d166fa39a6
  review: drafted
  review_note: 'support check: partial - Observing for 5 minutes then switching off then service is listed,
    but the passage does not state that the alarm…'
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Final escalation step
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=32.r1
    h: 65d166fa39a6
  review: drafted
---
