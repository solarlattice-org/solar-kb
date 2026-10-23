---
id: fc:sma-stp-core1-us-9038
type: FaultCode
name: SMA CORE1-US 9038
aliases:
- '9038'
- SMA 9038
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '9038'
code_key: '9038'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r5
    h: 7d6d4cbeb862
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r5
    h: 7d6d4cbeb862
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=24.r5
    h: 7d6d4cbeb862
  review: drafted
- claim_id: c4
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
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
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
- claim_id: c6
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
