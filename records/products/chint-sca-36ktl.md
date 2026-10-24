---
id: prod:chint-sca-36ktl
type: Product
name: CPS SCA36KTL-DO/US-480
aliases:
- SCA 36 KTL
- CPS 36 KTL
- CPS 36 kW
- Chint/36 kW
- CPS SCA36KTL-DO/US
- SCA36KTL-DO/US480
- SCA36KTL
category: Inverters
make: chint
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:chint
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: sec=h3
    h: a26f41a35a31
  - src: src:chint-cps-25-350kw-advanced-inverter-functionality-may-2026
    loc: sec=h2
    h: df81c0a3ffb4
  review: drafted
- claim_id: c2
  rel: subclass_of
  target: prod:chint-sca-50-60ktl
  note: The 36 kW model shares one user manual with the 50 and 60 kW SCA models; this is a shared-family
    link, not a strict parent record.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=h8
    h: f6f557299e04
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: sec=h1
    h: ee2226d9a024
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:modbus
  note: Industry standard Modbus over RS485
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=3.3.3
    h: 7cc772fcde58
  - src: src:chint-cps-36kw-user-manual-2024
    loc: sec=3.3.3
    h: 7cc772fcde58
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=3.3.3
    h: 7cc772fcde58
  - src: src:chint-cps-36kw-user-manual-2024
    loc: sec=3.3.3
    h: 7cc772fcde58
  review: drafted
- claim_id: c5
  rel: certified_to
  target: std:ul-1741-sa
  note: Listed as UL1741-SA Ed. 3
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=67.r28
    h: 8b1c54e66831
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c6
  rel: certified_to
  target: std:ul-1699b
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=67.r28
    h: 8b1c54e66831
  review: drafted
- claim_id: c7
  rel: certified_to
  target: std:ul-1998
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=67.r28
    h: 8b1c54e66831
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: certified_to
  target: std:ieee-1547-2018
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=67.r28
    h: 8b1c54e66831
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:fcc-part-15
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=67.r28
    h: 8b1c54e66831
  review: drafted
- claim_id: c10
  attr: rated_power
  value:
    nominal: 36
    unit: unit:KiloW
  conditions: Rated AC output power; maximum AC output power also given as 36 kW (36 kW user manual)
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=44.r14
    h: d99f5bbe8525
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=44.r15
    h: 629c40f70c55
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c11
  attr: max_input_voltage
  value:
    nominal: 1000
    unit: unit:V
  conditions: Maximum DC input voltage
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=66.r3
    h: 18f1069ee478
  review: drafted
- claim_id: c12
  attr: rated_output_current
  value:
    nominal: 43.5
    unit: unit:A
  conditions: Maximum AC output current at 480 VAC
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=66.r18
    h: 3dc5ad7c6679
  review: drafted
  review_note: 'support check: partial - 43.5A is the max AC output current at 480VAC; labeling it ''rated
    output current'' is a slight difference, though the condition notes it as maximum.'
- claim_id: c13
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Rated AC output voltage
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=66.r15
    h: 0463c0de3017
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=44.r16
    h: edeff6eb1664
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c14
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated output frequency
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=66.r20
    h: 163ac93a8a4a
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=44.r20
    h: 42933fe1b734
  review: drafted
---
The CPS SCA36KTL-DO/US-480 is a grid-tied three-phase PV string inverter from Chint Power Systems. It is covered in the same manual as the SCA50KTL and SCA60KTL models. It is rated for 36 kW AC output at a nominal 480 VAC and 60 Hz, with a maximum AC output current of 43.5 A. Maximum DC input voltage is 1000 VDC. The operating DC input range is 200 to 950 VDC. Power factor is above 0.99 and can be adjusted to ±0.8. The output voltage range is 422 to 528 VAC, and current THD is below 3%. Monitoring and control use industry standard Modbus over RS485, wired through the communication board. Known alarms include Arcboard Err, which can come from poor contact or damage on the arc board, and EepromErr, which indicates a problem with internal memory.

<!-- review notes
- sentence 1: support check: partial - Shared manual with SCA50/60 and CPS maker are shown, but 'grid-tied three-phase PV string inverter' is supported only via 'Grid-tied PV Inverter' and the application note's '3Phs PV string inverters' list, which is loosely tied to this model.
- sentence 5: support check: partial - Modbus RS485 and a communication board are stated, but 'monitoring and control' use and wiring through the board are only loosely implied.
-->
