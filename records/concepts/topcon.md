---
id: concept:topcon
type: Concept
name: TOPCon cell
aliases:
- TOPCon
- tunnel oxide passivated contact
category: Modules
concept_kind: technology
claims:
- claim_id: c1
  rel: subclass_of
  target: concept:crystalline-silicon
  note: Described as an advanced c-Si cell architecture, typically on n-type wafers.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6
    h: 0660da2db10d
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:heterojunction
  note: Both are advanced c-Si architectures that reach higher Voc by minimising contact recombination
    without reducing fill factor.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6
    h: 0660da2db10d
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:perc
  note: Both use glass-frit front metal pastes fired through the passivation; TOPCon was reported more
    susceptible to front contact corrosion than PERC.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.1
    h: b51dcb452e5b
  review: drafted
- claim_id: c4
  rel: related_to
  target: fm:severe-metallization-corrosion
  note: TOPCon front metal contacts and interconnects can corrode at the metal/Si interface, with sensitivity
    likely linked to high aluminium content in the front paste.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.1
    h: b51dcb452e5b
  review: drafted
  review_note: 'support check: partial - Corrosion at metal/Si interface and high Al content link are
    stated, but ''severe'' metallization corrosion as a named failure mode isn''t explicitly stated; it''s
    generic corrosion.'
- claim_id: c5
  rel: related_to
  target: stressor:acetic-acid-release
  note: Acetic acid from EVA decomposition in the presence of moisture drives front contact corrosion;
    TOPCon cells showed a larger contact resistivity increase under acetic acid exposure than PERC and
    SHJ.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.1
    h: b51dcb452e5b
  review: drafted
- claim_id: c6
  rel: related_to
  target: mit:alternative-encapsulant
  note: Use of TPO encapsulants was shown to mitigate power loss in 1000 h damp heat.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.1
    h: b51dcb452e5b
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:fill-factor
  note: Higher Voc is achieved without reducing fill factor.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6
    h: 0660da2db10d
  review: drafted
- claim_id: c8
  attr: typical_power_loss
  value:
    min: 4
    max: 65
    unit: unit:PERCENT
  conditions: Maximum power loss (relative) of encapsulated TOPCon modules after 1000 h damp-heat testing
    across seven encapsulant/backsheet combinations; strongly dependent on encapsulation material (Sen
    et al.). PERC modules in the same study lost 1 to 2 %rel.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.1
    h: b51dcb452e5b
  review: drafted
---
TOPCon stands for tunnel oxide passivated contact. It is an advanced crystalline silicon cell design, usually built on n-type wafers. Like heterojunction cells, it cuts recombination at the contacts. This gives a higher open-circuit voltage without lowering the fill factor. TOPCon is expected to become the dominant cell technology after 2025, and cell designs change about every six months. Because of this, the limited field data on TOPCon may not represent the modules being built today. The front contacts use a glass-frit metal paste that is fired through the passivation and the anti-reflective coating, the same method used on PERC cells. When the cells are laminated in EVA and moisture gets in, acetic acid from the EVA can corrode the front metallization and the interconnects. TOPCon has been reported to be even more sensitive to this than PERC. In damp-heat testing, power loss in TOPCon modules depended strongly on the encapsulant. Using TPO encapsulants helped limit the loss.

<!-- review notes
- sentence 4: support check: partial - Glass-frit paste etching through passivation and ARC is stated for PERC and TOPCon, but the 'front contacts' wording is general; fairly supported though 'same method' is implied; minor nuance of TOPCon's poly-Si emitter.
-->
