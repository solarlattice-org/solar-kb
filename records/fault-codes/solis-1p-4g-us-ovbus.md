---
id: fc:solis-1p-4g-us-ovbus
type: FaultCode
name: Solis 1P-4G-US OV-BUS
aliases:
- OV-BUS
- ovbus
- Solis OV-BUS
- DC BUS voltage is too high
category: Inverters
make: solis
make_name: Solis
model_family: 1p-4g-us
family_name: Solis-1P(3.6-10)K-4G-US
code: OV-BUS
code_key: ovbus
display_message: DC BUS voltage is too high
page: 62
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r1
    h: 8ef645cd1951
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
  cite:
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r1
    h: 8ef645cd1951
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r4
    h: 980abe97f48c
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r10
    h: 29b90f8a67cf
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r17
    h: 540042972c46
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r17
    h: 540042972c46
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r8
    h: 0a2486c1256c
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r8
    h: ccfd3c7218a8
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r4
    h: 980abe97f48c
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:choke
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r10
    h: 29b90f8a67cf
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r17
    h: 540042972c46
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r17
    h: 540042972c46
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r10
    h: 29b90f8a67cf
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r17
    h: 540042972c46
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r17
    h: 540042972c46
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r8
    h: 0a2486c1256c
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r8
    h: ccfd3c7218a8
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r4
    h: 980abe97f48c
  review: drafted
---
