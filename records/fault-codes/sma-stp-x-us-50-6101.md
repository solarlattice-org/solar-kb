---
id: fc:sma-stp-x-us-50-6101
type: FaultCode
name: SMA STP-X-US 6101
aliases:
- '6101'
- SMA 6101
- Interference device / DevFlt > Self-diagnosis/ SlfDiag
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '6101'
code_key: '6101'
display_message: Interference device / DevFlt > Self-diagnosis/ SlfDiag
page: 88
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.25
    h: f0d1b537696b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h490
    h: 3fe2a64dd6ba
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h490
    h: 3fe2a64dd6ba
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h491
    h: 7270c7c2cd1e
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h491
    h: 7270c7c2cd1e
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h491
    h: 7270c7c2cd1e
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Brief occurrence at low irradiance clears itself; if permanent, restart; if persisting, replace
    assembly or inverter.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h492
    h: 6a2a7f7a4a21
  review: drafted
  review_note: 'support check: partial - Brief occurrences need no action, but the passages don''t state
    the event clears itself automatically; permanent requires restart/replacement.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: When the event follows a parameter change.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h492
    h: 6a2a7f7a4a21
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h492
    h: 6a2a7f7a4a21
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h492
    h: 6a2a7f7a4a21
  review: drafted
---
