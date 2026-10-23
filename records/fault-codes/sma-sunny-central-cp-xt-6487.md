---
id: fc:sma-sunny-central-cp-xt-6487
type: FaultCode
name: SMA SC-CP-XT 6487
aliases:
- '6487'
- SMA 6487
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6487'
code_key: '6487'
page: 38
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r16
    h: ce01fc6fc3c9
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ground-fault
  note: Ground fault on the AC side.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r16
    h: ce01fc6fc3c9
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:surge-protection-device
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r16
    h: ce01fc6fc3c9
  review: drafted
  review_note: 'support check: partial - Overvoltage protection is to be checked, but the passage doesn''t
    state the surge protection device is affected.'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: After checking overvoltage protection.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r16
    h: ce01fc6fc3c9
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r16
    h: ce01fc6fc3c9
  review: drafted
---
