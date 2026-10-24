---
id: fc:sma-sunny-island-us-w713
type: FaultCode
name: SMA SI-US W713
aliases:
- W713
- w713
- SMA W713
- Watchdog has been tripped
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: W713
code_key: w713
display_message: Watchdog has been tripped
vendor_severity: '1'
page: 215
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r6
    h: aa0d4d291b15
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r6
    h: aa0d4d291b15
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  note: Watchdog trip of the device controller.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r6
    h: aa0d4d291b15
  review: drafted
  review_note: 'support check: partial - Watchdog tripped is stated, but ''of the device controller''
    and internal device fault are not explicit in the passage.'
- claim_id: c4
  rel: applies_to
  target: prod:sma-sunny-island-us
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r6
    h: aa0d4d291b15
  review: drafted
---
