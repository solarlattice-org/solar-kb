---
id: fc:sma-sunny-island-us-f928
type: FaultCode
name: SMA SI-US F928
aliases:
- F928
- f928
- SMA F928
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F928
code_key: f928
vendor_severity: '3'
page: 218
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r10
    h: 46116b699209
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r10
    h: 46116b699209
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:battery-charge-overcurrent
  note: Reported by the battery management via SiCom during charge mode.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r10
    h: 46116b699209
  review: drafted
  review_note: 'support check: partial - Row states SiCom charge-mode message but not that it is reported
    by the battery management.'
---
