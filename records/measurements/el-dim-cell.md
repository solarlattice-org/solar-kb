---
id: meas:el-dim-cell
type: Measurement
name: Dim cell in EL image
---
An EL image is made by driving a DC current through the module so the cells emit light, which a camera then records. This is done in the dark, at night, or with dark-field subtraction to remove stray light. A cell or part of a cell that emits less light shows up darker than its neighbours. Cell cracks show up as dark grey lines. If the brightness changes abruptly at such a line, the crack is already reducing conduction across the metallization. Cell cracks that cut cell parts off from the interconnect ribbon are easier to see in an image taken at about one tenth of rated current than in one taken at rated current. At nominal current, a dim cracked part may only show noise, so the image cannot tell whether that part costs power. At one tenth of short-circuit current, cell parts that fall below the noise level always matter for module power loss. Disconnected cell interconnections also show up in EL images of field modules. In potential induced degradation testing of heterojunction mini-modules, cells grew dark first at their edges, and the dark area then spread inward. Modules with higher power losses tend to show EL brightness shifted toward lower values. However, no clear link to a specific defect type has been established. A single image at one current and temperature may not identify the physical cause. Images at two bias currents, combined with IR thermography or photoluminescence, help narrow it down.

<!-- review notes
- sentence 2: support check: partial - Cracks as dark grey lines and abrupt-change implying reduced metallization conduction are stated, but the general claim that less-emitting areas look darker is only implied (cracks/defects appear dark).
-->
