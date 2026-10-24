---
id: concept:effective-grounding
type: Concept
name: Effective grounding
aliases:
- effectively grounded
- grounding transformer
- grounding bank
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: std:ieee-142-2007
  note: The IEEE Green Book defines effective grounding through zero-sequence to positive-sequence impedance
    ratios and suggests two grounding schemes.
  cite:
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h6
    h: df3ebcbd6c0b
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-solectria-effective-grounding-for-pv-plants
    loc: sec=h5
    h: 338071d5dee9
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-solectria-effective-grounding-for-pv-plants
    loc: fig=9
    h: 5b6e3941354e
  review: drafted
- claim_id: c2
  rel: related_to
  target: std:ieee-1547
  note: PV plants must meet IEEE 1547 and local utility interface rules. Some utilities also require AC-side
    grounding of the inverters to match their own grounding scheme.
  cite:
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-solectria-effective-grounding-for-pv-plants
    loc: sec=h2
    h: 0777d4c89a85
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:symmetrical-components
  note: Effective grounding is stated as ratios of zero-sequence to positive-sequence impedance. Grounding
    banks give a low-impedance path to zero-sequence voltage.
  cite:
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-solectria-effective-grounding-for-pv-plants
    loc: sec=h6
    h: f7484046292e
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h6
    h: df3ebcbd6c0b
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-solectria-effective-grounding-for-pv-plants
    loc: sec=h2
    h: 0777d4c89a85
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:transformer-winding-configuration
  note: Whether a transformer configuration provides effective grounding is judged case by case by each
    utility.
  cite:
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h14
    h: 0d98a148bbbb
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h18
    h: dce03f8db182
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-ju-effective-grounding-for-interconnection-2018
    loc: sec=h5
    h: 9abaa87be95a
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-solectria-effective-grounding-for-pv-plants
    loc: sec=h5
    h: 338071d5dee9
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:protection-coordination
  note: Solid grounding can let large fault currents flow, which can desensitize overcurrent coordination.
    Effective grounding speeds up utility ground-fault protection.
  cite:
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-solectria-effective-grounding-for-pv-plants
    loc: sec=h5
    h: 338071d5dee9
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-ju-effective-grounding-for-interconnection-2018
    loc: sec=h3
    h: e32722ef1cc0
  review: drafted
- claim_id: c6
  rel: related_to
  target: meas:transient-grid-overvoltage
  note: Systems that are not effectively grounded can see temporary overvoltage. One mitigation is a local
    3V0 relay scheme.
  cite:
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h6
    h: df3ebcbd6c0b
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-ju-effective-grounding-for-interconnection-2018
    loc: sec=h3
    h: e32722ef1cc0
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h25
    h: 9c2e61fc1e4e
  review: drafted
- claim_id: c7
  rel: related_to
  target: comp:mv-transformer
  note: A grounding reactor in the transformer neutral, or a grounding bank on the primary side of the
    MV transformer, can provide effective grounding.
  cite:
  - src: src:yaskawa-grounding-bank-design-guide-ieee-p1547-8
    loc: sec=5
    h: 98c779e01729
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-solectria-effective-grounding-for-pv-plants
    loc: sec=h5
    h: 338071d5dee9
  review: drafted
  review_note: 'support check: partial - Grounding reactor in neutral and grounding bank on the MV transformer
    primary side are supported, but the reactor is described for a transformer neutral generally, not
    specifically the MV transformer.'
- claim_id: c8
  rel: related_to
  target: tool:solectria-effective-grounding-design-tool
  note: Used to calculate the grounding bank impedance and current ratings.
  cite:
  - src: src:yaskawa-grounding-bank-design-guide-ieee-p1547-8
    loc: sec=5
    h: 98c779e01729
  - src: src:yaskawa-grounding-bank-design-guide-ieee-p1547-8
    loc: fig=12
    h: d43b060d84a6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
A system is effectively grounded when its ground connection has low enough impedance that a ground fault cannot raise voltages above the limits set for the connected equipment. The IEEE definition uses sequence impedances: the ratio X0/X1 must be positive and below 3, and R0/X1 must be positive and below 1. Under these conditions the coefficient of grounding stays at or below 80%. If a phase faults to ground and the system is not effectively grounded, equipment on the healthy phases can see up to 173% of nominal voltage. Effective grounding keeps this to roughly 125% to 138%, depending on the utility system. Utilities expect distributed generation and storage sites to match their level of grounding, so the site does not weaken the utility's grounding. Some utilities therefore require AC-side grounding of PV inverters. Effective grounding can be provided in two ways. One is a grounding reactor in the transformer neutral. The other is a grounding bank, built from a zig-zag or wye-delta transformer, which passes zero-sequence current easily but blocks positive-sequence current. A single grounding bank at the point of common coupling can effectively ground a whole multi-inverter plant, so the inverters can be connected without a neutral. Grounding banks are usually rated only for short-term duty and need overcurrent protection. The inverters should be interlocked so they shut off when the grounding bank breaker opens. Effective grounding also gives fault current a low-impedance return path, so utility ground-fault protection can operate faster. Related topics are symmetrical components, transformer winding configuration and protection coordination.
