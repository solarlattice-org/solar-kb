---
id: fc:solis-s6-eh2p-l-us-igfolf
type: FaultCode
name: Solis S6-EH2P IGFOL-F
aliases:
- IGFOL-F
- igfolf
- Solis IGFOL-F
- Grid current tracking failure
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh2p-l-us
family_name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
code: IGFOL-F
code_key: igfolf
display_message: Grid current tracking failure
page: 97
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r11
    h: b1d7bf4d96b3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-current-tracking-failure
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r8
    h: '23e710312339'
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r8
    h: '23e710312339'
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r16
    h: 94e94c8bc64c
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r9
    h: 7a4cbb7ed3ad
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r9
    h: 7a4cbb7ed3ad
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r11
    h: b1d7bf4d96b3
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r11
    h: faefc527751c
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r11
    h: faefc527751c
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r11
    h: b1d7bf4d96b3
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r11
    h: faefc527751c
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r11
    h: faefc527751c
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r8
    h: '23e710312339'
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r8
    h: '23e710312339'
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r16
    h: 94e94c8bc64c
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r9
    h: 7a4cbb7ed3ad
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r9
    h: 7a4cbb7ed3ad
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r8
    h: '23e710312339'
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r8
    h: '23e710312339'
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; installer contact or inverter replacement if it persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r8
    h: '23e710312339'
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r8
    h: '23e710312339'
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r16
    h: 94e94c8bc64c
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r9
    h: 7a4cbb7ed3ad
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r9
    h: 7a4cbb7ed3ad
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:solis-s6-eh2p-l-us
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r11
    h: b1d7bf4d96b3
  review: drafted
---
