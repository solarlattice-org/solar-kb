---
id: comp:solar-cell
type: Component
name: Solar cell
aliases:
- photovoltaic cell
- PV cell
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 1
    max: 3
    unit: unit:PERCENT
  conditions: Boron-oxygen LID in p-type crystalline silicon cells, within the first days of sun exposure
  note: The annex says LID affects mainly p-type boron-doped cells. Gallium-doped and n-type cells are
    much less affected or not affected.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: LeTID in crystalline silicon cells (first seen with PERC), at elevated temperatures above
    50°C; adds to LID loss
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: LeTID in multicrystalline cells, at active temperatures above 65°C, in specific conditions
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h5
    h: 048d7dac489d
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  attr: typical_power_loss
  value:
    max: 30
    unit: unit:PERCENT
  conditions: Light-induced degradation (light soaking effect) of module power, as reported in a general
    overview
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h3
    h: 950db263c013
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c5
  attr: temperature_rise
  value:
    max: 25
    unit: unit:DEG_C
  conditions: Hot cell in an IBC half-cell module compared with module temperature, in an indoor hot-spot
    test at 55°C module temperature per IEC 61215-2:2021
  note: The IBC cell's built-in Zener diode acts as a bypass diode and lowers the breakdown voltage.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c6
  attr: typical_power_loss
  value:
    min: 10
    unit: unit:PERCENT
  conditions: Nearly half of 159 modules (165 Wp) in one solar park with cell cracks, after 6 years of
    operation
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
---
The solar cell is the silicon device inside a PV module that turns light into electric current. Many cells are joined together and embedded in each module. Cells are made of silicon, which makes them very brittle. One reference example is a monocrystalline silicon cell. The front glass protects the cells from the outside environment. If the glass breaks, moisture can reach the cells, which speeds up degradation and can cause hotspots. Cell cracks can form during wafer slicing, stringing, transport and installation. Wind, snow and temperature swings can make cracks grow until parts of the cell become inactive. Light-induced degradation (LID and LeTID) happens at the cell level. It mainly affects p-type boron-doped cells and shows up as lower STC power, current and voltage early in the system's life. Cracking, shading or mismatch can push a cell into reverse bias, so it heats up as a hot cell or hotspot. This can lead to discoloration, interconnection failures, delamination and glass breakage. Dust on the glass scatters and absorbs light before it reaches the cells, so module current drops. The IEC 61215-2 MQT 09 hot-spot endurance test checks how well cells and module materials withstand localized heating. Manufacturers also sort cells by current and screen out cells with low shunt resistance.

<!-- review notes
- sentence 1: support check: partial - Passage says cells are silicon and many are embedded in a module, but does not state that they turn light into electric current (definition) in these passages.
-->
