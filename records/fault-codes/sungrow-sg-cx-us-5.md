---
id: fc:sungrow-sg-cx-us-5
type: FaultCode
name: Sungrow SG-CX-US 005
aliases:
- '005'
- '5'
- Sungrow 005
- Grid low voltage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '005'
code_key: '5'
display_message: Grid low voltage
page: 90
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r2
    h: c50b0671bfd5
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r2
    h: c50b0671bfd5
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
  review_note: 'support check: partial - No explicit fault classification; only implied.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
  review_note: 'support check: partial - Reconnection implies disconnection, but production stop is not
    explicit.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: If repeated, check grid, settings and AC cable, then contact service.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c8
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c12
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
  review_note: 'support check: partial - AC cable is only a check item, not stated as affected.'
- claim_id: c13
  rel: applies_to
  target: prod:sungrow-sg-cx-us
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r2
    h: c50b0671bfd5
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r2
    h: c50b0671bfd5
  review: drafted
---
