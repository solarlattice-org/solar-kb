---
id: tool:sma-sunny-explorer
type: Tool
name: SMA Sunny Explorer
aliases:
- Sunny Explorer
- Explorer-BA
- SE
category: Software
tool_kind: software
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  note: Offered free of charge from the SMA download area; the manual names SMA Solar Technology AG.
  cite:
  - src: src:sma-doc-262631
    loc: sec=8.2
    h: 12f517e1e0e6
  - src: src:sma-doc-279088
    loc: sec=2.1
    h: c64f290f9700
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:speedwire
  note: Wired connection through the computer's network port; select Speedwire as the communication type
    for US models.
  cite:
  - src: src:sma-doc-279088
    loc: sec=2.1
    h: c64f290f9700
  - src: src:eq-equip-inverters-sma-communications-explorer-ba-en-18
    loc: sec=2.1
    h: 4869ded9cbb3
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h60
    h: 4f16663e94bf
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:bluetooth
  note: Wireless connection; the computer needs Bluetooth, built in or through a USB stick. Sunny Explorer
    acts as the master device in the Bluetooth network. A US guide says not to select Bluetooth for US
    models.
  cite:
  - src: src:sma-doc-279088
    loc: sec=2.1
    h: c64f290f9700
  - src: src:eq-equip-inverters-sma-communications-explorer-ba-en-18
    loc: sec=2.1
    h: 4869ded9cbb3
  review: drafted
---
Sunny Explorer is free SMA software for Windows computers. It shows and manages the data of SMA Bluetooth or Speedwire systems and can configure one device or whole device classes. It manages up to 50 devices on a Bluetooth or Speedwire network. Inverters with the Webconnect function work with it from software version 1.04. To find a Speedwire-Webconnect plant, plug the laptop into the same LAN as the inverters with the network adapter set to obtain an address automatically. Then choose Enter a new plant, select Speedwire, and log in as Installer with the plant password (default 1111). With it you can review grid parameters under Settings > Grid Monitoring and export daily, monthly or event data to CSV under Tools > Export Data. As Installer you can also enter the SMA Grid Guard code under Options > SMA Grid Guard, and you leave Grid Guard mode by closing the program. It shows inverter event numbers and firmware versions, for example on Sunny Boy 240 and Sunny Multigate systems. Do not use it to configure inverters that have their own built-in web interface, such as the Sunny Boy 1.5/2.5. Do not use its data for billing. Only qualified people may use the Installer group. Wrong settings can damage the inverter, and safety-related grid settings should only be changed after talking to the grid operator. Before opening the inverter's lower lid to plug in a cable, switch off AC and then DC and wait at least five minutes for the capacitors to discharge. Installing the software needs Windows administrator rights, .NET Framework 4.0, and a restart afterwards.

<!-- review notes
- sentence 4: support check: partial - Grid Monitoring, Tools > Export Data, Options > SMA Grid Guard and exiting by closing are supported, but the passages never say the Grid Guard step is available only to the Installer group beyond the requirement being Installer login (that is stated); the 'Settings > Grid Monitoring' path is stated as tab Settings and menu item Grid Monitoring, so the minor gap is the 'monthly/daily/event' wording being fine—overall mostly supported but exiting Grid Guard 'by closing' is stated; the only weakness is the nuance of 'review' being under Settings, which is acceptable.
- sentence 5: support check: partial - Passages say event numbers and firmware versions appear in Sunny Portal or Sunny Explorer for SB240-10/Multigate, but the firmware version is stated as viewable in Sunny Explorer and event numbers displayed, which matches; the 'shows' claim is supported, though only for those specific systems' examples.
-->
