---
id: prod:alsoenergy-powerlogger
type: Product
name: AlsoEnergy PowerLogger 1000
aliases:
- PowerLogger
- PowerLogger1000
- Power Logger 1000
- PL1000
- CH-E0-1000
- Interactive Datalogger
category: Monitoring and communications
make: alsoenergy
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:alsoenergy
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-ch-e0-1000-powerlogger1000-datasheet-v2
    loc: sec=h1
    h: 13617579a61c
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:monitoring-gateway
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-ch-e0-1000-powerlogger1000-datasheet-v2
    loc: sec=h1
    h: 13617579a61c
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:modbus-rtu
  note: Used to connect to inverters, meters and weather stations.
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  - src: src:eq-equip-das-alsoenergy-install-manual-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-14-1
    loc: sec=4.2.2
    h: 58aac43aca61
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  rel: uses_protocol
  target: proto:modbus-tcp
  note: Used to connect to inverters, meters and weather stations.
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  - src: src:eq-equip-das-alsoenergy-install-manual-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-14-1
    loc: sec=4.2.2
    h: 58aac43aca61
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:dnp3
  note: Other protocols available with vendor cooperation.
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  - src: src:eq-equip-das-alsoenergy-install-manual-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-14-1
    loc: sec=4.2.2
    h: 58aac43aca61
  review: drafted
- claim_id: c6
  rel: certified_to
  target: std:ul-60950-1
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-ch-e0-1000-powerlogger1000-datasheet-v2
    loc: tbl=6.r2
    h: c5c35244b828
  review: drafted
  review_note: 'support check: partial - Passage says ''Listed to UL 60950-1'', not certified; listing
    is close but not exactly certification.'
- claim_id: c7
  rel: certified_to
  target: std:fcc-part-15b
  note: Class A.
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-ch-e0-1000-powerlogger1000-datasheet-v2
    loc: tbl=6.r2
    h: c5c35244b828
  review: drafted
  review_note: 'support check: partial - Passage says listed to FCC Part 15 Subpart B Class A; ''certified''
    wording is slightly stronger but core matches.'
- claim_id: c8
  rel: requires
  target: tool:alsoenergy-powertrack
  note: Designed for use with the cloud-based PowerTrack software; sends real-time field data and diagnostics
    to it.
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-ch-e0-1000-powerlogger1000-datasheet-v2
    loc: sec=h3
    h: 8ee2f59c00ce
  - src: src:eq-equip-das-alsoenergy-alsoenergy-ch-e0-1000-powerlogger1000-datasheet-v2
    loc: sec=h2
    h: cb3a85689752
  review: drafted
- claim_id: c9
  rel: implements
  target: func:remote-firmware-update
  note: Automatic remote firmware updates.
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  - src: src:eq-equip-das-alsoenergy-install-manual-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  review: drafted
- claim_id: c10
  rel: implements
  target: func:data-backfill
  note: Data stored on a removable SD card during network outages and uploaded once the network is restored.
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  - src: src:eq-equip-das-alsoenergy-install-manual-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-14-1
    loc: sec=4.2.2
    h: 58aac43aca61
  - src: src:eq-equip-das-alsoenergy-alsoenergy-ch-e0-1000-powerlogger1000-datasheet-v2
    loc: sec=h2
    h: cb3a85689752
  review: drafted
- claim_id: c11
  rel: implements
  target: func:remote-inverter-control
  note: Manual remote control to clear inverter faults, switch inverters off and on, and operate switchgear
    where permitted.
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-ch-e0-1000-powerlogger1000-datasheet-v2
    loc: sec=h2
    h: cb3a85689752
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c12
  attr: max_count
  value:
    max: 40
    unit: unit:NUM
  conditions: Total connected devices supported per logger
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  - src: src:eq-equip-das-alsoenergy-install-manual-alsoenergy-installation-manual-pv-rev-13
    loc: sec=2.2.2
    h: f35bc167c8b3
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-14-1
    loc: sec=4.2.2
    h: 58aac43aca61
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c13
  attr: warranty_term
  value:
    nominal: 5
    unit: unit:YR
  conditions: Standard warranty for AlsoEnergy integrated hardware solutions
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-ch-e0-1000-powerlogger1000-datasheet-v2
    loc: sec=h1
    h: 13617579a61c
  - src: src:eq-equip-das-alsoenergy-pl1000-cutsheet
    loc: sec=h1
    h: 13617579a61c
  review: drafted
---
The AlsoEnergy PowerLogger 1000 is the standard gateway data logger for AlsoEnergy's commercial PV monitoring solution, and it has a touch screen for on-site work without a laptop. It is usually mounted in a NEMA4 enclosure together with a power supply, cellular modem, network switch and revenue grade meter. It ships pre-loaded with AlsoEnergy software and configuration, and it polls inverters, meters and weather stations over Modbus RTU, Modbus TCP or DNP3. One logger supports up to 40 devices, with a recommended maximum of 20 per port. It uploads data to the cloud-based PowerTrack platform, typically every 3 to 5 minutes. During network outages it buffers data on a removable SD card and uploads it once the network is back. It supports automatic remote firmware updates and manual remote control to clear inverter faults, switch inverters off and on, and operate switchgear where permitted. It is listed to UL 60950-1 and CSA C22.2 and meets FCC Part 15 Subpart B Class A. It carries a standard 5-year warranty.
