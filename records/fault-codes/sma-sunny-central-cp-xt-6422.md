---
id: fc:sma-sunny-central-cp-xt-6422
type: FaultCode
name: SMA SC-CP-XT 6422
aliases:
- '6422'
- SMA 6422
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6422'
code_key: '6422'
page: 37
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r16
    h: e96aa25bb08b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r16
    h: e96aa25bb08b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h531
    h: 97b09800e944
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r16
    h: e96aa25bb08b
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h532
    h: fd79e3ee82cf
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if the event persists after restart and recommissioning.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h532
    h: fd79e3ee82cf
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h531
    h: 97b09800e944
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first, then disconnect and recommission; replace assembly or inverter if it persists.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h532
    h: fd79e3ee82cf
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r16
    h: e96aa25bb08b
  review: drafted
---
