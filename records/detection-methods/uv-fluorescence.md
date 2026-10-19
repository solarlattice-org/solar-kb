---
id: method:uv-fluorescence
type: DetectionMethod
name: UV fluorescence imaging
aliases:
- UVF
- FL imaging
- UV fluorescence
claims:
- claim_id: c1
  rel: produces
  target: meas:uvf-dark-crack-line
  note: A cell crack shows as a dark bar on the cell because the fluorescent encapsulant is photobleached
    along the crack, where oxygen diffusing through the backsheet reaches it. Number, position and orientation
    of cracks can be read from the image. Cracks at the cell edge cannot be seen because the cell border
    is bleached too.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.5
    h: da5687053a7f
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-19
- claim_id: c2
  rel: produces
  target: meas:uvf-uneven-cell-fluorescence
  note: With a disconnected cell interconnect, current flows through only one ribbon. That side of the
    cell heats more and forms more lumophores, so it fluoresces more strongly. When part of a cell is
    isolated, the reverse-biased non-isolated part shows increased fluorescence.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=23
    h: 3c7fbe882789
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
UV fluorescence imaging is a non-destructive way to analyse failures in PV modules. A camera records the visible light that the encapsulant gives off when UV light shines on it. It has to be done in the dark, usually at night. Modules do not need to be disconnected or powered, and imaging one module usually takes less than 60 seconds. The method only works after sunlight has built up fluorescent products in the encapsulant. The suggested UV dose is about 80 kWh/m², which is roughly 1.5 years outdoors in Germany. Cell cracks show up as dark bars caused by photobleaching. A crack is easier to identify this way than in an EL image, but cracks at the cell edge or close to the interconnector are hard or impossible to see. It can also show isolated cell parts and disconnected cell interconnects. It can find cell cracks caused by glass breakage, and the signal also depends on the defect type, such as hotspots or broken glass. Used together with EL, it helps date damage, because new cracks appear only in EL until the fluorescence has had time to bleach. Drone-based night inspections need at least two trained people and calm conditions. The drone's battery drains quickly with the extra load. Modules with UVA-transparent EVA reduce how well the method works, and reading the results takes expertise that many O&M providers lack.

<!-- review notes
- sentence 5: support check: partial - The table and u12 support isolated cell parts, disconnected interconnects, and EL/UVF identifying cracks from glass breakage, and u1 says the signal depends on defect type; however, u12's 'cell cracks caused by glass breakage' is stated loosely and this is only partly the same as the claim.
- sentence 7: support check: partial - u1 supports the two-person minimum, calm conditions, quick battery drain, UVA-transparent EVA reducing effectiveness, and O&M expertise gaps; however, the 'at least two trained people' and 'at night' are consistent, but the evidence says these apply to drone-based UVF specifically and that expertise lack is reported as 'many' providers, which the statement matches only loosely.
-->
