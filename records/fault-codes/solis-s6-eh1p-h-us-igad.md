---
id: fc:solis-s6-eh1p-h-us-igad
type: FaultCode
name: Solis S6-EH1P IG-AD
aliases:
- IG-AD
- igad
- Solis IG-AD
- Grid current sampling fail
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh1p-h-us
family_name: Solis S6-EH1P(3.8-11.4)K-H-US
code: IG-AD
code_key: igad
display_message: Grid current sampling fail
page: 72
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r10
    h: 9e79eac03e64
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:measurement-signal-error
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r1
    h: 6ec1f2ecd40d
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r1
    h: 6ec1f2ecd40d
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r17
    h: 966b32ee97bb
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r1
    h: 6ec1f2ecd40d
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r1
    h: 6ec1f2ecd40d
  review: drafted
  review_note: 'support check: partial - The passages describe grid current sampling failure but do not
    name a current sensor.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r1
    h: 6ec1f2ecd40d
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r17
    h: 966b32ee97bb
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r10
    h: 9e79eac03e64
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r17
    h: 966b32ee97bb
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r10
    h: 9e79eac03e64
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r10
    h: 9e79eac03e64
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r1
    h: 6ec1f2ecd40d
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r1
    h: 6ec1f2ecd40d
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r1
    h: 6ec1f2ecd40d
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: sec=10.3.1
    h: 16fa984bf0d2
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; installer or inverter replacement if it persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r1
    h: 6ec1f2ecd40d
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r17
    h: 966b32ee97bb
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:solis-s6-eh1p-h-us
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r10
    h: 9e79eac03e64
  review: drafted
---
