---
id: fc:solis-s6-eh2p-l-us-ovtem
type: FaultCode
name: Solis S6-EH2P OV-TEM
aliases:
- OV-TEM
- ovtem
- Solis OV-TEM
- Module over temperature
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh2p-l-us
family_name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
code: OV-TEM
code_key: ovtem
display_message: Module over temperature
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r3
    h: 1ad3cee87a05
  review: drafted
- claim_id: c2
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
- claim_id: c3
  rel: reports
  target: symptom:high-ambient-temperature
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:ambient-temperature-check
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  review: drafted
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
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
- claim_id: c8
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
- claim_id: c9
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if ambient temperature is within range.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  review: drafted
- claim_id: c10
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
