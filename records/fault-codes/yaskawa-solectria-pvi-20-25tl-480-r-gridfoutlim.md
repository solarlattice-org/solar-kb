---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-gridfoutlim
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R GridF.OutLim
aliases:
- GridF.OutLim
- gridfoutlim
- Yaskawa Solectria GridF.OutLim
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: GridF.OutLim
code_key: gridfoutlim
page: 80
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r5
    h: f9751340f176
  review: drafted
- claim_id: c2
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
- claim_id: c3
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
  review: drafted
  review_note: 'support check: partial - Passages say check grid frequency in range and the LCD measurement
    value, but do not explicitly say it is detected…'
- claim_id: c4
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
  review: drafted
- claim_id: c5
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
- claim_id: c6
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
