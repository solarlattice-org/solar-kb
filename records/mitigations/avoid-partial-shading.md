---
id: mit:avoid-partial-shading
type: Mitigation
name: Avoiding partial shading
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 1
    max: 5
    unit: unit:PERCENT
  conditions: Typical cumulative annual shading loss of PV systems
  note: Loss caused by the shading that this action aims to avoid.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h78
    h: df63666c4734
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 20
    max: 30
    unit: unit:PERCENT
  conditions: Energy losses that can be observed from shading on rooftop or facade systems
  note: Source states losses of up to 20-30%; loss caused by shading, not by the mitigation.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h78
    h: df63666c4734
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions)
---
Avoiding partial shading is a preventive action that extends the life of bypass diodes. Partial shading can cause cell hotspots, and these can lead to burn marks and Bypass Diode Failure; prolonged shading can also lead to glass breakage, arcing or fire. Shading is best dealt with at the system planning stage, because it is usually too late to fix later. Run a basic shading analysis using a full year of sun and shade data to find the areas and times with heavy shading. Avoid areas shaded during the middle of the day or the sunny season, or apply a cost-effective shading mitigation measure. Shading can change over the life of a plant as vegetation grows or new structures are built. Inspect the system regularly, cut back trees or vegetation causing extra shading, and repair or replace modules that were damaged as a result. Other ways to reduce shading losses include better string and module layouts such as landscape mounting, module-level power electronics, inverter MPPT behaviour, and shade-tolerant modules such as half-cut or back-contact cells. Module-level power electronics have limits: shading still activates the bypass diode and creates a hotspot on the shaded cell, and the gain does not always outweigh the device's own losses. Note that partial shading of a thin-film module may void its warranty.

<!-- review notes
- sentence 5: support check: partial - Shading changing with vegetation/new construction, regular inspections, cutting vegetation, and repairing/replacing indirectly damaged modules are stated, but repair/replacement is conditioned on safety/severity risk of 5, not all damaged modules.
- sentence 8: support check: partial - Passage says partial shading of a thin-film module voids the warranty as an example, whereas the statement says 'may void', slightly weaker than stated.
-->
