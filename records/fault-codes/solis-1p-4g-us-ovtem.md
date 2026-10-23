---
id: fc:solis-1p-4g-us-ovtem
type: FaultCode
name: Solis 1P-4G-US OV-TEM
aliases:
- OV-TEM
- ovtem
- Solis OV-TEM
- Temperature Protec on
category: Inverters
make: solis
make_name: Solis
model_family: 1p-4g-us
family_name: Solis-1P(3.6-10)K-4G-US
code: OV-TEM
code_key: ovtem
display_message: Temperature Protec on
page: 62
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r5
    h: 4278d3dde221
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
  cite:
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r5
    h: 4278d3dde221
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r18
    h: 828829faa49d
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r9
    h: 2a0503369d68
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r9
    h: 2a0503369d68
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r3
    h: 1ad3cee87a05
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r3
    h: 028624c8cfa5
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r2
    h: 028624c8cfa5
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:high-ambient-temperature
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:ambient-temperature-check
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r18
    h: 828829faa49d
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r9
    h: 2a0503369d68
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r9
    h: 2a0503369d68
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r18
    h: 828829faa49d
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r9
    h: 2a0503369d68
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r9
    h: 2a0503369d68
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r3
    h: 1ad3cee87a05
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r3
    h: 028624c8cfa5
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r2
    h: 028624c8cfa5
  review: drafted
  review_note: 'support check: partial - Passages say to check poor heat dissipation in the surroundings,
    but don''t explicitly state providing adequate cooling as a mitigation.'
- claim_id: c9
  rel: mitigated_by
  target: mit:proper-installation
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r3
    h: 1ad3cee87a05
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r3
    h: 028624c8cfa5
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r2
    h: 028624c8cfa5
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if ambient temperature is within range.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  review: drafted
- claim_id: c11
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15
    h: cb7b6f9ed265
  review: drafted
---
