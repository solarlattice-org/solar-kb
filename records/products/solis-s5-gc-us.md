---
id: prod:solis-s5-gc-us
type: Product
name: Solis S5-GC(75-125)K-US
aliases:
- S5-GC
- Solis S5
- S5 Series
- S5-GC75K-US
- S5-GC80K-US
- S5-GC90K-US
- S5-GC100K-US
- S5 Series Grid Inverter
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: sec=h1
    h: 3e00c077410c
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:rs485
  note: Standard communication connection on all models
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=16.r35
    h: a24bedbf8940
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=19.r35
    h: 0c1dbcc42ab3
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=17.r36
    h: 1e607db0967f
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=18.r36
    h: 1e607db0967f
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:wifi
  note: Optional communication connection
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=16.r35
    h: a24bedbf8940
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=19.r35
    h: 0c1dbcc42ab3
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=17.r36
    h: 1e607db0967f
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=18.r36
    h: 1e607db0967f
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:cellular
  note: Optional communication connection
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=16.r35
    h: a24bedbf8940
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=19.r35
    h: 0c1dbcc42ab3
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=17.r36
    h: 1e607db0967f
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=18.r36
    h: 1e607db0967f
  review: drafted
- claim_id: c5
  attr: efficiency
  value:
    nominal: 98.7
    unit: unit:PERCENT
  conditions: Maximum efficiency, S5-GC75K-US
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=16.r17
    h: 9699a08efe38
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions)
- claim_id: c6
  attr: efficiency
  value:
    nominal: 98.8
    unit: unit:PERCENT
  conditions: Maximum efficiency, S5-GC100K-US
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=19.r17
    h: 446ae11f775b
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions)
- claim_id: c7
  attr: efficiency
  value:
    nominal: 98.3
    unit: unit:PERCENT
  conditions: CEC efficiency, S5-GC75K-US
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=16.r18
    h: ba8e370b74b4
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions)
- claim_id: c8
  attr: rated_output_current
  value:
    nominal: 90.2
    unit: unit:A
  conditions: Rated output current, S5-GC75K-US
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=16.r13
    h: 6c3250a08603
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c9
  attr: rated_output_current
  value:
    nominal: 108.3
    unit: unit:A
  conditions: Rated output current, S5-GC100K-US
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=19.r13
    h: f212e99a964f
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c10
  attr: max_input_current
  value:
    nominal: 32
    unit: unit:A
  conditions: Per input, printed as 8x32, S5-GC75K-US
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=16.r6
    h: f670065548d8
  review: drafted
- claim_id: c11
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Rated grid voltage, three-phase plus PE (3/PE~480), S5-GC75K-US
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=16.r12
    h: ec6bd7465e8b
  review: drafted
---
The Solis S5 Series is a three-phase grid-tied string inverter family for the US market, covering the S5-GC75K-US, S5-GC80K-US, S5-GC90K-US and S5-GC100K-US models. The S5-GC75K-US connects to a 480 V three-phase grid with PE and has a rated output current of 90.2 A, while the S5-GC100K-US is rated at 108.3 A. On the S5-GC75K-US, maximum input current is listed as 8x32 A. Maximum efficiency is 98.7% for the 75K model and 98.8% for the 100K model, and the 75K model has a CEC efficiency of 98.3%. Current distortion is below 3% at rated output power. RS485 is the standard communication link, and Wi-Fi or cellular can be added as options; the unit has an LCD display.

<!-- review notes
- sentence 1: support check: partial - Models listed, but three-phase, string inverter and US market are only implied by names/3/PE, not explicitly stated.
-->
