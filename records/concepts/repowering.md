---
id: concept:repowering
type: Concept
name: Repowering
aliases:
- inverter repowering
- retrofit
- repower
- upgrading
- retrofitting
category: Lifecycle
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:revamping
  note: Revamping swaps components without substantially changing nominal plant power. Repowering increases
    it or substantially changes it.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=h68
    h: d7834d715d7c
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=7.1
    h: 5714d4cdb4e8
  - src: src:iea-pvps-t13-25-2022
    loc: sec=2.3.3
    h: d63a667b947f
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=h112
    h: 7b3b441daaf6
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: related_to
  target: concept:om-contract
  note: Contracts usually treat repowering as extraordinary maintenance. After repowering, the O&M KPIs
    may need to be redefined, or a new O&M contract may start.
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=2.3.3
    h: d63a667b947f
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=h23
    h: 6affbb7c86c9
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: related_to
  target: mit:inverter-replacement
  note: Inverter repowering can be a partial or a complete exchange, using inverters of the same or a
    different power class.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=7.3
    h: eac7ac6a2889
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=7.3
    h: 1f547ba4523f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: related_to
  target: mit:module-replacement
  note: Module repowering is considered when defective modules cannot be swapped like-for-like.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=7.2
    h: 6cf30040d904
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=7.2
    h: 8f4c02af265d
  review: drafted
- claim_id: c5
  rel: related_to
  target: prog:sma-repowering
  cite:
  - src: src:sma-kb-is-it-possible-to-repower-sma-trafo-inverters
    loc: sec=h1
    h: 39ea8049d591
  - src: src:sma-kb-is-it-possible-to-check-system-compabilities-when-repowering-a-plant
    loc: sec=h1
    h: d58f5d83921b
  review: drafted
  review_note: 'support check: partial - SMA repowering package and app exist in the passages, but no
    passage explicitly defines a program relation beyond SMA offering repowering services.'
- claim_id: c6
  rel: related_to
  target: concept:authority-having-jurisdiction
  note: AHJ and NEC requirements are one of three major challenges when repowering a legacy site.
  cite:
  - src: src:yaskawa-repowering-and-inverter-replacement-viability-2025-02-20
    loc: sec=h1
    h: aa35b9d8183e
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:system-voltage-class
  note: DC voltage differences make repowering difficult, especially for legacy 600 Vdc class systems.
  cite:
  - src: src:yaskawa-repowering-and-inverter-replacement-viability-2025-02-20
    loc: sec=h1
    h: aa35b9d8183e
  - src: src:yaskawa-repowering-and-inverter-replacement-viability-2025-02-20
    loc: fig=2
    h: 8a727ba6417d
  review: drafted
- claim_id: c8
  rel: related_to
  target: concept:grid-code
  note: Ask the regulator early about compatibility with the grid code and the plant certificate.
  cite:
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=h121
    h: 65e27c0fb04f
  review: drafted
- claim_id: c9
  rel: related_to
  target: concept:dc-ac-ratio
  note: New inverters should be optimised for shading or for the DC/AC ratio.
  cite:
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=h121
    h: 65e27c0fb04f
  review: drafted
- claim_id: c10
  rel: related_to
  target: std:iec-62446-1-2016
  note: Affected cables and connectors should be tested and documented during inverter repowering.
  cite:
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=h121
    h: 65e27c0fb04f
  review: drafted
- claim_id: c11
  rel: related_to
  target: std:iec-60364-6
  cite:
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=h121
    h: 65e27c0fb04f
  review: drafted
---
Repowering means replacing old components of a PV plant that produce power with new ones, to improve the plant's overall performance. It differs from revamping because repowering increases or substantially changes the plant's nominal power, while revamping keeps nominal power about the same. Unlike an ordinary replacement, it swaps all components in a functional area, or a large share of them, to raise performance. The main targets are inverters and modules. Inverter repowering can mean changing string lengths, combiner boxes, fuses, AC cable sizes and protection devices, as well as mounting and grounding, to suit the new inverter. For legacy sites, the main challenges are DC voltage differences, grounding differences, and AHJ or NEC requirements. This is especially true for 600 Vdc class systems. After the work, affected cables and connectors should be tested and documented. The preventive maintenance schedule and staff training should also be updated. Repowering can pay off even when the old inverter still works, if the new one produces more energy through higher efficiency. Depending on the scope, the O&M KPIs or the O&M contract itself may need to be renegotiated afterwards.

<!-- review notes
- sentence 6: support check: partial - Testing/documentation is said to occur during the repowering project, not after, though the maintenance schedule and training updates are stated.
-->
