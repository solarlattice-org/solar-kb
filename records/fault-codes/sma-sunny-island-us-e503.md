---
id: fc:sma-sunny-island-us-e503
type: FaultCode
name: SMA SI-US E503
aliases:
- E503
- e503
- SMA E503
- Grid request due to exceeding the power limit
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E503
code_key: e503
display_message: Grid request due to exceeding the power limit
page: 207
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r3
    h: 6c6009451b12
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Grid requested because load power exceeds the set limit.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r3
    h: 6c6009451b12
  review: drafted
  review_note: 'support check: partial - Grid request due to exceeding the power limit is stated, but
    ''load'' power is not mentioned.'
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=136.r3
    h: 6c6009451b12
  review: drafted
---
