---
id: fm:module-clamping-defect
type: FailureMode
name: Bad Module Clamping
aliases:
- PVFS 3-1
- PVFS 3-1vs.01
category: Mounting
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:installation-error
  note: Installation is listed as an origin stage of bad clamping.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r4
    h: 1d9525d24c4f
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=48.r4
    h: b48fac8b08bc
  review: drafted
  review_note: 'support check: partial - Installation is listed as an origin stage, but the passages don''t
    name an installation error stressor as the cause.'
- claim_id: c2
  rel: caused_by
  target: stressor:manufacturing-defect
  note: Production is also listed as an origin stage.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r4
    h: 1d9525d24c4f
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=48.r4
    h: b48fac8b08bc
  review: drafted
  review_note: 'support check: partial - Production is listed as an origin stage, but no manufacturing
    defect cause is stated.'
- claim_id: c3
  rel: affects
  target: comp:module-frame
  note: The clamp can damage the module or its frame.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r1
    h: 442c2f7b2631
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=48.r1
    h: 442c2f7b2631
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:module-clamp
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r1
    h: 442c2f7b2631
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=48.r1
    h: 442c2f7b2631
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r8
    h: 6bc860aa6245
  review: drafted
  review_note: 'support check: partial - Clamp is involved as the cause of damage, and mitigation concerns
    clamps, but the clamp being affected is not clearly stated.'
- claim_id: c5
  rel: presents_as
  target: symptom:loose-module-fastening
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r1
    h: 442c2f7b2631
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=48.r1
    h: 442c2f7b2631
  review: drafted
- claim_id: c6
  rel: presents_as
  target: symptom:clamp-damage
  note: Damage to the module or frame caused by the clamp.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r1
    h: 442c2f7b2631
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=48.r1
    h: 442c2f7b2631
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r2
    h: 77db01806201
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=48.r2
    h: 77db01806201
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:module-replacement
  note: Corrective action for modules with a safety risk or severity 5.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r8
    h: 6bc860aa6245
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:compatible-clamps
  note: Clamps, modules and mounting structure must be compatible.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r8
    h: 6bc860aa6245
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:proper-installation
  note: Follow the manufacturer mounting instructions.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r8
    h: 6bc860aa6245
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:site-load-check
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r8
    h: 6bc860aa6245
  review: drafted
- claim_id: c12
  rel: mitigated_by
  target: mit:mounting-configuration-testing
  note: 'Optional: accredited lab testing of non-standard mounting such as facade mounting.'
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r8
    h: 6bc860aa6245
  review: drafted
- claim_id: c13
  rel: mitigated_by
  target: mit:regular-inspections
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=30.r8
    h: 6bc860aa6245
  review: drafted
---
Bad module clamping means a module is not fastened well enough, or the clamp has damaged the module or its frame. It can start during production or installation and shows up during operation. Visual inspection is the listed way to find it. Replace any module that poses a safety risk or has the highest severity rating. To prevent it, use only clamps that suit both the module and the mounting structure, follow the manufacturer's mounting instructions, and check the local wind and snow loads. For non-standard mounting, such as on a facade, have the setup tested by an accredited laboratory, and inspect the system regularly.
