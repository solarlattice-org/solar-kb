---
id: fc:sma-sunny-island-us-f890
type: FaultCode
name: SMA SI-US F890
aliases:
- F890
- f890
- SMA F890
- Interference at external measurement point of Multicluster Box
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F890
code_key: f890
display_message: Interference at external measurement point of Multicluster Box
vendor_severity: '2'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r12
    h: 75bdbbc85e65
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r12
    h: 75bdbbc85e65
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:measurement-signal-error
  note: Interference at the external measurement point of the Multicluster Box
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r12
    h: 75bdbbc85e65
  review: drafted
---
