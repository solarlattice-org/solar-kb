---
id: fm:module-hotspot
type: FailureMode
name: Module Hotspot from Cell Damage
claims:
- claim_id: c1
  rel: caused_by
  target: fm:cell-cracks
  note: Cracked cells can cause current mismatch and reverse bias, so the cell dissipates power as heat.
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h4
    h: a46a7d318434
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c2
  rel: caused_by
  target: stressor:partial-shading
  note: Includes shadows from soiling.
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h4
    h: a46a7d318434
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:solder-bond-defect
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h4
    h: a46a7d318434
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:current-mismatch
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h4
    h: a46a7d318434
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:cell-reverse-bias
  note: Mismatch drives part of the module into reverse bias, where the underperforming cell heats up.
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h4
    h: a46a7d318434
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:solar-cell
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h4
    h: a46a7d318434
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c7
  rel: presents_as
  target: symptom:hotspot-ir-image
  note: Individual cells or substrings run locally hot while the module is under load.
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h4
    h: a46a7d318434
  review: drafted
  review_note: 'support check: partial - Localized high-temperature cells/substrings under load are stated,
    but IR imaging as the presentation is only implied by the drone IR detection method.'
- claim_id: c8
  rel: presents_as
  target: symptom:string-current-low
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=front
    h: 52a281766501
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h2
    h: f89fa075e5e7
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c9
  rel: detected_by
  target: method:ir-thermography
  note: Drone IR scan in clear, stable conditions with the inverter running and enough irradiance; compare
    against adjacent modules in the same string. Treat it as screening only.
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=front
    h: 52a281766501
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h2
    h: f89fa075e5e7
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h5
    h: dbed0f83b34d
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
  review_note: 'support check: partial - Drone IR scan conditions and neighbour comparison are stated,
    and the screening-only note appears in the notes, but the evidence cited for it is limited to u6 which
    is not listed here.'
- claim_id: c10
  rel: detected_by
  target: method:iv-curve-tracing
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=front
    h: 52a281766501
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h2
    h: f89fa075e5e7
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h5
    h: dbed0f83b34d
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c11
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=front
    h: 52a281766501
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h2
    h: f89fa075e5e7
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h5
    h: dbed0f83b34d
  review: drafted
- claim_id: c12
  rel: detected_by
  target: method:string-current-measurement
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h5
    h: dbed0f83b34d
  review: drafted
- claim_id: c13
  rel: mitigated_by
  target: mit:string-isolation
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=front
    h: 52a281766501
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h2
    h: f89fa075e5e7
  review: drafted
- claim_id: c14
  rel: mitigated_by
  target: mit:module-replacement
  note: Replace only once cell damage is confirmed and the electrical impact and repeatability have been
    checked.
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=front
    h: 52a281766501
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h2
    h: f89fa075e5e7
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h6
    h: 4629f9b5656e
  review: drafted
- claim_id: c15
  rel: mitigated_by
  target: mit:post-repair-verification
  note: Retest the string current after the repair.
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=front
    h: 52a281766501
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h2
    h: f89fa075e5e7
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c16
  rel: mitigated_by
  target: mit:bypass-diode-integration
  note: Caps the power the shaded cell dissipates but does not remove the effects of hot cells.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c17
  rel: mitigated_by
  target: mit:cell-current-binning
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c18
  rel: mitigated_by
  target: mit:cell-shunt-screening
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c19
  rel: mitigated_by
  target: mit:shade-resistant-modules
  note: For example half-cell, shingled, or per-cell diode modules; fewer cells per bypass diode also
    lowers hot cell temperature.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c20
  rel: leads_to
  target: fm:cell-interconnection-failure
  note: Includes solder joint failure if the cell temperature goes past the solder melting point.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c21
  rel: leads_to
  target: fm:cell-cracks
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c22
  rel: leads_to
  target: fm:glass-breakage
  note: Caused by a high temperature gradient, observed for example in non-tempered glass.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: fig=66
    h: fc43cc44285e
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
  review_note: 'support check: partial - Glass breakage risk from high cell temperatures and thin-film
    hot-spot glass breakage via temperature gradient in non-tempered glass are stated, but not specifically
    for this cause''s cell damage hot spot.'
- claim_id: c23
  rel: leads_to
  target: fm:delamination
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c24
  rel: leads_to
  target: fm:encapsulant-discoloration
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c25
  rel: leads_to
  target: fm:insulation-loss
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c26
  rel: leads_to
  target: fm:backsheet-deformation
  note: Reported for temperatures above 170°C.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c27
  rel: leads_to
  target: fm:junction-box-failure
  note: In extreme cases the junction box may detach.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c28
  rel: distinguished_from
  target: fm:hot-cell
  by: method:ir-thermography
  note: A hot spot is a localized heat point (local junction breakdown), mainly in multicrystalline cells.
    A hot cell heats evenly across the whole cell area, mainly in monocrystalline cells.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
  review_note: 'support check: partial - The hot spot versus hot cell distinction is stated, but using
    IR thermography to tell them apart is not stated.'
- claim_id: c29
  attr: temperature_rise
  value:
    max: 25
    unit: unit:DEG_C
  conditions: Hot cell in an IBC half-cell module relative to module temperature, indoor hot-spot test
    at 55°C module temperature per IEC 61215-2:2021
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
---
A module hotspot is a cell or substring that runs much hotter than the rest of the module while it is producing power. Common causes are cracked cells, solder bond defects, shadows from soiling, bypass diode behavior, or mismatch that pushes part of the module into reverse bias. It can reduce string output, and the risk grows if cracked cells or bypass diodes are left in service. Find it with a drone infrared scan in clear, stable conditions with the inverter running, comparing the module with its neighbours in the same string. Treat one thermal image as a screening result only, then confirm with string current, IV curve shape and a visual check before approving replacement. Raise the priority if the anomaly repeats across inspections or several modules in the same string show similar signatures. Isolate the string, check the heat signature under load, replace the module if cell damage is confirmed, and retest string current afterwards. If left in place, severe heating can lead to discoloration, delamination, interconnection and solder failures, backsheet damage and broken glass.
