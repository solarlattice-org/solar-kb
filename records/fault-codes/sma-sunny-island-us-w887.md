---
id: fc:sma-sunny-island-us-w887
type: FaultCode
name: SMA SI-US W887
aliases:
- W887
- w887
- SMA W887
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W887
code_key: w887
vendor_severity: '1'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r11
    h: 3ed311b18a55
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r11
    h: 3ed311b18a55
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:communication-loss
  note: Raised when communication has been absent for more than 24 hours.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r11
    h: 3ed311b18a55
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:charge-controller
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r11
    h: 3ed311b18a55
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r11
    h: 3ed311b18a55
  review: drafted
---
