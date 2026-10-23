---
id: fc:sma-sbse-us-50-9007
type: FaultCode
name: SMA SBSE-US-50 9007
aliases:
- '9007'
- SMA 9007
- Abort self-test
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9007'
code_key: '9007'
display_message: Abort self-test
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.64
    h: 5e1fd0a82618
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h733
    h: d581c675af69
  review: drafted
- claim_id: c2
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
- claim_id: c3
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
- claim_id: c4
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
