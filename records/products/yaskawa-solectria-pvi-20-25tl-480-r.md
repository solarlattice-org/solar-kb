---
id: prod:yaskawa-solectria-pvi-20-25tl-480-r
type: Product
name: Solectria PVI 20/25TL-480-R
aliases:
- PVI 20 25 TL 480 R
- PVI 20-25TL-480-R
- PVI 25TL-480-R
- SOLECTRIA PVI 25TL-480-R
- SOLECTRIA PVI 25TL
category: Inverters
make: yaskawa-solectria
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:yaskawa-solectria
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h172
    h: 2601fbde8e60
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=8
    h: d07d973c5e27
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=front
    h: 47b59c8eb39b
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Grid-tied, three-phase, grid-following PV string inverter for commercial or utility-scale use.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=2.1
    h: 141c9950a8e1
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:modbus
  note: Modbus over RS-485.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=3.6
    h: 3e0a6f3aaa98
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:rs485
  conditions: Required for third-party monitoring/DAS connections; shielded twisted-pair cable.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h104
    h: 1e1f2e0e6bb8
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=3.6
    h: 3e0a6f3aaa98
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:wifi
  note: Interface accessed from a smart device through the FOMlink wireless antenna device.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=2.4
    h: b38be33e932b
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=3.6
    h: 3e0a6f3aaa98
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:ethernet
  conditions: Via the optional Ethernet Network Card, needed for SolrenView monitoring.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h104
    h: 1e1f2e0e6bb8
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=3.6
    h: 3e0a6f3aaa98
  review: drafted
- claim_id: c7
  rel: implements
  target: func:remote-firmware-update
  conditions: Requires internet connection through the Ethernet Network Card.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=3.6
    h: 3e0a6f3aaa98
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h100
    h: ea880a03faa6
  review: drafted
  review_note: 'support check: partial - Automatic firmware upgrades via Ethernet card/internet are stated,
    but ''remote firmware update'' and internet-through-Ethernet-card requirement are only loosely implied.'
- claim_id: c8
  rel: implements
  target: func:remote-maintenance
  note: Remote diagnostics and troubleshooting and access for manufacturer technical support when connected
    to the internet.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=3.6
    h: 3e0a6f3aaa98
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h100
    h: ea880a03faa6
  review: drafted
- claim_id: c9
  rel: compatible_with
  target: arch:grid-tied-pv
  scope:
    applications:
    - on-grid
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h7
    h: 8c499e70d134
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=2.1
    h: 141c9950a8e1
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c10
  rel: compatible_with
  target: arch:ungrounded-pv-array
  note: To be installed with floating or ungrounded PV arrays only.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h7
    h: 8c499e70d134
  review: drafted
- claim_id: c11
  rel: compatible_with
  target: arch:rooftop-pv
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=2.1
    h: 141c9950a8e1
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c12
  rel: compatible_with
  target: arch:carport-pv
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=2.1
    h: 141c9950a8e1
  review: drafted
- claim_id: c13
  rel: compatible_with
  target: arch:ground-mounted-pv
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=2.1
    h: 141c9950a8e1
  review: drafted
- claim_id: c14
  rel: incompatible_with
  target: arch:microgrid
  note: Not intended for micro-grid use.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=2.1
    h: 141c9950a8e1
  review: drafted
- claim_id: c15
  rel: incompatible_with
  target: arch:off-grid-system
  scope:
    applications:
    - off-grid
  note: Not intended for off-grid use.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=2.1
    h: 141c9950a8e1
  review: drafted
- claim_id: c16
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: Maximum (peak) efficiency per datasheet
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=43.r3
    h: 91994928f0b0
  review: drafted
- claim_id: c17
  attr: max_input_current
  value:
    max: 45
    unit: unit:A
  conditions: Maximum PV current (Isc x 1.25) per zone, PVI 25TL-480-R
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=11.r10
    h: a4877c801687
  review: drafted
- claim_id: c18
  attr: max_input_current
  value:
    max: 90
    unit: unit:A
  conditions: Maximum PV current (Isc x 1.25) total, PVI 25TL-480-R
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=11.r10
    h: a4877c801687
  review: drafted
- claim_id: c19
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: AC output voltage
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=2.1
    h: 141c9950a8e1
  review: drafted
- claim_id: c20
  attr: max_input_voltage
  value:
    nominal: 1000
    unit: unit:V
  conditions: DC system voltage class of the commercial string inverter
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=front
    h: 47b59c8eb39b
  review: drafted
  review_note: 'support check: partial - Passage says 1000VDC string inverter class, but not explicitly
    a maximum input voltage.'
---
The Solectria PVI 25TL-480-R from Yaskawa Solectria Solar is a grid-tied, three-phase, grid-following PV string inverter for commercial or utility-scale sites, with a 1000 VDC input class and 480 VAC output. The datasheet gives a maximum efficiency of 98.5 percent, and maximum PV current is 45 A per zone and 90 A total. It must be used with floating or ungrounded PV arrays only, and it suits rooftop, carport and ground-mount installations; it is not intended for micro-grid or off-grid use, and the manufacturer does not support AC-coupled systems. Communication uses Modbus over RS-485 for third-party monitoring, and the interface can be reached over Wi-Fi from a smart device through the FOMlink wireless antenna. SolrenView monitoring needs the optional Ethernet Network Card, which also gives automatic firmware updates, remote diagnostics and technical support access over the internet. A shade cover is required if the inverter is mounted lower than 75 degrees from horizontal, because it reduces temperature derating. The enclosure is rated NEMA 4X, but an unpowered unit left outdoors for more than 90 days can collect condensation on the heatsink. Inspect the power head before applying DC or AC power, or a short circuit can result.
