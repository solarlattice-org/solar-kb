---
id: prod:sma-shp-peak3
type: Product
name: Sunny Highpower PEAK3
aliases:
- Sunny Highpower PEAK 3
- SHP PEAK 3
- PEAK 3 US
- PEAK3
- SHP US 20
- SHP xx 20
- Sunny High Power PEAK 3
- Sunny Highpower PEAK3-US
- Sunny Highpower PEAK3 US-20
- Sunny Highpower PEAK3 US-21
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:kb-sma-shpxxus20-troubleshooting
    loc: sec=front
    h: 391bb905f02c
  - src: src:kb-sma-shpxxxus21-commissioning
    loc: sec=front
    h: 948a683a5c8b
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:modbus-tcp
  note: SHPxx-US-20 units provide a Modbus TCP server for third-party SCADA systems.
  cite:
  - src: src:sma-kb-sunny-highpower-peak3-inverter-communication-issues-with-3rd-party-scada-systems
    loc: sec=h1
    h: 1f348e2e8be3
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:modbus
  note: Modbus function documented for the US-21 models.
  cite:
  - src: src:kb-sma-shpxxxus21-modbus-function
    loc: sec=front
    h: 4ba2a3b689fc
  review: drafted
  review_note: 'support check: partial - Only a title of a ''Modbus function'' page for US-21 is given;
    the content isn''t shown, though it implies Modbus use.'
- claim_id: c4
  rel: implements
  target: func:night-reactive-power
  note: Called Q on Demand. During non-feed-in operation the inverter stays connected and draws about
    1800 W of active power on average to cover its losses.
  cite:
  - src: src:sma-kb-power-loss-of-the-sunny-highpower-peak3-when-q-on-demand-is-applied
    loc: sec=h1
    h: 3566da50be0f
  review: drafted
- claim_id: c5
  rel: implements
  target: func:remote-firmware-update
  note: Automatic firmware updates can be enabled through the SMA Data Manager or on US-21 models. Manual
    update is possible through the inverter UI or a USB drive.
  cite:
  - src: src:sma-kb-sunny-highpower-peak3-inverter-communication-issues-with-3rd-party-scada-systems
    loc: sec=h1
    h: 1f348e2e8be3
  - src: src:kb-sma-shpxxxus21-automatic-firmware-update
    loc: sec=front
    h: 0fbb0ba90e0a
  review: drafted
  review_note: 'support check: partial - Automatic updates via Data Manager and manual update via UI or
    USB are stated, but ''remote'' and the US-21 automatic update claim rest only on a title; the Data
    Manager link isn''t specific to US-21.'
- claim_id: c6
  rel: compatible_with
  target: prod:sma-data-manager-m
  note: The Data Manager can show the inverter firmware version and run automatic updates.
  cite:
  - src: src:sma-kb-sunny-highpower-peak3-inverter-communication-issues-with-3rd-party-scada-systems
    loc: sec=h1
    h: 1f348e2e8be3
  review: drafted
  review_note: 'support check: partial - Data Manager use for firmware check and automatic updates is
    stated, but the specific model ''Data Manager M'' isn''t named.'
---
The Sunny Highpower PEAK3 is a family of SMA string inverters. It includes the SHP 100-20 and SHP 150-20, the SHP 100/150/172/180-21, and the US models SHP 125/150/165/172/FLEX-US-21. There are also US-20 models (SHP 125/150-US-20) and Japanese models (SHP 100-JP-20 and SHP 143-JP-20). The inverter supports Modbus TCP for third-party SCADA. Some SHPxx-US-20 units can lose this link at random or for good. A firmware update, a full AC/DC power cycle of at least 15 minutes, or switching the Modbus TCP server off and on may restore it. With the Q on Demand function, the inverter can supply reactive power at night. To do this it draws about 1800 W of active power on average. The filter capacitors cause a reactive power draw. With the grid relays open, this is roughly 127 to 219 VAr per inverter. With the relays closed and operation blocked, it can reach 1089 VAr. If event 6438 appears and the inverter does not feed in, check first that the firmware is 3.11.33.R or higher. If the event stays after a power cycle of at least 5 minutes, check the DC side for ground faults and insulation faults. You can update the firmware automatically through the SMA Data Manager, or by hand through the inverter user interface or a USB drive.

<!-- review notes
- sentence 1: support check: partial - The SHP 100/150-20, 100/150/172/180-21 and US-21 models are listed, but 'family of SMA string inverters' is only implied (string inverters category appears in the article footer for other docs, not in these passages).
- sentence 3: support check: partial - Modbus TCP and the power cycle and toggle remedies are stated, but firmware update is not given as a fix for this specific link loss; it is only a general installer step.
- sentence 6: support check: partial - Firmware 3.11.33.R check applies to sporadic occurrence and the DC check follows a persisting event after a 5-minute power cycle; the statement merges these and omits that the firmware check is for the sporadic case.
-->
