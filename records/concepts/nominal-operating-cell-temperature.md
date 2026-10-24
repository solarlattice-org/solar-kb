---
id: concept:nominal-operating-cell-temperature
type: Concept
name: Nominal operating cell temperature
aliases:
- NOCT
- NMOT
category: Modules
concept_kind: physics
claims:
- claim_id: c1
  rel: related_to
  target: concept:standard-test-conditions
  note: Both are defined sets of irradiance, spectrum and temperature used to rate cells and modules;
    STC uses 1,000 W/m2 and 25 C cell temperature, NOCT uses 800 W/m2.
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: tbl=8
    h: 251e1e2ddbf1
  - src: src:se-academy-home-hub-technical-essentials-na-technical-16-home-hub-oversizing
    loc: sec=h16
    h: 94ccca027dd5
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:ptc-rating
  note: PTC parameters were derived from the Nominal Terrestrial Environment that defines NOCT; NTE specifies
    a lower irradiance (800 W/m2) than PTC (1000 W/m2).
  cite:
  - src: src:std-standards-standards-testing-performance-testing-astm-e2848-13
    loc: sec=6
    h: 3dd726e44aca
  - src: src:se-academy-home-hub-technical-essentials-na-technical-16-home-hub-oversizing
    loc: sec=h16
    h: 94ccca027dd5
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:air-mass
  note: NOCT conditions specify an Air Mass 1.5 G spectral distribution.
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: tbl=8.r1
    h: 080c0b2004f3
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: tbl=8
    h: 251e1e2ddbf1
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:temperature-coefficient
  note: Cell operating temperature, which NOCT characterizes, drives voltage and power changes through
    the module temperature coefficients.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h73
    h: 0b03943db93d
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=2.1.2
    h: 54888f628680
  review: drafted
  review_note: 'support check: partial - Passages say cell temperature affects voltage/power via temperature
    coefficients, but do not link NOCT itself to temperature coefficients.'
---
Nominal operating cell temperature (NOCT) is a defined set of irradiance and temperature conditions used to characterize solar cells, PV modules and PV inverters. One solution guide lists the NOCT conditions as 800 W/m2 irradiance, an Air Mass 1.5 G spectrum, 20 C, and a wind speed of 1 m/s, which give a nominal operating cell temperature of 45±2 C. These conditions are closer to real field operation than standard test conditions (STC). STC uses 1,000 W/m2 irradiance and a 25 C cell temperature. NOCT is listed with STC, PTC and normal operating conditions as one of the conditions used to rate modules. The PTC rating conditions were based on the Nominal Terrestrial Environment that defines NOCT. The difference is that the NOCT environment uses a lower irradiance of 800 W/m2. Cell temperature matters because hotter crystalline silicon cells give lower voltage and power and only slightly more current. Higher temperatures also reduce cell efficiency and lifetime. Temperature coefficients turn a difference in cell temperature into changes in a module's voltage, current and power output.

<!-- review notes
- sentence 2: support check: partial - Values match, but the passage lists 45±2 C as a separate item and cell temperature 20 C; 'give a nominal operating cell temperature' is a mild interpretation, and 'solution guide' source is not shown.
- sentence 3: support check: partial - STC values are stated, but the passages never say NOCT conditions are closer to real field operation than STC.
-->
