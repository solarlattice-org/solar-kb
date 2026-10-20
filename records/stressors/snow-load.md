---
id: stressor:snow-load
type: Stressor
name: Heavy snowfall
aliases:
- heavy snow
- snow load
- snow loading
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 0
    max: 2
    unit: unit:PERCENT
  conditions: Annual average performance reduction from snow accumulation in southern US states
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h71
    h: a957afa61f49
  review: disputed
  review_note: 'support check: partial - The 0%–2% figure for southern states is stated, but the statement
    labels it ''heavy snowfall'' typical loss, which the passage assigns to heavy-snow places (10–16%).;
    possible conflict with c3 (same source; check the conditions)'
  conflicts_with:
  - stressor:snow-load#c5
  - stressor:snow-load#c6
  - stressor:snow-load#c7
  - stressor:snow-load#c9
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 2
    max: 4
    unit: unit:PERCENT
  conditions: Annual average performance reduction from snow accumulation in arid US states such as Colorado
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h71
    h: a957afa61f49
  review: disputed
  review_note: 'support check: partial - 2%–4% in arid states like Colorado is stated, but it is not described
    as heavy snowfall.; possible conflict with c3 (same source; check the conditions)'
  conflicts_with:
  - stressor:snow-load#c5
  - stressor:snow-load#c6
  - stressor:snow-load#c7
  - stressor:snow-load#c9
- claim_id: c3
  attr: typical_power_loss
  value:
    min: 10
    max: 16
    unit: unit:PERCENT
  conditions: Annual average performance reduction in heavy-snowfall US states such as Michigan, Wisconsin
    and Maine
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h71
    h: a957afa61f49
  review: disputed
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions)
  conflicts_with:
  - stressor:snow-load#c5
  - stressor:snow-load#c8
  - stressor:snow-load#c9
- claim_id: c4
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: Yearly snow losses for standard framed modules at latitudes above 60°N in Sweden (most often)
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: drafted
  review_note: 'support check: partial - The passage says losses are most often less than 10% yearly,
    an upper bound, not a typical loss value of ''up to 10%'' under heavy snowfall.; possible conflict
    with c5 (same source; check the conditions); possible conflict with c6 (same source; check the conditions);
    possible conflict with c7 (same source; check the conditions); possible conflict with c9 (same source;
    check the conditions)'
- claim_id: c5
  attr: typical_power_loss
  value:
    nominal: 18
    unit: unit:PERCENT
  conditions: Measured annual production loss, modules at 0° tilt, Sierra Mountains, USA
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: disputed
  conflicts_with:
  - stressor:snow-load#c1
  - stressor:snow-load#c2
  - stressor:snow-load#c3
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions);
    possible conflict with c8 (same source; check the conditions); possible conflict with c9 (same source;
    check the conditions)
- claim_id: c6
  attr: typical_power_loss
  value:
    nominal: 15
    unit: unit:PERCENT
  conditions: Measured annual production loss, modules at 24° tilt, Sierra Mountains, USA
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: disputed
  conflicts_with:
  - stressor:snow-load#c1
  - stressor:snow-load#c2
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions);
    possible conflict with c8 (same source; check the conditions); possible conflict with c9 (same source;
    check the conditions)
- claim_id: c7
  attr: typical_power_loss
  value:
    nominal: 12
    unit: unit:PERCENT
  conditions: Measured annual production loss, modules at 39° tilt, Sierra Mountains, USA
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: disputed
  conflicts_with:
  - stressor:snow-load#c1
  - stressor:snow-load#c2
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions);
    possible conflict with c8 (same source; check the conditions); possible conflict with c9 (same source;
    check the conditions)
- claim_id: c8
  attr: typical_power_loss
  value:
    min: 0.3
    max: 2.7
    unit: unit:PERCENT
  conditions: Annual snow-cover losses, frameless modules at 28° tilt, grid-connected system in Bavaria,
    Germany
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: disputed
  review_note: 'support check: partial - The 0.3–2.7% annual loss for frameless 28° modules in Bavaria
    is stated, but it is not described as heavy snowfall.; possible conflict with c5 (same source; check
    the conditions); possible conflict with c6 (same source; check the conditions); possible conflict
    with c7 (same source; check the conditions); possible conflict with c9 (same source; check the conditions)'
  conflicts_with:
  - stressor:snow-load#c3
- claim_id: c9
  attr: typical_power_loss
  value:
    nominal: 23
    unit: unit:PERCENT
  conditions: Monthly loss from snow cover in January 2017, Konya, Turkey, compared with daily-cleaned
    modules
  note: Daily losses there could approach 100%.
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: disputed
  conflicts_with:
  - stressor:snow-load#c1
  - stressor:snow-load#c2
  - stressor:snow-load#c3
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions);
    possible conflict with c7 (same source; check the conditions); possible conflict with c8 (same source;
    check the conditions)
---
Heavy snowfall loads PV arrays with snow mass and also covers modules so irradiance cannot reach the cells, which costs energy during winter. Under the weight of snow, modules can bend until the glass and cells crack. Ice dams can tear off the bottom frame, and racks that were not engineered for the load can collapse. Wet, wind-packed or refrozen snow is much denser than fresh snow. Freeze-thaw cycles in spring and drifts near walls or between rows can build loads high enough to burst or deform frames. Snow lying on the modules and snow sliding off unevenly cause snow accumulation yield losses and uneven current between strings. Mounds of shed snow can block the lower edge of the modules and stop trackers from moving. Cold makes cells more brittle, so cell cracks are more likely at snowy sites. Large-format modules and corner-clamped modules are especially vulnerable. Exposure can be reduced with steeper tilt, high ground clearance, tracker snow-stow strategies, and bifacial or frameless modules that shed snow faster. Robust modules with thicker glass and well-engineered racking also help. After winter, inspect the array visually and thermally image a subset of modules. Where snow sticks heavily, remove it with a turbo-fan rather than a shovel.

<!-- review notes
- sentence 5: support check: partial - Cold-induced brittleness and cracking at snowy sites is stated, and large-format modules are noted as not reinforced, but corner-clamped modules were only noted as damaged, not stated as especially cracking-vulnerable.
- sentence 7: support check: partial - Post-winter visual inspection with thermal imaging of a subset and turbo-fan snow removal are stated, but the passages do not tie turbo-fan removal specifically to heavily stuck snow, and say removal is generally not recommended.
-->
