---
id: fc:sma-sb-us-41-301
type: FaultCode
name: SMA SB-US-41 301
aliases:
- '301'
- SMA 301
- Grid incident
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '301'
code_key: '301'
display_message: Grid incident
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.9
    h: 0a382af15e0c
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h220
    h: 354164b2f12c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  note: Ten-minute average grid voltage out of range; grid voltage or impedance too high.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h239
    h: 8aae27dfe35e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h156
    h: 8aae27dfe35e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h241
    h: 8aae27dfe35e
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r1
    h: 5fb563f4f5f9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h221
    h: 3eae123eca32
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h459
    h: 3eae123eca32
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h393
    h: 3eae123eca32
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h239
    h: 8aae27dfe35e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h156
    h: 8aae27dfe35e
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r1
    h: 5fb563f4f5f9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h221
    h: 3eae123eca32
  review: drafted
  review_note: 'support check: partial - Passage titled ''Grid fault''/disconnects inverter, which suggests
    fault, but no explicit classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h239
    h: 8aae27dfe35e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h156
    h: 8aae27dfe35e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h241
    h: 8aae27dfe35e
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r1
    h: 5fb563f4f5f9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h221
    h: 3eae123eca32
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h459
    h: 3eae123eca32
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h393
    h: 3eae123eca32
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h240
    h: 1baae9a77bf7
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h157
    h: 1baae9a77bf7
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h242
    h: 1baae9a77bf7
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r1
    h: 5fb563f4f5f9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h222
    h: 62ae920ac057
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h460
    h: 62ae920ac057
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h394
    h: 1baae9a77bf7
  review: drafted
  review_note: 'support check: partial - Passages describe checking grid voltage and ten-minute average,
    implying voltage monitoring, but do not state the detection method explicitly.'
- claim_id: c6
  rel: mitigated_by
  target: mit:utility-consultation
  note: If voltage is out of range due to local grid; otherwise contact service.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h240
    h: 1baae9a77bf7
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h157
    h: 1baae9a77bf7
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h242
    h: 1baae9a77bf7
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h222
    h: 62ae920ac057
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h460
    h: 62ae920ac057
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h394
    h: 1baae9a77bf7
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: When grid voltage is within range and the message persists.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h240
    h: 1baae9a77bf7
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h157
    h: 1baae9a77bf7
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h242
    h: 1baae9a77bf7
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h222
    h: 62ae920ac057
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h460
    h: 62ae920ac057
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h394
    h: 1baae9a77bf7
  review: drafted
---
