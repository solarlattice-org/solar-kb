---
id: symptom:loose-cable-connection
type: Symptom
name: Loose cable connection
aliases:
- loose or untightened cables
- loose connection
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-hot-connection
  note: In IR images, a cable connection that runs clearly hotter than the wire itself points to a loose
    or corroded joint. Examples include an overheated string inverter AC cable and overheated cable-lug
    or cross-bar joints in DC combiner boxes, one of them caused by a loose screw.
  quote: If the connections are hotter, check to see if the connection has come loose or is corroded.
  cite:
  - src: src:iec-62446-1
    loc: sec=7.3.3.5
    h: ca1cdf780ae1
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: fig=31
    h: 49da710a318e
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.1.5
    h: 6f6486a9928e
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:network-comm-alert
  note: For communication cabling, a LAN or Ethernet disconnected message is linked to a physical cable
    connection fault. The fix is to check the pin-out assignment and the cable connection.
  cite:
  - src: src:solaredge-se-commercial-3ph-inverter-w-synergy-tech-installation-guide-pn-sexxk
    loc: tbl=10.r1
    h: 041690fed0d0
  - src: src:solaredge-solaredge-gateway-installation-guide
    loc: tbl=9.r1
    h: b7935920264c
  review: drafted
---
A loose cable connection is a terminal or joint that has not been tightened properly or has worked loose. It can be in the inverter wiring box, an AC or DC cable, or a DC combiner box. The clearest sign is in an infrared image: the connection runs noticeably hotter than the cable next to it. In combiner boxes, overheating usually comes from a loose joint at the internal cross bar or a badly compressed cable lug. In one case it was simply a loose screw. A hot joint can also mean corrosion rather than looseness, so look at the contact surfaces as well as checking the torque. On communication cabling, a LAN or Ethernet disconnected message points to a physical connection fault. Check the pin-out and the plug seating. Inverter manuals call for checking all cable connections about every six months, or at least once a year. Isolate and lock out the AC and DC sources first and confirm no voltage is present. Tighten loose cables to the torque given in the manual. Also check the cable jacket for scratches or damage, and repair or replace the cable if needed.

<!-- review notes
- sentence 1: support check: partial - Loose cables in the wiring box, AC cable and DC combiner box are supported, but the definition (not tightened properly or worked loose) is only implied and DC cable generally isn't stated.
- sentence 4: support check: partial - Corrosion as an alternative cause is stated, but advice to inspect contact surfaces is not explicitly given.
- sentence 5: support check: partial - Physical connection fault and checking pin-out and cable connection are stated, but plug seating is not specifically mentioned.
- sentence 7: support check: partial - Tightening, checking cable damage and repair/replace are stated, but the torque to follow is only referenced to the manual, and the 'jacket' is described as the cable surface.
-->
