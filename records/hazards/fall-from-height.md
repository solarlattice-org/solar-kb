---
id: hazard:fall-from-height
type: Hazard
name: Fall from height
aliases:
- roof fall
- fall hazard
- working at height
- falls from roofs
category: Mechanical
claims:
- claim_id: c1
  rel: controlled_by
  target: tool:fall-protection
  note: Fall protection is needed for work at elevated heights; the NABCEP guide calls it a primary safety
    concern for PV installers.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h160
    h: 181de92aa5a0
  - src: src:trn-oandm-femp-om-for-small-pv-systems
    loc: sec=h22
    h: 4b6ac616c69a
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: fig=133
    h: 710d823abf9d
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: tool:personal-fall-arrest-system
  note: Made up of a full-body harness, a shock-absorbing lanyard attached to the rear D-ring, rope, rope
    grab and a roof anchorage.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h160
    h: 181de92aa5a0
  - src: src:trn-oandm-femp-om-for-small-pv-systems
    loc: sec=h22
    h: 4b6ac616c69a
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: sec=h9
    h: 505f91f04c1e
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: tbl=8.r11
    h: af05f74620cf
  review: drafted
- claim_id: c3
  rel: controlled_by
  target: mit:guardrail-system
  note: Guardrails, barriers or parapet walls around roof edges and openings.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h160
    h: 181de92aa5a0
  - src: src:trn-oandm-femp-om-for-small-pv-systems
    loc: sec=h22
    h: 4b6ac616c69a
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: sec=h9
    h: 505f91f04c1e
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: tbl=8.r11
    h: af05f74620cf
  review: drafted
- claim_id: c4
  rel: controlled_by
  target: mit:roof-opening-covers
  note: Skylights and other roof holes have to be guarded or covered. Skylight glazing usually cannot
    hold a worker's weight. Roof windows and smoke/heat vents near PV must be breakthrough-proof or clearly
    marked and kept a safe distance away.
  cite:
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: tbl=2
    h: 7bddbb19b9fe
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: sec=h9
    h: 505f91f04c1e
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h80
    h: 137eb941add2
  review: drafted
- claim_id: c5
  rel: controlled_by
  target: mit:safety-nets
  cite:
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: sec=h9
    h: 505f91f04c1e
  review: drafted
- claim_id: c6
  rel: controlled_by
  target: mit:safety-monitor
  note: Protects workers between the warning line and the roof edge.
  cite:
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: tbl=8.r11
    h: af05f74620cf
  review: drafted
- claim_id: c7
  rel: controlled_by
  target: mit:ladder-securing
  cite:
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: sec=h9
    h: 505f91f04c1e
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: sec=h5
    h: 8d04810b75b3
  review: drafted
  review_note: 'support check: partial - Securing of ladders is named as an essential element reducing
    fall exposures, though the link is only loosely stated.'
- claim_id: c8
  rel: controlled_by
  target: mit:roof-structural-check
  note: Confirm the roof deck can carry workers, materials and equipment. A roof that held the PV equipment
    but not the extra weight of O&M staff has collapsed with loss of life.
  cite:
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: tbl=8.r11
    h: af05f74620cf
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h80
    h: 137eb941add2
  review: drafted
- claim_id: c9
  rel: controlled_by
  target: proc:job-hazard-analysis
  cite:
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: sec=h9
    h: 505f91f04c1e
  review: drafted
- claim_id: c10
  rel: controlled_by
  target: proc:fall-rescue
  note: Call 911, keep rescuers tied off, relieve suspension trauma, do not cut the fallen worker's lanyards
    or harness, and take impact-loaded fall arrest gear out of service.
  cite:
  - src: src:ref-standards-osha-fy12-sh-23536-12-studentreferencematerials
    loc: sec=h49
    h: 97ec155cf784
  review: drafted
---
Workers on rooftop and building-mounted PV systems can fall from roof edges, through roof openings, or from the structure the array is mounted on. High elevations, unprotected edges and steep slopes create the risk, and wind, wet surfaces, ladder misuse and unsafe behavior make it worse. Skylights, roof windows and smoke vents are a hidden danger because their glazing usually cannot hold a worker. Guard or cover them, or keep them clearly marked and well away from the PV equipment. A roof can also collapse if it can carry the PV equipment but not the added weight of maintenance staff, so check the roof structure before work starts. US construction rules require fall protection whenever a worker is 6 feet or more above a lower level. The main controls are guardrails or parapets at edges and a personal fall arrest system: a full-body harness, a shock-absorbing lanyard on the rear D-ring, and a roof anchorage. Safety nets, covers and safety monitors are also used. Most fatal falls happen when no fall protection is in place. Training, a job hazard analysis and a practiced rescue plan are therefore essential, and the rescue plan must include steps to relieve suspension trauma.

<!-- review notes
- sentence 7: support check: partial - The ~90% of fatal falls with no protection, training, JHA, and the practiced rescue with suspension trauma are stated, but 'therefore essential' and 'must include' are the KB's inference.
-->
