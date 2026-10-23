---
id: fc:sma-sunny-island-us-f935
type: FaultCode
name: SMA SI-US F935
aliases:
- F935
- f935
- SMA F935
- 'Error message via SiCom: Error in the generator'
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F935
code_key: f935
display_message: 'Error message via SiCom: Error in the generator'
vendor_severity: '3'
page: 219
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r2
    h: e1e34b4ff054
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r2
    h: e1e34b4ff054
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:backup-generator
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r2
    h: e1e34b4ff054
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
