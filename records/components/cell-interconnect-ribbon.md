---
id: comp:cell-interconnect-ribbon
type: Component
name: Cell interconnect ribbon
aliases:
- busbars
- interconnect ribbon
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 35
    unit: unit:PERCENT
  conditions: One crystalline silicon module with a single interconnect ribbon locally disconnected (failure
    stage 1), I-V curve measured indoors at standard test conditions
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.6
    h: 31f745f3dabf
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 46
    unit: unit:PERCENT
  conditions: Module with both parallel interconnect ribbons disconnected, so the sub-module is bypassed
    through its diode (failure stage 2), I-V curve measured at standard test conditions
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.6
    h: 31f745f3dabf
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions)
---
The cell interconnect ribbon connects wafer-based crystalline silicon cells in series. It runs from the front of one cell to the rear of the next, forming a string of cells and raising the voltage. The ribbon sits directly on top of the cell busbars, so it often hides them during inspection. Strings of cells are then joined by a separate string interconnect, usually near the module edge. The main failure mode is cell interconnection failure: the ribbon weakens and breaks. The ribbon kink between cells and the joint with the string interconnect are the most prone to fatigue breakage. Causes include poor soldering, ribbons placed in the wrong position, too much deformation of the kink, and cells spaced too closely. In the field, transport stress, thermal cycling, wind load, hail, corrosion and hot spots from partial shading also play a part. If the bypass diode also fails, a broken ribbon can overheat. This can lead to glass breakage and burn marks on the backsheet. Broken ribbons can be found with electroluminescence imaging, infrared thermography, UV fluorescence imaging, the signal transmission method and IV curve analysis.

<!-- review notes
- sentence 4: support check: partial - Most causes are listed (soldering, misplacement, kink deformation, narrow spacing, transport, thermal cycling, wind, hail, corrosion, shading hot spots), but those are stated as causes/fatigue contributors; broadly supported, though the passage doesn't phrase all as 'in the field' causes of ribbon failure uniformly.
- sentence 6: support check: partial - EL, IR, UV imaging and signal transmission are stated for detection, and IV curves show the loss, but the passages don't explicitly list IV curve analysis for detecting broken ribbons in the u4 text (u25 mentions IV analysis for interconnection issues generally).
-->
