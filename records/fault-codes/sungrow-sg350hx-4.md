---
id: fc:sungrow-sg350hx-4
type: FaultCode
name: Sungrow SG350HX 004
aliases:
- '004'
- '4'
- Sungrow 004
- Grid Undervoltage
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '004'
code_key: '4'
display_message: Grid Undervoltage
page: 87
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
  review_note: 'support check: partial - No explicit fault classification; only implied by the reconnection
    behaviour.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
  review_note: 'support check: partial - Reconnection implies disconnection, but production stop is not
    explicit.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: If repeated, check grid, settings and AC cable, then contact service.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
- claim_id: c11
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r1
    h: 1403d923cb73
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
  review_note: 'support check: partial - AC cable security is a check item, but the passages don''t say
    the fault affects the cable.'
- claim_id: c12
  rel: applies_to
  target: prod:sungrow-sg350hx
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=29.r2
    h: bf55335b853e
  review: drafted
---
