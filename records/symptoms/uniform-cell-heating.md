---
id: symptom:uniform-cell-heating
type: Symptom
name: Uniformly heated cell
aliases:
- Hot cell
- Heated cells
- Overheated cell
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-hot-cell
  note: Whole cell appears warmer than its neighbours, with an even temperature rise over the full cell
    area rather than a point hotspot; typical of monocrystalline cells in reverse bias.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=14.r5
    h: 9eee3a518c3f
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: fig=17
    h: 32129334468a
  review: drafted
- claim_id: c2
  attr: temperature_rise
  value:
    min: 10
    max: 20
    unit: unit:K
  conditions: Temperature gradients of heated cells seen in field thermography; called unproblematic for
    now, though they may grow during plant operation
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=h58
    h: df4b70555c37
  review: drafted
- claim_id: c3
  attr: temperature_rise
  value:
    max: 25
    unit: unit:K
  conditions: Hot cell in an IBC half-cell module compared with module temperature, during an indoor hot-spot
    test at 55°C module temperature (IEC 61215-2:2021); PERC and SHJ modules ran hotter under the same
    test
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
---
In an infrared image, a uniformly heated cell is one whole cell that is clearly warmer than the cells around it. The heat is spread evenly across the cell instead of sitting in one small spot. This hot cell pattern usually shows up in monocrystalline cells. Shading or cracking causes current mismatch and pushes the weak cell into reverse bias, so it dissipates power as heat. A small, localized hotspot points more to multicrystalline cells. Possible causes are shading, a defective or shunted cell, a delaminated cell, or other internal cell problems. Power lost to shading, such as from a leaf or lichen, may not be permanent. If only part of the cell is warm, suspect a broken cell or a disconnected interconnect instead. These usually come with a sharp drop in power and fill factor. Warm cells along the bottom frame or in a patchwork pattern, in modules near the negative end of the string, point to potential induced degradation (PID). Check first: look at the module for shading or soiling and clean it if needed, then take a new IR image to see whether the heating is still there. Gradients of 10 to 20 °C are not a problem for now but can grow over time. Keep these modules on the regular thermography inspection list. If a hot cell is left in place, it can lead to discoloration, interconnection failures, cell cracks, delamination and loss of electrical insulation.

<!-- review notes
- sentence 6: support check: partial - u9 says visual inspection and cleaning needed for cell mismatch, but does not state a check-first order or re-imaging after cleaning.
-->
