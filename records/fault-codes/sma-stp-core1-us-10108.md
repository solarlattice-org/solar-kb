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
  rel: has_event_class
  target: ec:informational
  note: Time adjustment status message reporting the previous time; the service line in the row looks
    like spillover from the table above.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r6
    h: 9f2513a35d22
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r6
    h: 9f2513a35d22
  review: drafted
  review_note: 'support check: partial - Time adjusted / old time is a status message, though the row
    contains ''Contact the Service'' text; informational not explicitly stated.'
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r6
    h: 9f2513a35d22
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r6
    h: 9f2513a35d22
  review: drafted
  review_note: 'support check: partial - A time adjustment message implies no production effect but is
    not explicitly stated.'
---
