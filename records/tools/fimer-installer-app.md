---
id: tool:fimer-installer-app
type: Tool
name: FIMER Installer app
aliases:
- FIMER Installer
- FIMER Installer for Solar Inverters
- Installer for Solar Inverters
category: Apps
tool_kind: app
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:fimer
  note: Described as FIMER's own advanced mobile app for its string inverters.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h163
    h: d4932b435963
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=7.2.1
    h: e6777c79f152
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: sec=11.1
    h: b1d4806f08bb
  review: drafted
---
The FIMER Installer app is FIMER's mobile app for commissioning, setting parameters on and troubleshooting FIMER string inverters, especially when a large solar plant has many inverters. FIMER recommends it as the commissioning tool for both multi-inverter plants and single-inverter installations. The app can set system settings on several inverters at once and update inverter firmware. It is one of the routes for remote firmware updates, along with the inverter's built-in web interface and Aurora Vision. For export limitation setup, you use the app to add devices and to turn on and configure the fallback plan. With the fallback plan active, each inverter holds a fallback setpoint if it loses communication with the export meter or cannot reach the export limit. The app runs on Android 6.0.1 or later and is installed from the Play Store. The manuals say iOS support is planned but not yet available. FIMER manuals warn not to do anything to the inverter while a firmware update is running, because interrupting it could damage the inverter.

<!-- review notes
- sentence 4: support check: partial - The fallback plan is enabled/configured in the app and the fallback behavior is stated, but the passages don't clearly say the app is used to add devices (only a figure caption on device acquisition); also fallback triggers are as stated.
-->
