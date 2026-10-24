---
id: fc:huawei-sun2000-25-30ktl-us-326
type: FaultCode
name: Huawei SUN2000-25-30KTL-US 326
aliases:
- '326'
- Huawei 326
- Electrical Grounding Fault
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-25-30ktl-us
family_name: Huawei SUN2000-25KTL-US / SUN2000-30KTL-US
code: '326'
code_key: '326'
display_message: Electrical Grounding Fault
vendor_severity: Major
page: 101
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r4
    h: a1ab36a45361
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r4
    h: a1ab36a45361
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:missing-ground-connection
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r4
    h: a1ab36a45361
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r6
    h: 864bd858dc99
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:neutral-line-abnormal
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r4
    h: a1ab36a45361
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r6
    h: 864bd858dc99
  review: drafted
  review_note: 'support check: partial - A neutral wire not connected is a listed cause, but ''abnormal
    neutral line'' is only loosely stated and the alarm…'
- claim_id: c5
  rel: mitigated_by
  target: mit:ground-conductor-check
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r4
    h: a1ab36a45361
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r6
    h: 864bd858dc99
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Neutral wire connection check; isolation transformer required if PV strings are grounded
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r4
    h: a1ab36a45361
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=57.r6
    h: 864bd858dc99
  review: drafted
  review_note: 'support check: partial - Neutral wire check and isolation transformer for grounded PV
    strings are stated, but the measure concerns the output-side transformer and…'
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r4
    h: a1ab36a45361
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=8.2
    h: db4d98f32335
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:huawei-sun2000-25-30ktl-us
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r4
    h: a1ab36a45361
  review: drafted
---
