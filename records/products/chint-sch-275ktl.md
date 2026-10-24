---
id: prod:chint-sch-275ktl
type: Product
name: CPS SCH275KTL-DO/US-800
aliases:
- SCH 275 KTL
- SCH 275 KTL DO US 800
category: Inverters
make: chint
product_level: family
claims:
- claim_id: c1
  attr: efficiency
  value:
    nominal: 99
    unit: unit:PERCENT
  conditions: Maximum (peak) efficiency
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=30.r27
    h: 7bf9799bd66d
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c2
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: CEC weighted efficiency
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=30.r28
    h: 308e98811e53
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions)
- claim_id: c3
  attr: nominal_voltage
  value:
    nominal: 800
    unit: unit:V
  conditions: Rated AC output voltage
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=30.r15
    h: 77dfbb5a4343
  review: drafted
- claim_id: c4
  attr: rated_output_current
  value:
    max: 198.5
    unit: unit:A
  conditions: Maximum AC output current at 800 Vac
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=30.r18
    h: 5dbf98bbf34e
  review: drafted
- claim_id: c5
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated output frequency
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=30.r19
    h: 978e6a72810c
  review: drafted
- claim_id: c6
  attr: frequency
  value:
    min: 57
    max: 63
    unit: unit:HZ
  conditions: Output frequency range
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=30.r20
    h: 7a301219758d
  review: drafted
- claim_id: c7
  attr: max_input_voltage
  value:
    max: 1500
    unit: unit:V
  conditions: Maximum DC input voltage
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=30.r2
    h: b311604ea759
  review: drafted
- claim_id: c8
  attr: operating_temperature
  value:
    min: -30
    max: 60
    unit: unit:DEG_C
  conditions: Ambient operating range; output derates above 42 °C
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=30.r33
    h: a9317be5d2e4
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:ul-1741-sa
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=31.r15
    h: a18eab499322
  review: drafted
- claim_id: c10
  rel: certified_to
  target: std:ul-1741-sb
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=31.r15
    h: a18eab499322
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:ieee-1547a-2014
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=31.r15
    h: a18eab499322
  review: drafted
- claim_id: c12
  rel: certified_to
  target: std:ieee-1547-2018
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=31.r15
    h: a18eab499322
  review: drafted
- claim_id: c13
  rel: certified_to
  target: std:fcc-part-15
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=31.r15
    h: a18eab499322
  review: drafted
- claim_id: c14
  rel: uses_protocol
  target: proto:modbus
  note: Modbus over RS-485
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: sec=4.2.5
    h: 4945869bea07
  review: drafted
- claim_id: c15
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: sec=4.2.5
    h: 4945869bea07
  review: drafted
- claim_id: c16
  rel: uses_protocol
  target: proto:ethernet
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: sec=4.2.5
    h: 4945869bea07
  review: drafted
- claim_id: c17
  rel: uses_protocol
  target: proto:can-bus
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: sec=4.2.5
    h: 4945869bea07
  review: drafted
- claim_id: c18
  rel: uses_protocol
  target: proto:power-line-communication
  note: AC-PLC mode needs the CPS AC-PLC kit accessory
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: sec=4.2.5
    h: 4945869bea07
  review: drafted
- claim_id: c19
  rel: requires
  target: prod:chint-ac-plc-kit
  conditions: Only when AC-PLC communication is used
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: sec=4.2.5
    h: 4945869bea07
  review: drafted
- claim_id: c20
  rel: implements
  target: func:surge-protection
  note: Type II surge protection on both DC and AC sides
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=30.r11
    h: 6b685f8dcbea
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=30.r25
    h: 7a9a3614db00
  review: drafted
- claim_id: c21
  rel: implements
  target: func:remote-firmware-update
  conditions: With FlexOM gateway
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=31.r6
    h: a836860653de
  review: drafted
- claim_id: c22
  rel: compatible_with
  target: prod:chint-flexom-gateway
  conditions: Used for remote diagnostics and firmware upgrade
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=31.r6
    h: a836860653de
  review: drafted
- claim_id: c23
  rel: has_hazard
  target: hazard:electric-shock
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: sec=h15
    h: 70edc0df020e
  review: drafted
---
The CPS SCH275KTL-DO/US-800 is a transformerless string inverter family. Its AC output is rated at 800 Vac and 60 Hz. It accepts up to 1500 V DC input and operates between 500 and 1450 VDC. Maximum AC output current is 198.5 A at 800 Vac. Peak efficiency is 99.0 percent and CEC efficiency is 98.5 percent. Power factor is adjustable to plus or minus 0.8. It runs from -30 °C to 60 °C ambient and derates above 42 °C. Cooling is by variable speed fans. It communicates over Modbus RS-485, Ethernet, CAN and AC-PLC. AC-PLC needs the CPS AC-PLC kit accessory. Remote diagnostics and firmware upgrades use the FlexOM gateway. Alarm CommErr means communication inside the inverter failed, usually because of poor contact at the internal communication terminal blocks. Alarm ExtFanErr points to a blocked, worn-out or poorly connected fan. First wait five minutes, then check the fan blades for foreign objects. If it persists, reboot with the three-phase supply off and call CPS service.

<!-- review notes
- sentence 1: support check: partial - 800 Vac and 60 Hz supported, but transformerless string inverter is not stated in the passages.
- sentence 6: support check: partial - Definition and poor-contact cause are stated, but 'usually' and the internal communication terminal blocks are slightly paraphrased; essentially supported.
-->
