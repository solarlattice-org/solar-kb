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
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19
    h: 2eb036f0fe1b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
  review_note: 'support check: partial - The passages say to verify grid frequency but do not state a
    measurement method as the detection means.'
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  note: When AC connections are loose
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19
    h: 2eb036f0fe1b
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Normally clears on its own; then checks, then service
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19
    h: 2eb036f0fe1b
  review: drafted
  review_note: 'support check: partial - Observe 10 min for auto-clear, then checks, then service; ''normally''
    is implied.'
---
