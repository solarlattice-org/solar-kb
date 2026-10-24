---
id: prod:chint-sca-25ktl-480
type: Product
name: CPS SCA25KTL-DO-R/US-480
aliases:
- SCA 25 KTL DO R US 480
- SCA 25 KTL DO R
category: Inverters
make: chint
product_level: family
claims:
- claim_id: c1
  attr: max_input_voltage
  value:
    nominal: 1000
    unit: unit:V
  conditions: Maximum DC input voltage, from the datasheet table
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=64.r3
    h: 024bd2795597
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=64
    h: 2eb30d32d328
  review: drafted
- claim_id: c2
  attr: mppt_voltage_range
  value:
    min: 560
    max: 850
    unit: unit:V
  conditions: MPPT voltage range, DC
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=64.r7
    h: 2024595ce3f1
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=64
    h: 2eb30d32d328
  review: drafted
- claim_id: c3
  rel: implements
  target: func:mppt
  note: Two MPP trackers, each with three DC inputs, for six DC inputs in total
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=64
    h: 2eb30d32d328
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=64.r6
    h: 376843339bf3
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:modbus
  note: Industry-standard Modbus over RS485
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: sec=3.5
    h: c620606826fc
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:rs485
  note: Wired through the communication board in the wire-box
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: sec=3.5
    h: c620606826fc
  review: drafted
- claim_id: c6
  rel: manufactured_by
  target: org:chint
  note: Sold under the CPS brand as part of the CPS SCA Series
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: sec=h1
    h: 6f93aaaf7a58
  review: drafted
  review_note: 'support check: partial - Passage only shows the CPS SCA Series manual title; it does not
    name CHINT POWER SYSTEMS as manufacturer.'
---
The CPS SCA25KTL-DO-R/US-480 is a grid-tied PV string inverter in the CPS SCA Series. Its maximum DC input voltage is 1000 VDC. Its operating DC input range is 200 to 950 VDC, and it starts up at 330 V and 80 W. It has two MPP trackers with an MPPT voltage range of 560 to 850 VDC. There are six DC inputs, three per tracker. Maximum PV power is 37.5 kW, with up to 22 kW per MPPT. Maximum PV short-circuit current is 45 A per MPPT. For monitoring, it supports standard Modbus over RS485, wired through the communication board in the wire-box.

<!-- review notes
- sentence 1: support check: partial - Titles show it is a CPS SCA Series grid-tied PV inverter, but 'string inverter' is not stated.
-->
