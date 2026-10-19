---
id: fm:backsheet-cracking
type: FailureMode
name: Backsheet Cracking
aliases:
- PVFS 1-5
category: Modules
claims:
- claim_id: c1
  rel: affects
  target: comp:backsheet
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r1
    h: 3f1be2072673
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r1
    h: a36a38e5f761
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h57
    h: 6959b882ad79
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:uv-exposure
  note: Weak UV stabilisation of the outer layer leads to photo-oxidation and surface microcracks (type
    I).
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.1
    h: 4dfb46bec383
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:thermal-cycling
  note: Thermal cycling drives microcracks to grow into macrocracks in polyamide backsheets.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h57
    h: 6959b882ad79
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:mechanical-stress
  note: Includes external loads and internal stress built in during lamination at busbar positions, plus
    thermal-expansion mismatch.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.3
    h: eb148eeff8d7
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:transport-damage
  note: Careless handling can leave local cuts and scratches.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:installation-error
  note: Careless handling during installation can leave cuts and scratches.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:low-quality-material
  note: For example, low UV resistance. The sources name this as a main cause of early failures.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  review: drafted
- claim_id: c8
  rel: caused_by
  target: stressor:material-incompatibility
  note: Backsheet and encapsulant that do not suit each other.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  review: drafted
- claim_id: c9
  rel: caused_by
  target: stressor:acetic-acid-release
  note: Acid from EVA attacks the backsheet's inner layer between cells and weakens it (squared cracks).
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.3
    h: eb148eeff8d7
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h57
    h: 6959b882ad79
  review: drafted
- claim_id: c10
  rel: caused_by
  target: stressor:humid-climate
  note: Hot, humid conditions make cracking and the damage that follows more frequent and more severe.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  review: drafted
  review_note: 'support check: partial - Passages say backsheet cracking followed by moisture ingress
    and corrosion is more frequent and severe in hot, humid conditions. They do not clearly say humidity
    causes the cracking itself.'
- claim_id: c11
  rel: caused_by
  target: fm:hot-cell
  note: Local overheating from hot cells breaks down the backsheet chemically, and it then cracks locally
    (type II).
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.2
    h: 5c74523d4701
  review: drafted
- claim_id: c12
  rel: caused_by
  target: fm:module-hotspot
  note: Hotspots or burn marks can split the backsheet or burst bubbles in it.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.2
    h: 5c74523d4701
  review: drafted
- claim_id: c13
  rel: caused_by
  target: fm:backsheet-chalking
  note: Chalking may come before cracking, but it is not a reliable predictor. Cracks also appear without
    chalking.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.1
    h: 4dfb46bec383
  review: drafted
  review_note: 'support check: partial - Chalking can be a precursor and cracks occur with and without
    chalking, but the passages treat chalking as a photo-oxidative co-symptom, not a cause.'
- claim_id: c14
  rel: presents_as
  target: symptom:backsheet-cracks
  note: Cracks, bursts or scratches. They can be local, run along busbars or between cells, or cover the
    whole surface.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r1
    h: 3f1be2072673
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r1
    h: a36a38e5f761
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.3
    h: eb148eeff8d7
  review: drafted
- claim_id: c15
  rel: presents_as
  target: symptom:ground-fault
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r5
    h: 585ab08017de
  review: drafted
  review_note: 'support check: partial - A broken backsheet can cause a potential ground fault, but the
    passages do not say it presents as an alarm or trip.'
- claim_id: c16
  rel: presents_as
  target: symptom:yellow-brown-discoloration
  note: Browning often accompanies cracks caused by overheating.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.2
    h: 5c74523d4701
  review: drafted
- claim_id: c17
  rel: presents_as
  target: symptom:backsheet-bubbles
  note: Burst bubbles or gas formation from local overheating.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r1
    h: 3f1be2072673
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r1
    h: a36a38e5f761
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.2
    h: 5c74523d4701
  review: drafted
- claim_id: c18
  rel: leads_to
  target: fm:insulation-loss
  note: Insulation resistance can collapse when the backsheet is cracked through, especially when wet.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.3
    h: eb148eeff8d7
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h57
    h: 6959b882ad79
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r5
    h: 585ab08017de
  review: drafted
- claim_id: c19
  rel: leads_to
  target: fm:delamination
  note: Moisture gets in through the cracks.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r5
    h: 585ab08017de
  review: drafted
- claim_id: c20
  rel: leads_to
  target: fm:severe-metallization-corrosion
  note: Deep cracks are often followed by moisture ingress and corrosion.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r5
    h: 585ab08017de
  review: drafted
- claim_id: c21
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r2
    h: 4b331eae91fd
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r2
    h: ba8af336477f
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=8
    h: 88163ae58405
  review: drafted
- claim_id: c22
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r2
    h: 4b331eae91fd
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r2
    h: ba8af336477f
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=8
    h: 88163ae58405
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r8
    h: b5b29b444147
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r8
    h: cf377b6ef813
  review: drafted
- claim_id: c23
  rel: detected_by
  target: method:wet-leakage-test
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r8
    h: b5b29b444147
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r8
    h: cf377b6ef813
  review: drafted
  review_note: 'support check: partial - Wet-leakage test is mentioned only as a criterion for module
    replacement, not explicitly as a detection method.'
- claim_id: c24
  rel: detected_by
  target: method:optical-profilometry
  note: A research method that used machine learning on surface scans. It found cracks before they could
    be seen.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h57
    h: 6959b882ad79
  review: drafted
- claim_id: c25
  rel: mitigated_by
  target: mit:module-replacement
  note: Replace modules with a direct safety risk or that fail insulation or wet-leakage tests. Squared
    cracks require replacing every module with the same BOM.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r8
    h: b5b29b444147
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r8
    h: cf377b6ef813
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.3
    h: eb148eeff8d7
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.2
    h: 5c74523d4701
  review: drafted
- claim_id: c26
  rel: mitigated_by
  target: mit:backsheet-repair-coating
  note: A suitable coating or film may repair longitudinal cracks. Squared cracks cannot be repaired.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.3
    h: eb148eeff8d7
  review: drafted
- claim_id: c27
  rel: mitigated_by
  target: mit:ground-fault-detection
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r8
    h: b5b29b444147
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r8
    h: cf377b6ef813
  review: drafted
- claim_id: c28
  rel: mitigated_by
  target: mit:certified-products
  note: Check that the IEC 61215 certification is valid.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r8
    h: b5b29b444147
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r8
    h: cf377b6ef813
  review: drafted
- claim_id: c29
  rel: mitigated_by
  target: mit:bom-verification
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r8
    h: b5b29b444147
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r8
    h: cf377b6ef813
  review: drafted
- claim_id: c30
  rel: mitigated_by
  target: mit:pre-installation-inspection
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r8
    h: b5b29b444147
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r8
    h: cf377b6ef813
  review: drafted
- claim_id: c31
  rel: mitigated_by
  target: mit:regular-inspections
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r8
    h: b5b29b444147
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r8
    h: cf377b6ef813
  review: drafted
- claim_id: c32
  rel: mitigated_by
  target: mit:arc-fault-circuit-interrupter
  note: Installing an arc detection tool is listed as an optional preventive action.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r8
    h: b5b29b444147
  review: drafted
- claim_id: c33
  rel: mitigated_by
  target: mit:accelerated-weathering-screening
  note: Weathering tests followed by wipe tests, run as a preventive screen.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.1
    h: 4dfb46bec383
  review: drafted
---
Backsheet cracking is any crack, burst or scratch in the module backsheet. It can affect only the surface or the whole layer stack. Causes include UV, thermal and mechanical stress, handling damage during transport or installation, poor-quality or mismatched materials, and local overheating from hot cells or hotspots. Cracks may be local, run along busbars or between cells, or cover the whole rear surface. Browning or bubbles may appear where a hot cell caused them. Deep cracks break the electrical insulation. This creates a safety hazard and possible ground faults, and it is worst in wet conditions. Over time, moisture that gets in through the cracks can cause corrosion and delamination, which lower power output. Confirm the failure with a visual inspection of the rear side, followed by insulation testing or wet-leakage testing. Replace modules that pose a direct safety risk or fail insulation or wet-leakage tests, and keep inspecting the modules that stay in service. To prevent it, keep ground fault detection running, check certification and the bill of materials, and inspect modules before installation.

<!-- review notes
- sentence 6: support check: partial - VI and (INS) are listed as detection methods, but the passages do not specify rear-side inspection, a sequence, or wet-leakage testing as detection.
-->
