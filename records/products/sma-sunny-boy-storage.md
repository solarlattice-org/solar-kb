---
id: prod:sma-sunny-boy-storage
type: Product
name: Sunny Boy Storage
aliases:
- SBS
- SBS 3.7-6.0-10
- SBS3.8-US-10
- SBS2.5-1VL-10
- SBS3.7-10
- SBS5.0-10
- SBS6.0-10
- SBSX.X-US-10
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:inverter
  note: Listed as a battery inverter
  cite:
  - src: src:sma-doc-275857
    loc: tbl=4.r7
    h: fbf19eb19359
  - src: src:sma-doc-275857
    loc: tbl=4.r6
    h: 808e41a97c08
  review: drafted
- claim_id: c2
  attr: rated_power
  value:
    nominal: 2500
    unit: unit:W
  conditions: Sunny Boy Storage 2.5, rated output power
  cite:
  - src: src:sma-doc-259463
    loc: tbl=24.r1
    h: 43c5b92f995b
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions)
- claim_id: c3
  attr: rated_power
  value:
    nominal: 3680
    unit: unit:W
  conditions: Sunny Boy Storage 3.7, rated output power
  cite:
  - src: src:sma-doc-259463
    loc: tbl=24.r2
    h: 48509a543e60
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions)
- claim_id: c4
  attr: rated_power
  value:
    nominal: 5000
    unit: unit:W
  conditions: Sunny Boy Storage 5.0, rated output power
  cite:
  - src: src:sma-doc-259463
    loc: tbl=25.r1
    h: '81e618806952'
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions)
- claim_id: c5
  attr: rated_power
  value:
    nominal: 6000
    unit: unit:W
  conditions: Sunny Boy Storage 6.0, rated output power
  cite:
  - src: src:sma-doc-259463
    loc: tbl=25.r2
    h: 492940a76d8e
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions)
- claim_id: c6
  rel: uses_protocol
  target: proto:webconnect
  note: Standard; sends data directly to Sunny Portal with no extra communication device
  cite:
  - src: src:sma-doc-259463
    loc: sec=h137
    h: a1ea248c89a6
  - src: src:sma-kb-will-i-receive-information-on-the-sunny-boy-storage-in-sunny-portal
    loc: sec=h1
    h: e33bfcaeb4ad
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:speedwire
  cite:
  - src: src:sma-kb-can-devices-with-bluetooth-interface-communicate-with-the-sunny-boy-storage
    loc: sec=h1
    h: 9d9715693e01
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:wifi
  cite:
  - src: src:sma-kb-can-devices-with-bluetooth-interface-communicate-with-the-sunny-boy-storage
    loc: sec=h1
    h: 9d9715693e01
  review: drafted
- claim_id: c9
  rel: lacks
  target: proto:bluetooth
  note: Bluetooth devices cannot talk to the Sunny Boy Storage
  cite:
  - src: src:sma-kb-can-devices-with-bluetooth-interface-communicate-with-the-sunny-boy-storage
    loc: sec=h1
    h: 9d9715693e01
  review: drafted
  review_note: 'support check: partial - Passage says Bluetooth devices cannot communicate with it and
    it has Speedwire and WiFi, but does not explicitly state it lacks a Bluetooth interface.'
- claim_id: c10
  rel: implements
  target: func:backup-power
  note: Has functions for the SMA battery-backup system
  cite:
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=1.r28
    h: 72400a17f7e8
  review: drafted
- claim_id: c11
  rel: implements
  target: func:remote-firmware-update
  note: Automatic inverter and battery firmware updates can be enabled in a communication product or Sunny
    Portal; when updating both manually, update the inverter first
  cite:
  - src: src:sma-kb-sunny-boy-storage-updating-the-firmware
    loc: sec=h1
    h: a2a4d7d1c87d
  - src: src:sma-kb-sbs-3-7-5-0-6-0-10-and-update-of-battery-era-powerbase
    loc: sec=h1
    h: 01f00ef983cb
  review: drafted
- claim_id: c12
  rel: compatible_with
  target: prod:sma-data-manager-m
  note: Communication product in which automatic firmware updates can be enabled
  cite:
  - src: src:sma-kb-sunny-boy-storage-updating-the-firmware
    loc: sec=h1
    h: a2a4d7d1c87d
  review: drafted
  review_note: 'support check: partial - Passage mentions ''SMA Data Manager'' generically as a communication
    product, not specifically Data Manager M compatibility.'
- claim_id: c13
  rel: compatible_with
  target: prod:bmz-hyperion
  scope:
    firmware_min: 3.12.26.R
    valid_from: '2020-08-01'
  conditions: SBS 3.7-6.0; new Helios VE modules from inverter firmware 3.12.26.R
  cite:
  - src: src:sma-kb-sunny-boy-storage-sbs-3-7-6-0-battery-compatibility-bmz-hyperion-ibc-era-powerbase
    loc: sec=h1
    h: 7186352d94de
  review: drafted
- claim_id: c14
  rel: compatible_with
  target: prod:axitec-axistorage
  scope:
    firmware_min: 3.12.26.R
    valid_from: '2020-08-01'
  conditions: SBS 3.7-6.0; new Helios VE modules from inverter firmware 3.12.26.R
  cite:
  - src: src:sma-kb-sunny-boy-storage-sbs-3-7-6-0-battery-compatibility-bmz-hyperion-ibc-era-powerbase
    loc: sec=h1
    h: 7186352d94de
  review: drafted
- claim_id: c15
  rel: compatible_with
  target: prod:ibc-solar-era-powerbase
  scope:
    firmware_min: 3.12.26.R
    valid_from: '2020-08-01'
  conditions: SBS 3.7-6.0; new Helios VE modules from inverter firmware 3.12.26.R; battery firmware can
    be updated through the SBS
  cite:
  - src: src:sma-kb-sunny-boy-storage-sbs-3-7-6-0-battery-compatibility-bmz-hyperion-ibc-era-powerbase
    loc: sec=h1
    h: 7186352d94de
  - src: src:sma-kb-sbs-3-7-5-0-6-0-10-and-update-of-battery-era-powerbase
    loc: sec=h1
    h: 01f00ef983cb
  review: drafted
- claim_id: c16
  rel: compatible_with
  target: prod:lg-energy-solution-resu
  conditions: LG Chem RESU 10 is only conditionally approved; quick start guides exist for LG Resu10 and
    LG Prime with the US models
  cite:
  - src: src:sma-kb-sunny-boy-storage-with-lg-chem-battery-and-abu
    loc: sec=h1
    h: 7704d2869a57
  - src: src:sma-kb-sunny-boy-storage-sbsx-x-us-10-quick-start-guides-and-manuals
    loc: sec=h1
    h: fad219407ee0
  review: drafted
  review_note: 'support check: partial - Conditional approval of RESU 10 and US quick start guides are
    stated, but general compatibility with LG RESU is only conditional and the ''US models'' link is implied
    by SBSX.X-US-10.'
- claim_id: c17
  rel: compatible_with
  target: prod:byd-battery-box-premium-hv
  conditions: Quick start guides for BYD HV and HVL with SBSX.X-US-10
  cite:
  - src: src:sma-kb-sunny-boy-storage-sbsx-x-us-10-quick-start-guides-and-manuals
    loc: sec=h1
    h: fad219407ee0
  review: drafted
---
The Sunny Boy Storage is an SMA battery inverter family. It includes the SBS2.5-1VL-10, the SBS3.7/5.0/6.0-10 and the US models SBS3.8/5.0/6.0-US-10. Rated output power is 2500 W for the 2.5, 3680 W for the 3.7, 5000 W for the 5.0 and 6000 W for the 6.0. It runs on one phase only and cannot be operated with three phases. It has Speedwire, Wi-Fi and Webconnect as standard, so it can send data straight to Sunny Portal for up to four inverters per system. It does not support Bluetooth devices. Use it only with an intrinsically safe lithium-ion battery that SMA has approved. Compatible batteries include BMZ Hyperion, IBC era:powerbase and AXITEC AXIstorage, and the newer Helios VE modules need inverter firmware 3.12.26.R or later. The LG Chem RESU 10 is only conditionally approved. Firmware for the inverter and the battery can update automatically through a communication product. If you update both by hand, do the inverter first. In a battery-backup system, the miniature circuit breaker can trip at most at B6 on the 3.7 and 5.0 and at B16 on the 6.0. A breaker with a higher trip characteristic will not be tripped by the inverter during a fault.

<!-- review notes
- sentence 4: support check: partial - Speedwire, WiFi, Webconnect, four inverters are stated; Bluetooth devices cannot communicate, but 'Speedwire, Wi-Fi and Webconnect as standard' is slightly stretched (Speedwire/WiFi 'equipped').
- sentence 8: support check: partial - Table gives B6/B6/B16 maximums, and u19 says higher characteristic breakers are not switched off, but the 'battery-backup system' context is not stated in the passages.
-->
