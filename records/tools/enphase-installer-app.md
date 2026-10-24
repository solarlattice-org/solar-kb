---
id: tool:enphase-installer-app
type: Tool
name: Enphase Installer App
aliases:
- Enphase Installer Toolkit
- Installer App
- Installer Toolkit App
- Enlighten Installer Toolkit
- ITK
category: Apps
tool_kind: app
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:enphase
  note: Source metadata lists the make as Enphase.
  cite:
  - src: src:kb-enphase-how-to-update-the-software-of-an-iq-gateway-using-the-enphase-installer-app
    loc: sec=front
    h: 586a17cf4ae4
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-4017
    loc: sec=front
    h: aa90636c7a11
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:wifi
  note: The mobile device connects to the Envoy-S either through the site's wireless router on the same
    LAN or through a wireless access point that the Envoy-S creates.
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h65
    h: 912a9bbef16e
  review: drafted
---
The Enphase Installer App is a mobile app for iOS and Android that lets installers set up an Enphase system on site without a laptop. Its earlier name was Enlighten Installer Toolkit. You log in with your Enphase account, scan the microinverter serial numbers and connect to the IQ Gateway (Envoy) to track how the installation is going. To connect to the gateway, put the phone on the same LAN through the site's wireless router, or use the access point that the gateway creates. The app is used to commission commercial Enphase systems, provision and scan for devices, check microinverter status in the Validation step, check PLC noise levels, set up a replacement IQ Gateway and update IQ Gateway software. Before going to site, make sure the app is on the latest version and download the applicable IQ Gateway software from Menu, then Settings. During commissioning the app picks the right software release for the site's devices and configuration. The older Installer Toolkit version needed Android 5 or later, or iOS 8 or later.
