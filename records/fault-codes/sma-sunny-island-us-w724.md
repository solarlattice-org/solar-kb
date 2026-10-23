---
id: fc:sma-sunny-island-us-w724
type: FaultCode
name: SMA SI-US W724
aliases:
- W724
- w724
- SMA W724
- Autostart meter slave 1 elapsed
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W724
code_key: w724
display_message: Autostart meter slave 1 elapsed
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r15
    h: 62d098a4cc54
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r15
    h: 62d098a4cc54
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:autostart-limit-reached
  note: Reported for slave device 1.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r15
    h: 62d098a4cc54
  review: drafted
---
