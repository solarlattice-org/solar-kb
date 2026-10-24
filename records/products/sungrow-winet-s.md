---
id: prod:sungrow-winet-s
type: Product
name: Sungrow WiNet-S
aliases:
- WiNet-S
category: Monitoring and communications
make: sungrow
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:communication-module
  note: Listed alongside the Eye and WiFi modules as an optional communication module for the inverter.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=7.1
    h: c61dccd5c719
  review: drafted
- claim_id: c2
  rel: manufactured_by
  target: org:sungrow
  note: Named as an optional module in a Sungrow inverter manual and in a Sungrow knowledge-base article.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=7.1
    h: c61dccd5c719
  - src: src:kb-sungrow-battery-device-in-the-power-station-can-not-be-displayed-as-a-separate-device-i
    loc: sec=h1
    h: dbf205e3c68f
  review: drafted
  review_note: 'support check: partial - Passages name WiNet-S as a module in an iSolarCloud/inverter
    manual and a KB article, but never state explicitly that Sungrow makes it (implied only by context).'
- claim_id: c3
  rel: implements
  target: func:remote-maintenance
  note: Lets the iSolarCloud App connect to the inverter over mobile data or WiFi for remote maintenance
    instead of near-end Bluetooth access.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=7.1
    h: c61dccd5c719
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c4
  rel: uses_protocol
  target: proto:wifi
  note: The source says the App connects over mobile data or WiFi through the Eye, WiFi or WiNet-S modules.
    It does not say which path belongs to which module.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=7.1
    h: c61dccd5c719
  review: drafted
  review_note: 'support check: partial - Passage mentions WiFi connection via the modules but does not
    say WiNet-S specifically uses Wi-Fi; the statement''s own note admits this.; review: partial - The
    passage says the App connects over mobile data or WiFi through the Eye, WiFi or WiNet-S modules, but
    it does not say WiNet-S itself uses Wi-Fi.'
---
With the module installed, the iSolarCloud App can reach the inverter over mobile data or WiFi for remote maintenance, rather than only over local Bluetooth. The inverter manual covers only Bluetooth maintenance and refers to the module's own manuals for remote setup. If a battery does not appear as a separate device in the iSolarCloud web portal, check that the WiNet-S firmware is higher than P012, the battery firmware is higher than V12, and the inverter firmware is the latest version. Upgrade any that are not. If the battery still does not show after all devices are upgraded, contact Sungrow customer service.
