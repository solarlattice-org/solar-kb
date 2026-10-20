---
id: symptom:dark-cells-el
type: Symptom
name: Dark cells in EL image
aliases:
- dark solar cells
- dark cell
claims:
- claim_id: c1
  rel: observed_as
  target: meas:el-dark-cell-edges
  note: With PID, cells at the module boundary next to the frame look dark. The darkening is attributed
    to current flowing through the reduced parallel (shunt) resistance rather than the PN junction. For
    PID-s it is most visible at a low current bias of about one tenth of rated current.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.3.1
    h: 1f95caadc75d
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c2
  rel: observed_as
  target: meas:el-intensity-shift
  note: Polarization-type PID lowers luminescence with no dependence on low current bias, so it is harder
    to pick out in EL than shunting-type PID.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:el-crack-pattern
  note: This is a differential pattern. Cracks show as dark lines and can leave large parts of cells electrically
    inactive. Useful for telling crack damage apart from PID-type edge darkening.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.4
    h: 1fb2586fa36b
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.3.1
    h: 1f95caadc75d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Cracks as dark lines and large electrically inactive areas versus
    PID edge darkening are stated, but ''differential pattern'' and its usefulness for telling them apart
    is only implied by the contrast.'
---
In an EL image, damaged parts of a module show up dark or give off less light than healthy areas. With potential induced degradation, the dark cells sit at the edges of the module, and the cell edges closest to the frame are darkened. Shunting-type PID shows up best when EL is taken at a low current of about one tenth of rated current, which can reveal affected modules before any power loss is noticeable. Polarization-type PID lowers luminescence without this low-current dependence, so it is harder to see in EL. Confirm PID with IV measurements together with IR or EL. A single fully dark cell can also mean a short-circuited cell, and a dimmer cell can mean a poor busbar connection. Cracks look different: they appear as dark lines that can leave parts of a cell inactive. Do an IR survey first to find suspect modules, then take EL images at night or in the dark with the string powered from a DC supply.
