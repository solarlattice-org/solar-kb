---
id: fc:sma-sbse-us-50-9350
type: FaultCode
name: SMA SBSE-US-50 9350
aliases:
- '9350'
- SMA 9350
- Timeout for battery status change
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9350'
code_key: '9350'
display_message: Timeout for battery status change
page: 121
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.78
    h: 56d2ff312488
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h801
    h: 92f63d932262
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:battery-status-timeout
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h801
    h: 92f63d932262
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h802
    h: d2d0c0e41c15
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:battery-connection-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h803
    h: bb24c2dbadaf
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h803
    h: bb24c2dbadaf
  review: drafted
---
