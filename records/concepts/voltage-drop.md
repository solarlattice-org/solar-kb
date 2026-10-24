---
id: concept:voltage-drop
type: Concept
name: Voltage drop
aliases:
- cable voltage drop
- line-voltage drop
- system voltage drop
category: Design
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:ampacity
  note: Check voltage drop after the NEC ampacity requirements are met. A conductor can pass on ampacity
    and still fail the voltage drop target.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h121
    h: ffdc1a631da7
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h120
    h: 2e35f0cf07ac
  review: drafted
- claim_id: c2
  rel: related_to
  target: mit:conductor-upsizing
  note: The fix is to step up conductor size until the calculated percent drop meets the target.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h121
    h: ffdc1a631da7
  review: drafted
- claim_id: c3
  rel: related_to
  target: fm:undersized-ac-conductor
  note: High drop on the inverter output conductors raises the voltage at the inverter terminals toward
    the overvoltage trip limit.
  cite:
  - src: src:ref-standards-mv-committee-inverter-requirements-with-mv-xmfr-cps-vdrop-and-transformer-document
    loc: sec=2
    h: 02fd1ba91dea
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:voltage-rise
  cite:
  - src: src:ref-standards-mv-committee-inverter-requirements-with-mv-xmfr-cps-vdrop-and-transformer-document
    loc: sec=2
    h: 02fd1ba91dea
  - src: src:book-electric-power-transformer-engineering
    loc: sec=17.4.2
    h: 1b1add41195d
  review: drafted
  review_note: 'support check: partial - u24 links drop on output conductors to a voltage increase at
    the POI, and u26 mentions voltage rise from capacitance, but no general relation between voltage drop
    and voltage rise is stated.'
- claim_id: c5
  rel: related_to
  target: mit:transformer-tap-adjustment
  note: May be needed when AC voltage drop is above 2% of nominal.
  cite:
  - src: src:ref-standards-mv-committee-inverter-requirements-with-mv-xmfr-cps-vdrop-and-transformer-document
    loc: sec=2
    h: 02fd1ba91dea
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:point-of-common-coupling
  cite:
  - src: src:ref-standards-mv-committee-inverter-requirements-with-mv-xmfr-cps-vdrop-and-transformer-document
    loc: sec=2
    h: 02fd1ba91dea
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:grid-impedance
  note: Line drop has a resistive part (IR) and a reactive part (IX).
  cite:
  - src: src:book-electric-power-transformer-engineering
    loc: sec=17.4.2
    h: 1b1add41195d
  review: drafted
---
Voltage drop is the voltage lost along a conductor. It follows Ohm's law: drop equals current times resistance. The calculation uses the round-trip wire length (twice the one-way distance) and the conductor resistance per 1000 ft from NEC Chapter 9, Table 8. For any given wire size, the drop grows with higher current and longer runs. Low-voltage systems (12 V, 24 V and 48 V) are the most sensitive, but long circuits in higher-voltage systems can also have significant drop. Voltage drop is not treated as a safety issue, so the code sets no compliance limit. Industry practice keeps the overall system drop within 2% to 5%. Non-mandatory NEC fine-print notes suggest 3% per feeder or branch circuit and 5% total. Check voltage drop after ampacity is satisfied, because it is often the deciding factor in wire sizing below 100 V. When you upsize conductors, confirm that the lugs, terminals and box sizes can take the larger wire. Moving a battery system from 24 V to 48 V cuts the DC voltage drop impact to 25% for the same wire sizes. Fuses, breakers and switches can add up to 0.5%, and charge controllers can add another 1% to 4%. On an inverter AC output, CPS recommends keeping the drop below 2% of nominal voltage at full power. A high drop pushes the inverter terminal voltage toward its overvoltage trip point, which can cause nuisance disconnects when grid voltage is already high. Include conductor temperature rise and ambient temperature in the calculation. Also consider transient dips from high inrush loads such as motor starting. On utility feeders, regulators use line drop compensation to boost voltage for the line drop. PV installed near the regulator can mask the load current, which can cause low voltage further down the feeder.

<!-- review notes
- sentence 6: support check: partial - CPS's <2% recommendation and the overvoltage-trip mechanism are in u24, but the passage says the inverter disconnects (example: 105% grid plus 3% drop), not specifically 'nuisance' disconnects.
-->
