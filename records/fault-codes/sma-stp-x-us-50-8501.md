---
id: fc:sma-stp-x-us-50-8501
type: FaultCode
name: SMA STP-X-US 8501
aliases:
- '8501'
- SMA 8501
- DC current sensor C offset
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '8501'
code_key: '8501'
display_message: DC current sensor C offset
page: 95
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.45
    h: 73a00920685b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h588
    h: '9515911612e1'
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:current-sensor-offset
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.45
    h: 73a00920685b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h588
    h: '9515911612e1'
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.45
    h: 73a00920685b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h588
    h: '9515911612e1'
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when the message recurs.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.45
    h: 73a00920685b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h589
    h: 6246028e59dd
  review: drafted
---
