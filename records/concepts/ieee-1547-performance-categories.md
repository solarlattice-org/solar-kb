---
id: concept:ieee-1547-performance-categories
type: Concept
name: IEEE 1547 performance categories
aliases:
- Category I
- Category II
- Category III
- Category A
- Category B
- abnormal performance category
- abnormal performance categories
- normal performance categories
- disturbance performance categories
category: Grid
concept_kind: technology
claims:
- claim_id: c1
  rel: part_of
  target: std:ieee-1547-2018
  note: Annex B gives guidance on how categories are assigned.
  quote: Categories I, II, and III for disturbance ride-through requirements (Clause 6)
  quote_source: IEEE 1547-2018 Annex B.3
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h270
    h: 5b6d91d448d7
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h41
    h: 0ac792f70c7e
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=B.3
    h: 5e20c065bea1
  review: drafted
- claim_id: c2
  rel: related_to
  target: func:voltage-ride-through
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h270
    h: 5b6d91d448d7
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: fig=115
    h: 715673b088ca
  review: drafted
- claim_id: c3
  rel: related_to
  target: func:frequency-ride-through
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: fig=117
    h: e0b80d252834
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:distributed-energy-resource
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=B.4.3.3
    h: 3e3a8aa66008
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=h41
    h: 0ac792f70c7e
  - src: src:ref-standards-ieee-ieee-1547-2018-highlights
    loc: sec=h48
    h: d192476f792c
  review: drafted
---
IEEE 1547-2018 groups DER requirements into performance categories, so that each DER type and application can be held to a performance level suited to it. Categories A and B cover voltage regulation and reactive power capability under Clause 5. These are called the normal performance categories. Categories I, II and III cover disturbance ride-through under Clause 6, meaning the voltage and frequency ride-through requirements. These are called the abnormal performance categories. The categories exist because some desirable DER technologies, such as synchronous generators or an engine running on landfill gas, cannot meet the full reactive power or ride-through requirements. The authority governing interconnection requirements (AGIR) decides which category each DER type and application must meet. It may use technical criteria such as DER type, capacity and expected penetration, as well as nontechnical criteria. The Clause 5 and Clause 6 categories are not tied to each other. Even so, the standard strongly recommends pairing Category I with Category A, and pairing Categories II and III with Category B. To protect the security of the bulk power system, most DER should have Category II ride-through. Category I or III is used only in notable exceptions.

<!-- review notes
- sentence 2: support check: partial - Categories A/B for voltage regulation and reactive power under Clause 5 are stated, and a heading 'Normal performance categories (Clause 5)' appears, but the naming is only implied by the heading.
- sentence 3: support check: partial - Categories I–III for ride-through under Clause 6 and the 'Abnormal performance categories (Clause 6)' heading appear, but voltage and frequency ride-through is only implied via figure titles.
- sentence 7: support check: partial - Majority should be Category II with notable exceptions for I and III, but 'only' in exceptions is slightly stronger than stated.
-->
