---
id: fm:backsheet-deformation
type: FailureMode
name: Backsheet bubbling and deformation
aliases:
- Backsheet delamination
- internal delamination
- Blisters
claims:
- claim_id: c1
  rel: affects
  target: comp:backsheet
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h26
    h: 2bddce4dac47
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:encapsulant
  note: Backsheet can separate from the encapsulant, sometimes exposing it.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h26
    h: 2bddce4dac47
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:backsheet-bubbles
  note: Backsheet looks wavy with local bumps, bubbles or ripples; in the worst case layers peel off.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h26
    h: 2bddce4dac47
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c4
  rel: caused_by
  target: stressor:thermal-cycling
  note: Thermo-mechanical stress from differing thermal expansion of the polymer layers.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:material-incompatibility
  note: Chemical reactions at interfaces or additive migration between encapsulant and backsheet films.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5
    h: cdcdc1167476
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:high-temperature
  note: Heat attack degrades interfacial bonding.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:uv-exposure
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c8
  rel: caused_by
  target: stressor:moisture-exposure
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c9
  rel: caused_by
  target: stressor:humid-climate
  note: More frequent and severe in hot and humid conditions.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c10
  rel: caused_by
  target: stressor:mechanical-stress
  note: External mechanical stress applied to the module.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c11
  rel: caused_by
  target: stressor:manufacturing-defect
  note: Insufficient lamination process, such as too short lamination times.
  quote: Delamination can be also caused by an insufficient lamination process e.g. too short lamination
    times.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c12
  rel: caused_by
  target: fm:module-hotspot
  note: Local overheating from hot cells or hot spots can cause gas formation in encapsulant and backsheet,
    and bubbles that may burst.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.2
    h: 5c74523d4701
  review: drafted
  review_note: 'support check: partial - Hot spots causing gas formation and bursted bubbles are stated,
    but in backsheet cracking context, not explicitly as cause of bubbling/deformation (delamination).'
- claim_id: c13
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=8
    h: 88163ae58405
  review: drafted
- claim_id: c14
  rel: detected_by
  target: method:insulation-resistance-test
  note: Listed as a secondary detection method (INS).
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=8
    h: 88163ae58405
  review: drafted
- claim_id: c15
  rel: detected_by
  target: method:wet-leakage-test
  note: Modules failing insulation or wet-leakage tests should be replaced.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
  review_note: 'support check: partial - Wet-leakage test appears only in the corrective action for failing
    modules, not as a listed detection method for this defect.'
- claim_id: c16
  rel: leads_to
  target: fm:insulation-loss
  note: Edge delamination can let rain or dew water in and create an electrical path to ground.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c17
  rel: leads_to
  target: fm:junction-box-failure
  note: Delamination near the junction box can loosen it and stress live components.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
  review_note: 'support check: partial - Delamination near the junction box can loosen it and stress live
    components with breakage danger, but ''junction box failure'' is only implied.'
- claim_id: c18
  rel: leads_to
  target: fm:arc-fault
  note: A break from a loosened junction box can disconnect a bypass diode and may cause an unmitigated
    arc.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c19
  rel: distinguished_from
  target: fm:backsheet-chalking
  by: method:tactile-inspection
  note: Chalking leaves a removable white powder felt by passing a finger over a dull surface; deformation
    shows as bubbles, ripples or peeling layers.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  review: drafted
  review_note: 'support check: partial - Chalking is described as removable powder felt by finger and
    deformation as bubbles/ripples, but no passage presents tactile inspection as a way to distinguish
    them.'
- claim_id: c20
  rel: mitigated_by
  target: mit:module-replacement
  note: Replace modules with a direct safety risk or highest severity.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c21
  rel: mitigated_by
  target: mit:close-monitoring
  note: Regular inspections of modules not replaced.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c22
  rel: mitigated_by
  target: mit:bom-verification
  note: Check IEC 61215 certification validity and BOM.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c23
  rel: mitigated_by
  target: mit:ground-fault-detection
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h25
    h: bb6b0316efb1
  review: drafted
- claim_id: c24
  rel: mitigated_by
  target: mit:material-compatibility-testing
  note: Select appropriate encapsulant and backsheet materials and test their compatibility.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5
    h: cdcdc1167476
  review: drafted
---
Backsheet bubbling and deformation happens when the polymer backsheet separates from the encapsulant, or when its layers separate from each other, leaving an air gap. From the rear the backsheet looks wavy, with local bumps, bubbles or ripples, and in bad cases one or more layers peel off. Common drivers are thermo-mechanical stress, incompatible materials, heat, UV and moisture, external mechanical stress, and poor lamination; hot spots can also cause gas bubbles. Confirm it by visual inspection of the rear side, with insulation testing when safety is in doubt. A bubble in the open centre of the back is a minor issue, but delamination at the module edge or near the junction box is a serious safety risk because of water ingress, ground faults and possible arcing. Replace modules that pose a direct safety risk or that fail insulation or wet-leakage tests, and keep inspecting the remaining ones. Ground fault detection should always be active, and certification and bill of materials should be checked to prevent this failure.

<!-- review notes
- sentence 2: support check: partial - Wavy, bumps, bubbles, ripples and peeling layers are stated, but 'from the rear' is only implied by backsheet location.
- sentence 3: support check: partial - Drivers are listed, but hot spots are linked to gas formation and cracking, not clearly to gas bubbles in this failure.
- sentence 4: support check: partial - VI and INS are listed as detection, but 'visual inspection of rear side' and insulation testing 'when safety is in doubt' are not stated.
-->
