---
id: fc:sma-sunny-central-cp-xt-9009
type: FaultCode
name: SMA SC-CP-XT 9009
aliases:
- '9009'
- SMA 9009
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '9009'
code_key: '9009'
page: 40
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r9
    h: ac35307d9f09
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:emergency-stop-triggered
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r9
    h: ac35307d9f09
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:emergency-stop
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r9
    h: ac35307d9f09
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r9
    h: ac35307d9f09
  review: drafted
  review_note: 'support check: partial - Row doesn''t explicitly classify as fault; the need for intervention
    suggests it, but no warning/fault marker is given.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r9
    h: ac35307d9f09
  review: drafted
  review_note: 'support check: partial - Fast stop tripped implies stop, but production stoppage is not
    explicitly stated.'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Fast stop must be switched back on after the cause is removed.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r9
    h: ac35307d9f09
  review: drafted
---
