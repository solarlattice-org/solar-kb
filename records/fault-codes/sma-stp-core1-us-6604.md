---
id: fc:sma-stp-core1-us-6604
type: FaultCode
name: SMA CORE1-US 6604
aliases:
- '6604'
- SMA 6604
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '6604'
code_key: '6604'
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r11
    h: bca34e0cf6a4
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r11
    h: bca34e0cf6a4
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r11
    h: bca34e0cf6a4
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r12
    h: c4cb08b4f931
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r11
    h: bca34e0cf6a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r12
    h: c4cb08b4f931
  review: drafted
  review_note: 'support check: partial - Cause must be determined by Service; fault classification is
    implied but not stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r11
    h: bca34e0cf6a4
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r12
    h: c4cb08b4f931
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r11
    h: bca34e0cf6a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r12
    h: c4cb08b4f931
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r11
    h: bca34e0cf6a4
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r12
    h: c4cb08b4f931
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r11
    h: bca34e0cf6a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r12
    h: c4cb08b4f931
  review: drafted
---
