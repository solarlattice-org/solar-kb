---
id: fc:sma-sb-us-41-7340
type: FaultCode
name: SMA SB-US-41 7340
aliases:
- '7340'
- SMA 7340
- Update communication failed
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '7340'
code_key: '7340'
display_message: Update communication failed
page: 64
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.46
    h: c9316e9883c0
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h360
    h: 83fd2d4db8a3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h360
    h: 83fd2d4db8a3
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h361
    h: 69703eaf6dc4
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:retry-update
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h362
    h: 72550f5f341e
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:update-file-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h362
    h: 72550f5f341e
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the message appears again after retry.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h362
    h: 72550f5f341e
  review: drafted
---
