---
id: symptom:el-nonuniform-pattern
type: Symptom
name: Non-uniform EL pattern
aliases:
- patchwork pattern
claims:
- claim_id: c1
  rel: observed_as
  target: meas:el-patchwork-pattern
  note: In crystalline silicon modules, EL images that grow less uniform over time (a patchwork pattern)
    can sometimes point to ongoing light-induced degradation (LID or LeTID).
  quote: Increasing non-uniformity of electroluminescence images (patchwork pattern) can in some cases
    highlight an ongoing degradation process.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:el-dark-cell-edges
  note: This points to PID rather than LID. Cells near the module frame or boundary appear dark, most
    clearly at low current bias (one tenth of rated current).
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.3.1
    h: 1f95caadc75d
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  review: drafted
  review_note: 'support check: partial - Passages say PID shows dark cells at module boundaries/near frame
    and is clearer at low bias (1/10 rated current), but do not compare it with LID or say such darkness
    ''points to PID rather than LID''.'
- claim_id: c3
  rel: observed_as
  target: meas:el-intensity-shift
  note: Modules with higher power loss tend to show a pixel-intensity histogram shifted toward lower EL
    intensity. This shift has not been clearly linked to any specific defect type.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.1.1
    h: 06ce46a9a853
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:el-dim-cell
  note: A single cell that is much dimmer than the others can come from a poor busbar connection. Bright
    and dark areas within a cell can come from uneven temperature during cell firing in production.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.3.1
    h: 1f95caadc75d
  review: drafted
- claim_id: c5
  attr: typical_power_loss
  value:
    min: 1
    max: 3
    unit: unit:PERCENT
  conditions: LID (boron-oxygen related) in p-type crystalline silicon modules, occurring within the first
    days of sun exposure
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c6
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: LeTID in susceptible modules (first seen with PERC) at module temperatures above 50 °C,
    building up over years and adding to the LID loss
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c7
  attr: typical_power_loss
  value:
    max: 30
    unit: unit:PERCENT
  conditions: Light-induced degradation (light soaking effect) in general, as reported by one source
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h3
    h: 950db263c013
  review: drafted
---
A non-uniform EL pattern is cell-to-cell or area-to-area variation in luminescence across a module, seen in electroluminescence images taken in the dark or at night while the module is forward-biased with a DC supply. In crystalline silicon modules, a patchwork pattern that grows over time can sometimes indicate ongoing light-induced degradation (LID or LeTID), even though LID itself leaves no visible defect. LID mainly shows as a drop in STC power, short-circuit current and open-circuit voltage early in the system's life, so confirm it with IV curves or flash tests rather than with EL alone. Potential-induced degradation can also look patchy, but its typical sign is dark cells near the module frame, clearest at low current bias, and it is worse in modules near one pole of the string. Bright and dark areas inside cells, or a single dim cell, can instead come from production problems such as uneven firing or a poor busbar connection. A single EL image taken at one bias current often cannot identify the cause, so take images at two bias currents and combine them with IR thermography or photoluminescence. In the field, use IR thermography first to find the anomalous modules, then do EL on site or in a lab, and send suspected underperformance to an accredited test laboratory for confirmation.

<!-- review notes
- sentence 1: support check: partial - Passages cover EL imaging with forward-bias DC supply in the dark or at night and variation across module surfaces, but never define a non-uniform EL pattern as cell-to-cell or area-to-area variation.
- sentence 3: support check: partial - Passages support the symptoms (drop in STC power, Isc, Voc) and verification with IV and flash testing, but do not say to use IV rather than EL alone; EL is even listed as a detection method.
- sentence 6: support check: partial - Passages say a single-bias EL image may not identify the cause and that two bias currents combined with IR thermography, photoluminescence or LBIC can help, but do not prescribe it as an instruction beyond that.
-->
