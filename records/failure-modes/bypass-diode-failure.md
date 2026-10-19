---
id: fm:bypass-diode-failure
type: FailureMode
name: Bypass Diode Failure
category: Modules
claims:
- claim_id: c1
  rel: affects
  target: comp:bypass-diode
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r3
    h: 23c38e687c9d
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r1
    h: 61b4b102e2b3
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:junction-box
  note: Heat from a failed diode can deform or burn the junction box.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r6
    h: c1a079fd37d5
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:partial-shading
  note: Frequent shading makes the diodes conduct more often and run hotter, which shortens their life.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h5
    h: 23f6264b1f6b
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r3
    h: 23c38e687c9d
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:lightning-strike
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h5
    h: 23f6264b1f6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r3
    h: 23c38e687c9d
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r4
    h: 0da0e147b72b
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c5
  rel: caused_by
  target: stressor:electrostatic-discharge
  note: Schottky bypass diodes are very sensitive to static high-voltage discharge.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h5
    h: 23f6264b1f6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r3
    h: 23c38e687c9d
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r4
    h: 0da0e147b72b
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:thermal-runaway
  note: Happens when the diode cannot dissipate the heat produced as it switches between operating modes.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: fig=2
    h: 996b8f1459b3
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h5
    h: 23f6264b1f6b
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c7
  rel: caused_by
  target: stressor:high-temperature
  note: Failure rate rises with diode operating temperature. Failures are more common in hot climates.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h5
    h: 23f6264b1f6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r3
    h: 23c38e687c9d
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r4
    h: 0da0e147b72b
  review: drafted
- claim_id: c8
  rel: caused_by
  target: stressor:mechanical-stress
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h5
    h: 23f6264b1f6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r3
    h: 23c38e687c9d
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r4
    h: 0da0e147b72b
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c9
  rel: caused_by
  target: stressor:manufacturing-defect
  note: Examples are a wrong specification, a non-functional diode, or a diode that was reversed or wrongly
    connected during assembly.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h5
    h: 23f6264b1f6b
  review: drafted
- claim_id: c10
  rel: caused_by
  target: stressor:installation-error
  note: The diode may be mounted the wrong way round or not properly connected.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h5
    h: 23f6264b1f6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r3
    h: 23c38e687c9d
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r4
    h: 0da0e147b72b
  review: drafted
- claim_id: c11
  rel: caused_by
  target: stressor:undersized-component
  note: An undersized diode cannot withstand continuous current flow.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r3
    h: 23c38e687c9d
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r4
    h: 0da0e147b72b
  review: drafted
- claim_id: c12
  rel: caused_by
  target: fm:junction-box-failure
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h5
    h: 23f6264b1f6b
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  review: drafted
  note: Corrosion inside the junction box can weaken the diode.
  review_note: 'reviewer 2026-10-19: target stressor:junction-box-corrosion merged into fm:junction-box-failure;
    re-verify against the cited passages'
- claim_id: c13
  rel: caused_by
  target: stressor:component-aging
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h5
    h: 23f6264b1f6b
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  review: drafted
- claim_id: c14
  rel: presents_as
  target: symptom:low-module-voc
  note: Points to a short-circuited diode.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  review: drafted
- claim_id: c15
  rel: presents_as
  target: symptom:hotspot-ir-image
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  - src: src:pv-root-cause-bypass-diode-failure
    loc: fig=5
    h: 8611a9da348a
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r6
    h: c1a079fd37d5
  review: drafted
  review_note: 'support check: partial - Passages say IR thermography might reveal diode activations or
    hotspots, but not definitively that failure presents as an IR hotspot.'
- claim_id: c16
  rel: presents_as
  target: symptom:burn-marks
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r6
    h: c1a079fd37d5
  review: drafted
- claim_id: c17
  rel: presents_as
  target: symptom:burnt-junction-box
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r6
    h: c1a079fd37d5
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c18
  rel: presents_as
  target: symptom:substring-loss
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=front
    h: 44eaacc73841
  review: drafted
  review_note: 'support check: partial - Substring loss appears only in the overview impact-factor list,
    without further description.'
- claim_id: c19
  rel: presents_as
  target: symptom:mpp-shift
  note: A shorted diode can move the operating point of the other modules in the string or array.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r6
    h: c1a079fd37d5
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c20
  rel: presents_as
  target: symptom:uneven-cell-heating
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  review: drafted
- claim_id: c21
  rel: detected_by
  target: method:multimeter-diode-test
  note: Described as the best way to tell whether a diode is shorted or open.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  review: drafted
- claim_id: c22
  rel: detected_by
  target: method:iv-curve-tracing
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  review: drafted
- claim_id: c23
  rel: detected_by
  target: method:voc-measurement
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  review: drafted
- claim_id: c24
  rel: detected_by
  target: method:ir-thermography
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c25
  rel: detected_by
  target: method:visual-inspection
  note: Look for burn marks.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=front
    h: 44eaacc73841
  review: drafted
- claim_id: c26
  rel: detected_by
  target: method:junction-box-inspection
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=front
    h: 44eaacc73841
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c27
  rel: mitigated_by
  target: mit:module-replacement
  note: In practice, the whole module is usually replaced.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  review: drafted
- claim_id: c28
  rel: mitigated_by
  target: mit:diode-replacement
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c29
  rel: mitigated_by
  target: mit:avoid-partial-shading
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c30
  rel: mitigated_by
  target: mit:post-repair-verification
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=front
    h: 44eaacc73841
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c31
  rel: mitigated_by
  target: mit:close-monitoring
  note: For affected modules that are not replaced.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  review: drafted
- claim_id: c32
  rel: mitigated_by
  target: mit:bypass-diode-check
  note: Check that the diodes activate when hotspots or burn marks are found.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c33
  rel: leads_to
  target: fm:module-hotspot
  note: With an open diode and a mismatch, current is forced through the affected cell string, which heats
    it and drives the cells into reverse bias.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r6
    h: c1a079fd37d5
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
  review_note: 'support check: partial - Open diode with mismatch causing heat and hotspots is stated,
    but the detail of driving cells into reverse bias with current forced through the string is a mix
    across passages.'
- claim_id: c34
  rel: leads_to
  target: fm:junction-box-failure
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r6
    h: c1a079fd37d5
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c35
  rel: leads_to
  target: fm:arc-fault
  note: Open-circuit diodes can lead to arcing and, in some cases, fire.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h2
    h: 55310ab45bb9
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h3
    h: 3d9666cc0784
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c36
  rel: leads_to
  target: fm:leakage-current
  note: Follows when the junction box or backsheet has burnt through.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r6
    h: c1a079fd37d5
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c37
  attr: time_to_onset
  value:
    max: 10
    unit: unit:YR
  conditions: Bypass diode failures show up mainly within the first ten years after a PV installation.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h5
    h: 23f6264b1f6b
  review: drafted
  review_note: 'support check: partial - Passages say failures are primarily revealed during the first
    ten years, supporting roughly 10 years as an upper window, not a precise onset time.'
---
A bypass diode usually fails in one of two states: shorted or open. A shorted diode keeps the module voltage and output permanently low. It can also pull the other modules in the string away from their maximum power point. An open diode often shows no loss at all until the module is mismatched or shaded. Then cells can be driven into reverse bias, which causes hotspots, burn marks, arcing or fire. Common causes are lightning or static discharge, thermal runaway, undersized or reversed diodes, poor connections, mechanical stress, junction box corrosion and frequent partial shading. To find it, look for low open-circuit voltage or odd IV curves, scan with an IR camera, and check the junction box and module for burn marks. To confirm, test the diode directly with a multimeter in diode or resistance mode. Affected modules are usually replaced, although the diode itself can be replaced. Any module left in service should be watched closely, and the string should be checked after the repair. Reducing partial shading helps bypass diodes last longer.
