---
id: fc:solis-s6-eh3p-30-60k-us-relaychkfail
type: FaultCode
name: Solis S6-EH3P30-60K RelayChk-Fail
aliases:
- RelayChk-Fail
- relaychkfail
- Solis RelayChk-Fail
- Relay failure
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-30-60k-us
family_name: Solis S6-EH3P(30-60)K-NV-YD-H-US
code: RelayChk-Fail
code_key: relaychkfail
display_message: Relay failure
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r4
    h: b1f2fd599fef
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=28.r4
    h: b1f2fd599fef
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r2
    h: 1940643dcd1b
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r14
    h: b0706deaf2d2
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r14
    h: b0706deaf2d2
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r4
    h: d551b846d262
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r4
    h: b1f2fd599fef
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r3
    h: b1f2fd599fef
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r2
    h: 1940643dcd1b
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r14
    h: b0706deaf2d2
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r14
    h: b0706deaf2d2
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r4
    h: d551b846d262
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r4
    h: b1f2fd599fef
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r3
    h: b1f2fd599fef
  review: drafted
  review_note: 'support check: partial - Relay failure is stated but the specific grid-tie relay is not
    named.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r2
    h: 1940643dcd1b
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r14
    h: b0706deaf2d2
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r14
    h: b0706deaf2d2
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r4
    h: d551b846d262
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r4
    h: b1f2fd599fef
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r3
    h: b1f2fd599fef
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r2
    h: 1940643dcd1b
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r2
    h: 1940643dcd1b
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r4
    h: d551b846d262
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r4
    h: b1f2fd599fef
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r3
    h: b1f2fd599fef
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; installer contact or inverter replacement if it persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r2
    h: 1940643dcd1b
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r14
    h: b0706deaf2d2
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r14
    h: b0706deaf2d2
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r4
    h: d551b846d262
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r4
    h: b1f2fd599fef
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r3
    h: b1f2fd599fef
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:solis-s6-eh3p-30-60k-us
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r4
    h: b1f2fd599fef
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=28.r4
    h: b1f2fd599fef
  review: drafted
---
