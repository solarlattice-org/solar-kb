---
id: fc:sma-stp-tl-us-6701-6702
type: FaultCode
name: SMA STP-TL-US 6701-6702
aliases:
- 6701-6702
- SMA 6701-6702
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 6701-6702
code_key: 6701-6702
code_from: 6701
code_to: 6702
page: 51
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r1
    h: 8255d77883cb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r3
    h: 113bcfa9193f
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r1
    h: 8255d77883cb
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:communication-processor
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r3
    h: 113bcfa9193f
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r1
    h: 8255d77883cb
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r3
    h: 113bcfa9193f
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r3
    h: 113bcfa9193f
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r3
    h: 113bcfa9193f
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r1
    h: 8255d77883cb
  review: drafted
---
