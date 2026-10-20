---
id: meas:el-crack-pattern
type: Measurement
name: Crack pattern in EL image
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 10
    unit: unit:PERCENT
  conditions: Nearly half of 159 modules rated 165 Wp in one solar park, after 6 years of operation; attributed
    to cell cracks
  note: Field example from the literature. In the same park, 3.8% of modules had cracks that made the
    bypass diode bypass the cracked sub-module.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: drafted
---
In an EL image a cell crack shows up as a dark grey line. Its width and grey level stay mostly the same along its length, and when the crack runs at an angle to the fingers it can look like a wavy step. If the EL brightness changes sharply across the dark line, it is a crack that already cuts conductivity through the metallisation. In multicrystalline cells, crystal defects can also look like dark lines, so a trained person has to read the image. Cracked cell parts that are fully cut off from the interconnect ribbon are easier to see in an image taken at about one tenth of rated current than at rated current. Some crack patterns point to a cause. An X-shaped pattern across the module means a heavy, even mechanical load. Branching (dendritic) cracks in the middle cells come from tilting the module over, dropping it, poor packaging or very heavy snow, and they form after lamination. Branching cracks that spread from a few impact points come from impacts, such as hail or local pressure during installation, and a visual inspection is needed to tell which. A repeating crack pattern that is rotated 180 degrees from one cell string to the next is a production fault from the stringer before lamination. Cracks starting at the ribbon come from soldering stress, and cross cracks in the middle of the cell come from needles pressing on the wafer. Wide crack patterns can leave large parts of cells electrically inactive and dark. Inactive areas above a certain size cause power loss, and they can cause hotspots and burn marks. EL is usually done in the dark with a DC supply driving current through the module. In the field this can be done at night or under curtains, often after IR thermography has found the suspect modules.

<!-- review notes
- sentence 4: support check: partial - The X pattern is tied to heavy homogeneous mechanical load, and dendritic cracks to tilting, dropping, packaging or heavy snow, and to occurrence after lamination. The passages do not say that the dendritic cracks are in the middle cells for all those causes (only the tilt-over row says so), so this detail is overgeneralised.
-->
