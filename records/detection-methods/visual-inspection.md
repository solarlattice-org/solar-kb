---
id: method:visual-inspection
type: DetectionMethod
name: Visual inspection
aliases:
- VI
claims:
- claim_id: c1
  rel: produces
  target: meas:visible-burn-marks
  note: Burn marks seen by eye point to hot spots and can show bypass diode failure; the units list visual
    burn-mark inspection among the diode checks.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=front
    h: 44eaacc73841
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.1.2
    h: 567ebeacf6c2
  review: drafted
---
Visual inspection means looking over PV modules and other parts by eye to find defects. It is described as the quickest and most effective way to find module failures. In laboratory testing under IEC 61215 and 61646, modules are inspected before and after stress tests, under more than 1000 lux of light, and only defects visible to the bare eye count. Record every visible defect with its position and size. Take photos without reflections and describe defects in clear, standard terms. In the field, a harmonised checklist is used so that inspection data stay uniform and can be compared between sites. The lab method itself does not suit weathered modules well. It finds burn marks from hot spots, delamination, yellowed encapsulant, blistered backsheets, junction box failures and cracked cells. It also finds discoloured or burned cable connections and fuses in combiner boxes, and defective DC connectors and cables. It helps confirm bypass diode failure, cable and connector defects, and cell interconnection failure. For fungal soiling, a close look or a handheld microscope confirms biofilms; check several parts of the array, because the deposits can be patchy. Its limit is that many performance changes leave no visible trace and need more advanced tools. It is usually paired with infrared thermography, insulation-resistance testing or electroluminescence. Inspect connectors only after the circuit has been safely isolated. Treat burned or overheated parts as a fire and arcing hazard.

<!-- review notes
- sentence 7: support check: partial - Passages say many performance changes are invisible and need sophisticated tools, and pairing with IRT, EL and insulation-resistance testing appears in detection lists, but 'usually paired' is not stated explicitly.
- sentence 8: support check: partial - Inspection under safe isolation and arcing/fire hazards from connector defects are stated, but the passages don't explicitly say to treat burned or overheated parts as a fire and arcing hazard.
-->
