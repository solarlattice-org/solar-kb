---
id: fc:sma-stp-core1-us-10254
type: FaultCode
name: SMA CORE1-US 10254
aliases:
- '10254'
- SMA 10254
- '[Interface]: duplex mode goes to [Full / Half]'
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10254'
code_key: '10254'
display_message: '[Interface]: duplex mode goes to [Full / Half]'
page: 57
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h310
    h: 426295aeba54
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h311
    h: ee3d968ae8d2
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h227
    h: 426295aeba54
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h228
    h: ee3d968ae8d2
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r2
    h: 66c1bfeddfc4
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:degraded-network-link
  note: Applies when duplex mode changes to half.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h311
    h: ee3d968ae8d2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h228
    h: ee3d968ae8d2
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r2
    h: 66c1bfeddfc4
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h478
    h: c263711fb27b
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h491
    h: c263711fb27b
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:network-cable
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h312
    h: d792c604460a
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h229
    h: d792c604460a
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r2
    h: 66c1bfeddfc4
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h492
    h: 3e364e48e1a4
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:network-connection-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h312
    h: d792c604460a
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h229
    h: d792c604460a
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r2
    h: 66c1bfeddfc4
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h280
    h: d792c604460a
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h492
    h: 3e364e48e1a4
  review: drafted
---
