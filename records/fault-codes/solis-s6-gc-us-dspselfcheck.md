---
id: fc:solis-s6-gc-us-dspselfcheck
type: FaultCode
name: Solis S6-GC DSP-SelfCheck
aliases:
- DSP-SelfCheck
- dspselfcheck
- Solis DSP-SelfCheck
- DSP self-check is abnormal
category: Inverters
make: solis
make_name: Solis
model_family: s6-gc-us
family_name: Solis S6-GC(25-60)K-US
code: DSP-SelfCheck
code_key: dspselfcheck
display_message: DSP self-check is abnormal
page: 75
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r2
    h: 1894d0c3a2b6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r2
    h: 1894d0c3a2b6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r2
    h: 1894d0c3a2b6
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:digital-signal-processor
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r2
    h: 1894d0c3a2b6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r2
    h: 1894d0c3a2b6
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r2
    h: 1894d0c3a2b6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r2
    h: 1894d0c3a2b6
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r2
    h: 1894d0c3a2b6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r2
    h: 1894d0c3a2b6
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r2
    h: 1894d0c3a2b6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: sec=10.3.1
    h: 16fa984bf0d2
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; replace inverter if it persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r2
    h: 1894d0c3a2b6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r2
    h: 1894d0c3a2b6
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:solis-s6-gc-us
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r2
    h: 1894d0c3a2b6
  review: drafted
---
