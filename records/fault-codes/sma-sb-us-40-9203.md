---
id: fc:sma-sb-us-40-9203
type: FaultCode
name: SMA SB-US-40 9203
aliases:
- '9203'
- SMA 9203
- Short circuit in the SPS power outlet
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-40
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP/1TP-US-40)
code: '9203'
code_key: '9203'
display_message: Short circuit in the SPS power outlet
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-40-ba-en-13
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h259
    h: b21b2845209a
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h260
    h: a672af75e661
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:backup-outlet-short-circuit
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h259
    h: b21b2845209a
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h260
    h: a672af75e661
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h446
    h: 0abd747128c4
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h447
    h: 24b38a6f05f3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h781
    h: a9d92f37b0fc
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h782
    h: 24b38a6f05f3
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:backup-power-outlet
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h260
    h: a672af75e661
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h447
    h: 24b38a6f05f3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h782
    h: 24b38a6f05f3
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:backup-load-reduction
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h261
    h: ef9e5124f939
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h448
    h: 1bbc59405139
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h783
    h: 1bbc59405139
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Operator re-enables secure power supply operation after removing the faulty load.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h448
    h: 1bbc59405139
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h783
    h: 1bbc59405139
  review: drafted
  review_note: 'support check: partial - Switching on secure power supply operation again is an operator
    action, but the passages don''t explicitly say it is a…'
- claim_id: c7
  rel: applies_to
  target: prod:sma-sb-us-40
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h259
    h: b21b2845209a
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h260
    h: a672af75e661
  review: drafted
---
