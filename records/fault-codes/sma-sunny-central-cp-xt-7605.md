---
id: fc:sma-sunny-central-cp-xt-7605
type: FaultCode
name: SMA SC-CP-XT 7605
aliases:
- '7605'
- SMA 7605
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7605'
code_key: '7605'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r14
    h: 9f9fdf56bcf5
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-kb-error-message-7605-communication-failure-stack
  cite:
  - src: src:sma-kb-error-message-7605-communication-failure-stack
    loc: sec=h1
    h: c1f652a3594e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r14
    h: 9f9fdf56bcf5
  - src: src:sma-kb-error-message-7605-communication-failure-stack
    loc: sec=h1
    h: c1f652a3594e
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:communication-cable-check
  note: Fiber optic link between stack and control module; applies to central inverter variants per knowledge
    article.
  cite:
  - src: src:sma-kb-error-message-7605-communication-failure-stack
    loc: sec=h1
    h: c1f652a3594e
  review: drafted
  review_note: 'support check: partial - Article covers checking fiber optic plug connection and bend
    radius, but it''s not a generic communication cable check by name;…'
- claim_id: c5
  rel: mitigated_by
  target: mit:cable-replacement
  cite:
  - src: src:sma-kb-error-message-7605-communication-failure-stack
    loc: sec=h1
    h: c1f652a3594e
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r14
    h: 9f9fdf56bcf5
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Acknowledge after checking connection; escalate to cable then module replacement if persistent.
  cite:
  - src: src:sma-kb-error-message-7605-communication-failure-stack
    loc: sec=h1
    h: c1f652a3594e
  review: drafted
  review_note: 'support check: partial - Article describes pressing Ack on the AST, then cable and AST
    replacement, but the classification as manual reset is only…'
- claim_id: c8
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r14
    h: 9f9fdf56bcf5
  - src: src:sma-kb-error-message-7605-communication-failure-stack
    loc: sec=h1
    h: c1f652a3594e
  review: drafted
---
