---
id: meas:el-patchwork-pattern
type: Measurement
name: Patchwork EL pattern
aliases:
- non-uniformity of electroluminescence images
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 1
    max: 3
    unit: unit:PERCENT
  conditions: Light induced degradation (LID) in crystalline silicon modules, within the first days of
    sun exposure
  note: Loss belongs to LID, the failure mode that can show up as a patchwork EL pattern.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
  review_note: 'support check: partial - LID is stated as limited to 1-3% within the first days of sun
    exposure, but the passages only say patchwork EL can in some cases highlight ongoing degradation,
    not that this loss is typical for a patchwork pattern.'
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: LeTID in crystalline silicon modules at elevated temperatures above 50 °C, over years; adds
    to the LID loss
  note: Loss belongs to LeTID, a light induced degradation effect that can show up as a patchwork EL pattern.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
  review_note: 'support check: partial - LeTID up to 10%, above 50 °C, over years, summing with LID is
    stated, but linking it as typical loss of a patchwork EL pattern is only loosely implied (patchwork
    may highlight degradation generally).'
---
A patchwork EL pattern is an electroluminescence image of a module that looks more and more uneven, with cells or areas of different brightness and no clear crack-type signature. In some cases it shows that light induced degradation (LID or LeTID) is going on in crystalline silicon modules. That degradation shows up mainly as a drop in STC output power, and also as lower short-circuit current and open-circuit voltage early in the system's life, with no visible defect. IV measurement is the main way to detect it, and EL and IR imaging give supporting evidence. EL images are taken with the module in forward bias from a DC power supply that can drive the module's short-circuit current, in a dark setting or at sunset or night in the field. One EL image at a single bias current and temperature often cannot pin down the physical cause, so images at two bias currents or other methods such as thermography or photoluminescence help. Modules with higher power losses generally have an EL intensity distribution shifted toward lower intensities, but no clear link to specific defect types has been found yet.

<!-- review notes
- sentence 1: support check: partial - The passages say increasing non-uniformity of EL images is called a patchwork pattern, but nothing about cells or areas of different brightness or the absence of a crack-type signature (cracks are said to have recognizable signature elsewhere).
- sentence 4: support check: partial - Detection lists IV with EL and IRT in parentheses, which implies IV primary and EL/IRT secondary, but the passages do not explicitly say IV is the main method or that EL/IR give supporting evidence.
-->
