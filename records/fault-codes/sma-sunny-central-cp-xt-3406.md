---
id: fc:sma-sunny-central-cp-xt-3406
type: FaultCode
name: SMA SC-CP-XT 3406
aliases:
- '3406'
- SMA 3406
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3406'
code_key: '3406'
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r3
    h: 37c2997eb420
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r3
    h: 37c2997eb420
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r3
    h: 37c2997eb420
  review: drafted
  review_note: 'support check: partial - Passage says voltage is too high and to check DC voltage, but
    doesn''t state detection method explicitly.'
- claim_id: c4
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r3
    h: 37c2997eb420
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r3
    h: 37c2997eb420
  review: drafted
  review_note: 'support check: partial - Check module wiring and system design suggests string configuration,
    but correction is not explicitly stated.'
---
