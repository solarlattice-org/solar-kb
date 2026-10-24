---
id: concept:protection-coordination
type: Concept
name: Protection coordination
aliases:
- relay coordination
- selectivity
- selective coordination
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:overcurrent-protection
  note: Coordination studies set the types, characteristics, settings and ratings of overcurrent protective
    devices.
  cite:
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: tbl=1.r31
    h: a6c0cf2be947
  - src: src:std-standards-neta-ats-ats-13
    loc: sec=6.2
    h: 28692410f1ca
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:ac-circuit-breaker
  note: Breaker trip units must be set so that pickup thresholds stay nested from one tier to the next.
  cite:
  - src: src:ref-standards-nfpa-selectivity-2018-r06-rcep
    loc: sec=h8
    h: ea60b6fffbeb
  - src: src:ref-standards-nfpa-06634249-advances-in-ocpd-zsi-iast-2014
    loc: sec=h12
    h: 110018c7e858
  review: drafted
- claim_id: c3
  rel: related_to
  target: hazard:ac-arc-flash
  note: Selectivity can force upstream breakers to be less sensitive to low-magnitude arcing faults.
  cite:
  - src: src:ref-standards-nfpa-selectivity-2018-r06-rcep
    loc: sec=h4
    h: 8bc77f946a5f
  - src: src:ref-standards-nfpa-06634249-advances-in-ocpd-zsi-iast-2014
    loc: sec=h12
    h: 110018c7e858
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:single-line-diagram
  note: Coordination studies need a one-line diagram, and their reports include one.
  cite:
  - src: src:std-standards-mv-committee-ieee-standards-mv-equipment-ieee-std-c37-246-2017-protection-systems-of-t
    loc: sec=6.4
    h: ce647f1edbd9
  - src: src:std-standards-neta-ats-ats-13
    loc: sec=6.2
    h: 28692410f1ca
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:automatic-reclosing
  note: Sequence coordination aligns substation breakers with downstream reclosers and fuses.
  cite:
  - src: src:eq-equip-relays-reclosers-ieee-seminar-fundamentals-of-modern-protective-relaying-part1
    loc: sec=h211
    h: 6a797b1202c0
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:distributed-energy-resource
  note: High PV penetration can change fault current levels, so existing distribution protection coordination
    needs review.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=2.5
    h: 5f5869ed077c
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.3.5
    h: ea00e42abfe9
  review: drafted
---
Protection coordination, also called selectivity or selective coordination, means setting protective devices so that the device closest to a fault clears it and the devices upstream wait. A coordination study takes the device settings, including CT and VT ratios, puts them into a short-circuit model of the system and works out the clearing times for each zone of protection. The results are shown as time-current curves, fuse selectivity ratios or breaker selectivity tables. Some fuse families only need a 2:1 amp-rating ratio between upstream and downstream fuses to be selective. Curves need a time margin between them to allow for timing errors, relay overshoot and CT errors. One relaying seminar gives a typical coordination time of 0.4 s for electromechanical relays and 0.3 s for digital relays. There is a trade-off: keeping upstream breakers selective can make them slow or less sensitive to low arcing currents. Methods such as zone-selective interlocking try to give both fast protection and selectivity. When coordination cannot be complete, the study aims to get as much selectivity as possible while still protecting the equipment. In PV work, a high share of PV on a feeder can change fault current levels, so the utility may need to review existing protection coordination before it approves an interconnection.

<!-- review notes
- sentence 1: support check: partial - Passages discuss coordination and fault clearing sequence, but none state the definition that the closest device clears the fault while upstream devices wait, nor the synonyms selectivity.
- sentence 4: support check: partial - The 0.4 s and 0.3 s coordination times and error sources are supported, but the 'relaying seminar' attribution is not in the passages.
- sentence 7: support check: partial - High PV changing fault current and requiring coordination review is supported, but the utility reviewing before approving interconnection is not explicitly stated.
-->
