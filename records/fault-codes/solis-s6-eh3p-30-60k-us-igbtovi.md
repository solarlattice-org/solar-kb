---
id: fc:solis-s6-eh3p-30-60k-us-igbtovi
type: FaultCode
name: Solis S6-EH3P30-60K IGBT-OV-I
aliases:
- IGBT-OV-I
- igbtovi
- Solis IGBT-OV-I
- IGBT overcurrent
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-30-60k-us
family_name: Solis S6-EH3P(30-60)K-NV-YD-H-US
code: IGBT-OV-I
code_key: igbtovi
display_message: IGBT overcurrent
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r2
    h: 016e2b1f49a9
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=28.r2
    h: 016e2b1f49a9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:overcurrent
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r7
    h: 814ee6595879
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r7
    h: 814ee6595879
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r14
    h: 674a8840593d
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r7
    h: 814ee6595879
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r7
    h: 814ee6595879
  review: drafted
  review_note: 'support check: partial - The passages name the IGBT but never mention the inverter bridge.'
- claim_id: c5
  rel: affects
  target: comp:power-board
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r14
    h: 674a8840593d
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r8
    h: 68109c9bccc4
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r8
    h: 68109c9bccc4
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r7
    h: 814ee6595879
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r14
    h: 674a8840593d
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r2
    h: 52a8701fe4ed
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:power-board-replacement
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r14
    h: 674a8840593d
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r8
    h: 68109c9bccc4
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r8
    h: 68109c9bccc4
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r7
    h: 814ee6595879
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r7
    h: 814ee6595879
  review: drafted
- claim_id: c9
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r7
    h: 814ee6595879
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: sec=10.3.1
    h: 16fa984bf0d2
  review: drafted
- claim_id: c10
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; power board or inverter replacement if it persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r7
    h: 814ee6595879
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r14
    h: 674a8840593d
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r2
    h: 52a8701fe4ed
  review: drafted
---
