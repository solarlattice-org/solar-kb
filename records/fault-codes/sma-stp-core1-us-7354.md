---
id: fc:sma-stp-core1-us-7354
type: FaultCode
name: SMA CORE1-US 7354
aliases:
- '7354'
- SMA 7354
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7354'
code_key: '7354'
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r6
    h: a5c2cad80410
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r6
    h: a5c2cad80410
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:firmware-update-failure
  note: Applies to the time zone database update.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r6
    h: a5c2cad80410
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r6
    h: a5c2cad80410
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:firmware-update
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r6
    h: a5c2cad80410
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r6
    h: a5c2cad80410
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the message recurs after retrying.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r6
    h: a5c2cad80410
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r6
    h: a5c2cad80410
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Operator retries update first; service only if failure repeats.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r6
    h: a5c2cad80410
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r6
    h: a5c2cad80410
  review: drafted
  review_note: 'support check: partial - Operator retry is stated, but the passages don''t say the code
    clears by manual reset or acknowledgement.'
---
