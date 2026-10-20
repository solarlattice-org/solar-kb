---
id: symptom:uneven-cell-heating
type: Symptom
name: Uneven cell heating
aliases:
- inhomogeneous heating
- Heated cells
- overheated cells
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-hot-cell
  note: One cell is clearly warmer than its neighbours. Possible causes are shading, a defective cell
    or a delaminated cell. In monocrystalline cells the hot cell effect raises the temperature evenly
    across the whole cell.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=14.r5
    h: 9eee3a518c3f
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
  review_note: 'support check: partial - One warmer cell, causes (shading, defect, delaminated) and the
    monocrystalline homogeneous heating are stated, but the TmpBOM signal pattern is not in the passages
    (not judged), and ''hot cell effect'' is described as associated with mono cells generally.'
- claim_id: c2
  rel: observed_as
  target: meas:ir-hotspot
  note: Heating at a point. Possible causes are partial shading (for example a bird dropping or a lightning
    rod), local junction breakdown, which is mainly seen in multicrystalline cells, or a micro-arc in
    the interconnection circuit.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=14.r7
    h: 2ecdf25b9b10
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=24.r1
    h: 0e754337dfa9
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:ir-partial-cell-heating
  note: Part of one cell is warmer than the rest. This is linked to a broken cell or a disconnected string
    interconnect, and comes with a drastic power loss and a lower fill factor.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=14.r6
    h: 156474127b00
  review: drafted
- claim_id: c4
  attr: temperature_rise
  value:
    min: 10
    max: 20
    unit: unit:K
  conditions: Temperature gradients between heated cells seen in field IR inspection. The source calls
    this range unproblematic for now but says it may grow during operation.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=h58
    h: df4b70555c37
  review: drafted
- claim_id: c5
  attr: temperature_rise
  value:
    max: 25
    unit: unit:K
  conditions: Hot cell temperature above module temperature for an IBC half-cell module in an indoor hot-spot
    test at 55°C module temperature (IEC 61215-2:2021).
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
---
Uneven cell heating is seen in an IR image of a module under load: some cells, or parts of cells, are warmer than the cells around them. A bypass diode that has failed short-circuited makes individual cells heat unevenly during operation. It also keeps the module's voltage and power low all the time. When one whole cell is warmer, the cause may be shading, a defective cell or a delaminated cell. Look at the module first, because a leaf or lichen can cause a loss that clears after cleaning. When only part of a cell is warmer, suspect a broken cell or a disconnected interconnect. This usually comes with a large power loss and a lower fill factor on the IV curve. Heating at a single point usually points to partial shading such as bird droppings. A close visual inspection can then reveal a cell crack. Shading or cracking can drive a cell into reverse bias, so that it dissipates power as heat. Monocrystalline hot cells heat evenly across the cell, while multicrystalline hotspots stay local. Temperature differences of 10 to 20°C between cells are not a problem yet, but they may grow. Check such modules again in regular IR inspections.

<!-- review notes
- sentence 1: support check: partial - Cells or parts of cells warmer is supported, but 'module under load' is not stated in the passages.
- sentence 5: support check: partial - Partial shading like bird droppings is a listed cause and crack detection after visual inspection is possible, but 'usually' points to shading is not stated and the passages list other causes (artifact, micro-arc, junction breakdown).
-->
