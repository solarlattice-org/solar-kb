---
id: stressor:object-impact
type: Stressor
name: Object impact
aliases:
- heavy impacts
- impact stresses
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 1
    max: 2
    unit: unit:PERCENT
  conditions: Documented glass breakage events of any cause in temperate climates, as a share of whole-system
    power; the dataset had one exception
  note: The figure covers glass breakage events in general, not only those caused by object impact.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: fig=40
    h: 5ad82fec7183
  review: drafted
---
Object impact is a mechanical stressor: a heavy object such as a stone or hailstone hits the module and can break the front glass. Blows to the glass edge are another cause of breakage. This is common with CdTe modules, and frameless modules suffer edge breakage more often than framed ones. Annealed or only slightly hardened front glass, which thin-film superstrate modules use, holds far less compressive stress than thermally tempered glass. It therefore breaks under weaker impacts. To check the origin of a break, look at the fragments. Tempered glass shatters into small pieces across the whole sheet, while non-tempered glass does not fragment, so the impact point is easy to find. Vandalism and animals, such as goats, can also damage module glass. Broken glass can create safety hazards and insulation faults, let moisture in, and speed up electrical degradation. Use visual inspection, insulation testing, electroluminescence imaging and a review of operating data to judge the impact. Replace broken modules when safety or insulation is at risk, and investigate the root cause.
