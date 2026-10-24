---
id: fc:solis-s6-eh3p-30-60k-us-dcinjfault
type: FaultCode
name: Solis S6-EH3P30-60K DCInj-Fault
aliases:
- DCInj-Fault
- dcinjfault
- Solis DCInj-Fault
- The current DC component exceeds the limit
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-30-60k-us
family_name: Solis S6-EH3P(30-60)K-NV-YD-H-US
code: DCInj-Fault
code_key: dcinjfault
display_message: The current DC component exceeds the limit
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r1
    h: 343ddc0a98d9
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=28.r1
    h: 343ddc0a98d9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-injection-high
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r4
    h: 13f3370757f3
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r7
    h: b8dccd8805ed
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r3
    h: 15d7a6b32058
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r1
    h: 69c05042a23a
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r1
    h: 343ddc0a98d9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r17
    h: 343ddc0a98d9
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r1
    h: 69c05042a23a
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r1
    h: 343ddc0a98d9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r17
    h: 343ddc0a98d9
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Passages advise checking AC cable connection, but don''t state
    the fault affects the AC cable.'
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r1
    h: 69c05042a23a
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r1
    h: 343ddc0a98d9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r17
    h: 343ddc0a98d9
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r4
    h: 13f3370757f3
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r7
    h: b8dccd8805ed
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r3
    h: 15d7a6b32058
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r1
    h: 69c05042a23a
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r1
    h: 343ddc0a98d9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r17
    h: 343ddc0a98d9
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r4
    h: 13f3370757f3
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r4
    h: 13f3370757f3
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r7
    h: b8dccd8805ed
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r3
    h: 15d7a6b32058
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r1
    h: 69c05042a23a
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r1
    h: 343ddc0a98d9
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r17
    h: 343ddc0a98d9
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; installer contact or inverter replacement if it persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r4
    h: 13f3370757f3
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r7
    h: b8dccd8805ed
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r3
    h: 15d7a6b32058
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:solis-s6-eh3p-30-60k-us
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r1
    h: 343ddc0a98d9
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=28.r1
    h: 343ddc0a98d9
  review: drafted
---
