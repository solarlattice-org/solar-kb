---
id: tool:solaredge-go
type: Tool
name: SolarEdge Go app
aliases:
- SolarEdge Go
category: Apps
tool_kind: app
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solaredge
  note: SolarEdge training presents SolarEdge Go as its mobile app for installation, management and service.
  cite:
  - src: src:se-academy-solaredge-go
    loc: sec=h1
    h: d3ba09068f6a
  - src: src:se-academy-single-sku-inverter-training-na-technical-01-single-sku-commissioning-update
    loc: sec=h2
    h: d221b0206225
  review: drafted
---
SolarEdge Go is a SolarEdge mobile app that covers installation, management and service work, from a single site up to a whole fleet. It replaces SetApp for commissioning SolarEdge Single SKU residential inverters, and SetApp is due to expire. The app runs on iOS and Android. Power up the inverter, then connect by scanning its QR code. If the scan fails, use the manual commissioning option. During commissioning you select the inverter model and power class in the app. This choice is locked after commissioning, so it must match the label sticker you applied and the plan set approved by the AHJ and utility. The commissioning wizard asks you to create a new Monitoring Platform site for the inverter. You can also choose register later and create the site from the platform afterwards. For backup or standalone systems, set the inverter standalone rating under Power Control in the app menu. Once commissioning is done and the app is connected to the inverter, generate a commissioning report with the site and inverter settings. You can share it with the AHJ or utility to confirm the model and power class. SolarEdge Academy offers a training course on the app.

<!-- review notes
- sentence 5: support check: partial - The app prompts you to create a new site, and you can select register later. The passage ties the register-later option to having an existing site. It calls the prompt part of commissioning in the app, not specifically the wizard, and it says you can create a site or replace an inverter from the platform if you skip.
-->
