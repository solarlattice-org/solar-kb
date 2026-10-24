---
id: prod:sma-stp-x-us-50
type: Product
name: Sunny Tripower X US-50
aliases:
- Sunny Tripower X US
- STP X US
- STPxx US 50
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:kb-sma-stpxxus50-troubleshooting
    loc: sec=front
    h: 6d5d93525714
  - src: src:kb-sma-stpxxus50-modbus
    loc: sec=front
    h: 7e91c095964f
  review: drafted
- claim_id: c2
  rel: implements
  target: func:system-manager
  note: The operating manual shows a system in which a Sunny Tripower X 30-US is the SMA System Manager,
    with one energy meter.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=4.2.1
    h: 2fb4bf26fe97
  - src: src:sma-stpxx-us-50-be-en-14
    loc: tbl=1.r17
    h: 18db88256ce7
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:modbus
  note: The SMA manual for STP 13/20/25/30-US-50 has a Modbus section.
  cite:
  - src: src:kb-sma-stpxxus50-modbus
    loc: sec=front
    h: 7e91c095964f
  review: drafted
- claim_id: c4
  attr: nominal_voltage
  value:
    nominal: 208
    unit: unit:V
  conditions: STP 13-US-50 variant (Sunny Tripower X 13-US), as given in its designation
  cite:
  - src: src:sma-stpxx-us-50-is-xx-13
    loc: sec=h71
    h: 9b2637f8c2dc
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=1.1
    h: d1f9d61cd426
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h1
    h: 5d39b685c1ed
  review: drafted
---
The Sunny Tripower X US-50 is an SMA family of three-phase PV string inverters. It covers the STP 13-US-50, STP 20-US-50, STP 25-US-50 and STP 30-US-50. The STP 13-US-50 model is the 208 V version. The current operating manual applies to the STP 13-US-50 from firmware 3.14.22.R. It applies to the 20, 25 and 30 kW models from firmware 03.06.15.R. The STP 20-US-50, 25-US-50 and 30-US-50 can act as the SMA System Manager from firmware 03.02.07.R. The manual shows a system with a 30-US as System Manager and one energy meter. SMA's online manual for this family includes sections on Modbus, grid management services, grid types, LED signals, ground-fault checks, manual firmware updates and troubleshooting.

<!-- review notes
- sentence 1: support check: partial - The four models are listed as a family, but 'three-phase' and 'PV string inverters' are not stated (only 'Inverter'/'PV inverter').
- sentence 1: review: partial - The passages list the four models under Sunny Tripower X and call it an inverter, but they never say it is three-phase or a PV string inverter.
-->
