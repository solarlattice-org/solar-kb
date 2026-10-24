---
id: tool:solis-soliscloud
type: Tool
name: SolisCloud
aliases:
- SolisCloud Monitoring System
- SolisCloud Monitoring APP
- Solis Cloud App
- SolisCloud Mobile App
category: Platforms
tool_kind: platform
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  note: Solis publishes the SolisCloud datasheet, and the service comes included with Solis loggers.
  cite:
  - src: src:eq-equip-inverters-solis-solis-datasheet-soliscloud-usa-v2-1-202410
    loc: sec=h1
    h: 3c6b0f560eed
  - src: src:solis-manual-solis-s1-w4g-st-v3-2-20250806
    loc: sec=h61
    h: d7ba554d55b0
  review: drafted
  review_note: 'support check: partial - Passages say SolisCloud is free and included in the logger cost,
    but never say Solis makes it (only the name ''SolisCloud'' appears) and mention no datasheet.; review:
    partial - The passages say SolisCloud comes free with the Solis logger, which suggests Solis makes
    it, but they never say so outright, and the quoted datasheet passage holds only the title, so nothing
    shows Solis publishing it.'
---
SolisCloud is the Solis monitoring platform. It collects plant data uploaded by Solis GPRS/4G, WiFi, LAN and RF-Link sticks and data logger boxes, then shows and analyses that data. You can open it in the app or in a web browser. The service is free with a Solis logger. You need a logger to see your own inverter. Without one, you can only view systems you have been added to as a guest. First-time users register an account at www.soliscloud.com before they can log in. The manual expects users to have basic network knowledge and to know Solis products. If the network drops, Solis stick and box loggers store operating data locally. Once the connection returns, they backfill that history to SolisCloud automatically, and real-time uploads keep running during the backfill. For S6 hybrid parallel systems, create one plant and add only the Master logger to it. All production, battery and alarm data then shows up through the Master inverter. Firmware updates are not yet supported through the Master inverter, so Solis suggests giving each parallel inverter its own S2 or S4 logger. This lets support update each unit separately. Solis describes SolisCloud as providing remote monitoring, real-time diagnostics and remote OTA updates for its storage systems.

<!-- review notes
- sentence 7: support check: partial - Passages mention remote monitoring, real-time diagnostics and remote OTA updates via SolisCloud/SolisStorage Cloud, but only for the C&I storage systems, and the OTA and diagnostics claims come from separate bullets rather than one description of SolisCloud.
-->
