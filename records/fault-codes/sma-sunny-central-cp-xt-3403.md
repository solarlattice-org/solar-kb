---
id: fc:sma-sunny-central-cp-xt-3403
type: FaultCode
name: SMA SC-CP-XT 3403
aliases:
- '3403'
- SMA 3403
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3403'
code_key: '3403'
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r1
    h: 403fe351ab02
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-kb-error-message-3403-dc-overvoltage
  cite:
  - src: src:sma-kb-error-message-3403-dc-overvoltage
    loc: sec=h1
    h: 17910a6f1c18
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r1
    h: 403fe351ab02
  - src: src:sma-kb-error-message-3403-dc-overvoltage
    loc: sec=h1
    h: 17910a6f1c18
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r1
    h: 403fe351ab02
  - src: src:sma-kb-error-message-3403-dc-overvoltage
    loc: sec=h1
    h: 17910a6f1c18
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r1
    h: 403fe351ab02
  - src: src:sma-kb-error-message-3403-dc-overvoltage
    loc: sec=h1
    h: 17910a6f1c18
  review: drafted
  review_note: 'support check: partial - Corrective measure is to check the DC voltage, but detection
    method isn''t explicitly stated.'
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r1
    h: 403fe351ab02
  - src: src:sma-kb-error-message-3403-dc-overvoltage
    loc: sec=h1
    h: 17910a6f1c18
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Applies when the array is oversized for the permitted DC voltage range.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r1
    h: 403fe351ab02
  - src: src:sma-kb-error-message-3403-dc-overvoltage
    loc: sec=h1
    h: 17910a6f1c18
  review: drafted
---
