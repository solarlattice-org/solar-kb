---
id: fc:sma-sunny-island-us-f781
type: FaultCode
name: SMA SI-US F781
aliases:
- F781
- f781
- SMA F781
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F781
code_key: f781
vendor_severity: '4'
page: 216
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r19
    h: cc87ed74c9f6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r19
    h: cc87ed74c9f6
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  note: Error located at a slave device
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r19
    h: cc87ed74c9f6
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Row states the system shuts down
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r19
    h: cc87ed74c9f6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
