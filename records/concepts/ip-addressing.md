---
id: concept:ip-addressing
type: Concept
name: DHCP and static IP addressing
aliases:
- DHCP
- static IP
- IP address
- static IP address
- dynamic IP address
category: Communication
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: proto:tcp-ip
  note: Static addressing is set from the datalogger's TCP/IP configuration menu.
  cite:
  - src: src:eq-equip-das-alsoenergy-locus-lgate-360-v-1-3
    loc: sec=h18
    h: bd33ca71158b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c2
  rel: related_to
  target: proto:ethernet
  note: DHCP or static mode is selected for the wired LAN port; on the LGate 360 the static option needs
    a CAT5 LAN connection.
  cite:
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=h228
    h: b8822a62d53a
  - src: src:eq-equip-das-alsoenergy-locus-lgate-360-v-1-3
    loc: sec=h18
    h: bd33ca71158b
  review: drafted
- claim_id: c3
  rel: related_to
  target: comp:monitoring-gateway
  note: Dataloggers support DHCP or static IP networking.
  cite:
  - src: src:eq-equip-das-alsoenergy-locus-locus-energy-commercial-pv-monitoring
    loc: tbl=8.r3
    h: 91899c02da17
  - src: src:eq-equip-das-alsoenergy-locus-locus-lgate-360
    loc: tbl=2.r3
    h: 91899c02da17
  - src: src:eq-equip-das-alsoenergy-locus-lgate-360-v-1-3
    loc: sec=h18
    h: bd33ca71158b
  review: drafted
- claim_id: c4
  rel: related_to
  target: fm:monitoring-network-fault
  note: If a static IP is set without reserving it on the router, the result can be duplicate IP addresses
    and intermittent Internet connection problems.
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h96
    h: 328dfcb44952
  review: drafted
- claim_id: c5
  rel: related_to
  target: prod:enphase-envoy
  note: The Envoy can be switched from DHCP to a static IP with the installer toolkit.
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h96
    h: 328dfcb44952
  review: drafted
- claim_id: c6
  rel: related_to
  target: prod:locus-energy-lgate
  cite:
  - src: src:eq-equip-das-alsoenergy-locus-locus-lgate-360
    loc: tbl=2.r3
    h: 91899c02da17
  - src: src:eq-equip-das-alsoenergy-locus-lgate-360-v-1-3
    loc: sec=h18
    h: bd33ca71158b
  review: drafted
- claim_id: c7
  rel: related_to
  target: prod:generac-pwrmanager
  cite:
  - src: src:generac-generac-pwrmanager-owners-manual
    loc: tbl=10.r2
    h: 728c6eb5cf49
  - src: src:generac-generac-pwrmanager-install-manual
    loc: tbl=11.r2
    h: 728c6eb5cf49
  review: drafted
- claim_id: c8
  rel: related_to
  target: concept:scada
  note: SCADA designs assign static IP ranges to devices such as meters and RTACs.
  cite:
  - src: src:tesla-scada-design-manual-v3-4
    loc: tbl=13.r8
    h: b81ef0b04c7e
  - src: src:tesla-scada-design-manual-v3-4
    loc: tbl=13.r9
    h: c9fdb82e3634
  review: drafted
---
Every networked device, such as an inverter, datalogger or gateway, needs an IP address. It gets one either automatically through DHCP or as a fixed static address entered by hand. In DHCP mode the router hands the device a dynamic address each time it joins the network. Many inverters ship with DHCP as the default setting. To use a static address, you enter the IP address, subnet mask, gateway and DNS servers. Get these values from the site's IT administrator, who should set the address up beforehand. A secondary DNS server is usually optional. Secure networks often require each device to have its own assigned address. If DHCP can't be used, a static IP is the fallback. Another option is a DHCP reservation, which ties a fixed address to the device's MAC address. If you set a static IP on a device without also reserving that address on the router, two devices can end up with the same address. This causes intermittent loss of the Internet connection. In larger plants, the SCADA design gives meters and controllers static addresses from planned ranges. Some inverters also report through Modbus whether their address is static or came from DHCP.

<!-- review notes
- sentence 1: support check: partial - DHCP and static options are stated for inverters and dataloggers, but 'every networked device needs an IP address' is a general claim not stated.
- sentence 2: support check: partial - The router assigns a dynamic address and DHCP is the default in the inverter passages, but 'each time it joins' is only loosely supported and 'many inverters' is a generalization.
- sentence 3: support check: partial - The needed fields, the IT administrator source and the optional secondary DNS are stated, but 'usually optional' and the LGate/inverter variations are slightly off.
- sentence 5: support check: partial - The warning says duplicate IPs and intermittent connection problems 'may' result, whereas the statement says it definitely does, and it is Envoy-specific.
- sentence 1: review: partial - DHCP or static addressing is stated for inverters and dataloggers, but the claim that every networked device, gateways included, needs an IP address goes beyond the passages.
-->
