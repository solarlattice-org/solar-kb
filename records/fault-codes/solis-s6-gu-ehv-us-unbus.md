---
id: fc:solis-s6-gu-ehv-us-unbus
type: FaultCode
name: Solis S6-GU UN-BUS
aliases:
- UN-BUS
- unbus
- Solis UN-BUS
- DC BUS voltage is too low
category: Inverters
make: solis
make_name: Solis
model_family: s6-gu-ehv-us
family_name: Solis S6-GU(250-350)K-EHV-US
code: UN-BUS
code_key: unbus
display_message: DC BUS voltage is too low
page: 45
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r5
    h: 81c6417ed68c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r1
    h: 2e74ad175265
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-bus-undervoltage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r5
    h: 7868f947bd08
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r5
    h: 7868f947bd08
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r5
    h: 7868f947bd08
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r1
    h: 2e74ad175265
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r5
    h: 81c6417ed68c
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r2
    h: 87b661b382e3
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r2
    h: 87b661b382e3
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r5
    h: 7868f947bd08
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r5
    h: 7868f947bd08
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r5
    h: 7868f947bd08
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r1
    h: 2e74ad175265
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r5
    h: 81c6417ed68c
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r2
    h: 87b661b382e3
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r2
    h: 87b661b382e3
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  note: Internal damage or wire loosened in shipping.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r5
    h: 7868f947bd08
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r5
    h: 7868f947bd08
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r5
    h: 7868f947bd08
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r5
    h: 81c6417ed68c
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r2
    h: 87b661b382e3
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r2
    h: 87b661b382e3
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r1
    h: 2e74ad175265
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r5
    h: 7868f947bd08
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=12.r5
    h: 7868f947bd08
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=11.r5
    h: 7868f947bd08
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r1
    h: 2e74ad175265
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r5
    h: 81c6417ed68c
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r2
    h: 87b661b382e3
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r2
    h: 87b661b382e3
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r5
    h: 81c6417ed68c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10
    h: d1948e6b3649
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r1
    h: 2e74ad175265
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14
    h: ea15e4c7ba67
  review: drafted
  review_note: 'support check: partial - Row says ''DC bus voltage too low for inverter to operate'' and
    suggests restart or replace, implying a stop, but…'
- claim_id: c8
  rel: applies_to
  target: prod:solis-s6-gu-ehv-us
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=10.r5
    h: 81c6417ed68c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r1
    h: 2e74ad175265
  review: drafted
---
