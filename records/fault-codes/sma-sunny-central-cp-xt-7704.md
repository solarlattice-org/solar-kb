---
id: fc:sma-sunny-central-cp-xt-7704
type: FaultCode
name: SMA SC-CP-XT 7704
aliases:
- '7704'
- SMA 7704
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7704'
code_key: '7704'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r15
    h: 6ba85e02f613
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-kb-error-message-7704-dc-disconnection-point
  cite:
  - src: src:sma-kb-error-message-7704-dc-disconnection-point
    loc: sec=h1
    h: 3a7c628891d1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:switch-status-fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r15
    h: 6ba85e02f613
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-disconnect-switch
  note: Motor-driven DC switchgear breakers.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r15
    h: 6ba85e02f613
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:pv-switch-function-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r15
    h: 6ba85e02f613
  review: drafted
  review_note: 'support check: partial - Row says to check that breaker switches are OFF, which is a switch
    check but not explicitly a function check.'
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r15
    h: 6ba85e02f613
  review: drafted
---
