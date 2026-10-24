---
id: concept:pv-hazard-control
type: Concept
name: PV hazard control
aliases:
- PVHCS
- PV hazard control system
- PV FHC
- Photovoltaic Hazard Control
category: Safety
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: std:ul-3741
  note: UL 3741 is the standard used to evaluate PV hazard control components, equipment and systems.
  cite:
  - src: src:solis-ul3741-commercial-implementation-guide-pe-tb-0001-r00
    loc: sec=h2
    h: 8d4f642e59d2
  - src: src:std-standards-nec-2020-nec-2020-690
    loc: sec=h66
    h: 76108b790475
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h48
    h: d7e4bde5a07d
  - src: src:solis-ul3741-commercial-implementation-guide-pe-tb-0001-r00
    loc: sec=h11
    h: 1d560fe853bb
  - src: src:solis-ul3741-commercial-implementation-guide-pe-tb-0001-r00
    loc: sec=h12
    h: debcafe0ad5d
  review: drafted
- claim_id: c2
  rel: related_to
  target: req:nfpa-70-2023-690-12
  scope:
    standard: std:nfpa-70-2023
  note: The 2020 and 2023 NEC both allow a listed PVHCS for rapid shutdown inside the array boundary.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h48
    h: d7e4bde5a07d
  review: drafted
- claim_id: c3
  rel: related_to
  target: func:rapid-shutdown
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h48
    h: d7e4bde5a07d
  - src: src:std-standards-nec-2020-nec-2020-690
    loc: sec=h66
    h: 76108b790475
  - src: src:solis-ul3741-commercial-implementation-guide-pe-tb-0001-r00
    loc: sec=h11
    h: 1d560fe853bb
  review: drafted
- claim_id: c4
  rel: related_to
  target: comp:rapid-shutdown-initiator
  note: When a hazard control system needs initiation to reach its controlled state, the rapid shutdown
    initiation device performs it.
  cite:
  - src: src:std-standards-nec-2020-nec-2020-690
    loc: sec=h66
    h: 76108b790475
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h48
    h: d7e4bde5a07d
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:array-boundary
  cite:
  - src: src:std-standards-nec-2020-nec-2020-690
    loc: sec=h66
    h: 76108b790475
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h48
    h: d7e4bde5a07d
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:listed-equipment
  cite:
  - src: src:std-standards-nec-2020-nec-2020-690
    loc: sec=h66
    h: 76108b790475
  review: drafted
- claim_id: c7
  rel: related_to
  target: hazard:electric-shock
  note: PV hazard control reduces shock hazard from energized circuits in a damaged PV array during firefighting.
  cite:
  - src: src:solis-ul3741-commercial-implementation-guide-pe-tb-0001-r00
    loc: sec=h2
    h: 8d4f642e59d2
  - src: src:std-standards-nec-2020-nec-2020-690
    loc: sec=h66
    h: 76108b790475
  review: drafted
- claim_id: c8
  rel: related_to
  target: prod:generac-pwrcell-inverter
  note: Listed as UL 3741 PVHCE; may be installed as part of a PVHCS.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h17
    h: 1bd168492dc0
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h48
    h: d7e4bde5a07d
  review: drafted
- claim_id: c9
  rel: related_to
  target: prod:generac-pv-link
  note: The S2502HC PV Link is UL 3741 listed PVHCE.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h48
    h: d7e4bde5a07d
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h17
    h: 1bd168492dc0
  review: drafted
---
PV hazard control is a way of reducing electric shock hazard from energized PV equipment and circuits inside a PV array, so firefighters can stay out of hazardous current paths. A PV hazard control system can be one piece of equipment or several coordinated pieces, and it is evaluated to UL 3741. Under the 2020 and 2023 NEC, a listed PV hazard control system is one of the permitted methods for meeting rapid shutdown requirements inside the array boundary. If the system needs a trigger to reach its controlled state, the rapid shutdown initiator performs that initiation. A typical system can include modules, approved racking, inverters, rapid shutdown components, wire management, conduit, and compliance placards. Install the system exactly as its listing instructions say, and replace parts only with certified hazard control equipment that carries the same or better ratings, or the system may no longer be compliant. Check with the local utility and the authority having jurisdiction about which compliance method they prefer.
