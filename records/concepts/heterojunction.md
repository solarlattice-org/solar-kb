---
id: concept:heterojunction
type: Concept
name: Heterojunction cell
aliases:
- HJT
- heterojunction
- SHJ
- Silicon Hetero-Junction
- Silicon HeteroJunction
category: Modules
concept_kind: technology
claims:
- claim_id: c1
  rel: subclass_of
  target: concept:crystalline-silicon
  note: HJT is listed among current c-Si cell structures together with TOPCon, PERT and PERC.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.3
    h: 447bcab4e244
  review: drafted
  review_note: 'support check: partial - Passages list HJT among current c-Si cell structures, but "kind
    of crystalline silicon PV" is only implied (c-Si/a-Si:H, ''current c-Si cell structures'').'
- claim_id: c2
  rel: related_to
  target: concept:topcon
  note: Both are newer cell designs whose reliability, including UV-induced and potential-induced degradation,
    is assessed side by side.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.3
    h: 447bcab4e244
  - src: src:iea-pvps-t13-30-2025
    loc: sec=h15
    h: 1e249684bb32
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c3
  rel: related_to
  target: concept:perc
  note: Field degradation of SHJ modules was compared with PERC; PERC losses come mainly from Isc, while
    SHJ losses come mainly from voltage.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.3
    h: 447bcab4e244
  review: drafted
- claim_id: c4
  rel: related_to
  target: fm:uv-induced-degradation
  note: In SHJ cells, UV exposure lowers Voc because the front passivating layers partly lose their properties.
    Light soaking may recover the loss.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.3
    h: 447bcab4e244
  - src: src:iea-pvps-t13-30-2025
    loc: sec=h15
    h: 1e249684bb32
  review: drafted
- claim_id: c5
  rel: related_to
  target: fm:potential-induced-degradation
  note: A new possible PID mechanism has been identified for SHJ modules, but no field modules affected
    by it have been found yet.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=h15
    h: 1e249684bb32
  - src: src:iea-pvps-t13-30-2025
    loc: fig=69
    h: ac9e8219941f
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:temperature-coefficient
  note: Heterojunction modules are named as having low temperature coefficients, which makes them suitable
    for hot sites.
  cite:
  - src: src:iea-pvps-t13-33-2025
    loc: sec=6.5
    h: 778f245ec3d5
  review: drafted
- claim_id: c7
  attr: degradation_rate
  value:
    nominal: -0.51
    unit: unit:PERCENT-PER-YR
  conditions: Observed degradation rate of fielded SHJ modules (Jordan et al.), on par with conventional
    Si cell technologies
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.3
    h: 447bcab4e244
  review: drafted
- claim_id: c8
  attr: typical_power_loss
  value:
    min: 1
    max: 2.5
    unit: unit:PERCENT
  conditions: Power degradation of 2 SHJ module types after an accelerated UV test dose of 60 kWh/m² under
    short-circuit conditions
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.6.3
    h: 447bcab4e244
  review: drafted
---
A heterojunction cell, also called SHJ or HJT, is a crystalline silicon cell structure. Its junction is formed by amorphous silicon (a-Si:H) passivation layers on a crystalline silicon wafer. Along with TOPCon, it is one of the newer cell technologies whose long-term reliability is still being studied. Fielded SHJ modules degrade at about the same yearly rate as conventional silicon modules. The loss shows up mainly as lower voltage, not lower current. This voltage loss is linked to weathering-related defects near the boundary between the wafer and the a-Si:H layer, which raise recombination. SHJ cells can lose Voc under UV light because the front passivation weakens. Moving to rear-emitter designs historically solved this, and light soaking may recover UV losses. A possible new potential-induced degradation mechanism has been found for SHJ modules, but no affected modules have been seen in the field yet. Heterojunction modules have low temperature coefficients, so they are a good choice for hot sites.

<!-- review notes
- sentence 1: support check: partial - SHJ/HJT abbreviation and c-Si/a-Si:H junction-forming passivation layers are stated, but explicit 'HJT also called SHJ' equivalence and c-Si classification are only implied.
- sentence 2: support check: partial - TOPCon and SHJ are treated as innovations with reliability being evaluated, but 'still being studied' is only loosely implied.
-->
