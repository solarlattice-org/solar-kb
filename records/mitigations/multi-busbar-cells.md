---
id: mit:multi-busbar-cells
type: Mitigation
name: Multi-busbar cell design
aliases:
- multi wire
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 0.2
    unit: unit:PERCENT
  conditions: Multi-wire PERC modules, per half-cell with a dendritic-like crack
  quote: For multi wire PERC modules 0.2% power loss per dendritic like cracked half-cell is typical.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r5
    h: 0a21fb8dc566
  review: drafted
---
This design puts more than three busbars on each cell, or uses multi-wire interconnection, instead of the older layout with 2 to 4 interconnect ribbons. It is a module design choice that limits the power lost to cell cracks. With more interconnecting ribbons, the cell keeps collecting current even when it is cracked, so series resistance and mismatch losses are lower. Because the contacts are closer together, a crack can only cut small pieces of the cell off from their busbar. Multi-wire and multi-busbar modules lose much less power from cracks than ribbon-based modules, and a typical figure for multi-wire PERC modules is 0.2% per half-cell with a dendritic crack. One limit is that modern high fill factor modules run with Impp close to Isc, so even small detached cell pieces can still cost power. For a module with a fill factor near 79%, only about 5% of the total cell area can be detached before power is affected, compared with 8% to 10% for older modules near 73%.

<!-- review notes
- sentence 2: support check: partial - The passages say multi-busbar or multi-wire designs reduce the risk of power loss and give much lower crack-related losses, but they don't call it a design choice and don't say it limits the loss in those words.
- sentence 4: support check: partial - u3 says only small pieces can detach from their busbar with more busbars or multi wire, but it doesn't say the contacts are closer together.
-->
