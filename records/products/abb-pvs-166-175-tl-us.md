---
id: prod:abb-pvs-166-175-tl-us
type: Product
name: FIMER PVS-166/175-TL-US string inverter
aliases:
- PVS-166-TL-US
- PVS-175-TL-US
- PVS-166-175-TL-US
- PVS-166/175-TL-US
category: Inverters
make: abb
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:fimer
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: fig=51
    h: febe2b4c4aee
  review: drafted
  review_note: 'support check: partial - The evidence is only a manual title naming FIMER and the product;
    it implies but does not state manufacturer.'
- claim_id: c2
  attr: rated_power
  value:
    nominal: 175000
    unit: unit:W
  conditions: PVS-175-TL US model, rated AC power at cosφ=1 and 40°C
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=9.r25
    h: f8b68fd6fbfb
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-quick-installation-guide-reve
    loc: tbl=23.r24
    h: fbb2f466bee8
  review: drafted
- claim_id: c3
  attr: nominal_voltage
  value:
    nominal: 800
    unit: unit:V
  conditions: Rated AC grid voltage, both models
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=9.r28
    h: 6a86f3ad90a5
  review: drafted
- claim_id: c4
  attr: efficiency
  value:
    nominal: 98.6
    unit: unit:PERCENT
  conditions: Maximum (peak) efficiency
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=9.r43
    h: 5606429953bb
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-quick-installation-guide-reve
    loc: tbl=23.r42
    h: 00ff82ea66b5
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:modbus-rtu
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=10.r4
    h: f6b57076a012
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:modbus-tcp
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=10.r4
    h: f6b57076a012
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:sunspec-modbus
  note: Modbus implementation stated as SunSpec compliant; also used for remote parameter upgrade
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=10.r4
    h: f6b57076a012
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=10.r8
    h: f2d5c9d69c73
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:ethernet
  note: Remote inverter parameter upgrade via Ethernet/WLAN
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=10.r8
    h: f2d5c9d69c73
  review: drafted
- claim_id: c9
  rel: uses_protocol
  target: proto:wifi
  note: Wi-Fi connection required to change grid settings through the internal webserver
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=10.r8
    h: f2d5c9d69c73
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=7.5
    h: c4b5570a38df
  review: drafted
- claim_id: c10
  rel: implements
  target: func:string-monitoring
  note: Current sensing at MPPT level rather than per string
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=9.r22
    h: a3a66281271f
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-quick-installation-guide-reve
    loc: tbl=23.r21
    h: fce07ebc6485
  review: drafted
- claim_id: c11
  rel: implements
  target: func:voltage-ride-through
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=7.5
    h: c4b5570a38df
  review: drafted
- claim_id: c12
  rel: implements
  target: func:frequency-ride-through
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=7.5
    h: c4b5570a38df
  review: drafted
- claim_id: c13
  rel: implements
  target: func:voltage-trip
  note: Disconnects from grid after programmed delay on abnormal voltage
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=7.5
    h: c4b5570a38df
  review: drafted
- claim_id: c14
  rel: implements
  target: func:frequency-trip
  note: Disconnects after programmed delay on frequency excursion
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=7.5
    h: c4b5570a38df
  review: drafted
- claim_id: c15
  rel: implements
  target: func:constant-power-factor
  note: Cosφ set mode; default reactive power setting is disabled (unity power factor)
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=7.5
    h: c4b5570a38df
  review: drafted
- claim_id: c16
  rel: implements
  target: func:constant-reactive-power
  note: Q Set mode
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=7.5
    h: c4b5570a38df
  review: drafted
- claim_id: c17
  rel: implements
  target: func:watt-power-factor
  note: Cosφ(P) with a 4-point curve adjustable via webserver
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=7.5
    h: c4b5570a38df
  review: drafted
- claim_id: c18
  rel: implements
  target: func:volt-var
  note: Q(V) with a 4-point curve adjustable via webserver
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=7.5
    h: c4b5570a38df
  review: drafted
---
The FIMER PVS-166/175-TL-US is a three-phase string inverter family made up of the PVS-166-TL US and PVS-175-TL US models. At unity power factor and 40°C, the PVS-166-TL US is rated 166 500 W of AC output and the PVS-175-TL US 175 000 W. Both connect to an 800 V rated AC grid. Maximum efficiency is 98.6 percent. Current is monitored per MPPT, not per individual string. For communication it uses SunSpec-compliant Modbus RTU and Modbus TCP. Inverter parameters can be upgraded remotely over Ethernet or WLAN using SunSpec Modbus. Its grid support functions are voltage and frequency ride-through with trip limits, fixed power factor, fixed reactive power, power factor as a function of output power, and Volt/VAr control. Reactive power control is disabled by default, so the inverter runs at unity power factor. To change grid settings in the internal webserver, you need a Wi-Fi connection to the inverter.

<!-- review notes
- sentence 1: support check: partial - The two models are evidenced, but 'three-phase' and 'string inverter' are not stated in the passages.
-->
