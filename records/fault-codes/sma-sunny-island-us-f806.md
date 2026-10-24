---
id: fc:sma-sunny-island-us-f806
type: FaultCode
name: SMA SI-US F806
aliases:
- F806
- f806
- SMA F806
- Multicluster Box settings do not match software settings.
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F806
code_key: f806
display_message: Multicluster Box settings do not match software settings.
vendor_severity: '4'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r4
    h: 6822ad69fff7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r4
    h: 6822ad69fff7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  note: Multicluster Box settings conflict with software settings
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r4
    h: 6822ad69fff7
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r4
    h: 6822ad69fff7
  review: drafted
---
