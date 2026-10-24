---
id: fc:sma-stp-core1-us-10108
type: FaultCode
name: SMA CORE1-US 10108
aliases:
- '10108'
- SMA 10108
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10108'
code_key: '10108'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r6
    h: 9f2513a35d22
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r6
    h: 9f2513a35d22
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=24.r6
    h: 9f2513a35d22
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:informational
  note: Status message that clock time was adjusted, showing old time; preceding service text belongs
    to prior row.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r6
    h: 9f2513a35d22
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r6
    h: 9f2513a35d22
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=24.r6
    h: 9f2513a35d22
  review: drafted
  review_note: 'support check: partial - Row shows ''Time adjusted / old time'' but the informational
    classification is only implied; the passage also shows a contact-Service…'
- claim_id: c5
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r6
    h: 9f2513a35d22
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r6
    h: 9f2513a35d22
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=24.r6
    h: 9f2513a35d22
  review: drafted
---
