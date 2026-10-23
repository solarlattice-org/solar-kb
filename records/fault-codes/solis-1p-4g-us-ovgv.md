---
id: fc:solis-1p-4g-us-ovgv
type: FaultCode
name: Solis 1P-4G-US OV-G-V
aliases:
- OV-G-V
- ovgv
- Solis OV-G-V
- Over Grid Voltage
category: Inverters
make: solis
make_name: Solis
model_family: 1p-4g-us
family_name: Solis-1P(3.6-10)K-4G-US
code: OV-G-V
code_key: ovgv
display_message: Over Grid Voltage
page: 60
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=12.r3
    h: 0fbabf964113
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
  cite:
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=11.r3
    h: 0fbabf964113
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r3
    h: 52c3fd63f040
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r3
    h: 52c3fd63f040
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r3
    h: 52c3fd63f040
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r3
    h: a2b4f75b9aab
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r3
    h: 52c3fd63f040
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r3
    h: 52c3fd63f040
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r3
    h: 52c3fd63f040
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r3
    h: a2b4f75b9aab
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Upper voltage limit change only with utility approval.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r3
    h: 52c3fd63f040
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r3
    h: 52c3fd63f040
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r3
    h: 52c3fd63f040
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r3
    h: a2b4f75b9aab
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r3
    h: 52c3fd63f040
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r3
    h: 52c3fd63f040
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r3
    h: 52c3fd63f040
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r3
    h: a2b4f75b9aab
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:ac-cable
  note: When voltage is high only at full power, AC cables may be undersized.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r3
    h: 52c3fd63f040
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r3
    h: 52c3fd63f040
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r3
    h: 52c3fd63f040
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r3
    h: a2b4f75b9aab
  review: drafted
  review_note: 'support check: partial - Passages say if AC is high at full power, cables between inverter
    and interconnect are too small; ''only at full…'
---
