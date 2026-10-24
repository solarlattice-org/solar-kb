---
id: concept:half-cut-cells
type: Concept
name: Half-cut cells
aliases:
- half-cell module
- half cut cell
- half cells
- halved cells
- Half-cut series module
- half-cut-cell modules
category: Modules
concept_kind: technology
claims:
- claim_id: c1
  rel: subclass_of
  target: concept:crystalline-silicon
  note: Half cells are made by cutting Si wafer-based cells in half (or thirds).
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.1
    h: 894ffea14400
  review: drafted
  review_note: 'support check: partial - Passage says Si wafer-based cells are cut into half or third
    cells, but does not explicitly classify half-cut cells as crystalline silicon PV; it''s implied via
    Si wafer-based.'
- claim_id: c2
  rel: related_to
  target: fm:cell-cracks
  note: Laser cutting introduces micro cracks at the cut edge that can grow into dendritic cracks during
    transport, installation and field loads.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h103
    h: 5b4f784910a6
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.1
    h: 894ffea14400
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r3
    h: 92b47e236381
  review: drafted
- claim_id: c3
  rel: related_to
  target: fm:hot-cell
  note: Half cells dissipate heat better due to a larger perimeter-to-area ratio, but larger wafer formats
    reduce this benefit.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c4
  rel: related_to
  target: mit:shade-resistant-modules
  note: Half-cell modules are marketed as one type of shade-resistant module.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:shading-loss
  note: Half-cut cell modules are more resistant to shading, e.g. when the lower half is shaded in portrait
    orientation.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h103
    h: 5b4f784910a6
  review: drafted
- claim_id: c6
  rel: related_to
  target: stressor:snow-load
  note: Half-cut cells may be susceptible to cracking under heavy snow loads or extreme cold.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h103
    h: 5b4f784910a6
  review: drafted
- claim_id: c7
  rel: related_to
  target: mit:multi-busbar-cells
  note: Multi-wire interconnection reduces power loss from cracks in halved cells compared with ribbon-based
    modules.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.1
    h: 894ffea14400
  review: drafted
- claim_id: c8
  rel: related_to
  target: method:el-imaging
  note: EL inspection on arrival revealed cut-edge cracks in half-cell modules.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.1
    h: 894ffea14400
  review: drafted
- claim_id: c9
  rel: related_to
  target: prod:enphase-iq7
  note: IQ7PLUS-72-2-US pairs with most 120 half-cell and 144 half-cell modules.
  cite:
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: tbl=22.r10
    h: 219f838d3084
  review: drafted
- claim_id: c10
  attr: typical_power_loss
  value:
    nominal: 0.2
    unit: unit:PERCENT
  conditions: Module power loss per dendritic-like cracked half-cell in a multi-wire PERC module (Hwang
    et al.)
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.1
    h: 894ffea14400
  review: drafted
  review_note: possible conflict with c11 (same source; check the conditions)
- claim_id: c11
  attr: typical_power_loss
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: Module power loss reached with about 25 dendritic-like cracked half-cells in a multi-wire
    module
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.1
    h: 894ffea14400
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions)
---
Half-cut cells are silicon wafer-based solar cells cut in half, usually by a laser, before being built into a module. Half-cut cell modules use six strings of cells instead of the usual four, which gives a higher voltage and better tolerance of shading. In portrait orientation they do better than standard modules when the lower half is shaded, for example by snow. That is why they are sold as shade-resistant modules. Because a half cell has more edge for its area, it sheds heat better, which helps limit hot cell temperatures. Larger wafers reduce this benefit. The drawback is that cutting leaves small cracks at the cut edge. These can grow into dendritic cracks during transport, installation, mechanical loading and temperature swings, so electroluminescence imaging on arrival is worthwhile. In multi-wire modules, each cracked half cell costs only a small amount of power, so the impact usually stays low unless many cells are cracked. Field degradation data for cut-cell, multi-wire designs is still lacking, especially from snowy northern sites. Equipment datasheets often quote module compatibility by half-cell count, for example 120 or 144 half-cell modules for microinverters.

<!-- review notes
- sentence 1: support check: partial - Cutting Si wafer cells into half, by laser ablation, is stated, but 'usually by a laser' and 'before being built into a module' are only loosely supported; other methods (thermal laser separation) are also mentioned.
- sentence 3: support check: partial - Outperforming in portrait when lower half is shaded is stated, but 'for example by snow' and 'that is why they are sold as shade-resistant' is a causal link not explicitly stated.
- sentence 5: support check: partial - Cut-edge cracks growing into dendritic cracks and EL inspection on arrival are described, but recommending EL on arrival as 'worthwhile' is not explicitly stated.
- sentence 8: support check: partial - The datasheet example supports 120/144 half-cell compatibility for a microinverter, but the generalization that equipment datasheets often do this rests on one example.
-->
