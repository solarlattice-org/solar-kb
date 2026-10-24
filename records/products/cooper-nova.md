---
id: prod:cooper-nova
type: Product
name: Cooper NOVA recloser
aliases:
- NOVA 15 27 38
- NOVA recloser
- Type NOVA recloser
- NOVA 15
- NOVA 27
- NOVA 38
category: Protection and BOS
make: cooper
product_level: family
claims:
- claim_id: c1
  attr: operating_temperature
  value:
    min: -40
    max: 55
    unit: unit:DEG_C
  conditions: Rated operating temperature range of the recloser
  cite:
  - src: src:eq-equip-relays-reclosers-cooper-nova-15-27-38-s280421
    loc: sec=h19
    h: a49db2084948
  review: drafted
- claim_id: c2
  attr: nominal_voltage
  value:
    max: 34.5
    unit: unit:KiloV
  conditions: Distribution system voltage the recloser is designed for (through 34.5 kV)
  cite:
  - src: src:eq-equip-relays-reclosers-cooper-nova-15-27-38-s280421
    loc: sec=h19
    h: a49db2084948
  review: drafted
- claim_id: c3
  attr: nominal_voltage
  value:
    nominal: 120
    unit: unit:V
  conditions: Auxiliary-powered interface supply option, AC; normal current 0.2 A, operating current 1.0
    A for 3 s, recommended power 150 VA
  cite:
  - src: src:eq-equip-relays-reclosers-cooper-nova-15-27-38-s280421
    loc: tbl=7.r1
    h: 45d4bf9158f5
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions);
    possible conflict with c7 (same source; check the conditions)
- claim_id: c4
  attr: nominal_voltage
  value:
    nominal: 240
    unit: unit:V
  conditions: Auxiliary-powered interface supply option, AC; normal current 0.1 A, operating current 0.5
    A for 3 s, recommended power 150 VA
  cite:
  - src: src:eq-equip-relays-reclosers-cooper-nova-15-27-38-s280421
    loc: tbl=7.r2
    h: ae0c4c5c7380
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions);
    possible conflict with c7 (same source; check the conditions)
- claim_id: c5
  attr: nominal_voltage
  value:
    nominal: 48
    unit: unit:V
  conditions: Auxiliary-powered interface supply option, DC; normal current 0.4 A, operating current 2.0
    A for 3 s, recommended power 150 VA
  cite:
  - src: src:eq-equip-relays-reclosers-cooper-nova-15-27-38-s280421
    loc: tbl=7.r3
    h: 9f298476221b
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions);
    possible conflict with c7 (same source; check the conditions)
- claim_id: c6
  attr: nominal_voltage
  value:
    nominal: 125
    unit: unit:V
  conditions: Auxiliary-powered interface supply option, DC; normal current 0.2 A, operating current 1.0
    A for 3 s, recommended power 150 VA
  cite:
  - src: src:eq-equip-relays-reclosers-cooper-nova-15-27-38-s280421
    loc: tbl=7.r4
    h: 1fc12c6a40b5
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c7 (same source; check the conditions)
- claim_id: c7
  attr: nominal_voltage
  value:
    nominal: 250
    unit: unit:V
  conditions: Auxiliary-powered interface supply option, DC; normal current 0.1 A, operating current 0.5
    A for 3 s, recommended power 150 VA
  cite:
  - src: src:eq-equip-relays-reclosers-cooper-nova-15-27-38-s280421
    loc: tbl=7.r5
    h: 692d562be721
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c6 (same source; check the conditions)
---
The Cooper NOVA is a three-phase, microprocessor-controlled vacuum-interrupting recloser for distribution systems up to 34.5 kV, offered as NOVA 15, NOVA 27 and NOVA 38. It uses three solid-polymer interrupter modules with an embedded current transformer and an aluminum mechanism housing, and its insulation needs no gas, liquid or foam dielectric. It is rated for operation from -40°C to +55°C and resists ozone, moisture, contamination and ultraviolet light. Two mechanism interface options exist: control-powered and auxiliary-powered; the auxiliary interface accepts 120 or 240 VAC, or 48, 125 or 250 VDC supplies with 150 VA recommended power. The recloser is designed and tested to work with Cooper Power Systems control types. Check the data plate ratings against the system at the point of application before installation; BIL rating depends on serial number. Its minimum mechanical life is 10,000 operations, and it should be inspected every ten years for physical damage and proper operation.

<!-- review notes
- sentence 1: support check: partial - Three-phase, vacuum, through 34.5 kV, microprocessor-controlled and NOVA 15/27/38 are stated, but 'offered as' is only via title; acceptable core though microprocessor-controlled is only in the title. Models listed in title; mostly supported but the 'recloser itself microprocessor-controlled' is slightly loose.
-->
