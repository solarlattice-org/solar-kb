---
id: fm:mounting-structure-defect
type: FailureMode
name: Defective Mounting Structure
aliases:
- PVFS 3-2
- Inappropriate/defect mounting structure
- PVFS 3-2vs.01
category: Mounting
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:high-wind
  note: The structure was not designed for the wind loads typical of the site, for example when it does
    not match the static calculations.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r3
    h: 37b0c9de0af8
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:snow-load
  note: The structure was not designed for the snow loads typical of the site, or the environmental conditions
    were underestimated.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r3
    h: 37b0c9de0af8
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:weak-anchorage
  note: Weak anchoring to the ground or roof, for example when ground conditions were not considered enough
    while choosing the structure. Roof strength for the added load and O&M work may also be left unchecked.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r3
    h: 37b0c9de0af8
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:low-quality-material
  note: Examples are corrosive materials in a corrosive environment, too little galvanisation, or poor
    material from weak quality assurance. These lead to early degradation or mechanical failure.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r3
    h: 37b0c9de0af8
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:installation-error
  note: Examples are missing or non-original components and screws tightened too much or too little.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r3
    h: 37b0c9de0af8
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:dissimilar-metal-contact
  note: Galvanic corrosion where two different metals touch, such as an aluminium frame on a steel structure.
    It often occurs around fastening screws.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:humid-climate
  note: Galvanic corrosion matters most in humid or coastal areas.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  review: drafted
  review_note: 'support check: partial - Passages say galvanic corrosion matters in humid or coastal areas,
    but don''t frame humid climate as a cause of the defect generally.'
- claim_id: c8
  rel: affects
  target: comp:mounting-structure
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r1
    h: ef1e45148c78
  review: drafted
- claim_id: c9
  rel: affects
  target: comp:module-frame
  note: Corrosion of the frame or mounting holes can be seen. A damaged structure also compromises the
    integrity of the modules mounted on it.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r1
    h: ef1e45148c78
  review: drafted
  review_note: 'support check: partial - Corrosion of frame and compromised module integrity are stated,
    but the frame mentioned is on the mounting structure, not clearly the module frame.'
- claim_id: c10
  rel: affects
  target: comp:roof-substructure
  note: The substructure, such as roof insulation, can be compromised. In the worst case the roof collapses.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:bent-or-cracked-structure
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r1
    h: ef1e45148c78
  review: drafted
- claim_id: c12
  rel: presents_as
  target: symptom:visible-corrosion
  note: Corrosion of the frame or the mounting holes.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r1
    h: ef1e45148c78
  review: drafted
- claim_id: c13
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r2
    h: 847604f4d482
  review: drafted
- claim_id: c14
  rel: leads_to
  target: fm:glass-breakage
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  review: drafted
- claim_id: c15
  rel: leads_to
  target: fm:cell-cracks
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  review: drafted
- claim_id: c16
  rel: leads_to
  target: fm:junction-box-failure
  note: The junction box may be damaged or detached.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  review: drafted
- claim_id: c17
  rel: mitigated_by
  target: mit:structural-hardware-repair
  note: 'Corrective action: replace or repair any structure that poses a direct safety risk.'
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r8
    h: e4c63f6979ff
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=31
    h: cc9fed5e1ebd
  review: drafted
- claim_id: c18
  rel: mitigated_by
  target: mit:compatible-mounting-structure
  note: The ground, the mounting structure and the modules must be compatible with each other.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r8
    h: e4c63f6979ff
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=31
    h: cc9fed5e1ebd
  review: drafted
- claim_id: c19
  rel: mitigated_by
  target: mit:proper-installation
  note: Follow the manufacturer's mounting instructions.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r8
    h: e4c63f6979ff
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=31
    h: cc9fed5e1ebd
  review: drafted
- claim_id: c20
  rel: mitigated_by
  target: mit:site-load-check
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r8
    h: e4c63f6979ff
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=31
    h: cc9fed5e1ebd
  review: drafted
- claim_id: c21
  rel: mitigated_by
  target: mit:regular-inspections
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r8
    h: e4c63f6979ff
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=31
    h: cc9fed5e1ebd
  review: drafted
- claim_id: c22
  rel: mitigated_by
  target: mit:mounting-configuration-testing
  note: An accredited laboratory tests non-standard configurations, such as facade mounting.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=49.r8
    h: e4c63f6979ff
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=31
    h: cc9fed5e1ebd
  review: drafted
- claim_id: c23
  rel: mitigated_by
  target: mit:dissimilar-metal-insulation
  note: Required in humid and coastal areas.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h51
    h: a44e0a777296
  review: drafted
---
A defective mounting structure was either never right for the site or has failed. Common causes are design for too little wind or snow load, weak anchoring to the ground or roof, unsuitable or corroding materials, and installation errors. Look for bent or cracked members and for corrosion on the frame or around the mounting holes. Visual inspection is the detection method. Where aluminium and steel touch, check the fastening screws for galvanic corrosion, especially at humid or coastal sites. In those areas the two metals need insulation between them. A failing structure can damage the modules, causing broken glass, cracked cells and damaged junction boxes. In the worst case modules or the whole structure come loose, or the roof collapses, which is a serious danger to people. Replace or repair any structure that poses a direct safety risk. To prevent this failure, use compatible structures, follow the manufacturer's mounting instructions, check local wind and snow loads, and inspect the system regularly. Non-standard configurations should be tested by an accredited laboratory.

<!-- review notes
- sentence 4: support check: partial - Insulation requirement and galvanic corrosion near screws are stated, but an explicit instruction to check screws is not.
-->
