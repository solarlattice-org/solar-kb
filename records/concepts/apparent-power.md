---
id: concept:apparent-power
type: Concept
name: Apparent power
aliases:
- kVA
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:active-power
  note: Active power is one component of apparent power.
  cite:
  - src: src:eq-equip-meters-ge-kv2c-meters-metermate-5-51-files-software-instruction-manuals-geh-5082x-mmprofile
    loc: sec=h512
    h: ecc9cecadf91
  - src: src:book-handbook-of-power-system-engineering
    loc: sec=11.1.1
    h: 86f2f1c0884d
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285
    loc: sec=h98
    h: 8a0d3daeea45
  - src: src:eq-equip-bess-enel-enel-x-der-os-site-modbus-server-manual-v1-1-2
    loc: tbl=14.r8
    h: 67aa74f29bc2
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:reactive-power
  note: Reactive power is the quadrature component of apparent power.
  cite:
  - src: src:eq-equip-meters-ge-kv2c-meters-metermate-5-51-files-software-instruction-manuals-geh-5082x-mmprofile
    loc: sec=h512
    h: ecc9cecadf91
  - src: src:book-handbook-of-power-system-engineering
    loc: sec=11.1.1
    h: 86f2f1c0884d
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285
    loc: sec=h98
    h: 8a0d3daeea45
  - src: src:eq-equip-bess-enel-enel-x-der-os-site-modbus-server-manual-v1-1-2
    loc: tbl=14.r8
    h: 67aa74f29bc2
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:power-factor
  note: The kV2c meter manual presents apparent power together with power factor relationships.
  cite:
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285
    loc: sec=h98
    h: 8a0d3daeea45
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:harmonic-distortion
  note: Some meter definitions include distortion power as a third component of apparent power.
  cite:
  - src: src:eq-equip-meters-ge-kv2c-meters-metermate-5-51-files-software-instruction-manuals-geh-5082x-mmprofile
    loc: sec=h512
    h: ecc9cecadf91
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285
    loc: sec=h98
    h: 8a0d3daeea45
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:pq-capability-diagram
  note: A constant apparent power setpoint keeps operation on a circle in the PQ diagram.
  cite:
  - src: src:sma-doc-265222
    loc: sec=5.2.9
    h: 70ae6b2510ff
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:nameplate-rating
  note: Inverters are rated by continuous or rated apparent output power in kVA.
  cite:
  - src: src:eq-equip-inverters-solectria-xgi-1500-fl-xgi1500-01-05-03-2021
    loc: tbl=1.r11
    h: ce6ea512f7c6
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=14
    h: 697bb48891a9
  - src: src:sma-doc-278742
    loc: tbl=85.r7
    h: 01da6523899a
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:symmetrical-components
  note: Apparent power can be expressed in the 0-1-2 domain.
  cite:
  - src: src:book-handbook-of-power-system-engineering
    loc: sec=h253
    h: 4fb54ba669b5
  review: drafted
  review_note: 'support check: partial - The passage is only a heading saying apparent power is expressed
    in the 0-1-2 and d-q-0 domains, with no detail.'
- claim_id: c8
  rel: related_to
  target: concept:phase-unbalance
  note: SMA inverters offer a maximum unbalanced apparent power threshold.
  cite:
  - src: src:sma-doc-275857
    loc: tbl=83
    h: a5a32dd7a3fa
  review: drafted
  review_note: 'support check: partial - Parameters for a maximum unbalanced apparent power threshold
    exist, but the passage does not name SMA.'
---
Apparent power, written S, is defined as the complex quantity P + jQ. It combines effective (active) power P and reactive power Q at the fundamental frequency. Some revenue meters use a broader definition. In those meters the square of apparent power equals the sum of the squares of active, reactive and distortion power. Monitoring platforms often compute apparent power as the square root of active power squared plus reactive power squared. Meters and inverters report apparent power in kVA, per phase or as a total. A variant called arithmetic apparent power adds up the magnitudes of the individual phase values. Inverters are rated by their continuous or rated apparent output power in kVA. This rating limits the combined active and reactive output. Some grid codes require a constant apparent power setpoint. With that setpoint, the inverter adds reactive power when active power falls below the setpoint. Avoid this mode where a local load is connected, because it can cut active power production.

<!-- review notes
- sentence 2: support check: partial - The sum-of-squares relation with distortion power is stated, but the passages do not say it is specific to some revenue meters, as opposed to a general definition.
- sentence 3: support check: partial - One monitoring register uses sqrt(P²+Q²), but the passage does not support 'often' for monitoring platforms.
- sentence 4: support check: partial - Per-phase and total apparent power and the arithmetic variant are stated, but the passages do not clearly give kVA units for both per-phase and total values (some show VA).
- sentence 5: support check: partial - The kVA ratings are shown and a maximum apparent power limit exists, but the passages do not explicitly say the rating limits combined active and reactive output.
-->
