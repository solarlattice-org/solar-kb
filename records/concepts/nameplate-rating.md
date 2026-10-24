---
id: concept:nameplate-rating
type: Concept
name: Nameplate rating
aliases:
- kWp
- kWdc
- kWac
- nameplate capacity
- nameplate active power rating
- installed nameplate capacity
category: Design
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:apparent-power
  note: Nameplate data includes a maximum apparent power rating in voltamperes, and reactive capability
    is given as a percentage of nameplate kVA.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=35.r6
    h: cb332deddc3c
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=14.r1
    h: 3ca24c270633
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=14.r2
    h: 01593f358619
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:reactive-power
  note: Nameplate data includes maximum injected and absorbed reactive power ratings in vars.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=35
    h: 229df2c680b1
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=15.r9
    h: 83e739cd7bbb
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=16.r7
    h: a48d70a894bb
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:power-factor
  note: Installed nameplate capacity is the MVA rating multiplied by the rated power factor.
  cite:
  - src: src:std-standards-ieee-ieee762-ieee-standard-definitions
    loc: sec=5.8
    h: bc5c09b3cf66
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c4
  rel: related_to
  target: concept:standard-test-conditions
  note: PV module nameplate electrical ratings are stated at STC.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h82
    h: b9526e5ec1a6
  review: drafted
---
A nameplate rating is the set of rated values given for a piece of equipment. Examples are the active power rating in watts at unity power factor, the maximum apparent power rating in voltamperes, and the nominal, maximum and minimum AC voltage ratings. Every listed PV module must be labeled with its key ratings at standard test conditions: Voc, Isc, Vmp, Imp, Pmp, the maximum system voltage and the maximum overcurrent device rating. These ratings set the circuit design and the limits for using the module. The nameplate figure may not show the real maximum or dependable capacity of a unit, because other equipment in the unit can limit its output. During a Category I disturbance ride-through, the active power output capability is the lower of 80 percent of the nameplate active power rating or the active power output before the disturbance. Transformer loading guides cover what happens when a transformer is loaded beyond its nameplate rating, so the nameplate value is a reference point for planned overloads.

<!-- review notes
- sentence 5: support check: partial - Headings show loading beyond nameplate rating is covered, but the passages don't state the nameplate is a reference point for planned overloads or that these are transformer guides.
-->
