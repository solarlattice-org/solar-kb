---
id: symptom:el-dark-regions
type: Symptom
name: Dark regions in EL image
aliases:
- dark EL areas
- dark region
- isolated cell parts
- symptom:dark-cells-el
- Dark cells in EL image
claims:
- claim_id: c1
  rel: observed_as
  target: meas:el-inactive-cell-area
  note: A cell area that stays dark because it no longer collects carriers. Causes include a failed interconnect,
    or a crack that cuts part of the cell off from the interconnect ribbon. Isolated parts show up better
    at about one tenth of rated current than at rated current.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=33.r1
    h: d997fdfa0219
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.3.1
    h: 1f95caadc75d
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=19.r5
    h: 3162f03181ef
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:el-crack-pattern
  note: Cracks appear as dark grey lines. Wide crack patterns can leave large parts of cells electrically
    inactive.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.4
    h: 1fb2586fa36b
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.3.1
    h: 1f95caadc75d
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:el-dark-cell-edges
  note: With PID, cells turn dark at the module boundaries, with darkened cell edges next to the frame.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.3.1
    h: 1f95caadc75d
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:el-dim-cell
  note: In one example, a whole cell was much dimmer than the others because its busbars were not connected
    properly.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.3.1
    h: 1f95caadc75d
  review: drafted
- claim_id: c6
  rel: observed_as
  target: meas:el-intensity-shift
  note: Polarization-type PID lowers luminescence with no dependence on low current bias, so it is harder
    to pick out in EL than shunting-type PID.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  review: drafted
---
In an EL image, damaged parts of a module look dark or give off less light than healthy areas. A broken or weak cell interconnection is hard to see by eye. In EL it shows as a dark region where the failed interconnect would otherwise collect carriers, and in IR it often shows as a hot spot. Other causes give different patterns. Cracks show as dark grey lines and can cut off parts of a cell. A badly connected busbar can make a whole cell dimmer. PID darkens cells along the module edges next to the frame. EL alone does not show how much power a dark area costs, so combine it with IR thermography and IV curve analysis to separate interconnection faults from cracks or diode failures. In the field, use IR first to find the abnormal modules, then take EL images of them on site in the dark or in a lab. If you need to know whether an isolated cell part really costs power, take the EL image at about one tenth of rated current. At rated current, isolated parts may only show as noise, and their power impact cannot be judged.

<!-- review notes
- sentence 2: support check: partial - Passages support hard to see by eye, dark region in EL, and hot spot in IR, but do not say the IR hot spot is 'often' seen; they say 'or as a hot spot'.
-->
