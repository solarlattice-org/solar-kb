---
id: fc:sma-stp-core1-us-10286
type: FaultCode
name: SMA CORE1-US 10286
aliases:
- '10286'
- SMA 10286
- Wi-Fi connection lost
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10286'
code_key: '10286'
display_message: Wi-Fi connection lost
page: 58
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h322
    h: 31aa4a940e19
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h323
    h: c03208dd7c40
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h239
    h: 31aa4a940e19
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h240
    h: c03208dd7c40
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h314
    h: 31aa4a940e19
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h315
    h: c03208dd7c40
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h323
    h: c03208dd7c40
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h240
    h: c03208dd7c40
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h315
    h: c03208dd7c40
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h500
    h: 5b3b9a176516
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:network-connection-check
  note: Check router or access point status and range; add a repeater if the message recurs often.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h324
    h: 174f589044d1
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h241
    h: 174f589044d1
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h316
    h: 174f589044d1
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h501
    h: 174f589044d1
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h323
    h: c03208dd7c40
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h324
    h: 174f589044d1
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h240
    h: c03208dd7c40
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h241
    h: 174f589044d1
  review: drafted
  review_note: 'support check: partial - The passages give no warning classification; a lost connection
    with corrective measures only loosely implies a warning.'
---
