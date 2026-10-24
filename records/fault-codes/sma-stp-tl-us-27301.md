---
id: fc:sma-stp-tl-us-27301
type: FaultCode
name: SMA STP-TL-US 27301
aliases:
- '27301'
- SMA 27301
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '27301'
code_key: '27301'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r3
    h: 8b80a8cadd1e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Firmware update of communication component in progress.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r11
    h: 8b80a8cadd1e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r11
    h: 8b80a8cadd1e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=27.r11
    h: 8b80a8cadd1e
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=21.r4
    h: 929ecb3807eb
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r3
    h: 8b80a8cadd1e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.101
    h: fd03b05de813
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h564
    h: 8a89e68bb1f3
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h565
    h: 622fab418a3e
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:communication-module
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r11
    h: 8b80a8cadd1e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r11
    h: 8b80a8cadd1e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=27.r11
    h: 8b80a8cadd1e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h565
    h: 622fab418a3e
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r3
    h: 8b80a8cadd1e
  review: drafted
---
