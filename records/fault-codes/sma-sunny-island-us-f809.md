---
id: fc:sma-sunny-island-us-f809
type: FaultCode
name: SMA SI-US F809
aliases:
- F809
- f809
- SMA F809
- Error Q10 contactor (load shedding)
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F809
code_key: f809
display_message: Error Q10 contactor (load shedding)
vendor_severity: '4'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r7
    h: f6970a88ee55
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r7
    h: f6970a88ee55
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:switch-status-fault
  note: Load-shedding contactor Q10 reported in error.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r7
    h: f6970a88ee55
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-contactor
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r7
    h: f6970a88ee55
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r7
    h: f6970a88ee55
  review: drafted
---
