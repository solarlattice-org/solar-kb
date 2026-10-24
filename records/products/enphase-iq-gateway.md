---
id: prod:enphase-iq-gateway
type: Product
name: Enphase IQ Gateway
aliases:
- Envoy
- IQ Envoy
- Envoy-S
- IQ Gateway Commercial
- Envoy S Metered
- Envoy S Standard
- ENV-IQ-AM1-240
- IQ Gateway Commercial 2
- IQ Gateway Metered
- IQ Gateway Standard
category: Monitoring and communications
make: enphase
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:enphase
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5420
    loc: sec=front
    h: f47feb6a4ca7
  - src: src:kb-enphase-what-are-the-key-features-of-iq-gateway-commercial-pro
    loc: sec=front
    h: 654620442bcf
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:monitoring-gateway
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=1
    h: 50634e717f87
  review: drafted
- claim_id: c3
  rel: part_of
  target: prod:enphase-iq-combiner
  note: The IQ Gateway is included in IQ Combiner units.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: prod:enphase-iq8
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: prod:enphase-iq7
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=1
    h: 50634e717f87
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:enphase-iq-battery
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=1
    h: 50634e717f87
  review: drafted
- claim_id: c7
  rel: compatible_with
  target: prod:enphase-iq-system-controller
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:power-line-communication
  note: Collects microinverter production and performance data over the site AC power lines.
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=1
    h: 50634e717f87
  review: drafted
- claim_id: c9
  rel: uses_protocol
  target: proto:cellular
  note: Mobile Connect cellular modem plugs into a USB port on the gateway.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5263
    loc: tbl=1.r3
    h: 3730f00321da
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=1
    h: 50634e717f87
  review: drafted
- claim_id: c10
  rel: uses_protocol
  target: proto:wifi
  cite:
  - src: src:kb-enphase-reconnecting-an-iq-gateway-or-envoy-s-to-wi-fi-using-the-enphase-app
    loc: sec=h1
    h: ac3ac28424b3
  - src: src:kb-enphase-reconnecting-an-iq-gateway-or-envoy-s-to-wi-fi-using-the-enphase-app
    loc: sec=front
    h: 050f7ee173bb
  review: drafted
  review_note: 'support check: partial - Passages only show titles about reconnecting the gateway to Wi-Fi,
    and a wireless network connection; the title implies Wi-Fi but little detail.'
- claim_id: c11
  rel: uses_protocol
  target: proto:rs485
  note: Only the IQ Gateway Commercial Pro variant, for third-party energy meters.
  cite:
  - src: src:kb-enphase-what-are-the-key-features-of-iq-gateway-commercial-pro
    loc: sec=h1
    h: ca9195a2f2e9
  review: drafted
- claim_id: c12
  rel: uses_protocol
  target: proto:modbus
  note: Only the IQ Gateway Commercial Pro variant, for third-party meter integration over RS-485.
  cite:
  - src: src:kb-enphase-what-are-the-key-features-of-iq-gateway-commercial-pro
    loc: sec=h1
    h: ca9195a2f2e9
  review: drafted
- claim_id: c13
  rel: uses_protocol
  target: proto:ethernet
  note: The Commercial Pro adds a second Ethernet port for a dedicated utility connection.
  cite:
  - src: src:kb-enphase-what-are-the-key-features-of-iq-gateway-commercial-pro
    loc: sec=h1
    h: ca9195a2f2e9
  review: drafted
- claim_id: c14
  rel: implements
  target: func:production-metering
  note: The Envoy-S Standard (ENV-S-AB-120-A) offers standard production monitoring, accuracy +/- 5%.
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: tbl=8.r1
    h: b85d6b08129c
  review: drafted
- claim_id: c15
  attr: max_count
  value:
    max: 600
    unit: unit:NUM
  conditions: Enphase IQ Microinverters monitored by one IQ Gateway
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=1
    h: 50634e717f87
  review: drafted
- claim_id: c16
  attr: max_count
  value:
    max: 39
    unit: unit:NUM
  conditions: Enphase IQ Batteries monitored by one IQ Gateway
  cite:
  - src: src:enphase-enphase-iq7-series-microinverters-installation-and-operation-manual
    loc: sec=1
    h: 50634e717f87
  review: drafted
- claim_id: c17
  attr: warranty_term
  value:
    nominal: 15
    unit: unit:YR
  conditions: Limited warranty, IQ Gateway Commercial Pro variant
  cite:
  - src: src:kb-enphase-what-are-the-key-features-of-iq-gateway-commercial-pro
    loc: sec=h1
    h: ca9195a2f2e9
  review: drafted
---
The Enphase IQ Gateway, formerly called the IQ Envoy or Envoy-S, is a communications gateway. It collects performance data from Enphase microinverters and batteries and sends it to the Enphase Cloud. It reads microinverter data over the site AC power lines and connects to the internet by Wi-Fi or by a cellular modem plugged into its USB port. One gateway can monitor up to 600 IQ Microinverters and up to 39 IQ Batteries. It talks to IQ7 and IQ8 microinverters, IQ Batteries and the IQ System Controller. IQ Combiner units ship with a gateway built in. You need a gateway to set or change the grid profile. All 208 VAC installs must be commissioned through it so the correct trip points reach the microinverters. The IQ Gateway Commercial Pro adds RS-485 Modbus for third-party meters and a second Ethernet port, and comes with a 15-year limited warranty.

<!-- review notes
- sentence 2: support check: partial - Power line reading and USB cellular modem are stated; Wi-Fi is supported only by a title about reconnecting to Wi-Fi.
-->
