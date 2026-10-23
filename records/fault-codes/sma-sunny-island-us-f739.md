---
id: fc:sma-sunny-island-us-f739
type: FaultCode
name: SMA SI-US F739
aliases:
- F739
- f739
- SMA F739
- Internal communication of the master is interrupted
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F739
code_key: f739
display_message: Internal communication of the master is interrupted
vendor_severity: '3'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r25
    h: c5983f62a144
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r25
    h: c5983f62a144
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  note: Applies to the cluster master device.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r25
    h: c5983f62a144
  review: drafted
---
