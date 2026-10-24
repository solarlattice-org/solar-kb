---
id: fc:solis-s5-gc-us-ungv
type: FaultCode
name: Solis S5-GC UN-G-V
aliases:
- UN-G-V
- ungv
- Solis UN-G-V
- Under Grid Voltage
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: UN-G-V
code_key: ungv
display_message: Under Grid Voltage
page: 69
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r4
    h: cab3a7061bcd
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r4
    h: 7d67b538652f
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=13.r1
    h: 3b959bd32936
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r1
    h: 3b959bd32936
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r4
    h: cab3a7061bcd
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r4
    h: 7d67b538652f
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=13.r1
    h: 3b959bd32936
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r1
    h: 3b959bd32936
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:voltage-sensor-fault
  note: Only when measured AC disagrees with the displayed reading.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r4
    h: cab3a7061bcd
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r4
    h: 7d67b538652f
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=13.r1
    h: 3b959bd32936
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r1
    h: 3b959bd32936
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Lower limit change only with utility approval.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r4
    h: cab3a7061bcd
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r4
    h: 7d67b538652f
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=13.r1
    h: 3b959bd32936
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r1
    h: 3b959bd32936
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r4
    h: cab3a7061bcd
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r4
    h: 7d67b538652f
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=13.r1
    h: 3b959bd32936
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r1
    h: 3b959bd32936
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r4
    h: cab3a7061bcd
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r4
    h: cab3a7061bcd
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r4
    h: 7d67b538652f
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=13.r1
    h: 3b959bd32936
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r1
    h: 3b959bd32936
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: applies_to
  target: prod:solis-s5-gc-us
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  review: drafted
---
