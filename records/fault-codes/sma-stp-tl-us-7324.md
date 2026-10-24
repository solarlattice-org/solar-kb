---
id: fc:sma-stp-tl-us-7324
type: FaultCode
name: SMA STP-TL-US 7324
aliases:
- '7324'
- SMA 7324
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '7324'
code_key: '7324'
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r8
    h: a232f4198228
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
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r8
    h: a232f4198228
  review: drafted
---
