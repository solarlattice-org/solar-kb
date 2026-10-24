---
id: tool:chint-cps-connect-app
type: Tool
name: CPS Connect App
aliases:
- CPS Connect
- Chint Power Systems Connect
- Chint Power Connect
category: Apps
tool_kind: app
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:chint
  cite:
  - src: src:eq-equip-inverters-chint-comm-gateway-cps-connect-app-user-manual
    loc: sec=h5
    h: 24e3ae17b0e9
  - src: src:eq-equip-inverters-chint-comm-gateway-cps-connect-app-user-manual
    loc: sec=1
    h: 41465d718b87
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:wifi
  note: The phone joins a local Wi-Fi network created by the Wi-Fi module attached to the Flex Gateway
    or inverter.
  cite:
  - src: src:eq-equip-inverters-chint-comm-gateway-cps-connect-app-user-manual
    loc: sec=h5
    h: 24e3ae17b0e9
  - src: src:eq-equip-inverters-chint-100-125-kw-inverter-chint-cps-sch100-125ktl-do-us-600-manual
    loc: tbl=6.r8
    h: bef7f8cbba1f
  review: drafted
  review_note: 'support check: partial - Passages say the Wi-Fi module creates a local Wi-Fi network for
    the app, but they don''t mention a phone joining it or that the module attaches to an inverter as
    well as the Flex Gateway.'
---
The CPS Connect app is a CHINT Power Systems mobile app for setting up and programming the Flex Gateway communications equipment wirelessly in the field. It is meant for installers, operations and maintenance staff, and other site personnel. Each Flex Gateway comes with a Wi-Fi module that sets up a local Wi-Fi network. Once the phone is connected to it, the app can program every inverter on the Modbus daisy chain. The app is one of four parts of the CPS data and controls system. The other three are standard inverter Modbus communications, the optional Flex Gateway communications card and the CPS Service Web Portal. You can download it from the Apple iOS store or the Google store for Android, or by scanning the QR code in the user manual with a phone that has internet access. For local programming, newer FlexOM Gateway documents point to the CPS Connect Pro app on iOS and Android instead.
