---
id: fc:sma-sb-us-40-7347
type: FaultCode
name: SMA SB-US-40 7347
aliases:
- '7347'
- SMA 7347
- Incompatible file
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-40
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP/1TP-US-40)
code: '7347'
code_key: '7347'
display_message: Incompatible file
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-40-ba-en-13
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h218
    h: d3c9de41c57d
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h219
    h: 516b9b5b7c33
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h188
    h: 516b9b5b7c33
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h273
    h: 516b9b5b7c33
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h219
    h: 516b9b5b7c33
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h365
    h: 9e3ce0655013
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h386
    h: 9e3ce0655013
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:config-file-verification
  note: Verify file suitability, then retry the import.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h272
    h: 4f102694362d
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h189
    h: 4f102694362d
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h274
    h: 4f102694362d
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h220
    h: 4f102694362d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h366
    h: 4f102694362d
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h387
    h: 4f102694362d
  review: drafted
---
