---
id: fc:sma-sb-us-41-7324
type: FaultCode
name: SMA SB-US-41 7324
aliases:
- '7324'
- SMA 7324
- Wait for update conditions
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '7324'
code_key: '7324'
display_message: Wait for update conditions
page: 63
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.42
    h: 608906a7e86e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h346
    h: 42228ca4b612
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  note: One source instead describes successful update awaiting sufficient DC irradiation.
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=18.r4
    h: dbea9e1ec4ba
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h347
    h: d330f7b2eab4
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h373
    h: d330f7b2eab4
  review: drafted
  review_note: 'support check: partial - Passages say update conditions test failed and package unsuitable,
    implying update failure, but ''firmware update failure'' isn''t stated explicitly; the…'
- claim_id: c3
  rel: mitigated_by
  target: mit:retry-update
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=18.r4
    h: dbea9e1ec4ba
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h348
    h: 38838d9d831b
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h374
    h: 38838d9d831b
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:update-file-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h348
    h: 38838d9d831b
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h374
    h: 38838d9d831b
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the message appears again after retry.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h348
    h: 38838d9d831b
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h374
    h: 38838d9d831b
  review: drafted
---
