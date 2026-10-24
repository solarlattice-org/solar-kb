---
id: prod:alsoenergy-weather-station
type: Product
name: AlsoEnergy weather station (digitizer and sensor kit)
aliases:
- AlsoEnergy Weather Station
- WS-BC-01
- WS-AMB-01
- WS-WD-01
- WS-BR-PY2
- WS-IT-MP
- WS-IT-RC
- WS-KZ-SP2
- Integrated Weather Station Digitizer
- Signal Conditioner / Digitizer
- weather station digitizer
category: Sensors
make: alsoenergy
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:alsoenergy
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-13
    loc: sec=6.7
    h: 6228f013b320
  - src: src:eq-equip-das-alsoenergy-install-manual-alsoenergy-installation-manual-pv-rev-15
    loc: sec=5.7
    h: ac0d42681341
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-ws-bc-01-alsoenergy-weather-station-base-2020-06-11
    loc: sec=h2
    h: e25a15a66ff8
  review: drafted
  review_note: 'support check: partial - Passages describe the AlsoEnergy Weather Station and digitizer
    but never explicitly state AlsoEnergy makes it, though the name strongly implies it.'
- claim_id: c2
  rel: uses_protocol
  target: proto:modbus-rtu
  note: Digitizer sends converted sensor values to the AlsoEnergy Data Logger over Modbus RTU.
  cite:
  - src: src:eq-equip-das-alsoenergy-install-manual-alsoenergy-installation-manual-pv-rev-15
    loc: sec=5.7
    h: ac0d42681341
  - src: src:alsoenergy-alsoenergy-installation-manual-pv-rev-15-1
    loc: sec=5.7
    h: ac0d42681341
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:modbus
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-13
    loc: sec=6.7
    h: 6228f013b320
  - src: src:eq-equip-das-alsoenergy-install-manual-alsoenergy-installation-manual-pv-rev-13
    loc: sec=6.7
    h: 6228f013b320
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-14-1
    loc: sec=8.7
    h: fa1d2a20afe7
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-ws-bc-01-alsoenergy-weather-station-base-2020-06-11
    loc: sec=h2
    h: e25a15a66ff8
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:rs485
  note: MODBUS/485 interface; Modbus ground is isolated from analog and pulse grounds.
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-ws-bc-01-alsoenergy-weather-station-base-2020-06-11
    loc: sec=h2
    h: e25a15a66ff8
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:current-loop-4-20ma
  note: Two analog inputs accept 0-10 VDC or 4-20 mA; terminals P4 and P6 carry 4-20 mA temperature signals.
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-ws-bc-01-alsoenergy-weather-station-base-2020-06-11
    loc: sec=h2
    h: e25a15a66ff8
  - src: src:eq-equip-das-alsoenergy-install-manual-alsoenergy-installation-manual-pv-rev-15
    loc: tbl=8
    h: fe408f901016
  - src: src:alsoenergy-alsoenergy-installation-manual-pv-rev-15-1
    loc: tbl=9
    h: fe408f901016
  review: drafted
- claim_id: c6
  attr: max_count
  value:
    nominal: 6
    unit: unit:NUM
  conditions: 'Sensor inputs per digitizer: 2 low-level analog (0-25 mV, 0-250 mV, 0-2.5 V), 2 analog
    (0-10 VDC or 4-20 mA), 2 pulse'
  cite:
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-ws-bc-01-alsoenergy-weather-station-base-2020-06-11
    loc: sec=h2
    h: e25a15a66ff8
  review: drafted
---
The digitizer converts the analog sensor signals to digital values and sends them to the AlsoEnergy Data Logger over a Modbus RTU link on an RS-485 interface. It has six sensor inputs: two low-level, low-noise analog inputs, two inputs for 0-10 VDC or 4-20 mA, and two pulse inputs. The standard kit measures module temperature, ambient temperature, solar irradiance, and wind speed and direction. Relative humidity, barometric pressure and rain gauge sensors are optional add-ons. Terminals P1 and P2 supply +24 VDC, P8 and P10 take millivolt pyranometer signals, P10 also takes wind direction, and P12 supplies +2.5 VDC for the Davis wind sensor only. Mount the anemometer pointing north. The clear pyranometer shield wire does not go to the digitizer; it lands on the shield terminal of the RS-485 field terminal block. The Modbus ground is isolated from the analog and pulse grounds, and configuration and pulse data are kept in nonvolatile memory.

<!-- review notes
- sentence 1: support check: partial - Conversion and Modbus RTU to the logger are stated, and the MODBUS/485 interface is mentioned, but nothing explicitly ties the Modbus RTU link to RS-485 to the logger.
-->
