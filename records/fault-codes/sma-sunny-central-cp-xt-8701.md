---
id: fc:sma-sunny-central-cp-xt-8701
type: FaultCode
name: SMA SC-CP-XT 8701
aliases:
- '8701'
- SMA 8701
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '8701'
code_key: '8701'
page: 40
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r4
    h: 02e2835e142b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:invalid-power-setpoint
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r4
    h: 02e2835e142b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r4
    h: 02e2835e142b
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  note: Inverter keeps operating on last valid setpoint or Pmax after day change.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r4
    h: 02e2835e142b
  review: drafted
  review_note: 'support check: partial - Operation continues on last valid value or Pmax, but ''no production
    effect'' is not explicitly stated; Pmax use may change output.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Valid setpoints are used again automatically; contact service if the condition persists.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r4
    h: 02e2835e142b
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r4
    h: 02e2835e142b
  review: drafted
---
