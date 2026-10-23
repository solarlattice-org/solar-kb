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
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r5
    h: 7aa84c496d40
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:self-test-failure
  note: Self-test was aborted.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r5
    h: 985fbbab0d31
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r5
    h: 985fbbab0d31
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r5
    h: 7aa84c496d40
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h734
    h: ab2f8aa642a3
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r5
    h: 985fbbab0d31
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r5
    h: 985fbbab0d31
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r5
    h: 7aa84c496d40
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h735
    h: 46c322cdc774
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:grid-settings-check
  note: Verify country data set before restarting the self-test.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h735
    h: 46c322cdc774
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h619
    h: 46c322cdc774
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h452
    h: 46c322cdc774
  review: drafted
---
