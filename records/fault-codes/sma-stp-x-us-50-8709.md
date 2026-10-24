---
id: fc:sma-stp-x-us-50-8709
type: FaultCode
name: SMA STP-X-US 8709
aliases:
- '8709'
- SMA 8709
- Timeout in communication for reactive power spec.
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '8709'
code_key: '8709'
display_message: Timeout in communication for reactive power spec.
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.47
    h: 88362aa00bc0
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h597
    h: b1c5cbca1260
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  note: Loss of communication to the system control
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=20.r3
    h: 3213da9359ea
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h724
    h: 4026503bfd7c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h598
    h: 4026503bfd7c
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h431
    h: f532e08430b1
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  note: Only when fallback is set to limit active power to a configured percentage; otherwise last values
    retained
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h724
    h: 4026503bfd7c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h598
    h: 4026503bfd7c
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:network-cable
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h725
    h: 800a134e3dfa
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h599
    h: 800a134e3dfa
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h432
    h: 800a134e3dfa
  review: drafted
  review_note: 'support check: partial - Cables and plugs are checked in corrective measures, but a network
    cable is not explicitly named as affected.'
- claim_id: c5
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h725
    h: 800a134e3dfa
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h599
    h: 800a134e3dfa
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h432
    h: 800a134e3dfa
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-x-us-50
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.47
    h: 88362aa00bc0
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h597
    h: b1c5cbca1260
  review: drafted
---
