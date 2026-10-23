---
id: fc:sma-sunny-island-us-f704
type: FaultCode
name: SMA SI-US F704
aliases:
- F704
- f704
- SMA F704
- Invalid DSP calibration
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F704
code_key: f704
display_message: Invalid DSP calibration
vendor_severity: '4'
page: 214
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=150.r3
    h: b7b83b9ebb07
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=150.r3
    h: b7b83b9ebb07
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:calibration-failure
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=150.r3
    h: b7b83b9ebb07
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:digital-signal-processor
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=150.r3
    h: b7b83b9ebb07
  review: drafted
---
