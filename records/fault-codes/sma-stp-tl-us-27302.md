---
id: fc:sma-stp-tl-us-27302
type: FaultCode
name: SMA STP-TL-US 27302
aliases:
- '27302'
- SMA 27302
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '27302'
code_key: '27302'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r4
    h: f6506a55ac68
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Firmware update of main inverter component in progress.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r12
    h: f6506a55ac68
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r12
    h: f6506a55ac68
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=27.r12
    h: f6506a55ac68
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=21.r5
    h: 3d887bb4eb3e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.102
    h: 6dec59dcbaba
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h567
    h: f4036659500d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h568
    h: fb0faf43ec55
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r4
    h: f6506a55ac68
  review: drafted
---
