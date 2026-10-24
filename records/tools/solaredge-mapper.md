---
id: tool:solaredge-mapper
type: Tool
name: SolarEdge Site Mapper app
aliases:
- SolarEdge Mapper
- Site Mapper
- Mapper App
- Mapper Application
- Site Mapper Application
- Site Mapper app
- SolarEdge Site Mapper
- Mapper
category: Apps
tool_kind: app
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solaredge
  cite:
  - src: src:eq-equip-inverters-solaredge-design-installation-3phase-inverter-w-synergy-technology-guide-na-v1-1
    loc: sec=h125
    h: 828393e1c25d
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: sec=h123
    h: f2fdfb2af938
  - src: src:eq-equip-inverters-solaredge-design-installation-3phase-inverter-w-synergy-technology-guide-na-v1-1
    loc: sec=h124
    h: 3a6905ce9ff0
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:bluetooth
  note: Barcodes can be scanned with an external scanner connected over Bluetooth, as an alternative to
    the phone camera.
  cite:
  - src: src:se-academy-mapper-app-01-process-overview-mapper-app
    loc: sec=h2
    h: 61e1c4165a83
  review: drafted
  review_note: 'support check: partial - Passage says barcodes can be scanned with an external Bluetooth-connected
    scanner, but the app itself is not stated to use Bluetooth as a protocol; it is an optional scanner
    connection.'
---
SolarEdge Site Mapper is a SolarEdge smartphone app. You use it to scan the 2D barcodes on power optimizers and inverters, which builds a virtual map of the PV site's physical layout in the SolarEdge monitoring platform. The app works with the monitoring platform. You can register new systems on site, create, edit and check the physical layout, and assign each power optimizer serial number to its correct module position. An accurate site map lets you use module-level monitoring and makes remote diagnostics and troubleshooting easier. You can scan with the phone's built-in camera or with an external scanner connected over Bluetooth. Changes save automatically while you are online. When you are offline they are stored on the device and synced later. Several users can map the same site at once and see each other's edits in real time. Map the site after installation is finished. Mapper stays in sync with the Layout Editor, the desktop tool for mapping a site remotely, and with layouts exported from SolarEdge Designer, which can also show the roof edges. To use the app, you need SolarEdge login credentials linked to the company account that owns the site. If you don't have them, ask your company's SolarEdge account admin to add you.

<!-- review notes
- sentence 6: support check: partial - Mapping after installation, Layout Editor sync and the Designer roof edges display are supported, but 'layouts exported from Designer' staying in sync with Mapper is not stated; Designer export creates the site and roof edges display is stated, with no explicit sync claim.
-->
