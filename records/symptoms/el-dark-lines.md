---
id: symptom:el-dark-lines
type: Symptom
name: Dark lines in EL image
aliases:
- dark grey line
claims:
- claim_id: c1
  rel: observed_as
  target: meas:el-crack-pattern
  note: A crack shows as a dark grey line of mostly constant width and grey level. It usually starts or
    ends at a busbar or cell edge; cross cracks sit mid-cell. An abrupt change in EL intensity across
    the line confirms a crack that reduces metallization conductivity. Impact cracks branch out from a
    few centres.
  quote: Cell cracks appear as dark lines on the solar cell in the EL image.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.4
    h: 1fb2586fa36b
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.3.1
    h: 1f95caadc75d
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: fig=49
    h: 9e8b5f835bf3
  review: drafted
---
In electroluminescence images, cracked solar cells show dark lines running across the cell. A typical crack is a dark grey line of fairly constant width and shade that starts or ends at a busbar or the cell edge, while cross cracks often sit in the middle of the cell. In multicrystalline cells, crystal defects can also look like dark lines. Comparing wafers that were neighbours in the ingot helps tell them apart, and an abrupt brightness change across the line points to a real crack. Cracks running almost parallel to the busbars can cut off large parts of a cell. An EL image taken at about 1/10 of rated current shows these isolated areas better than one taken at rated current. Branching cracks that spread from a few impact points suggest local pressure or hail, and a visual inspection of the module is needed to tell which. Weak or broken cell interconnects usually show up as dark regions rather than thin lines, and also as hot spots in IR images. First use IR thermography to find the suspect modules, then take EL images in the dark or at night to confirm cracks.

<!-- review notes
- sentence 6: support check: partial - Passage supports dark regions in EL and hot spots in IR for interconnect failures, but does not say they appear 'rather than thin lines' or 'usually'.
- sentence 7: support check: partial - Passages describe IR first to localize anomalous modules then EL (night/dark) follow-up, but u22 says modules are shipped to a lab for EL and nothing says EL is specifically to confirm cracks via this sequence.
-->
