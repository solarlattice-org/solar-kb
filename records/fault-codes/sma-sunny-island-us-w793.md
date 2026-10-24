---
id: fc:sma-sunny-island-us-w793
type: FaultCode
name: SMA SI-US W793
aliases:
- W793
- w793
- SMA W793
- DSP reset detected on slave 3
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W793
code_key: w793
display_message: DSP reset detected on slave 3
vendor_severity: '1'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r27
    h: 253a272f03ed
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r27
    h: 253a272f03ed
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dsp-reset
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r27
    h: 253a272f03ed
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:digital-signal-processor
  note: Slave device 3 of the cluster
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r27
    h: 253a272f03ed
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r27
    h: 253a272f03ed
  review: drafted
---
