---
id: fm:junction-box-failure
type: FailureMode
name: Junction Box Failure
aliases:
- stressor:junction-box-corrosion
category: Modules
claims:
- claim_id: c1
  rel: affects
  target: comp:junction-box
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.3
    h: fe63e32ab7ec
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c2
  rel: affects
  target: comp:bypass-diode
  note: The junction box houses the bypass diodes; its failure can damage them.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h2
    h: 631415923f8a
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.3
    h: fe63e32ab7ec
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:moisture-exposure
  note: Water ingress, e.g. through a box with inadequate IP rating, corrodes connections and string interconnects.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.3
    h: fe63e32ab7ec
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r3
    h: b816426a98a2
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: caused_by
  target: stressor:manufacturing-defect
  note: Poor manufacturing leaves boxes opened or badly closed.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.3
    h: fe63e32ab7ec
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r3
    h: b816426a98a2
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:solder-bond-defect
  note: Cold or bad solder joints from low soldering temperature or chemical residues; contamination from
    lamination material is a concern in half-cell modules.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.3
    h: fe63e32ab7ec
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:low-quality-material
  note: Low-quality adhesive (e.g. early acrylic or PE foam tapes) causes the box to detach from the backsheet.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r3
    h: b816426a98a2
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:installation-error
  note: 'Examples: pulling modules up by their cables, unfixed cables, or cabling that is too short.'
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r3
    h: b816426a98a2
  review: drafted
- claim_id: c8
  rel: caused_by
  target: stressor:mechanical-stress
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r3
    h: b816426a98a2
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c9
  rel: caused_by
  target: stressor:thermal-cycling
  note: Daily and seasonal cycles loosen mechanical contacts.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  review: drafted
- claim_id: c10
  rel: caused_by
  target: stressor:high-temperature
  note: Heat-driven air pressure can open boxes that have no exhaust path; hot climates may speed up failures.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r3
    h: b816426a98a2
  review: drafted
- claim_id: c11
  rel: caused_by
  target: stressor:electrical-overstress
  note: Chang et al. name energy over stress as the main root cause.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c12
  rel: caused_by
  target: fm:delamination
  note: Delamination near the box can let water in and loosen the box.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r3
    h: b816426a98a2
  review: drafted
- claim_id: c13
  rel: caused_by
  target: fm:bypass-diode-failure
  note: Heat from a failed diode can deform or burn the box.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  review: drafted
- claim_id: c14
  rel: caused_by
  target: stressor:mounting-structure-defect
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  review: drafted
- claim_id: c15
  rel: presents_as
  target: symptom:burnt-junction-box
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: fig=2
    h: c93b4815ec6c
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c16
  rel: presents_as
  target: symptom:cracked-housing
  note: The lid may look weathered, brittle, cracked or warped.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  review: drafted
- claim_id: c17
  rel: presents_as
  target: symptom:detached-junction-box
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.3
    h: fe63e32ab7ec
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r3
    h: b816426a98a2
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c18
  rel: presents_as
  target: symptom:damaged-seal
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  review: drafted
- claim_id: c19
  rel: presents_as
  target: symptom:contact-corrosion
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.3
    h: fe63e32ab7ec
  review: drafted
- claim_id: c20
  rel: presents_as
  target: symptom:hotspot-ir-image
  note: Higher resistance from bad contacts or corrosion heats the box.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:pv-root-cause-junction-box-failure
    loc: fig=7
    h: eb7dd22abf25
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c21
  rel: presents_as
  target: symptom:burn-marks
  note: Burn marks or discolored cells may appear above the hotter box.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c22
  rel: presents_as
  target: symptom:substring-loss
  note: Open-circuit substrings result from cold solder joints in the box.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c23
  rel: presents_as
  target: symptom:open-circuit
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  review: drafted
- claim_id: c24
  rel: leads_to
  target: fm:arc-fault
  note: Internal arcing can start a fire.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h2
    h: 631415923f8a
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.3
    h: fe63e32ab7ec
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: drafted
- claim_id: c25
  rel: leads_to
  target: fm:cell-interconnection-failure
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c26
  rel: leads_to
  target: fm:insulation-loss
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  review: drafted
- claim_id: c27
  rel: leads_to
  target: fm:bypass-diode-failure
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h2
    h: 631415923f8a
  review: drafted
- claim_id: c28
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h2
    h: 631415923f8a
  review: drafted
- claim_id: c29
  rel: detected_by
  target: method:ir-thermography
  note: Finds open-circuit substrings and hot boxes, but cannot detect a disconnected bypass diode path
    unless the module is shaded.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h2
    h: 631415923f8a
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: drafted
- claim_id: c30
  rel: detected_by
  target: method:performance-monitoring
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: drafted
- claim_id: c31
  rel: detected_by
  target: method:iv-curve-tracing
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h2
    h: 631415923f8a
  review: drafted
- claim_id: c32
  rel: detected_by
  target: method:voc-measurement
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: drafted
- claim_id: c33
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h2
    h: 631415923f8a
  review: drafted
- claim_id: c34
  rel: detected_by
  target: method:string-reverse-bias-test
  note: At night, apply 3% to 5% of rated Isc in reverse to each string. Unusually high reverse voltage
    marks the string, and night IR then finds the module.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c35
  rel: distinguished_from
  target: fm:bypass-diode-failure
  by: method:destructive-analysis
  note: A failing bypass diode looks the same as a disconnected diode path (mode A). Only a destructive
    analysis of the box can tell them apart.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c36
  rel: mitigated_by
  target: mit:module-replacement
  note: Repairing junction boxes can easily cause new fires.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h2
    h: 631415923f8a
  review: drafted
- claim_id: c37
  rel: mitigated_by
  target: mit:string-isolation
  note: Make safety isolation the priority when there is evidence of arcing or burning.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h2
    h: 631415923f8a
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c38
  rel: mitigated_by
  target: mit:proper-installation
  note: Use qualified installers, check string polarity, and avoid unauthorized rework of cables and connectors.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c39
  rel: mitigated_by
  target: mit:surge-protection
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: drafted
- claim_id: c40
  rel: mitigated_by
  target: mit:junction-box-sealing
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h2
    h: 631415923f8a
  review: drafted
- claim_id: c41
  rel: mitigated_by
  target: mit:automated-visual-inspection
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: drafted
- claim_id: c42
  rel: mitigated_by
  target: mit:reverse-voltage-sweep
  note: Used in production and per string; it reveals unconnected diodes and high contact resistance.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: drafted
- claim_id: c43
  rel: mitigated_by
  target: mit:fleet-wide-testing
  note: Fire risk is high, so test all modules after a single failure.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c44
  attr: temperature_rise
  value:
    min: 5
    max: 10
    unit: unit:K
  conditions: Open-circuit substrings or module strings compared with active strings in IR thermography
    inspection
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: drafted
---
A junction box failure is a defect in the box on the back of the module that protects the string connections and holds the bypass diodes. It can interrupt the module circuit, damage the diodes and cause arcing or fire. Common causes are poor adhesion, boxes left open or badly closed, moisture ingress that corrodes contacts, cold solder joints, and installation errors that put mechanical stress on the box. In the field, look for a cracked, warped, melted, burnt or detached box, damaged seals, and burn marks above the box. An infrared camera shows a box running hotter than others or open-circuit substrings that are 5 to 10 K warmer than active strings. An infrared camera cannot see a disconnected bypass diode path unless the module is shaded. To find it, run a night reverse-bias test on each string, then use IR to locate the warm substring. IV curves, open-circuit voltage checks and insulation tests help confirm the damage. Isolate the circuit first if you see arcing or burning. Replace the module instead of repairing the box, because repairs can start new fires. Cold solder joints usually affect a whole production batch, so if one module fails, test every module from that batch.

<!-- review notes
- sentence 6: support check: partial - IV curve/Voc and insulation checks are mentioned for detection, but 'confirm the damage' framing is loose and Voc check is only for short-circuits.
- sentence 8: support check: partial - Cold solder joints being batch-wide and testing all modules after a single failure are stated, but 'every module from that batch' is slightly narrower than the 'all modules' wording.
-->
