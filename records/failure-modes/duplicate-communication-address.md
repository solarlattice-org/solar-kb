---
id: fm:duplicate-communication-address
type: FailureMode
name: Duplicate device bus address
aliases:
- inverter address conflict
- Modbus slave address
- set address
- default address 1
- Duplicate communication address
- Physical address conflict
- Addr-Conflict
claims:
- claim_id: c1
  rel: presents_as
  target: symptom:communication-loss
  note: When two devices on an RS485 bus share an address, neither one communicates, and the whole serial
    bus may behave unpredictably.
  cite:
  - src: src:alsoenergy-alsoenergy-installation-manual-pv-rev-15-1
    loc: sec=4.2.4
    h: 6f538ee4b1bf
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: sec=h21
    h: adb70cddef2a
  review: drafted
- claim_id: c2
  rel: presents_as
  target: symptom:address-conflict-alarm
  note: Solis parallel systems report this as Addr-Conflict (code 1064).
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r5
    h: 41aeb940851d
  - src: src:kb-solis-44002781192-full-alarm-code-maintenance-overview
    loc: sec=h11
    h: ee2da61a2b27
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=32.r4
    h: 1b1cc7a64c58
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=21.r3
    h: 573075c41ee2
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r5
    h: 41aeb940851d
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:monitoring-gateway
  note: The address must not match any other device or the data logger on the bus.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=44.r14
    h: 26350ed1ccff
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: sec=6.3.2
    h: ca868a3501fd
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:energy-meter
  note: Meters on a Modbus network also need a unique slave ID.
  cite:
  - src: src:sel-735-im-20250228
    loc: sec=h1095
    h: 091dea4e2116
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:inverter-settings-review
  note: Check whether two or more units have been given the same address.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r5
    h: 41aeb940851d
  - src: src:kb-solis-44002781192-full-alarm-code-maintenance-overview
    loc: sec=h11
    h: ee2da61a2b27
  review: drafted
  review_note: 'support check: partial - u4 says to check whether units share an address, but it doesn''t
    name inverter settings review as a detection method; it is a parallel-system check.'
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  note: Restart only if the fault remains after the addresses have been checked.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r5
    h: 41aeb940851d
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Contact service if the fault persists after a restart.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r5
    h: 41aeb940851d
  review: drafted
---
Every inverter, meter or logger on a shared Modbus RS485 bus needs its own slave address, and this failure happens when two devices are given the same one. When addresses clash, neither device communicates properly and the master may lose contact with the whole bus. Some inverters raise a specific alarm, such as Addr-Conflict in Solis parallel systems. Some inverters ship with the same default address, so units on a multi-inverter site must be readdressed during setup. To confirm, read the address setting on each device on the bus and look for duplicates. To fix it, give each device a unique address within its allowed range, following the site design package if there is one. If the alarm stays after readdressing, restart the inverter, and contact the manufacturer if it still persists.

<!-- review notes
- sentence 4: support check: partial - Passages say the default address is 01 and addresses are set for multi-inverter setups, but they don't say that units must be readdressed because they ship identical (that is implied only).
- sentence 5: support check: partial - Passages say to check whether machines share an address, but reading each device's address setting on the bus isn't explicitly stated.
- sentence 4: review: partial - The passages give the default address as 01 and say to set addresses when multiple inverters share one monitor, but they never say units must be readdressed because they ship with identical addresses; that is only implied.
-->
