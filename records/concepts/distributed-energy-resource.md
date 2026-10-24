---
id: concept:distributed-energy-resource
type: Concept
name: Distributed energy resource
aliases:
- DER
- distributed generation
- distributed resources
- alternative energy resources
category: Grid
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: std:ieee-1547-2018
  note: IEEE 1547-2018 defines DER and sets interconnection and interoperability requirements for DER
    connected to electric power systems.
  quote: A source of electric power that is not directly connected to a bulk power system.
  quote_source: IEEE 1547-2018 §3.1 (definition of distributed energy resource)
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h35
    h: 6ba6e11f766a
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h324
    h: db541ac9456c
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h38
    h: 2804f0eb796a
  review: drafted
- claim_id: c2
  rel: related_to
  target: std:ieee-1547-2003
  note: In the 2018 edition, the term DER is treated as equivalent to the term distributed resources (DR)
    used in IEEE 1547-2003.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h35
    h: 6ba6e11f766a
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:area-eps
  note: Interconnection is defined as adding DER to an Area EPS, either directly or through Local EPS
    facilities.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h35
    h: 6ba6e11f766a
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:interconnection-process
  note: An authority governing interconnection requirements sets the policies and procedures for connecting
    DER to the Area EPS.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h35
    h: 6ba6e11f766a
  review: drafted
- claim_id: c5
  rel: related_to
  target: comp:battery-storage
  note: Energy storage technologies that can export active power count as DER.
  cite:
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: sec=h384
    h: a79eacb73522
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h35
    h: 6ba6e11f766a
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:demand-response
  note: Controllable loads used for demand response are excluded from the IEEE 1547-2018 definition of
    DER.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h35
    h: 6ba6e11f766a
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:cease-to-energize
  note: Under IEEE 1547-2018, clearing time is measured until the DER ceases to energize the Area EPS.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h35
    h: 6ba6e11f766a
  review: drafted
- claim_id: c8
  rel: related_to
  target: concept:virtual-power-plant
  note: In some neighborhoods, many small residential PV systems add up to virtual power plants of several
    megawatts.
  cite:
  - src: src:iea-pvps-t13-07-2017
    loc: sec=1
    h: 6071f58ccb27
  review: drafted
- claim_id: c9
  rel: related_to
  target: proto:sunspec-information-model
  note: SunSpec is an application-layer protocol that lets DER components interoperate with smart grid
    applications.
  cite:
  - src: src:eq-equip-inverters-solaredge-sunspec-implementation-technical-note
    loc: sec=h6
    h: f3e6a1d65ba4
  review: drafted
- claim_id: c10
  rel: related_to
  target: org:nerc
  note: A February 2017 NERC task force report covers DER connection, modeling and impacts on bulk system
    reliability.
  cite:
  - src: src:ref-standards-ieee-ieee-1547-2018-highlights
    loc: sec=h71
    h: b3019abcbf75
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h263
    h: 18d0c0b8cfbf
  review: drafted
---
A distributed energy resource (DER) is a source of electric power that is not directly connected to the bulk power system. DER covers both generators and energy storage that can export active power to an electric power system, and it also includes any interconnection system or supplemental device needed for compliance. DER are usually small to medium generation sources, such as PV systems, battery storage, wind, engine generators, gas turbines, hydro, fuel cells and microturbines. Controllable loads used for demand response do not count as DER. IEEE 1547-2018 sets the interconnection and interoperability requirements for DER connected to the Area EPS, and utilities publish their own requirements for distributed generation operating in parallel with their systems. Many small residential PV systems can add up to a virtual power plant, and their weather-driven output makes reserve planning and voltage and frequency control harder for the grid operator. Communication protocols such as SunSpec let DER equipment interoperate with smart grid applications, and a DER managing entity such as a utility or aggregator can monitor and manage the DER through its local communication interface.

<!-- review notes
- sentence 5: support check: partial - The 1547-2018 title supports interconnection and interoperability requirements, but the utility-publishes-own-requirements part rests only on a title-only National Grid/Massachusetts passage with no text.
-->
