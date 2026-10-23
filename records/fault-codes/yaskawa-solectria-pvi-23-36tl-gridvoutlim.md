---
id: fc:yaskawa-solectria-pvi-23-36tl-gridvoutlim
type: FaultCode
name: Yaskawa Solectria PVI-TL GridV.OutLim
aliases:
- GridV.OutLim
- gridvoutlim
- Yaskawa Solectria GridV.OutLim
- Grid voltage exceeds the specified range
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: GridV.OutLim
code_key: gridvoutlim
display_message: Grid voltage exceeds the specified range
vendor_severity: Protection
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r7
    h: 63e0302d5223
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r8
    h: 4750b1db994d
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r9
    h: 3984d80b71b9
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r10
    h: 863af6e45e45
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r7
    h: 63e0302d5223
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r8
    h: 4750b1db994d
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r9
    h: 3984d80b71b9
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r10
    h: 863af6e45e45
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-voltage-out-of-range
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r7
    h: 63e0302d5223
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r7
    h: 5446ad2f8947
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r7
    h: 63e0302d5223
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r8
    h: ffc9550a6b8b
  review: drafted
  review_note: 'support check: partial - Passages say verify grid voltage within range but do not state
    the fault is detected by grid voltage measurement.'
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r9
    h: 3984d80b71b9
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r10
    h: 863af6e45e45
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r9
    h: 1c59ae17c9bc
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r10
    h: 27d31db0ef7c
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r7
    h: 63e0302d5223
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r9
    h: 1c59ae17c9bc
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r4
    h: 091fc2edb4f3
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Final escalation if the alarm persists.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r7
    h: 63e0302d5223
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r10
    h: 27d31db0ef7c
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Watch for automatic clearing first; then check grid and wiring, restart; then service.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r7
    h: 63e0302d5223
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r7
    h: 5446ad2f8947
  review: drafted
---
