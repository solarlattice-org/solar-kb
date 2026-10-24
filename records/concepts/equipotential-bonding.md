---
id: concept:equipotential-bonding
type: Concept
name: Equipotential bonding
aliases:
- potential equalization
- equipotential connection
category: Safety
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: comp:mounting-structure
  note: Mounting racks are named as components that may need equipotential bonding. Metallic support structures
    need identified bonding jumpers between separate sections.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=6.1.1
    h: d09005a0d519
  - src: src:std-standards-nec-2020-nec-2020-690
    loc: sec=h120
    h: e551ddd81d11
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:module-frame
  note: Module and array frames are named as parts that are bonded.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=6.1.1
    h: d09005a0d519
  - src: src:iec-62446-1
    loc: sec=h170
    h: b8b0d5b3d0c2
  - src: src:iec-62446-1
    loc: sec=6.1
    h: 285ee2d2196e
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:electromagnetic-compatibility
  note: Solis says proper grounding and equipotential bonding are critical for EMC performance.
  cite:
  - src: src:kb-solis-44002862909-radio-frequency-interference-rfi-in-solar-pv-installations
    loc: sec=h8
    h: 06d68d012a0f
  review: drafted
- claim_id: c4
  rel: related_to
  target: std:iec-62548
  note: Array frame bonding arrangements are to be specified and installed to IEC TS 62548:2013.
  cite:
  - src: src:iec-62446-1
    loc: sec=h170
    h: b8b0d5b3d0c2
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
Equipotential bonding means electrically joining conductive parts, such as mounting racks and module frames, so they stay at the same potential. In a PV system, parts that need bonding should be connected to a central equipotential panel provided for that purpose. Do not use the inverter enclosure as the bonding point. SMA warns that bonding done wrong can damage the inverter, and that this damage is not covered under warranty. Where protective earthing or bonding conductors are installed on the DC side, run them parallel to the DC cables and bundle them together. During commissioning, test the continuity of all such conductors and check their connection to the main earthing terminal. Metallic support structures need identified bonding jumpers between separate sections, and they connect to the equipment grounding conductor. Good bonding also matters for electromagnetic compatibility. In lightning protection, potential equalization ties grounded media together at ground, roof and intermediate levels.

<!-- review notes
- sentence 1: support check: partial - Passages name racks and frames needing bonding to a central panel, but none defines bonding as keeping parts at the same potential.
- sentence 5: support check: partial - u20 requires a continuity test on all such conductors and says the main earthing terminal connection should be verified; it doesn't say this is done during commissioning.
- sentence 7: support check: partial - u9 supports the EMC point and u10 covers ground, roof and intermediate levels, but the roof-level requirement applies only to structures over 60 ft and intermediate loops have exceptions.
- sentence 1: review: partial - The SMA passage names mounting racks and module frames as parts needing equipotential bonding to a central panel, but no passage defines bonding as keeping parts at the same potential.
-->
