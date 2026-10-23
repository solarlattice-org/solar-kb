---
id: fc:sma-sunny-central-cp-xt-7600
type: FaultCode
name: SMA SC-CP-XT 7600
aliases:
- '7600'
- SMA 7600
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7600'
code_key: '7600'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r11
    h: 822431bdacd0
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r11
    h: 822431bdacd0
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:communication-module
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r11
    h: 822431bdacd0
  review: drafted
  review_note: 'support check: partial - The communication is between the touch display and communication
    unit, so the communication module is involved, but the passage doesn''t…'
- claim_id: c4
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r11
    h: 822431bdacd0
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation if cabling check between display and communication unit does not clear it.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r11
    h: 822431bdacd0
  review: drafted
---
