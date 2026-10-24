---
id: prod:chint-sch-125ktl-aio
type: Product
name: CPS SCH125KTL-AIO/US-600
aliases:
- SCH 125 KTL AIO
- SCH 125 KTL AIO US 600
- SCH125KTL-AIO/US-600
category: Inverters
make: chint
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:chint
  note: Marketed under the CPS brand as part of the CPS SCH Series of grid-tied PV inverters.
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: sec=h1
    h: 17470d9f00c3
  review: drafted
  review_note: 'support check: partial - Passage shows the CPS SCH Series product name but does not state
    the manufacturer is CHINT POWER SYSTEMS.'
- claim_id: c2
  attr: rated_power
  value:
    nominal: 125
    unit: unit:KiloW
  conditions: Rated AC output power
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=37.r11
    h: 63b192d37055
  review: drafted
- claim_id: c3
  attr: max_input_voltage
  value:
    nominal: 1500
    unit: unit:V
  conditions: Maximum DC input voltage, ungrounded array
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=37.r3
    h: 3a9d58a9a56a
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=37.r1
    h: b3d2c8633e55
  review: drafted
- claim_id: c4
  attr: nominal_voltage
  value:
    nominal: 600
    unit: unit:V
  conditions: Rated AC output voltage
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=37.r13
    h: b7ee123387c1
  review: drafted
- claim_id: c5
  attr: rated_output_current
  value:
    nominal: 120.4
    unit: unit:A
  conditions: Maximum AC current at 125 kVA
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=37.r16
    h: f5a7d4e57113
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions)
- claim_id: c6
  attr: rated_output_current
  value:
    nominal: 127.2
    unit: unit:A
  conditions: Maximum AC current at 132 kVA
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=37.r16
    h: f5a7d4e57113
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c7
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated output frequency
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=37.r17
    h: '883824011282'
  review: drafted
- claim_id: c8
  attr: efficiency
  value:
    nominal: 99
    unit: unit:PERCENT
  conditions: Maximum (peak) efficiency
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=37.r24
    h: 1f23481f24cd
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c9
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: CEC weighted efficiency
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=37.r25
    h: 05a0e497c271
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c10
  rel: compatible_with
  target: arch:ungrounded-pv-array
  note: DC input is specified for an ungrounded array.
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=37.r1
    h: b3d2c8633e55
  review: drafted
- claim_id: c11
  rel: implements
  target: func:constant-power-factor
  note: Power factor above 0.99, adjustable to plus or minus 0.8.
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=37.r19
    h: 14255a5f7bdd
  review: drafted
- claim_id: c12
  rel: implements
  target: func:remote-firmware-update
  note: Remote diagnostics and firmware upgrade are standard with the CPS Flex Gateway.
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=38.r13
    h: 0d4b8e53d07f
  review: drafted
- claim_id: c13
  rel: requires
  target: prod:chint-flexom-gateway
  conditions: For remote diagnostics and firmware upgrade functions
  note: Datasheet names it the CPS Flex Gateway.
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=38.r13
    h: 0d4b8e53d07f
  review: drafted
  review_note: 'support check: partial - Passage says standard with CPS Flex Gateway, not that it requires
    it, and FlexOM naming is not in passage.'
- claim_id: c14
  rel: uses_protocol
  target: proto:sunspec-modbus
  note: Modbus data mapping is SunSpec or CPS proprietary.
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=38.r12
    h: 3bbde4636255
  review: drafted
- claim_id: c15
  rel: uses_protocol
  target: proto:modbus
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=38.r12
    h: 3bbde4636255
  review: drafted
- claim_id: c16
  rel: certified_to
  target: std:ieee-1547a-2014
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=38.r20
    h: 077c0d63279e
  review: drafted
- claim_id: c17
  rel: certified_to
  target: std:ieee-1547-2003
  note: Listed as IEEE 1547-2003 (R2008).
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=38.r20
    h: 077c0d63279e
  review: drafted
- claim_id: c18
  rel: certified_to
  target: std:ieee-1547-1-2005
  note: Listed as IEEE 1547.1-2005 (R2011).
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=38.r20
    h: 077c0d63279e
  review: drafted
- claim_id: c19
  rel: certified_to
  target: std:ieee-1547-1a-2015
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=38.r20
    h: 077c0d63279e
  review: drafted
- claim_id: c20
  rel: certified_to
  target: std:cpuc-rule-21
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=38.r20
    h: 077c0d63279e
  review: drafted
- claim_id: c21
  rel: certified_to
  target: std:ul-1741-sa
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=38.r20
    h: 077c0d63279e
  review: drafted
---
The CPS SCH125KTL-AIO/US-600 is a grid-tied, transformerless three-phase string inverter from the CPS SCH Series, rated 125 kW AC output. It takes up to 1500 Vdc from an ungrounded PV array through 20 DC inputs, and feeds a 600 Vac, 60 Hz grid with a permitted output range of 528 to 660 Vac. Maximum AC current is 120.4 A at 125 kVA or 127.2 A at 132 kVA. Peak efficiency is 99.0% and CEC efficiency is 98.5%. Power factor is above 0.99 and can be adjusted to plus or minus 0.8. Current THD is below 3%. The inverter has no integrated AC disconnect, uses variable-speed cooling fans, and has LED indicators and an app as its user interface. Modbus data mapping is SunSpec or CPS proprietary. Remote diagnostics and firmware upgrades are standard when used with the CPS Flex Gateway. Listed grid standards include IEEE 1547-2003, IEEE 1547a-2014, IEEE 1547.1-2005, IEEE 1547.1a-2015, CA Rule 21, UL 1741 SA and ISO-NE. Alarm codes include CommErr, meaning communication inside the inverter has failed, and ExtFanErr, meaning a cooling fan failure found by visual check.

<!-- review notes
- sentence 1: support check: partial - Transformerless, 125kW and SCH series supported, but three-phase and string inverter are not stated.
-->
