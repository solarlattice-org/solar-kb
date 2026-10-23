---
id: fc:sma-sb-us-41-9037
type: FaultCode
name: SMA SB-US-41 9037
aliases:
- '9037'
- SMA 9037
- Generator not connected
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '9037'
code_key: '9037'
display_message: Generator not connected
page: 70
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.67
    h: bffcb96841f0
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h438
    h: 09568097bfe0
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:pv-array-not-connected
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r4
    h: ef67ddc41dfe
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=24.r4
    h: ef67ddc41dfe
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h752
    h: 5ea07515b868
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-disconnect-switch
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r4
    h: ef67ddc41dfe
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=24.r4
    h: ef67ddc41dfe
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h752
    h: 5ea07515b868
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:pv-switch-function-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h753
    h: 3aa2c335ba4a
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: PV generator not connected, so no feed-in.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r4
    h: ef67ddc41dfe
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=24.r4
    h: ef67ddc41dfe
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h752
    h: 5ea07515b868
  review: drafted
  review_note: 'support check: partial - Passages say the PV generator was not connected, but do not state
    the device trips or stops production.'
---
