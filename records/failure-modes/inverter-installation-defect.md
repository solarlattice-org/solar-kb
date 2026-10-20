---
id: fm:inverter-installation-defect
type: FailureMode
name: Inverter Incorrect Installation
aliases:
- PVFS 4-2
- PVFS 4-2vs.01
category: Inverters
claims:
- claim_id: c1
  rel: affects
  target: comp:inverter
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=6.r29
    h: 3f8a36f3151e
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=7.r29
    h: 3f8a36f3151e
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h57
    h: 6ee6caf78272
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:installation-error
  note: Instruction manual not followed, e.g. placed near flammable materials such as wood, in direct
    sunlight, or without the required minimum distances to adjacent components.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h57
    h: 6ee6caf78272
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r1
    h: 8dae9fa5191e
  review: drafted
- claim_id: c3
  rel: leads_to
  target: fm:inverter-overheating
  note: Improper installation is listed as one origin of inverter temperature derating.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h57
    h: 6ee6caf78272
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r5
    h: 46c42be6ee70
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=33.r3
    h: e1cf6ecb59de
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=51.r3
    h: f67d18849d2b
  review: drafted
- claim_id: c4
  rel: presents_as
  target: symptom:loose-cable-connection
  note: Input cables that are not properly fixed can heat up at the loose contact, lowering performance
    or creating a fire risk.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h57
    h: 6ee6caf78272
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r1
    h: 8dae9fa5191e
  review: drafted
  review_note: 'support check: partial - Passages say unfixed input cables cause increased temperature
    at the loose contact, but don''t list loose cable connection as a presented symptom explicitly; it''s
    close though.'
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r2
    h: 5c5fd5f57aaf
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h57
    h: 6ee6caf78272
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:performance-monitoring
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r2
    h: 5c5fd5f57aaf
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h57
    h: 6ee6caf78272
  review: drafted
  review_note: 'support check: partial - Detection lists VI (MON), with MON implying monitoring, but performance
    monitoring is not explicitly stated.'
- claim_id: c7
  rel: mitigated_by
  target: mit:proper-installation
  note: 'Corrective action: dismount the inverter and reinstall it following the installation procedure.'
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r8
    h: 4199cee18f7d
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h57
    h: 6ee6caf78272
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c8
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r8
    h: 4199cee18f7d
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h57
    h: 6ee6caf78272
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:regular-inspections
  note: Regular inspection of the ventilation units.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r8
    h: 4199cee18f7d
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h57
    h: 6ee6caf78272
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:inverter-temperature-monitoring
  note: Listed as an optional preventive action.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r8
    h: 4199cee18f7d
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h57
    h: 6ee6caf78272
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:installation-clearance
  note: Leave gaps at the sides and top so the inverter can cool properly.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h57
    h: 6ee6caf78272
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r5
    h: 46c42be6ee70
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c12
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h57
    h: 6ee6caf78272
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r5
    h: 46c42be6ee70
  review: drafted
---
This failure is an inverter that was not installed according to the manufacturer's installation instructions. Common errors include placing the inverter near flammable, explosive, corrosive or humid sources or in direct sunlight, and not keeping the minimum distances at the bottom, top and sides. Input cables that are not properly fixed can run hot at the loose contact, which can lower performance or create a fire risk. Incorrect installation can cause the inverter to overheat, puts users at risk, and can lead to explosions if flammable vapours or gases are present. Look for the fault with a visual inspection and with monitoring data. To fix it, dismount the inverter and install it again following the installation procedure, keeping it accessible and secured to a suitable base. To prevent it, use adequate cooling, leave gaps at the sides and top, keep the inverter out of direct sunlight, inspect the ventilation units regularly, and consider monitoring inverter temperature.

<!-- review notes
- sentence 1: support check: partial - Passages say inverter must be installed according to the installation instruction, but don't say 'manufacturer's' explicitly.
- sentence 5: support check: partial - Detection is VI (MON), which suggests visual inspection and monitoring, but the abbreviation's meaning is not spelled out in the passages.
- sentence 6: support check: partial - Dismount and follow installation procedure is stated, and accessibility and secure base are stated as requirements, but not as part of the fix explicitly.
-->
