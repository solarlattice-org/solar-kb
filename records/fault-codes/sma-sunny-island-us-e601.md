---
id: fc:sma-sunny-island-us-e601
type: FaultCode
name: SMA SI-US E601
aliases:
- E601
- e601
- SMA E601
- Relay 1 off
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E601
code_key: e601
display_message: Relay 1 off
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r1
    h: 51e9494c6577
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Status event recording a relay switching state.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=137.r1
    h: 51e9494c6577
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=131
    h: 5537eaf27082
  review: drafted
---
