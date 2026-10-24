---
id: tool:solaredge-monitoring-platform
type: Tool
name: SolarEdge Monitoring Platform
aliases:
- SE monitoring API
- SolarEdge Cloud-Based Monitoring Platform
- SolarEdge API
- Monitoring Platform
category: Platforms
tool_kind: platform
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solaredge
  cite:
  - src: src:eq-equip-inverters-solaredge-design-installation-3phase-inverter-w-synergy-technology-guide-na-v1-1
    loc: sec=h29
    h: 5b7244481723
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: sec=h33
    h: 5b7244481723
  - src: src:eq-equip-inverters-solaredge-monitoring-communications-se-monitoring-api
    loc: sec=h4
    h: f4a6d8ea8686
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:https-rest-api
  note: Web-service API reached at an HTTPS monitoring API link; an API key (account level or site level)
    is needed for every request.
  cite:
  - src: src:eq-equip-inverters-solaredge-monitoring-communications-se-monitoring-api
    loc: sec=h4
    h: f4a6d8ea8686
  - src: src:eq-equip-inverters-solaredge-monitoring-communications-se-monitoring-api
    loc: sec=h7
    h: 0220092190c7
  review: drafted
  review_note: 'support check: partial - The API, the monitoring API link and the API key (account or
    site level) are stated, but the passages never say the API is HTTPS REST, though the link is https.'
---
The SolarEdge Monitoring Platform is a web-based online service for tracking and controlling SolarEdge PV sites remotely. It shows the technical and financial performance of one or more sites, with past and present data at the module, string and system levels. Its data comes from sensors and transmitters built into the SolarEdge power optimizers and inverters, so many faults can be found remotely without taking measurements on site. You can create a site by exporting a project from SolarEdge Designer or by building it from scratch, then map components with the Layout Editor or the Mapper app by scanning the QR codes on optimizers and inverters. The platform starts tracking the system once the devices are connected and producing, which lets you check performance right after installation. Only SolarEdge communication products are supported for sending inverter data to the platform, and communication options should be connected only while the inverter and related devices are powered down. Other software can pull data from the platform through an API for analysis or fleet management, but each request needs an API key at account or site level. SolarEdge training courses cover the Alerts tool, remote pairing and user and account management on the platform.

<!-- review notes
- sentence 4: support check: partial - The passages cover creating a site via Designer export or from scratch, mapping with the Layout Editor or Mapper app, and scanning QR codes. They don't explicitly say the QR scan is done within the Layout Editor or Mapper.
-->
