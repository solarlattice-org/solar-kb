---
id: method:el-imaging
type: DetectionMethod
name: Electroluminescence imaging
aliases:
- EL
- EL imaging
claims:
- claim_id: c1
  rel: produces
  target: meas:el-crack-pattern
  note: Cracks show a signature pattern in EL that is easy to recognize.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.1.1
    h: 06ce46a9a853
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-19
- claim_id: c2
  rel: produces
  target: meas:el-intensity-shift
  note: Histograms of EL pixel intensity tend to move toward lower intensities in modules with higher
    power loss. No clear link to specific defect types has been established yet.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.1.1
    h: 06ce46a9a853
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
Electroluminescence imaging puts the module or string in forward bias with a DC power supply and photographs the light the cells give off using a CCD, CMOS or InGaAs camera. The power supply has to be able to drive the short-circuit current, which can take roughly the module's open-circuit voltage depending on the technology. Most EL systems only work at night or in low light, or with curtains blocking stray light. Daylight systems exist but need advanced equipment and image processing. Keep the camera as close as possible to the module and perpendicular to it. In the field, tripods fixed to the string frame help with this, while drones struggle with orthogonality, focus and vibration. EL shows cracks with an easily recognized pattern. Field studies also used it to find cell fracture, deficient solder joints, short-circuited cells and bypassed substrings. EL also reveals metallization corrosion and light induced degradation, and it was used to image disconnected cell interconnections. A single image taken at one bias current and temperature cannot always identify the physical cause. Combining two bias currents, or adding thermography or photoluminescence, helps explain what the image shows.

<!-- review notes
- sentence 2: support check: partial - The passage says the supply must be able to apply Isc and may need a voltage of about Voc depending on technology, but the statement muddles this by saying the short-circuit current takes the voltage.
-->
