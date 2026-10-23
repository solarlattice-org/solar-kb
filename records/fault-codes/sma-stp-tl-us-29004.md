---
id: fc:sma-stp-tl-us-29004
type: FaultCode
name: SMA STP-TL-US 29004
aliases:
- '29004'
- SMA 29004
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '29004'
code_key: '29004'
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=22.r2
    h: 9a60070f2b45
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:parameter-change-rejected
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r15
    h: 1851894a0a87
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r15
    h: 1851894a0a87
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=27.r15
    h: 1851894a0a87
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=22.r5
    h: 4a55c0f1a1eb
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=22.r2
    h: 9a60070f2b45
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.107
    h: edd3590f7093
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h582
    h: 978b87543654
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h583
    h: 65873cd56889
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r15
    h: 1851894a0a87
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r15
    h: 1851894a0a87
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=27.r15
    h: 1851894a0a87
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=22.r5
    h: 4a55c0f1a1eb
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=22.r2
    h: 9a60070f2b45
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h583
    h: 65873cd56889
  review: drafted
  review_note: 'support check: partial - Message ''Grid parameter unchanged'' is stated but nothing in
    the passages identifies it as informational.'
---
