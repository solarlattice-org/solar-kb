---
id: meas:el-inactive-cell-area
type: Measurement
name: Inactive cell area in EL
aliases:
- inactive cell part
- isolated cell parts
- inactive area
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 10
    unit: unit:PERCENT
  conditions: Field solar park of 159 modules rated 165 Wp, after 6 years of operation; nearly half of
    the modules affected, linked to cell cracks
  note: Reported for cracked-cell modules in general, not measured per unit of inactive area; some modules
    had cracks forcing the bypass diode to conduct.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: drafted
  review_note: 'support check: partial - Passage says nearly 50% of 159 modules (165 Wp) show power loss
    of ~10% or more after 6 years and 3.8% have bypass-forcing cracks, but it doesn''t tie this to inactive
    cell area in EL; the statement''s ''at least 10 percent'' matches ''~10% or more'' loosely and the
    note acknowledges this.'
---
In an EL image, an inactive or dead cell area is a part of a cell that stays dark because it no longer adds to the module's power output. It usually shows up next to large cell cracks: thermal stress, mechanical stress and humidity can cut that part of the cell off electrically. A failed cell interconnection can also leave a dark region, because the broken connection no longer collects carriers. In the IR image, the same spot often shows as a hot spot. Take EL images at night or in low light, with DC current driven through the module. Subtracting a dark field image helps cut out stray light. Above about 8 percent inactive area in a typical 60-cell module, power loss rises roughly in line with the inactive area. In a string, the loss rises much more steeply. At half the cell area or more, the bypass diode switches on and about one third of the module's power is lost. Inactive cell parts larger than this can also cause hot spots and burn marks if the active part of the cell has a localized reverse current path. If you image at nominal current, a cell part that looks isolated may not actually cost much power. Imaging at about one tenth of Isc shows more reliably which dark parts matter for power. Check the electrical impact with IV curve tracing, and use IR thermography to look for active heating.

<!-- review notes
- sentence 1: support check: partial - Passage defines dead/inactive cell part as no longer contributing to power output, but never says it appears dark in EL images.
-->
