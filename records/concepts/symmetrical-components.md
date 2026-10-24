---
id: concept:symmetrical-components
type: Concept
name: Symmetrical components
aliases:
- phasor analysis
- negative sequence
- zero sequence
- symmetrical coordinate method
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:effective-grounding
  note: Grounding classes such as effective and very effective are defined using ratios of symmetrical
    component parameters.
  cite:
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: tbl=26.r3
    h: 025ee7e2f1da
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-eaton-power-system-design-basics-tb081
    loc: tbl=26.r2
    h: dbee68a36dab
  review: drafted
- claim_id: c2
  rel: explains
  target: concept:phase-unbalance
  note: The method turns an unbalanced three-phase system into balanced sequence sets so faults and unbalanced
    operation can be analyzed.
  cite:
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-lwp0010-02-tutorialsymmetrical-pt2-ar-20140506
    loc: sec=h2
    h: 6d5ab52710fd
  - src: src:ref-reference-zigzag-effective-grounding-symmetical-components-ieee
    loc: sec=h1
    h: 69ac904ac8d9
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:harmonic-distortion
  note: Third harmonic currents behave like zero-sequence currents and can circulate in delta windings.
  cite:
  - src: src:ref-reference-zigzag-effective-grounding-symmetical-components-ieee
    loc: sec=h1
    h: 69ac904ac8d9
  - src: src:ref-reference-zigzag-effective-grounding-symmetical-components-ieee
    loc: sec=h8
    h: bf3f131c3680
  review: drafted
  review_note: 'support check: partial - The u38 passage says third harmonic currents behave like zero-sequence
    currents and circulate in delta, but the cited u30/u38 text is supported only via u38; it is stated,
    though u30 adds nothing; core is present, but ''can circulate'' is fine—still, relation is stated.'
- claim_id: c4
  rel: explains
  target: concept:transformer-winding-configuration
  note: Zero-sequence current flows in grounded-wye windings and circulates inside delta windings, never
    leaving the delta onto the lines.
  cite:
  - src: src:ref-reference-zigzag-effective-grounding-symmetical-components-ieee
    loc: sec=h8
    h: bf3f131c3680
  review: drafted
- claim_id: c5
  rel: related_to
  target: meas:negative-sequence-voltage-imbalance
  note: Meters report negative-sequence voltage magnitude and angle.
  cite:
  - src: src:sel-735-im-20250228
    loc: tbl=358.r13
    h: b736ad35cee8
  - src: src:sel-735-im-20250228
    loc: tbl=358.r7
    h: 1faedb9cb255
  review: drafted
- claim_id: c6
  rel: related_to
  target: meas:zero-sequence-imbalance
  note: Meters report three-phase zero-sequence voltage and current quantities.
  cite:
  - src: src:sel-735-im-20250228
    loc: tbl=358.r8
    h: 39147b502a7e
  - src: src:sel-735-im-20250228
    loc: tbl=358.r5
    h: 6c024f6102b0
  - src: src:sel-735-im-20250228
    loc: tbl=358.r11
    h: 6043f60167cc
  review: drafted
- claim_id: c7
  rel: related_to
  target: tool:sel-synchrowave
  note: Calculates phasor quantities and their symmetrical components automatically, so signals can be
    compared.
  cite:
  - src: src:sel-synchrowave-instruction-manual
    loc: sec=h4
    h: 6f60bb780055
  review: drafted
---
Symmetrical components is a method that breaks an unbalanced three-phase system into positive-, negative- and zero-sequence components. The positive and negative sequences are balanced phasor sets. Analysis is easier in the sequence domain, and the results are then converted back to phase quantities. Each sequence current can see a different impedance, so engineers build separate positive-, negative- and zero-sequence networks of the system. Generated voltage appears only in the positive-sequence network. Zero-sequence current needs a fourth conductor or ground path to return, so delta and ungrounded wye connections block it. Grounding impedance appears only in the zero-sequence network, where it is counted at three times its value, because only zero-sequence current can flow to ground. The method is the main tool for fault studies. It is also used for switching surges, lightning surges and harmonic resonance. Effective grounding classes are defined by ratios of symmetrical component parameters, so the method matters when a PV plant is grounded through a transformer neutral or a grounding bank.

<!-- review notes
- sentence 6: support check: partial - Passages cover fault analysis, switching/lightning surges and harmonic resonance, but 'main tool for fault studies' is not explicitly stated; u16 calls it a very important method.
- sentence 7: support check: partial - Grounding classes defined by symmetrical component ratios are shown, and transformer neutral and grounding bank headings exist, but the passages don't explicitly tie this to PV plants or say the method matters for them.
- sentence 7: review: partial - The table defines grounding classes by ratios of symmetrical component parameters, and the figures show PV plant grounding through a transformer neutral or a grounding bank, but the passages never draw the causal 'so the method matters' link.
-->
