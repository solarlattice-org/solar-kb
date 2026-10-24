---
id: fc:solis-s6-gu-ehv-us-ileakcheck
type: FaultCode
name: Solis S6-GU ILeak-Check
aliases:
- ILeak-Check
- ileakcheck
- Solis ILeak-Check
- Leakage current self check protect ion
category: Inverters
make: solis
make_name: Solis
model_family: s6-gu-ehv-us
family_name: Solis S6-GU(250-350)K-EHV-US
code: ILeak-Check
code_key: ileakcheck
display_message: Leakage current self check protect ion
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r5
    h: f9955ed5e9c6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r5
    h: f9955ed5e9c6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r5
    h: f9955ed5e9c6
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:current-sensor-fault
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r5
    h: f9955ed5e9c6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r5
    h: f9955ed5e9c6
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r13
    h: e68b88f4d054
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r13
    h: 0ba0864d0182
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r12
    h: 0ba0864d0182
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r5
    h: f9955ed5e9c6
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r13
    h: e68b88f4d054
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:ground-conductor-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r13
    h: e68b88f4d054
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r13
    h: 0ba0864d0182
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r12
    h: 0ba0864d0182
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r5
    h: f9955ed5e9c6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r5
    h: f9955ed5e9c6
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r5
    h: f9955ed5e9c6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r5
    h: f9955ed5e9c6
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r5
    h: f9955ed5e9c6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: sec=10.3.1
    h: 16fa984bf0d2
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; replace inverter if the fault persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r5
    h: f9955ed5e9c6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r5
    h: f9955ed5e9c6
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:solis-s6-gu-ehv-us
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r5
    h: f9955ed5e9c6
  review: drafted
---
