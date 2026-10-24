---
id: fc:sma-stp-tl-us-6606
type: FaultCode
name: SMA STP-TL-US 6606
aliases:
- '6606'
- SMA 6606
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '6606'
code_key: '6606'
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r8
    h: 95098f816e27
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r8
    h: 95098f816e27
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h649
    h: 731fc1a6c0ad
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r8
    h: 95098f816e27
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h650
    h: cca77e1e7cd3
  review: drafted
  review_note: 'support check: partial - Device-level fault implies the inverter, but the component is
    not explicitly stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r8
    h: 95098f816e27
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h651
    h: 417f2f122215
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r8
    h: 95098f816e27
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h650
    h: cca77e1e7cd3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h651
    h: 417f2f122215
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r8
    h: 95098f816e27
  review: drafted
---
