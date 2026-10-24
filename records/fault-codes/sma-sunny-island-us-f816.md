---
id: fc:sma-sunny-island-us-f816
type: FaultCode
name: SMA SI-US F816
aliases:
- F816
- f816
- SMA F816
- Error Q7 contactor
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: F816
code_key: f816
display_message: Error Q7 contactor
vendor_severity: '2'
page: 217
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r11
    h: cb5f6725f147
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r11
    h: cb5f6725f147
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:switch-status-fault
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r11
    h: cb5f6725f147
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-contactor
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r11
    h: cb5f6725f147
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r11
    h: cb5f6725f147
  review: drafted
---
