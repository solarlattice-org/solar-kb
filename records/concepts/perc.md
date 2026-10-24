---
id: concept:perc
type: Concept
name: PERC cell
aliases:
- passivated emitter and rear cell
- PERC
- bifacial PERC
category: Modules
concept_kind: technology
claims:
- claim_id: c1
  rel: subclass_of
  target: concept:crystalline-silicon
  note: Al-BSF and PERC are named as the most common industrial crystalline silicon cell types.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h56
    h: 8d42c4699ab3
  review: drafted
  review_note: 'support check: partial - Passage names Al-BSF and PERC as the most common cell types and
    mentions crystalline silicon cells, but never explicitly states PERC is a kind of crystalline silicon
    PV.'
- claim_id: c2
  rel: related_to
  target: comp:solar-cell
  note: PERC is a solar cell architecture.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h56
    h: 8d42c4699ab3
  review: drafted
- claim_id: c3
  rel: related_to
  target: fm:potential-induced-degradation
  note: The rear side of bifacial PERC cells is especially prone to polarisation-type PID (PID-p) under
    negative bias.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  - src: src:iea-pvps-t13-30-2025
    loc: fig=21
    h: d8cf6c55256f
  review: drafted
- claim_id: c4
  rel: related_to
  target: fm:cell-cracks
  note: Bifacial PERC cells with localized rear contacts are more prone to degradation from cracking and
    corrosion under thermal cycling.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h56
    h: 8d42c4699ab3
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r5
    h: 0a21fb8dc566
  review: drafted
- claim_id: c5
  rel: related_to
  target: comp:anti-reflective-coating
  note: The cell stack runs from front to back as ARC/n+/p/ARC, and the rear dielectric may be AlOx, SiOx
    or SiNx.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  review: drafted
- claim_id: c6
  rel: related_to
  target: mit:alternative-encapsulant
  note: A more resistive polyolefin-containing encapsulant instead of EVA is a more certain PID-p mitigation.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  review: drafted
- claim_id: c7
  rel: related_to
  target: std:iec-62804-1
  note: This is the PID test standard for crystalline silicon modules. The 2025 edition adds UV-illuminated
    methods for PID-p.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  review: drafted
  review_note: 'support check: partial - Passages describe IEC 62804-1 test methods for c-Si modules and
    2025 UV methods for PID-p, but not explicitly that PERC relates to it as ''the'' standard; mostly
    supported though.'
- claim_id: c8
  rel: related_to
  target: concept:topcon
  note: TOPCon and PERT have a p+/n front, which is more sensitive to polarisation than the n+/p front
    of PERC.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.2
    h: a3572257e49a
  review: drafted
- claim_id: c9
  rel: related_to
  target: concept:half-cut-cells
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: fig=40
    h: d8f9ab4a58de
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r5
    h: 0a21fb8dc566
  review: drafted
  review_note: 'support check: partial - Passages mention PERC half-cell modules and PERC half-cell cracking,
    but no explicit relation stated beyond that.'
- claim_id: c10
  rel: related_to
  target: fm:light-induced-degradation
  note: In combined stress testing, a smaller amount of LID was mixed in with PID-p.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  review: drafted
- claim_id: c11
  attr: typical_power_loss
  value:
    nominal: 0.2
    unit: unit:PERCENT
  conditions: Multi-wire PERC modules, per half-cell with dendritic-like cracking
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r5
    h: 0a21fb8dc566
  review: disputed
  conflicts_with:
  - concept:perc#c13
- claim_id: c12
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: Relative degradation from PID-p in glass/glass PERC modules with EVA after combined-accelerated
    stress testing at -1200 V bias, flash tested from the front at STC
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  review: drafted
  review_note: 'support check: partial - Passage says ''almost 10%'' relative degradation from the front,
    not ''up to 10%''; conditions otherwise match.; possible conflict with c13 (same source; check the
    conditions)'
- claim_id: c13
  attr: typical_power_loss
  value:
    min: 50
    unit: unit:PERCENT
  conditions: Same combined-accelerated PID-p stress test of glass/glass PERC modules with EVA, flash
    tested from the rear at STC
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  review: disputed
  conflicts_with:
  - concept:perc#c11
  review_note: possible conflict with c12 (same source; check the conditions)
---
PERC stands for passivated emitter and rear cell. Together with Al-BSF, it is one of the most widely used crystalline silicon cell types in industry. A bifacial PERC cell has, from front to back, an anti-reflective coating, an n+ emitter, a p-type base and a rear dielectric stack. That stack may contain AlOx, SiOx or SiNx, and the AlOx carries a negative charge that pushes minority electrons away from the rear surface. The rear of a bifacial PERC cell is especially prone to polarisation-type potential-induced degradation. When the cells sit at negative voltage to ground, positive charge drifts through the encapsulant, which increases recombination at the rear and lowers current and voltage. Field tests found this degradation in PERC modules biased at negative system voltage within several weeks. Modules biased at positive voltage did not show it. Adding SiOx to the rear stack partly reduces the effect. Using a more resistive polyolefin encapsulant or a polymer backsheet instead of EVA and glass is a more certain fix, and the IEC 62804-1 test methods are used to check susceptibility. Bifacial PERC cells with localized rear contacts are more prone to cracking and corrosion under thermal cycling. However, many cracks do not cause power loss, and multi-wire PERC modules lose little power per cracked half-cell. PERT and TOPCon cells have a p+/n front, which is more sensitive to polarisation than the n+/p front of PERC.

<!-- review notes
- sentence 5: support check: partial - SiOx partial mitigation and PO encapsulant/polymer backsheet being more certain are stated, but IEC 62804-1 is described as a PID test generally, not explicitly for checking PERC PID-p susceptibility.
-->
