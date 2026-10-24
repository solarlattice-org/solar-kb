---
id: fc:sma-sunny-island-us-e405
type: FaultCode
name: SMA SI-US E405
aliases:
- E405
- e405
- SMA E405
- Manual error acknowledgment of generator error
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E405
code_key: e405
display_message: Manual error acknowledgment of generator error
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=135.r2
    h: 08a5fcf07a2b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Logs that a generator error was acknowledged manually.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=135.r2
    h: 08a5fcf07a2b
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=135.r2
    h: 08a5fcf07a2b
  review: drafted
---
