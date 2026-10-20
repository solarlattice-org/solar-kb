---
id: symptom:degraded-network-link
type: Symptom
name: Degraded network link
claims:
- claim_id: c1
  rel: observed_as
  target: meas:network-status-half
  note: SMA inverter network status shown as [Half]. The fixes listed are checking the Ethernet cable
    and connectors and checking that the DHCP server (router) and switches show correct operation.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h312
    h: d792c604460a
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h229
    h: d792c604460a
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:network-overloaded-message
  note: 'SMA message ''[Interface]: network overloaded''. No data is exchanged between devices.'
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h214
    h: 059ce03933b4
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:no-dhcp-message
  note: The SolarEdge 'No DHCP' message points to an IP settings issue. Check the router and its configuration.
  cite:
  - src: src:solaredge-se-commercial-3ph-inverter-w-synergy-tech-installation-guide-pn-sexxk
    loc: tbl=10
    h: 92bd7cab887c
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:network-comm-alert
  note: A monitoring-platform rule that flags common communication problems on devices connected over
    TCP and RS-485, to identify local network failures.
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=11.r4
    h: 0b0e0447d7ec
  review: drafted
---
A degraded network link appears as inverter or monitoring messages showing that data exchange over Ethernet or the local network is partial or has stopped. On SMA inverters, the network status may read Half, or the interface may report that the network is overloaded and no data is exchanged between devices. On SolarEdge inverters, a failed ping to the router shows as Gateway not responding, and a No DHCP message points to IP settings rather than cabling. Monitoring platforms can raise a network communication alert when devices on TCP or RS-485 show common communication problems. First check that the network cable and connectors are undamaged and fully plugged in, and that the link LED on the router or switch is lit. If the link LED is not lit, replace the cable or change it from a crossover to a straight connection. If the physical link is fine, review the router, DHCP and switch status with the site network IT.

<!-- review notes
- sentence 1: support check: partial - Overloaded message states no data exchange, but the [Half] passages only give corrective measures and don't state partial data exchange; generalization is loose.
- sentence 2: support check: partial - Overloaded message is stated, but the passages never describe what Half means beyond corrective measures, and are not explicitly tied to SMA inverters in the text.
- sentence 3: support check: partial - Gateway not responding = ping to router failed and No DHCP = IP settings issue are stated, but 'rather than cabling' is an inference and SolarEdge isn't named.
-->
