---
id: stressor:current-mismatch
type: Stressor
name: Cell current mismatch
aliases:
- cell mismatch
- mismatch
claims:
- claim_id: c1
  attr: temperature_rise
  value:
    max: 25
    unit: unit:DEG_C
  conditions: IBC half-cell module with built-in Zener bypass behaviour, indoor hot-spot test at 55°C
    module temperature per IEC 61215-2:2021; hot cell temperature compared with module temperature
  note: The same tests found PERC and SHJ modules ran clearly hotter under these conditions. 55°C is a
    lab setpoint, not a rise.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
---
Cell current mismatch happens when some cells in a series circuit make less current than the rest, for example because they are cracked or shaded. The weaker cells are pushed into reverse bias, where they absorb power and heat up. This drives module hotspots and hot cells. In multicrystalline cells the heating tends to stay at one point. In monocrystalline cells it tends to warm the whole cell evenly. Common sources are cracked cells that lose active area, solder bond defects, shadows from soiling, and strong cell mismatch caused by potential induced degradation. A hot cell can go on to cause discoloration, interconnection failures, more cell cracks, delamination and loss of electrical insulation. Very high temperatures can also damage the backsheet, solder joints and glass. Bifacial modules with uneven light on the rear side, and modules built with larger wafers, can reach higher hot cell temperatures when currents are mismatched. Manufacturers reduce the risk by sorting cells by current, screening out cells with low shunt resistance, and fitting bypass diodes. Putting fewer cells on each diode lowers the hot cell temperature. In the field, check warm cells visually. Clean off temporary shading such as leaves or lichen, and replace the module if a defective cell is causing the mismatch.

<!-- review notes
- sentence 1: support check: partial - Passages say cracking or shading causes current mismatch in underperforming cells, but don't define mismatch as some cells in a series circuit producing less current.
-->
