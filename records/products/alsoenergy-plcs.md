---
id: prod:alsoenergy-plcs
type: Product
name: AlsoEnergy PLCS power limiting control system
aliases:
- PLCS 400
- PLCS 600
- PowerLCS 400
- PowerLCS
- PLCS600
category: Monitoring and communications
make: alsoenergy
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:alsoenergy
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h13
    h: 7182e97cca68
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=3.0
    h: 970b49e9dd35
  - src: src:eq-equip-das-alsoenergy-plcs-202202-plcs-600-installation-guide
    loc: sec=h16
    h: 0fa868ddad33
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:monitoring-gateway
  note: Integrated monitoring enclosure with datalogger, revenue-grade meter and weather sensors.
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=3.0
    h: 970b49e9dd35
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h13
    h: 7182e97cca68
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:modbus-rtu
  note: Used for inverter communications.
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=3.0
    h: 970b49e9dd35
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h13
    h: 7182e97cca68
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:modbus-tcp
  note: Used for inverter communications.
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=3.0
    h: 970b49e9dd35
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h13
    h: 7182e97cca68
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:ethernet
  note: Internet-accessible Ethernet connection used to upload data to AlsoEnergy PowerTrack.
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h13
    h: 7182e97cca68
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:cellular
  note: Optional cell modem when no internet connection is available.
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=3.0
    h: 970b49e9dd35
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h13
    h: 7182e97cca68
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:rs485
  note: Wire as a daisy chain; avoid star or branch layouts and keep stubs short, never over 50 ft (15
    m) per the PLCS 600 guide.
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202202-plcs-600-installation-guide
    loc: sec=h30
    h: d256869c83b0
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h35
    h: f1a82a805a5a
  review: drafted
- claim_id: c8
  rel: lacks
  target: func:remote-maintenance
  note: PowerLCS 400 guide states remote access is not supported or possible and no additional configuration
    options are available.
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h13
    h: 7182e97cca68
  review: drafted
- claim_id: c9
  rel: implements
  target: func:production-metering
  note: Includes a revenue-grade meter with solid-core 400 A CTs; data logged at 5-minute granularity.
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=3.0
    h: 970b49e9dd35
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h13
    h: 7182e97cca68
  review: drafted
  review_note: 'support check: partial - Revenue-grade meter, 400A solid-core CTs and 5-minute granularity
    are stated, but the passages do not say it does production metering specifically.'
- claim_id: c10
  rel: requires
  target: role:licensed-electrician
  note: Installation guide is written for a licensed electrician to plan, install and commission the system.
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h14
    h: 72e8520404e6
  review: drafted
- claim_id: c11
  attr: max_count
  value:
    max: 16
    unit: unit:NUM
  conditions: Inverters interfaced via Modbus RTU or Modbus TCP, PowerLCS 400
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h13
    h: 7182e97cca68
  review: drafted
- claim_id: c12
  attr: nominal_voltage
  value:
    min: 100
    max: 277
    unit: unit:V
  conditions: Control power supply input, auto-ranging AC; neutral required, do not use two hot phases
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202202-plcs-600-installation-guide
    loc: sec=h16
    h: 0fa868ddad33
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h32
    h: 3a898a412944
  - src: src:alsoenergy-kb-attachments-assets-powerlcs400installationmanualv5booklet
    loc: sec=h32
    h: eaa29ce95499
  review: drafted
- claim_id: c13
  attr: frequency
  value:
    min: 50
    max: 60
    unit: unit:HZ
  conditions: Control power supply input
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202202-plcs-600-installation-guide
    loc: sec=h16
    h: 0fa868ddad33
  - src: src:eq-equip-das-alsoenergy-plcs-202112-plcs-400-installation-guide
    loc: sec=h32
    h: 3a898a412944
  - src: src:alsoenergy-kb-attachments-assets-powerlcs400installationmanualv5booklet
    loc: sec=h32
    h: eaa29ce95499
  review: drafted
- claim_id: c14
  attr: warranty_term
  value:
    nominal: 5
    unit: unit:YR
  conditions: Standard AlsoEnergy warranty, PowerLCS 400; all parts except irradiance sensor and cell
    modem
  cite:
  - src: src:eq-equip-das-alsoenergy-plcs-202202-plcs-400-cut-sheet
    loc: sec=h4
    h: e58cf9d38599
  review: drafted
---
The AlsoEnergy PLCS (PowerLCS) is a preconfigured, prewired monitoring enclosure that combines a datalogger, revenue-grade meter, irradiance sensor and module temperature sensor, and offers a cell modem as an option. The PowerLCS 400 connects to up to 16 inverters over Modbus RTU or Modbus TCP and uploads compressed 5-minute data to AlsoEnergy PowerTrack over Ethernet every 2 hours. The PowerLCS 400 enclosure is rated for up to 325 kW AC at 480 VAC, ships with solid-core 400 A CTs, logs data only in daylight hours, and is not recommended for demand metering. The control power supply is auto-ranging from 100 to 277 VAC at 50 to 60 Hz. It needs a neutral, must not be fed from two hot phases, and should be protected by a breaker rated up to 20 A, wired with 12 to 14 AWG. Remote access is not supported on the PowerLCS 400, and its enclosure has no further configuration options. On the PLCS 600, wire RS-485 as a daisy chain without star or branch runs, and keep stubs as short as possible. The installation guides are written for licensed electricians. Except for the irradiance sensor and cell modem, the PowerLCS 400 parts carry the standard AlsoEnergy 5-year warranty.

<!-- review notes
- sentence 1: support check: partial - Enclosure contents and optional cell modem are stated, but a 'datalogger' is mentioned only in u37 and the preconfigured/prewired claim is for the PowerLCS 400 specifically; irradiance and module temperature sensors are in the integrated system description. Mostly supported but loosely generalized.
-->
