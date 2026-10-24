---
id: fc:sungrow-sg-cx-us-88
type: FaultCode
name: Sungrow SG-CX-US 088
aliases:
- '088'
- '88'
- Sungrow 088
- Electric arc fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '088'
code_key: '88'
display_message: Electric arc fault
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r3
    h: da4d057331c3
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r3
    h: da4d057331c3
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r3
    h: da4d057331c3
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r3
    h: da4d057331c3
  review: drafted
  review_note: 'support check: partial - Wiring terminals and fuses are checked, but a PV input terminal
    is not named specifically.'
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r3
    h: da4d057331c3
  review: drafted
  review_note: 'support check: partial - Checking cables, terminals and burnt parts is visual-like, but
    inspection is not explicitly stated.'
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r3
    h: da4d057331c3
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r3
    h: da4d057331c3
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  note: Inverter must be brought back to normal after the arc fault is cleared.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r3
    h: da4d057331c3
  review: drafted
  review_note: 'support check: partial - The inverter must be recovered after clearing, which implies
    stoppage, but a stop is not explicitly stated.'
- claim_id: c10
  rel: has_recovery
  target: ec:manual-reset
  note: Operator clears the arc fault via App or LCD after repair; service if it persists.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r3
    h: da4d057331c3
  review: drafted
- claim_id: c11
  rel: applies_to
  target: prod:sungrow-sg-cx-us
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r3
    h: da4d057331c3
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r3
    h: da4d057331c3
  review: drafted
---
