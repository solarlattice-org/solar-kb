---
id: concept:grounding-electrode-system
type: Concept
name: Grounding electrode system
aliases:
- GEC
- grounding electrode conductor
- earth electrode
- Earth Grounding Electrode
category: Safety
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:equipment-grounding
  note: PV array equipment grounding conductors connect to the grounding electrode system of the supporting
    building or structure.
  cite:
  - src: src:std-standards-nec-2017-nec2017-690
    loc: sec=h25
    h: 7c78d6bce279
  - src: src:std-standards-nec-2017-nec-2017-690-solar
    loc: sec=h18
    h: 4b2e62ca545b
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: sec=h191
    h: b2b150974526
  review: drafted
- claim_id: c2
  rel: related_to
  target: func:ground-fault-protection
  note: For PV systems that are not solidly grounded, the output equipment grounding conductor may serve
    as the connection to ground for ground-fault protection.
  cite:
  - src: src:std-standards-nec-2017-nec2017-690
    loc: sec=h25
    h: 7c78d6bce279
  - src: src:std-standards-nec-2017-nec-2017-690-solar
    loc: sec=h18
    h: 4b2e62ca545b
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h111
    h: 0e2ddb8366bb
  review: drafted
- claim_id: c3
  rel: related_to
  target: arch:functionally-grounded-pv-array
  cite:
  - src: src:std-standards-nec-2017-nec2017-690
    loc: sec=h25
    h: 7c78d6bce279
  - src: src:std-standards-nec-2017-nec-2017-690-solar
    loc: sec=h18
    h: 4b2e62ca545b
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h111
    h: 0e2ddb8366bb
  review: drafted
  review_note: 'support check: partial - The passages discuss functional grounded systems only in an informational
    note about the ac EGC connection, and do not clearly state how the grounding electrode system relates
    to the functionally grounded array.'
- claim_id: c4
  rel: related_to
  target: arch:grounded-pv-array
  note: In solidly grounded PV systems the grounded conductor connects to the electrode system through
    a GEC sized per 250.166.
  cite:
  - src: src:std-standards-nec-2017-nec2017-690
    loc: sec=h25
    h: 7c78d6bce279
  - src: src:std-standards-nec-2017-nec-2017-690-solar
    loc: sec=h18
    h: 4b2e62ca545b
  review: drafted
- claim_id: c5
  rel: related_to
  target: std:ul-1741
  note: UL 1741 requires a marked GEC connection point where an inverter or charge controller bonds the
    grounded dc conductor to the grounding system.
  cite:
  - src: src:std-standards-nec-2014-nec2014-690-solar
    loc: sec=h21
    h: a8f72658843f
  - src: src:std-standards-nec-2014-nec2014-690
    loc: sec=h23
    h: aad4ac72bbcb
  - src: src:std-standards-nec-2011-2011-nec2011-690
    loc: sec=h28
    h: 6ea4528217b3
  review: drafted
- claim_id: c6
  rel: related_to
  target: prod:sma-stp-tl-us
  note: The inverter has a DC-side grounding terminal with a connection point labeled GEC for extra grounding,
    such as a grounding electrode.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=6.3.3
    h: 847d5ba35c00
  review: drafted
---
A grounding electrode system is the set of electrodes that ties the electrical system and equipment grounds to the earth, and they are connected to it by a grounding electrode conductor (GEC). Common electrodes include a metal underground water pipe, the building's metal frame, a concrete-encased electrode (also called a Ufer ground), a copper ground ring, and driven rods or buried plates. Whichever ones are present must be bonded together into one system. A metal water pipe counts as an electrode only if it is in direct contact with the earth for at least 10 ft, and it must be supplemented by at least one other electrode because the piping may be or later become plastic. Most PV systems are functionally grounded rather than solidly grounded. In those systems the ac equipment grounding conductor to the distribution equipment can act as the connection to ground for ground-fault protection and for equipment grounding of the array. Extra auxiliary electrodes are allowed at ground-mounted and roof-mounted arrays and may connect straight to the array frame or structure. A ground-mount structure can itself count as an electrode if it meets 250.52. Inverters often have a marked GEC terminal on a grounding busbar for this connection. Soil conditions affect how the system is designed: sandy or gravelly soil has high resistivity and needs multiple electrodes for lightning grounding.

<!-- review notes
- sentence 3: support check: partial - The passage calls a water pipe in direct contact with the earth for 10 ft the preferred electrode and says it must be supplemented by another, citing plastic piping. It does not say the pipe counts as an electrode only if it meets the 10 ft contact.
-->
