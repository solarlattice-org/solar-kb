---
id: fc:sma-sunny-central-cp-xt-7510
type: FaultCode
name: SMA SC-CP-XT 7510
aliases:
- '7510'
- SMA 7510
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7510'
code_key: '7510'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r10
    h: d4f7ec89274a
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-kb-error-message-7510-fan-failure-inside-3
  cite:
  - src: src:sma-kb-error-message-7510-fan-failure-inside-3
    loc: sec=h1
    h: fe9f9e69d560
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r10
    h: d4f7ec89274a
  - src: src:sma-kb-error-message-7510-fan-failure-inside-3
    loc: sec=h1
    h: fe9f9e69d560
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r10
    h: d4f7ec89274a
  - src: src:sma-kb-error-message-7510-fan-failure-inside-3
    loc: sec=h1
    h: fe9f9e69d560
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:sma-kb-error-message-7510-fan-failure-inside-3
    loc: sec=h1
    h: fe9f9e69d560
  review: drafted
  review_note: 'support check: partial - The article asks whether the fan is operational, but it is a
    question to report to SMA rather than a…'
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r10
    h: d4f7ec89274a
  - src: src:sma-kb-error-message-7510-fan-failure-inside-3
    loc: sec=h1
    h: fe9f9e69d560
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation after cleaning fan inlets.
  cite:
  - src: src:sma-kb-error-message-7510-fan-failure-inside-3
    loc: sec=h1
    h: fe9f9e69d560
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r10
    h: d4f7ec89274a
  - src: src:sma-kb-error-message-7510-fan-failure-inside-3
    loc: sec=h1
    h: fe9f9e69d560
  review: drafted
---
