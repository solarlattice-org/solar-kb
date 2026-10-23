---
id: fc:sma-sunny-island-us-f758
type: FaultCode
name: SMA SI-US F758
aliases:
- F758
- f758
- SMA F758
- No output voltage measured from the main cluster
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F758
code_key: f758
display_message: No output voltage measured from the main cluster
vendor_severity: '2'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r15
    h: 09ced55720ef
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r15
    h: 09ced55720ef
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:no-output-voltage
  note: Applies to the main cluster as a whole
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r15
    h: 09ced55720ef
  review: drafted
---
