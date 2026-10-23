---
id: fc:sma-sunny-island-us-w792
type: FaultCode
name: SMA SI-US W792
aliases:
- W792
- w792
- SMA W792
- DSP reset detected on slave 2
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W792
code_key: w792
display_message: DSP reset detected on slave 2
vendor_severity: '1'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r26
    h: 88c96cde3448
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r26
    h: 88c96cde3448
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dsp-reset
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r26
    h: 88c96cde3448
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:digital-signal-processor
  note: Slave device 2 of the cluster
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r26
    h: 88c96cde3448
  review: drafted
---
