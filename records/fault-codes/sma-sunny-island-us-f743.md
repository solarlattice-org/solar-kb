---
id: fc:sma-sunny-island-us-f743
type: FaultCode
name: SMA SI-US F743
aliases:
- F743
- f743
- SMA F743
- Internal CAN communication of the master is interrupted
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F743
code_key: f743
display_message: Internal CAN communication of the master is interrupted
vendor_severity: '3'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r29
    h: 320c9cabda63
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r29
    h: 320c9cabda63
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  note: Internal CAN bus communication of the cluster master is interrupted.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r29
    h: 320c9cabda63
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r29
    h: 320c9cabda63
  review: drafted
---
