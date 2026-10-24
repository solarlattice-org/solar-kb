---
id: concept:system-voltage-class
type: Concept
name: System voltage class
aliases:
- 1000 V DC
- 1500 V DC
- 600 V DC
- Voltage class
category: Design
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:voltage-levels
  note: NETA defines low voltage as nominal system voltages of 1000 V or less and medium voltage as above
    1000 V and below 100,000 V; a voltage category groups several voltage classes.
  cite:
  - src: src:std-standards-neta-ansi-neta-ecs-2020
    loc: sec=h107
    h: a8275f210e5a
  - src: src:std-standards-neta-ats-ats-13
    loc: sec=h600
    h: 220f2245214b
  - src: src:book-electric-power-system-basics
    loc: sec=h92
    h: 7b9d9eadee34
  - src: src:book-electric-power-system-basics
    loc: tbl=6
    h: f4c326638895
  review: drafted
- claim_id: c2
  rel: related_to
  target: prod:sma-sunny-central-up-us
  note: 'Example of 1500 V class equipment: maximum DC input voltage 1500 V.'
  cite:
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc-up-us-be-en-14
    loc: tbl=174.r24
    h: c3732eb3d053
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc2-3xxxup-us-data-sheet
    loc: tbl=2.r4
    h: 0af1426c61bc
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc-up-us-be-en-14
    loc: tbl=176.r5
    h: c3732eb3d053
  review: drafted
  review_note: 'support check: partial - Max DC input 1500 V is stated for SC UP-US, but passages don''t
    call it a 1500 V class equipment relation explicitly.'
- claim_id: c3
  rel: related_to
  target: prod:yaskawa-solectria-pvi-3800-7600tl
  note: 'Example of 600 V class equipment: maximum system voltage 600 V.'
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=51.r2
    h: fefbd0daf618
  review: drafted
  review_note: 'support check: partial - Max system voltage 600 V is stated for the PVI TL models, but
    the ''600 V class'' link is not stated in the passages.'
---
Voltage class is the term manufacturers and utilities use for the system voltage that a piece of equipment is meant to connect to. One voltage class can cover several nominal operating voltages. For example, a breaker in the 125 kV class may run on a nominal 115 kV system. NETA testing standards call nominal system voltages of 1000 V or less low voltage. Voltages above 1000 V and below 100,000 V are medium voltage. Customer service voltages such as 208Y/120, 240/120, 480Y/277 and 600 V all fall in the low-voltage class. Smaller residential inverters are often rated for a 600 V maximum. Utility-scale central inverters are rated for a 1500 V maximum DC input.

<!-- review notes
- sentence 3: support check: partial - Definitions of low and medium voltage are given, but the passages don't attribute them to NETA testing standards explicitly.
- sentence 5: support check: partial - 600 V and 1500 V maxima are shown for specific products, but the generalizations about residential vs utility-scale inverters being typical are not stated.
-->
