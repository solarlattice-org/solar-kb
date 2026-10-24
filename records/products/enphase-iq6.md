---
id: prod:enphase-iq6
type: Product
name: Enphase IQ6 Microinverters
aliases:
- IQ6
- IQ6+
- IQ6PLUS
- IQ 6 Micros
category: Inverters
make: enphase
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:microinverter
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: tbl=6.r1
    h: a212cddc1540
  - src: src:enphase-enphase-iq6-iq6-microinverter-installation-guide
    loc: tbl=1.r1
    h: 1932d428cae9
  review: drafted
  review_note: 'support check: partial - Passages show IQ6 Microinverters per branch, implying microinverters
    by name, but never classify the IQ6 as a microinverter explicitly beyond naming.'
- claim_id: c2
  rel: compatible_with
  target: prod:enphase-iq9n
  note: IQ9N units can be added to existing IQ6 sites without an additional IQ Gateway; installation and
    commissioning follow the IQ8 Series process.
  cite:
  - src: src:kb-enphase-can-iq9n-microinverters-be-installed-with-iq6-iq7-iq8-microinverters-in-the-sam
    loc: sec=h1
    h: 9944f57123ab
  review: drafted
- claim_id: c3
  attr: max_count
  value:
    max: 16
    unit: unit:NUM
  conditions: Maximum IQ6 microinverters per AC branch circuit, 240 V single phase
  cite:
  - src: src:enphase-enphase-iq6-iq6-microinverter-installation-guide
    loc: tbl=1.r1
    h: 1932d428cae9
  review: drafted
- claim_id: c4
  attr: max_count
  value:
    max: 13
    unit: unit:NUM
  conditions: Maximum IQ6+ microinverters per AC branch circuit, 240 V single phase
  cite:
  - src: src:enphase-enphase-iq6-iq6-microinverter-installation-guide
    loc: tbl=1.r1
    h: 1932d428cae9
  review: drafted
---
The Enphase IQ6 family is a line of module-level microinverters made by Enphase, with an IQ6 and a higher-output IQ6+ version. On a 240 V single-phase branch circuit you can put up to 16 IQ6 units or up to 13 IQ6+ units. Enphase's AC voltage-rise tech brief gives branch current and voltage-rise tables for each branch size of IQ6 and IQ6+ units. Use these tables to size branch conductors. In those tables, one IQ6 unit adds about 0.96 A or 1.17 A of branch current depending on the table, and one IQ6+ unit adds about 1.35 A. IQ9N microinverters can be added to an existing IQ6 site without an extra IQ Gateway. They are installed and commissioned the same way as IQ8 Series units.

<!-- review notes
- sentence 1: support check: partial - IQ6 and IQ6+ versions are shown, but the passages don't say Enphase makes them or that IQ6+ is higher-output (though the current per unit is higher).
- sentence 3: support check: partial - Current and voltage-rise tables exist for IQ6 and IQ6+, but the passages don't mention a tech brief or say to use them for sizing conductors.
- sentence 1: review: partial - The IQ6 and IQ6+ versions appear in the passages, but they don't say the units are module-level microinverters made by Enphase or that the IQ6+ is the higher-output version.
-->
