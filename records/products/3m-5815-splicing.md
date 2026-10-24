---
id: prod:3m-5815-splicing
type: Product
name: 3M 5815 Series modular splicing system
aliases:
- 3M 5815
- 5815 Series
- Modular Splicing System
category: Connectors and cable
make: 3m
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:3m
  cite:
  - src: src:eq-equip-bos-mv-termination-3m-cable-splicing-system-78812454540-a
    loc: sec=1.1
    h: 7e23ea5e8f8f
  - src: src:eq-equip-bos-mv-termination-3m-catalog-separable-connectors-emd-2013-11
    loc: sec=h19
    h: a2dd1aea84e8
  review: drafted
  review_note: 'support check: partial - Passages describe the 3M 5815 Series but none name 3M Electrical
    Markets as the maker (only the 3M brand mark).'
- claim_id: c2
  rel: instance_of
  target: comp:mv-separable-connector
  note: Fully shielded 600 A separable insulated connector system for shielded power cable.
  cite:
  - src: src:eq-equip-bos-mv-termination-3m-cable-splicing-system-78812454540-a
    loc: sec=1.1
    h: 7e23ea5e8f8f
  - src: src:eq-equip-bos-mv-termination-3m-catalog-separable-connectors-emd-2013-11
    loc: sec=h19
    h: a2dd1aea84e8
  review: drafted
- claim_id: c3
  rel: certified_to
  target: std:ieee-386
  note: Meets ANSI/IEEE 386 requirements for 600 A dead-break interfaces.
  cite:
  - src: src:eq-equip-bos-mv-termination-3m-catalog-separable-connectors-emd-2013-11
    loc: sec=h25
    h: ce8952e0bc1a
  - src: src:eq-equip-bos-mv-termination-3m-cable-splicing-system-78812454540-a
    loc: sec=4.0
    h: 8e70b8e8197f
  - src: src:eq-equip-bos-mv-termination-3m-cable-splicing-system-78812454540-a
    loc: sec=1.1
    h: 7e23ea5e8f8f
  - src: src:eq-equip-bos-mv-termination-3m-catalog-separable-connectors-emd-2013-11
    loc: sec=h19
    h: a2dd1aea84e8
  review: drafted
  review_note: 'support check: partial - Passages say it meets ANSI/IEEE 386 requirements, but not that
    it is certified.'
- claim_id: c4
  rel: requires
  target: prod:3m-5815-b-adapter-kit
  note: One adapter kit is needed per cable connected; adapter kits fit the tee modules to specific cable
    sizes.
  cite:
  - src: src:eq-equip-bos-mv-termination-3m-catalog-separable-connectors-emd-2013-11
    loc: sec=h25
    h: ce8952e0bc1a
  - src: src:eq-equip-bos-mv-termination-3m-cable-splicing-system-78812454540-a
    loc: sec=1.2
    h: d9131c3aac43
  - src: src:eq-equip-bos-mv-termination-3m-cable-splicing-system-78812454540-a
    loc: sec=8.0
    h: 5b91904f83ab
  - src: src:eq-equip-bos-mv-termination-3m-catalog-separable-connectors-emd-2013-11
    loc: tbl=21.r1
    h: 6da3aec98a02
  review: drafted
  review_note: 'support check: partial - An adapter kit is required per cable, and 5815-B Series adapter
    kits fit cable sizes, but a specific ''5815-B adapter kit'' product is a series, not singly named.'
- claim_id: c5
  attr: nominal_voltage
  value:
    min: 5
    max: 25
    unit: unit:KiloV
  conditions: Cable voltage class rating of the kits (5, 8, 15 and 25 kV shielded power cables)
  cite:
  - src: src:eq-equip-bos-mv-termination-3m-catalog-separable-connectors-emd-2013-11
    loc: sec=h25
    h: ce8952e0bc1a
  - src: src:eq-equip-bos-mv-termination-3m-catalog-separable-connectors-emd-2013-11
    loc: sec=h19
    h: a2dd1aea84e8
  - src: src:eq-equip-bos-mv-termination-3m-cable-splicing-system-78812454540-a
    loc: sec=h1
    h: 51d865a82f90
  review: drafted
- claim_id: c6
  attr: nominal_voltage
  value:
    max: 25
    unit: unit:KiloV
  conditions: Voltage rating of completed connections
  cite:
  - src: src:eq-equip-bos-mv-termination-3m-cable-splicing-system-78812454540-a
    loc: sec=4.0
    h: 8e70b8e8197f
  review: drafted
- claim_id: c7
  attr: rated_output_current
  value:
    nominal: 600
    unit: unit:A
  conditions: Continuous current rating of the separable connector system
  cite:
  - src: src:eq-equip-bos-mv-termination-3m-catalog-separable-connectors-emd-2013-11
    loc: sec=h25
    h: ce8952e0bc1a
  - src: src:eq-equip-bos-mv-termination-3m-cable-splicing-system-78812454540-a
    loc: sec=1.1
    h: 7e23ea5e8f8f
  - src: src:eq-equip-bos-mv-termination-3m-catalog-separable-connectors-emd-2013-11
    loc: sec=h19
    h: a2dd1aea84e8
  review: drafted
- claim_id: c8
  attr: operating_temperature
  value:
    nominal: 90
    unit: unit:DEG_C
  conditions: Rated operating temperature of the shielded power cable the system is used on
  cite:
  - src: src:eq-equip-bos-mv-termination-3m-cable-splicing-system-78812454540-a
    loc: sec=4.0
    h: 8e70b8e8197f
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c9
  attr: operating_temperature
  value:
    nominal: 130
    unit: unit:DEG_C
  conditions: Emergency overload rating of the shielded power cable the system is used on
  cite:
  - src: src:eq-equip-bos-mv-termination-3m-cable-splicing-system-78812454540-a
    loc: sec=4.0
    h: 8e70b8e8197f
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
---
The 3M 5815 Series is a modular, fully shielded 600 A separable connector system. It is used to splice, tap and dead-end medium-voltage shielded power cable, and to connect cable to deadfront apparatus. The kits are rated for 5, 8, 15 and 25 kV class industrial shielded cables, and connections are rated up to 25 kV. The system meets ANSI/IEEE 386 for 600 A dead-break interfaces and connects to transformers, switches and switchgear that have 600 A bushings. Kits can be combined for 3-way, 4-way and parallel feed tap configurations, and modules can be added or removed later. The basic 5815-S kit is a two-way splice that can be disconnected to isolate circuits for maintenance. Every cable needs its own 5815-B Series adapter kit, which fits the tee module to the cable size. A T-Wrench tool is available for kits that include connecting plugs. A capacitive test point on the insulating plug lets you test the circuit without disturbing the bolted connection. The finished installation is suitable for submerged or direct burial locations. It suits tape shield, wire shield, UniShield and jacketed concentric neutral solid dielectric cables rated for 90 °C operation and 130 °C emergency overload. Freezing does not harm the components.

<!-- review notes
- sentence 5: support check: partial - Adapter kit per cable and 5815-B adapt to cable sizes are stated, and an AT-Wrench is available for kits with connecting plugs; the 'T-Wrench' name is a minor variation.
-->
