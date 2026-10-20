---
id: fc:sma-stp-core1-us-9007
type: FaultCode
name: SMA CORE1-US 9007
aliases:
- '9007'
- SMA 9007
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '9007'
code_key: '9007'
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r5
    h: 985fbbab0d31
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r5
    h: 985fbbab0d31
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  note: Self-test applies to Italy only.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r5
    h: 985fbbab0d31
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r5
    h: 985fbbab0d31
  review: drafted
  review_note: 'support check: partial - Self-test was aborted (Italy only), which is not exactly a failure
    but close.'
- claim_id: c4
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Then rerun the self-test.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r5
    h: 985fbbab0d31
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r5
    h: 985fbbab0d31
  review: drafted
  review_note: 'support check: partial - AC connection check is stated, but the ''rerun the self-test''
    note is not in the passages.'
---
