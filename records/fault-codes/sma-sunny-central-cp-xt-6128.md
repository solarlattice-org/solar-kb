---
id: fc:sma-sunny-central-cp-xt-6128
type: FaultCode
name: SMA SC-CP-XT 6128
aliases:
- '6128'
- SMA 6128
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6128'
code_key: '6128'
page: 37
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r10
    h: 754756f09748
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  note: 'Per knowledge-base article: AC voltage briefly above reconnection threshold at morning start-up.'
  cite:
  - src: src:sma-kb-shpxxx-xx-20-event-6128
    loc: sec=h1
    h: 9a7250093a96
  review: drafted
  review_note: 'support check: partial - The article describes AC voltage briefly above the reconnection
    threshold at morning start-up, but the event is labeled a General…'
- claim_id: c3
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:sma-kb-shpxxx-xx-20-event-6128
    loc: sec=h1
    h: 9a7250093a96
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-kb-shpxxx-xx-20-event-6128
    loc: sec=h1
    h: 9a7250093a96
  review: drafted
  review_note: 'support check: partial - The voltage threshold comparison is implied, but the passage
    does not explicitly describe a grid voltage measurement detection method.'
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: Only if the high voltage persists and cannot be eliminated.
  cite:
  - src: src:sma-kb-shpxxx-xx-20-event-6128
    loc: sec=h1
    h: 9a7250093a96
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r10
    h: 754756f09748
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  note: Grid connection withheld until voltage drops below threshold.
  cite:
  - src: src:sma-kb-shpxxx-xx-20-event-6128
    loc: sec=h1
    h: 9a7250093a96
  review: drafted
  review_note: 'support check: partial - Grid connection is withheld until voltage drops, which implies
    not feeding in, but the passage doesn''t explicitly call it a…'
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Sporadic case connects automatically; permanent case needs voltage check, utility adjustment or
    service.
  cite:
  - src: src:sma-kb-shpxxx-xx-20-event-6128
    loc: sec=h1
    h: 9a7250093a96
  review: drafted
  review_note: 'support check: partial - The sporadic case connects automatically once voltage drops,
    but the permanent case is not auto-reset, and ''service'' is only loosely implied.'
- claim_id: c9
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r10
    h: 754756f09748
  review: drafted
---
