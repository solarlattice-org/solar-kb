---
id: fc:huawei-sun2000-45ktl-us-hv-d0-202
type: FaultCode
name: Huawei SUN2000-45KTL-US-HV-D0 202
aliases:
- '202'
- Huawei 202
- Abnormal Invert Circuit
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-45ktl-us-hv-d0
family_name: Huawei SUN2000-45KTL-US-HV-D0
code: '202'
code_key: '202'
display_message: Abnormal Invert Circuit
vendor_severity: Major
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r2
    h: f3ba906275f0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r2
    h: f3ba906275f0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r1
    h: 1b664a229ba3
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r2
    h: f3ba906275f0
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=55.r1
    h: 762dcaeccc34
  review: drafted
  review_note: 'support check: partial - Instantaneous high output current and output short-circuit surge
    are stated, though the alarm is named an invert module fault.'
- claim_id: c4
  rel: reports
  target: symptom:dc-injection-high
  note: Cause 16
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r1
    h: 1b664a229ba3
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r2
    h: f3ba906275f0
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r1
    h: 1b664a229ba3
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r2
    h: f3ba906275f0
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:ac-cable
  note: Output short circuit, cause 20
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r1
    h: 1b664a229ba3
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r2
    h: f3ba906275f0
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r1
    h: 1b664a229ba3
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r2
    h: f3ba906275f0
  review: drafted
  review_note: 'support check: partial - Only checking output cables for short circuits is stated, not
    a broader AC connection check.'
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the alarm persists
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r1
    h: 1b664a229ba3
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r2
    h: f3ba906275f0
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r1
    h: 1b664a229ba3
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=8.2
    h: db4d98f32335
  review: drafted
- claim_id: c10
  rel: has_recovery
  target: ec:auto-reset
  note: For grid-caused causes 13/14/16; escalate to service if it persists
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=39.r1
    h: 1b664a229ba3
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r2
    h: f3ba906275f0
  review: drafted
- claim_id: c11
  rel: applies_to
  target: prod:huawei-sun2000-45ktl-us-hv-d0
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=54.r2
    h: f3ba906275f0
  review: drafted
---
