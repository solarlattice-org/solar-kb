---
id: prod:kaco-blueplanet-87-165-tl3
type: Product
name: KACO blueplanet 87.0-165 TL3
aliases:
- blueplanet 87.0 TL3
- blueplanet 92.0 TL3
- blueplanet 105 TL3
- blueplanet 110 TL3
- blueplanet 125 TL3
- blueplanet 137 TL3
- blueplanet 150 TL3
- blueplanet 155 TL3
- blueplanet 165 TL3
- KACO blueplanet 125 TL3 US
- KACO blueplanet 105TL3
- KACO blueplanet 155TL3
- KACO blueplanet 165TL3
category: Inverters
make: kaco
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:kaco
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: sec=h1
    h: 8abdc4754ff9
  review: drafted
  review_note: 'support check: partial - Passage shows KACO blueplanet models but doesn''t state the manufacturer
    as ''KACO new energy'' explicitly (only KACO brand name).'
- claim_id: c2
  rel: uses_protocol
  target: proto:modbus-tcp
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=18.r6
    h: eeef002f2fb9
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:sunspec-information-model
  note: Listed as 'Sunspec' alongside TCP/IP and Modbus TCP in the communication row of the data sheet.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=18.r6
    h: eeef002f2fb9
  review: drafted
- claim_id: c4
  rel: implements
  target: func:mppt
  note: One MPP control per inverter for the listed models.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=10.r9
    h: 9b9e2d280d25
  review: drafted
- claim_id: c5
  rel: lacks
  target: func:reverse-polarity-protection
  note: Data sheet lists polarity safeguard as 'no'; string fuses are also not included.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=11
    h: f0cf68a6d308
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=11.r2
    h: fd1d39390af8
  review: drafted
- claim_id: c6
  rel: implements
  target: func:surge-protection
  note: Data sheet lists DC overvoltage protection as 'Yes'.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=11
    h: f0cf68a6d308
  review: drafted
  review_note: 'support check: partial - DC overvoltage protection ''Yes'' is stated, but surge protection
    is not explicitly equated with it.'
- claim_id: c7
  rel: requires
  target: role:licensed-electrician
  note: Manual is addressed to an authorised electrician.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: sec=h1
    h: 8abdc4754ff9
  review: drafted
- claim_id: c8
  attr: efficiency
  value:
    nominal: 98.8
    unit: unit:PERCENT
  conditions: Maximum efficiency, KACO blueplanet 105TL3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=16.r2
    h: e8c6944788ec
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions); possible conflict with c11 (same source; check the conditions);
    possible conflict with c13 (same source; check the conditions)
- claim_id: c9
  attr: efficiency
  value:
    nominal: 99.1
    unit: unit:PERCENT
  conditions: Maximum efficiency, KACO blueplanet 125 TL3 US
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=16.r2
    h: e8c6944788ec
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions); possible conflict with c11 (same source; check the conditions);
    possible conflict with c12 (same source; check the conditions); possible conflict with c13 (same source;
    check the conditions)
- claim_id: c10
  attr: efficiency
  value:
    nominal: 99.2
    unit: unit:PERCENT
  conditions: Maximum efficiency, value printed across the 155TL3/165TL3 columns
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=16.r2
    h: e8c6944788ec
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions); possible conflict with c11 (same source; check the conditions);
    possible conflict with c12 (same source; check the conditions); possible conflict with c13 (same source;
    check the conditions)
- claim_id: c11
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: European efficiency, KACO blueplanet 105TL3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=16.r3
    h: 8d611fd71e71
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions); possible conflict with c10 (same source; check the conditions);
    possible conflict with c12 (same source; check the conditions); possible conflict with c13 (same source;
    check the conditions)
- claim_id: c12
  attr: efficiency
  value:
    nominal: 98.8
    unit: unit:PERCENT
  conditions: European efficiency, KACO blueplanet 125 TL3 US
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=16.r3
    h: 8d611fd71e71
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions); possible conflict with c11 (same source; check the conditions);
    possible conflict with c13 (same source; check the conditions)
- claim_id: c13
  attr: efficiency
  value:
    nominal: 99
    unit: unit:PERCENT
  conditions: European efficiency, value printed across the 155TL3/165TL3 columns
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=16.r3
    h: 8d611fd71e71
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions); possible conflict with c10 (same source; check the conditions);
    possible conflict with c11 (same source; check the conditions); possible conflict with c12 (same source;
    check the conditions)
---
The KACO blueplanet 87.0-165 TL3 is a family of three-phase string inverters made by KACO, with models from 87.0 TL3 up to 165 TL3. Each model is sold in order variants with their own KACO article numbers, for example the 110 TL3 M1 WM OD IIK0 and IIKX. Each inverter has a single MPP tracker. Maximum efficiency is listed as 98.8 percent for the 105TL3 and 99.1 percent for the 125 TL3 US. For communication the inverters use TCP/IP, Modbus TCP and SunSpec. The DC input has overvoltage protection but no polarity safeguard and no string fuses, so check string polarity before you connect. Grid monitoring is set per country. The unit shows its status on LEDs and has an aluminium housing. Installation is meant to be done by an authorised electrician. If the grid fuse trips, the manual points to possible hardware damage and says to contact KACO Service.

<!-- review notes
- sentence 1: support check: partial - Models 87.0 to 165 TL3 and KACO name are listed, but 'three-phase string inverters' is not stated in the passage (TL3 only implied).
- sentence 5: support check: partial - Overvoltage protection yes, no polarity safeguard, no string fuse are stated; the advice to check polarity is not in the passages.
- sentence 7: support check: partial - Fault row supports the grid fuse/hardware damage/contact Service; the heading only shows the manual is for an authorised electrician, installation not explicitly stated.
-->
