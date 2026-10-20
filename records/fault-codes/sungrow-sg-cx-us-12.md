---
id: fc:sungrow-sg-cx-us-12
type: FaultCode
name: Sungrow SG-CX-US 12
aliases:
- '12'
- Sungrow 12
- Excessive leakage current
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '12'
code_key: '12'
display_message: Excessive leakage current
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r4
    h: 8b79a5df44df
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r4
    h: 8b79a5df44df
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=9.1
    h: 7e543aeb5157
  review: drafted
  review_note: 'support check: partial - The passages show it is a listed fault code in the troubleshooting
    table, but they give no explicit fault classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r4
    h: 8b79a5df44df
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  review: drafted
  review_note: 'support check: partial - Reconnection after the environment improves implies disconnection,
    but the passages don''t explicitly state a trip.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Reconnects when damp or low-light conditions improve; otherwise check cable insulation, then service.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r4
    h: 8b79a5df44df
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r4
    h: 8b79a5df44df
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  review: drafted
  review_note: 'support check: partial - The passages say to check that the AC and DC cables are well
    insulated, but they don''t mention insulation resistance testing.'
- claim_id: c7
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r4
    h: 8b79a5df44df
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  review: drafted
  review_note: 'support check: partial - The passages say to check that the AC cables are well insulated,
    but not that the fault affects the AC cable.'
- claim_id: c8
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r4
    h: 8b79a5df44df
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r5
    h: 843ebdc64972
  review: drafted
  review_note: 'support check: partial - The passages say to check that the DC cables are well insulated,
    but not that the fault affects the DC cable.'
---
