---
id: fc:sma-sbse-us-50-9038
type: FaultCode
name: SMA SBSE-US-50 9038
aliases:
- '9038'
- SMA 9038
- Redundant rapid shutdown discharge function not assured
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9038'
code_key: '9038'
display_message: Redundant rapid shutdown discharge function not assured
page: 118
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.69
    h: 150d51208104
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h756
    h: 7d79bd380ca1
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:rapid-shutdown-failure
  note: Redundant discharge path of rapid shutdown not assured.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r5
    h: 7d6d4cbeb862
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r5
    h: 7d6d4cbeb862
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=24.r5
    h: 7d6d4cbeb862
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h756
    h: 7d79bd380ca1
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h635
    h: 7d79bd380ca1
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h758
    h: 417f2f122215
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h637
    h: 417f2f122215
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h757
    h: cca77e1e7cd3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h636
    h: cca77e1e7cd3
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  note: Cause must be determined by Service.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h757
    h: cca77e1e7cd3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h758
    h: 417f2f122215
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h636
    h: cca77e1e7cd3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h637
    h: 417f2f122215
  review: drafted
---
