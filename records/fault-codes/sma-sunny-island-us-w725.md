---
id: fc:sma-sunny-island-us-w725
type: FaultCode
name: SMA SI-US W725
aliases:
- W725
- w725
- SMA W725
- Autostart meter slave 2 elapsed
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W725
code_key: w725
display_message: Autostart meter slave 2 elapsed
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r16
    h: 10a1df2ef455
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r16
    h: 10a1df2ef455
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:autostart-limit-reached
  note: Reported for slave device 2.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r16
    h: 10a1df2ef455
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r16
    h: 10a1df2ef455
  review: drafted
---
