---
id: func:remote-firmware-update
type: Function
name: Remote firmware update
aliases:
- OTA update
- automatic firmware update
- remote update
- Automatic Remote Firmware Updates
- over-the-air firmware updates
- FW Upgrade
category: Monitoring
function_kind: monitoring
claims:
- claim_id: c1
  rel: requires
  target: prod:chint-flexom-gateway
  scope:
    products:
    - prod:chint-sch-125ktl-aio
    - prod:chint-sch-275ktl
    - prod:chint-sch-350ktl
    - prod:chint-sca-50-60ktl
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-100k-t
  note: CPS inverters list remote diagnostics and firmware upgrade as standard when the FlexOM Gateway
    is installed; the gateway is sold as an accessory for some models.
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=38.r13
    h: 0d4b8e53d07f
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=31.r6
    h: a836860653de
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=38.r13
    h: a836860653de
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=67.r19
    h: 557187612a54
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: sec=6.10
    h: b156623e2c48
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: sec=3.6.5
    h: 48f05460b386
  review: drafted
  review_note: 'support check: partial - Passages say remote diagnostics/firmware upgrade is standard
    with FlexOM gateway, gateway purchasable as accessory, and remote upgrade if installed; but per-product
    scope coverage isn''t shown for all listed models (only some u-ids), and ''sold as accessory for some
    models'' is only generally stated.'
- claim_id: c2
  rel: requires
  target: tool:fimer-installer-app
  scope:
    products:
    - prod:abb-pvs-166-175-tl-us
  note: One of three alternative paths, the other two being the integrated web UI and Aurora Vision.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=h60
    h: 78b71b354898
  review: drafted
---
Remote firmware update lets you load new inverter or logger firmware over a network connection, so nobody has to bring a USB drive to site. On FIMER and ABB UNO-DM and PVS inverters, you start a remote update from the internal web server: press CHECK to look for the newest firmware on the manufacturer's servers, then press UPDATE. On SMA products, the parameter Upd.AutoUpdIsOn switches automatic updates on or off, with No as the standard setting. You can change it from the device user interface, a System Manager or Sunny Portal. The Sunny WebBox has its own setting under Data transmission. Generac PV Link and the CSI-125KTL-GS-E support over-the-air updates. Generac says installers should still check that the firmware is current and recommends a high-speed internet connection.

<!-- review notes
- sentence 1: support check: partial - Passages support remote firmware update of inverter over network, but nothing about logger firmware or the USB-drive-avoidance claim beyond USB being the local alternative for CPS.
- sentence 2: support check: partial - CHECK then UPDATE in the web server is stated for FIMER/ABB servers, but the passages don't name UNO-DM and PVS models specifically.
- sentence 4: support check: partial - CSI-125KTL-GS-E OTA is stated and Generac's advice is stated for PV Link, but the passage doesn't explicitly say PV Link supports OTA by name beyond 'PV Links' updates; fairly implied, though the advice is about PWRcell systems.
-->
