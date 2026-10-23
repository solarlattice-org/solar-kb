---
id: fc:sma-sunny-island-us-f754
type: FaultCode
name: SMA SI-US F754
aliases:
- F754
- f754
- SMA F754
- Communication with Multicluster Box interrupted
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F754
code_key: f754
display_message: Communication with Multicluster Box interrupted
vendor_severity: '2'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r11
    h: 15d01e47d623
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r11
    h: 15d01e47d623
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r11
    h: 15d01e47d623
  review: drafted
---
