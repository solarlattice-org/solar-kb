---
id: tool:fronius-solar-web
type: Tool
name: Fronius Solar.web
aliases:
- Solar.web
- Fronius Solar.web live app
- Fronius Solar.web App
category: Platforms
tool_kind: platform
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:fronius
  note: Described as Fronius' online and mobile monitoring platform.
  cite:
  - src: src:eq-equip-inverters-fronius-symo-datasheet
    loc: sec=h1
    h: 0139866f84ec
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
Fronius Solar.web is the Fronius online and mobile platform for monitoring PV systems, where real-time and archived system data can be viewed over the internet. A Fronius Datamanager 2.0 connected to the internet by Ethernet or Wi-Fi can send PV system values to Solar.web automatically. The Datamanager can also feed third-party systems over SunSpec Modbus RTU, SunSpec Modbus TCP and the Fronius Solar API at the same time as it sends data to Solar.web. During commissioning, you run the Solar.web wizard or the commissioning wizard from the Fronius Solar.start app to put the inverter online and connect it to Solar.web. To check for new inverter firmware, open Solar.web and go to Settings, then Components, and run the update if one is offered. On Fronius Symo inverters, the Solar.web connection LED is green when the connection exists. It is red when a connection is required but missing, and it stays off when no connection is required. On the Fronius Tauro, the Solar.web live app takes you through the steps to set up the connection and to deal with faults shown on the status LEDs. The mobile Solar.web app lets owners check the energy yield of their PV system while away from the site.

<!-- review notes
- sentence 4: support check: partial - The commissioning wizard in the Solar.start app brings the inverter online and connects it to Solar.web, but the passages don't say the Solar.web wizard is an alternative way to do this.
- sentence 7: support check: partial - The passages say the Solar.web live app steps are for establishing the connection and for faults, but they don't tie this explicitly to the Tauro or to "status LEDs" in general. The communications LED covers connection and the operating status LED covers faults.
- sentence 4: review: partial - The passages back the Solar.start commissioning wizard bringing the inverter online and connecting it to Solar.web, and they say the Solar Web Wizard is run at startup, but they never say that wizard puts the inverter online.
-->
