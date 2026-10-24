---
id: prod:sma-data-manager-m
type: Product
name: SMA Data Manager M
aliases:
- Data Manager M
- EDMM
- EDMM-10
- EDMM-US-10
- EDMM-20
- ennexOS Data Manager M
category: Monitoring and communications
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-kb-data-manager-manuals
    loc: sec=h1
    h: ad52815d2887
  - src: src:sma-edmx-modbus-ti-en-16
    loc: sec=1.1
    h: bdd527e918d5
  review: drafted
  review_note: 'support check: partial - Passages show the product name and SMA-branded manuals/service
    site, but never explicitly state SMA makes it; implied by naming only.'
- claim_id: c2
  rel: instance_of
  target: comp:monitoring-gateway
  cite:
  - src: src:sma-kb-what-is-the-difference-between-the-sma-data-manager-m-sma-energy-meter-and-the-sma
    loc: sec=h1
    h: d19c74c9d3ae
  review: drafted
- claim_id: c3
  attr: max_count
  value:
    max: 50
    unit: unit:NUM
  conditions: Devices per Data Manager M; larger systems need several Data Managers M in master/slave
    configuration
  cite:
  - src: src:sma-kb-can-i-represent-more-than-50-devices-in-a-system
    loc: sec=h1
    h: 1f78c654d034
  review: drafted
- claim_id: c4
  attr: max_count
  value:
    max: 20
    unit: unit:NUM
  conditions: SMA eChargers (charging points) via Modbus TCP, monitoring only, EDMM-20
  cite:
  - src: src:sma-kb-compatibility-sma-echarger-and-sma-data-manager-m
    loc: sec=h1
    h: 0f753c82108d
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:modbus-tcp
  cite:
  - src: src:sma-kb-compatibility-sma-echarger-and-sma-data-manager-m
    loc: sec=h1
    h: 0f753c82108d
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:sunspec-modbus
  note: Sunny Tripower CORE2 is controlled and monitored via SunSpec Modbus profile with Unit ID 1
  cite:
  - src: src:sma-kb-registering-sunny-tripower-core2-in-sma-data-manager-m
    loc: sec=h1
    h: a17fc3cdf3cc
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:speedwire
  cite:
  - src: src:sma-kb-edmm-us-10-quick-start-guide
    loc: sec=h1
    h: dbd13d67d997
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:sma-kb-sma-data-manager-m-connecting-rs485-devices
    loc: sec=h1
    h: 72486a9ae0ea
  - src: src:sma-kb-can-each-rs485-device-connected-to-an-sma-com-gateway-be-used-with-the-data-manager
    loc: sec=h1
    h: 6fa992734eac
  review: drafted
- claim_id: c9
  rel: uses_protocol
  target: proto:wifi
  note: Soft access Wi-Fi for local commissioning login
  cite:
  - src: src:sma-kb-edmm-us-10-quick-start-guide
    loc: sec=h1
    h: dbd13d67d997
  review: drafted
- claim_id: c10
  rel: compatible_with
  target: prod:sma-sunny-tripower-core2
  cite:
  - src: src:sma-kb-registering-sunny-tripower-core2-in-sma-data-manager-m
    loc: sec=h1
    h: a17fc3cdf3cc
  review: drafted
- claim_id: c11
  rel: compatible_with
  target: prod:sma-com-gateway
  note: Compatible RS485 devices behind a Com Gateway can be used; SMA Meteo Station only with restrictions
  cite:
  - src: src:sma-kb-can-each-rs485-device-connected-to-an-sma-com-gateway-be-used-with-the-data-manager
    loc: sec=h1
    h: 6fa992734eac
  review: drafted
- claim_id: c12
  rel: compatible_with
  target: prod:sma-echarger
  scope:
    firmware_min: 2.5.9.R
  conditions: Monitoring only, no control; eCharger and Data Manager M firmware 2.5.9.R or later; EDMM-20
  cite:
  - src: src:sma-kb-compatibility-sma-echarger-and-sma-data-manager-m
    loc: sec=h1
    h: 0f753c82108d
  review: drafted
- claim_id: c13
  rel: incompatible_with
  target: prod:sma-sunny-sensorbox
  cite:
  - src: src:sma-kb-can-each-rs485-device-connected-to-an-sma-com-gateway-be-used-with-the-data-manager
    loc: sec=h1
    h: 6fa992734eac
  review: drafted
- claim_id: c14
  rel: supersedes
  target: prod:sma-data-manager-m-lite
  note: EDMM-10.A discontinued; EDMM-10 named as alternative and substitute
  cite:
  - src: src:sma-kb-discontinuation-data-manager-m-lite
    loc: sec=h1
    h: eb0e815b0a9c
  review: drafted
  review_note: 'support check: partial - M Lite discontinued and EDMM-10 named as alternative/substitute,
    but ''supersedes'' is not stated exactly.'
- claim_id: c15
  rel: implements
  target: func:volt-var
  note: Reactive power as a function of grid voltage, Q(U)
  cite:
  - src: src:sma-kb-sma-data-manager-m-configuring-reactive-power-as-a-function-of-grid-voltage
    loc: sec=h1
    h: 4d5c59565369
  - src: src:sma-kb-measuring-voltage-by-using-energy-meter-for-q-u
    loc: sec=h1
    h: 7dadb4dcf6b6
  review: drafted
  review_note: 'support check: partial - Articles refer to configuring reactive power as function of grid
    voltage in the manual; implies support but sparse and no explicit Volt-VAr statement.'
- claim_id: c16
  rel: implements
  target: func:closed-loop-plant-control
  note: Only a Data Manager M in master mode performs control
  cite:
  - src: src:sma-kb-measuring-voltage-by-using-energy-meter-for-q-u
    loc: sec=h1
    h: 7dadb4dcf6b6
  - src: src:sma-kb-can-i-represent-more-than-50-devices-in-a-system
    loc: sec=h1
    h: 1f78c654d034
  review: drafted
- claim_id: c17
  rel: implements
  target: func:remote-firmware-update
  note: Updates firmware of connected SMA products
  cite:
  - src: src:sma-kb-sma-data-manger-m-updating-the-firmware-of-connected-sma-products
    loc: sec=h1
    h: c59c8996f09d
  review: drafted
- claim_id: c18
  rel: implements
  target: func:digital-input-power-reduction
  note: Transfer of power specifications via pulse signals
  cite:
  - src: src:sma-doc-273430
    loc: sec=h1
    h: 37b8afe6824d
  review: drafted
  review_note: 'support check: partial - Only a title ''Transfer of power specifications via pulse signals''
    for EDMM; no explicit digital-input power reduction detail.'
---
The SMA Data Manager M (EDMM) is a data logger that reports to the ennexOS portal, which is the successor of Sunny Portal. Each Data Manager M handles up to 50 devices. Bigger systems use several units, with one set as master and the others as slaves, and the total system power may not exceed 2.5 MVA; above that a Data Manager L must be the master. Only one measuring device is supported at the point of interconnection. That energy meter must be assigned to the master unit, and only the master can do control. It talks to SMA devices over Speedwire, to RS485 devices, and to Modbus devices such as the Sunny Tripower CORE2 using the SunSpec Modbus profile with Unit ID 1. From firmware 2.5.9.R, the EDMM-20 can monitor up to 20 SMA eChargers over Modbus TCP, but it cannot control them. It supports Q(U) reactive power control, power setpoints sent as pulse signals, a WAGO 750 I/O system, and firmware updates of connected SMA products. The Sunny SensorBox, Windy Boy, Hydro Boy and SolTrk are not supported. Function button: hold 5 to 10 seconds to restart, 10 to 15 seconds to reset the admin account, and 15 to 20 seconds to restore factory settings, which erases all data. If the user interface shows no data, the real-time clock buffer capacitor may have discharged after a long time without power, so check that the unit can reach an internet time server.

<!-- review notes
- sentence 6: support check: partial - Q(U), pulse signals and firmware updates are covered; WAGO 750 I/O system is only listed as a document validity, support implied.
-->
