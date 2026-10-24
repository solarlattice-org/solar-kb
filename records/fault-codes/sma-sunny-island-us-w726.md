---
id: fc:sma-sunny-island-us-w726
type: FaultCode
name: SMA SI-US W726
aliases:
- W726
- w726
- SMA W726
- Autostart meter slave 3 elapsed
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W726
code_key: w726
display_message: Autostart meter slave 3 elapsed
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r17
    h: ff936afd3095
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r17
    h: ff936afd3095
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:autostart-limit-reached
  note: Reported for slave device 3.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r17
    h: ff936afd3095
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r17
    h: ff936afd3095
  review: drafted
---
