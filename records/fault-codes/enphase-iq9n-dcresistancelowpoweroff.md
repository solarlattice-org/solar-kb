---
id: fc:enphase-iq9n-dcresistancelowpoweroff
type: FaultCode
name: Enphase IQ9N DC Resistance Low - Power Off
aliases:
- DC Resistance Low - Power Off
- dcresistancelowpoweroff
- Enphase DC Resistance Low - Power Off
category: Inverters
make: enphase
make_name: Enphase
model_family: iq9n
family_name: Enphase IQ9N Microinverters (IQ9N-A, IQ9N-HPB)
code: DC Resistance Low - Power Off
code_key: dcresistancelowpoweroff
page: 17
claims:
- claim_id: c1
  rel: defined_in
  target: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
  cite:
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: sec=8.1.2
    h: cafef1507658
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=8.1.2
    h: 658f56a93fd4
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-insulation-resistance
  note: PV input to ground resistance below threshold; IQ9N states 7 kOhm
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=4.1.2
    h: 85d421b9d5f6
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: sec=h47
    h: 2994670ac7b6
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=5.1.2
    h: d9666a3d9cee
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: sec=8.1.2
    h: cafef1507658
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h100
    h: c4f8a92bf35b
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: indicates
  target: fm:insulation-loss
  note: One possible cause; moisture ingress or wiring and connector defects also named
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=4.1.2
    h: 85d421b9d5f6
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: sec=h47
    h: 2994670ac7b6
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=5.1.2
    h: d9666a3d9cee
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: sec=8.1.2
    h: cafef1507658
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h100
    h: c4f8a92bf35b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=4.1.2
    h: 85d421b9d5f6
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: sec=h47
    h: 2994670ac7b6
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=5.1.2
    h: d9666a3d9cee
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: sec=8.1.2
    h: cafef1507658
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h100
    h: c4f8a92bf35b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Passages tie the condition to PV inputs and module insulation,
    but they never state that it affects the PV array…'
- claim_id: c6
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=4.1.2
    h: 85d421b9d5f6
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: sec=h47
    h: 2994670ac7b6
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=5.1.2
    h: d9666a3d9cee
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: sec=8.1.2
    h: cafef1507658
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h100
    h: c4f8a92bf35b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Defective wiring is named as a possible cause, but DC cable is
    not explicitly identified as an affected component.'
- claim_id: c7
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=4.1.2
    h: 85d421b9d5f6
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: sec=h47
    h: 2994670ac7b6
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=5.1.2
    h: d9666a3d9cee
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: sec=8.1.2
    h: cafef1507658
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h100
    h: c4f8a92bf35b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Defective connectors are named as a possible cause, but the DC
    connector is not explicitly identified as an affected component.'
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=4.1.2
    h: 85d421b9d5f6
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: sec=h47
    h: 2994670ac7b6
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=5.1.2
    h: d9666a3d9cee
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: sec=8.1.2
    h: cafef1507658
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h100
    h: c4f8a92bf35b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=4.1.2
    h: 85d421b9d5f6
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: sec=h47
    h: 2994670ac7b6
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=5.1.2
    h: d9666a3d9cee
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: sec=8.1.2
    h: cafef1507658
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h100
    h: c4f8a92bf35b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c10
  rel: has_recovery
  target: ec:manual-reset
  note: Operator sends clear command via gateway; if condition persists, contact installer or Enphase
    support
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=4.1.2
    h: 85d421b9d5f6
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: sec=h47
    h: 2994670ac7b6
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=5.1.2
    h: d9666a3d9cee
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: sec=8.1.2
    h: cafef1507658
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h100
    h: c4f8a92bf35b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
