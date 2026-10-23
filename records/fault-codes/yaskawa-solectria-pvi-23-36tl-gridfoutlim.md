---
id: fc:yaskawa-solectria-pvi-23-36tl-gridfoutlim
type: FaultCode
name: Yaskawa Solectria PVI-TL GridF.OutLim
aliases:
- GridF.OutLim
- gridfoutlim
- Yaskawa Solectria GridF.OutLim
- Grid voltage frequency is abnormal
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: GridF.OutLim
code_key: gridfoutlim
display_message: Grid voltage frequency is abnormal
vendor_severity: Protection
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19
    h: 2eb036f0fe1b
  review: drafted
  review_note: code printed in the table header line
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19
    h: 2eb036f0fe1b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-frequency-out-of-range
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19
    h: 2eb036f0fe1b
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r1
    h: 1fe4f91d526d
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19
    h: 2eb036f0fe1b
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r1
    h: 1fe4f91d526d
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r5
    h: f9751340f176
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19
    h: 2eb036f0fe1b
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r2
    h: 34e2ecbf2d22
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r5
    h: f9751340f176
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Final escalation if the alarm persists.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19
    h: 2eb036f0fe1b
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r3
    h: 01a96f3c3374
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Watch for automatic clearing first; then check frequency and wiring, restart; then service.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19
    h: 2eb036f0fe1b
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=13.r1
    h: 1fe4f91d526d
  review: drafted
---
