---
id: tool:laptop-commissioning
type: Tool
name: Commissioning laptop
aliases:
- laptop with Ethernet port
- service laptop
- laptop
- end device
- computer
category: Instruments
tool_kind: instrument
claims:
- claim_id: c1
  rel: uses_protocol
  target: proto:ethernet
  note: The laptop connects to the inverter's Ethernet module, the controller's LAN port or the logger's
    network cable through its own Ethernet port.
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: sec=h98
    h: 87be1242bc1a
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: sec=h97
    h: 87be1242bc1a
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: sec=h93
    h: 6dc705cc1f78
  - src: src:man-alsoenergy-running-a-network-test-on-a-logger
    loc: sec=h1
    h: 2787af9236e5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h191
    h: 98d547ae766b
  review: drafted
  review_note: 'review: partial - The passages back Ethernet use: a laptop is required for Ethernet commissioning,
    cabled to the inverter''s Ethernet module or the logger''s network cable, but none mentions a controller''s
    LAN port.'
- claim_id: c2
  rel: uses_protocol
  target: proto:bluetooth
  note: A laptop with Bluetooth running Sunny Explorer acts as master; a Class 1 USB Bluetooth stick can
    be added to reach longer distances.
  cite:
  - src: src:eq-equip-inverters-sma-communications-bt-ten100511
    loc: tbl=3.r5
    h: b9d760ceeca7
  - src: src:eq-equip-inverters-sma-communications-bt-ten100511
    loc: sec=h58
    h: c21bf8a5486f
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: 'support check: partial - Laptop with Bluetooth and Sunny Explorer as master and Class
    1 USB stick for large distances are stated, but ''acts as master'' fits and ''longer distances'' is
    fine; the passages don''t explicitly say Bluetooth is the commissioning protocol link, though implied.'
- claim_id: c3
  rel: uses_protocol
  target: proto:rs485
  note: Through a USB to RS485 converter, used with Delta Solar System software to check inverter settings.
  cite:
  - src: src:eq-equip-inverters-delta-heco-information-hawaii-delta-introduction-of-heco-rule14-default-setting-2
    loc: sec=h3
    h: 3bd9659c4cd2
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
A commissioning laptop is a field computer used to set up and check inverters, controllers and data loggers on site. Some inverter manuals require a laptop for on-site commissioning over Ethernet. If the router does not hand out IP addresses automatically, connect the laptop straight to the inverter's Ethernet module with a cable, give the laptop a fixed IP and open the module's address in a web browser. Some SMA products must be wired directly to a laptop or similar device that has an Ethernet port. For Tesla systems, the laptop plugs into the System Controller's LAN 2 port after its IP address has been set. For a logger network test, plug the logger's own network cable into the laptop, copy the logger's exact network settings and try to load websites. If the laptop gets online, the logger is likely at fault. If it cannot, suspect the network or the cable. With a USB to RS485 converter and Delta Solar System software, the laptop can read back inverter values after the initial setup. A laptop with Bluetooth running Sunny Explorer can act as the master device. A Class 1 USB Bluetooth stick gives more range through walls, but the laptop's built-in adapter should then be turned off. Bluetooth communication drains the laptop battery faster, so plan for this on long site visits.

<!-- review notes
- sentence 3: support check: partial - Direct connection to an end device with Ethernet interface and Tesla LAN 2 with laptop IP config are stated, but the evidence doesn't say the first requirement is for SMA products explicitly, and order 'after IP set' is loosely stated.
- sentence 7: support check: partial - Passage says battery running time is shortened during Bluetooth communication; the advice to plan for long site visits is an added inference.
- sentence 7: review: partial - The passage says battery running time is shortened during Bluetooth communication, but the advice to plan for long site visits is an added inference.
-->
