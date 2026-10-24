---
id: prod:chint-sca-50-60ktl
type: Product
name: CPS SCA50-60KTL-DO/US-480
aliases:
- SCA 50 60 KTL
- CPS 50 60 kW
- Chint/50 60 kW
- 50_60 Update firmware
- CPS SCA50KTL-DO/US-480
- CPS SCA60KTL-DO/US-480
category: Inverters
make: chint
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:chint
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=h3
    h: a26f41a35a31
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=h170
    h: ceaf75016dc5
  review: drafted
- claim_id: c2
  rel: certified_to
  target: std:ul-1741-sa
  note: Listed as UL1741-SA Ed. 3
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=67.r28
    h: 8b1c54e66831
  review: drafted
- claim_id: c3
  rel: certified_to
  target: std:ul-1699b
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=67.r28
    h: 8b1c54e66831
  review: drafted
- claim_id: c4
  rel: certified_to
  target: std:ul-1998
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=67.r28
    h: 8b1c54e66831
  review: drafted
- claim_id: c5
  rel: certified_to
  target: std:ieee-1547-2018
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=67.r28
    h: 8b1c54e66831
  review: drafted
- claim_id: c6
  rel: certified_to
  target: std:fcc-part-15
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=67.r28
    h: 8b1c54e66831
  review: drafted
- claim_id: c7
  rel: implements
  target: func:anti-islanding
  note: Uses bi-directional frequency perturbation
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=2.3
    h: 6bc1b385ebca
  review: drafted
- claim_id: c8
  rel: implements
  target: func:dc-arc-fault-protection
  note: Detection and circuit interruption
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=2.3
    h: 6bc1b385ebca
  review: drafted
- claim_id: c9
  rel: implements
  target: func:insulation-monitoring
  note: DC input insulation to ground monitoring
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=2.3
    h: 6bc1b385ebca
  review: drafted
- claim_id: c10
  rel: implements
  target: func:residual-current-monitoring
  note: Leakage current to ground monitoring
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=2.3
    h: 6bc1b385ebca
  review: drafted
- claim_id: c11
  rel: implements
  target: func:rapid-shutdown
  conditions: Only with RSD version wireboxes
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=2.3
    h: 6bc1b385ebca
  review: drafted
- claim_id: c12
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Rated AC output voltage, SCA50KTL and SCA60KTL
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=66.r15
    h: 0463c0de3017
  review: drafted
- claim_id: c13
  attr: rated_output_current
  value:
    nominal: 60.2
    unit: unit:A
  scope:
    products:
    - prod:chint-sca-50-60ktl
  conditions: SCA50KTL-DO/US-480, maximum AC output current at 480 VAC (first listed value)
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=66.r18
    h: 3dc5ad7c6679
  review: drafted
  review_note: 'support check: partial - 60.2A is the first listed max AC output current, but it is a
    maximum, not clearly a ''rated'' current; the statement''s condition does say maximum.'
- claim_id: c14
  attr: rated_output_current
  value:
    nominal: 66.2
    unit: unit:A
  conditions: SCA50KTL-DO/US-480, maximum AC output current at 480 VAC (second listed value)
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=66.r18
    h: 3dc5ad7c6679
  review: drafted
  review_note: 'support check: partial - 66.2A is the second listed max output current; its meaning as
    rated current is not stated.; possible conflict with c15 (same source; check the conditions); possible
    conflict with c16 (same source; check the conditions)'
- claim_id: c15
  attr: rated_output_current
  value:
    nominal: 72.2
    unit: unit:A
  conditions: SCA60KTL-DO/US-480, maximum AC output current at 480 VAC (first listed value)
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=66.r18
    h: 3dc5ad7c6679
  review: drafted
  review_note: 'support check: partial - 72.2A is the first listed max current for SCA60KTL; rated meaning
    not stated.; possible conflict with c14 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions)'
- claim_id: c16
  attr: rated_output_current
  value:
    nominal: 79.4
    unit: unit:A
  conditions: SCA60KTL-DO/US-480, maximum AC output current at 480 VAC (second listed value)
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=66.r18
    h: 3dc5ad7c6679
  review: drafted
  review_note: 'support check: partial - 79.4A is the second listed max current for SCA60KTL; rated meaning
    not stated.; possible conflict with c14 (same source; check the conditions); possible conflict with
    c15 (same source; check the conditions)'
---
The CPS SCA50KTL-DO/US-480 and SCA60KTL-DO/US-480 are three-phase string inverters for 480 V service, made by CHINT POWER SYSTEMS. The datasheet gives a rated AC output voltage of 480 VAC and a maximum efficiency of 98.8%. Maximum AC output current is 60.2A/66.2A for the 50 kW model and 72.2A/79.4A for the 60 kW model. Built-in protections include anti-islanding, DC arc-fault detection with interruption, insulation-to-ground monitoring and leakage current monitoring. The inverter also has extra kVA headroom so it can deliver full active power down to 0.91 PF. A neutral connection is not required, and a delta connection is allowed if an external AC GFCI is fitted. Rapid shutdown that meets NEC 2017/2020 is available only on the RSD versions of the wirebox. Firmware is upgraded through a USB port on the unit. Known alarms include Arcboard Err: check that the arc board connector is seated and run the Arc Fault Test. Another is EepromErr, an internal memory alarm: watch it for five minutes, then call service if it does not clear.

<!-- review notes
- sentence 1: support check: partial - Models, maker and 480 VAC are supported, but 'three-phase string inverter' is not stated in the passages.
- sentence 6: support check: partial - Figure caption indicates a USB port for firmware upgrades, but 'on the unit' and the process are only implied.
-->
