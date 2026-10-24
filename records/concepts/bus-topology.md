---
id: concept:bus-topology
type: Concept
name: Daisy-chain and star topology
aliases:
- daisy chain
- star topology
- Linear daisy chain
- Star connection
- Star configuration
- Daisy chain configuration
- Daisy Chain Wiring
- Daisy chain topology
category: Communication
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: proto:ethernet
  note: Inverter Ethernet networks can be wired as a linear daisy chain, a star around an Ethernet switch,
    or a ring.
  cite:
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=46
    h: 0ea60d475ba2
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=44.r9
    h: c2a1c2dde822
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h83
    h: ab1fc026555f
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:inverter
  note: Several inverters are linked to each other or to a switch in daisy-chain or star layouts.
  cite:
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=46
    h: 0ea60d475ba2
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h83
    h: ab1fc026555f
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: fig=74
    h: 4a4304fbedcc
  review: drafted
---
Daisy-chain and star are two ways of wiring devices such as inverters onto a communication network. In a linear daisy chain, each device connects to the next one in a line. In a star topology, every device has its own link back to a central Ethernet switch or router. Some inverters support star, ring and daisy-chain layouts on their Ethernet port. Ring layouts are only allowed when spanning tree is in use. Because a single fault can cut off devices further down a daisy chain, one manual recommends connecting both the first and the last inverter to the local switch to form a ring, so every inverter stays reachable. Daisy chaining can mean fewer network switches: one meter web module allows up to 32 devices on one switch using RSTP, with each device given its own IP address, either set manually or assigned by the network. Installation guides from gateway, inverter and monitoring vendors show the correct daisy-chain wiring, so check the manufacturer drawing before wiring a chain. Do not confuse this with module wiring: daisy chain wiring also describes connecting PV modules in a series string one after another, which is different from leapfrog wiring.

<!-- review notes
- sentence 2: support check: partial - Passages name and depict the topologies but do not describe in words that each device connects to the next or that each has its own link to a central switch.
- sentence 4: support check: partial - Ring recommendation by connecting first and last inverter to the switch is stated for fault presence, but the explicit reasoning about a single fault cutting off downstream devices is only partly present.
- sentence 5: support check: partial - Up to 32 devices, RSTP, one switch, and IP addressing are stated, but 'meter web module' is not identified in the passage and 'fewer switches' matches only loosely.
- sentence 6: support check: partial - Figures of daisy chain wiring exist in several manuals, but vendor types and the advice to check the manufacturer drawing are not stated.
- sentence 7: support check: partial - Passage shows conventional daisy chain wiring of modules in a series string versus leapfrog wiring, but does not say they are different in the stated terms or explicitly warn about confusion; the series-string-in-order claim is only implied.
-->
