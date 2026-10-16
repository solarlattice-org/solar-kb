---
id: fm:cell-interconnection-failure
type: FailureMode
name: Cell Interconnection Failure
claims:
- claim_id: c1
  rel: affects
  target: comp:cell-interconnect-ribbon
  note: Covers both the busbars and the string interconnect ribbons; the busbar to string ribbon joint
    is the most fatigue-prone.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h4
    h: 3710145a6f87
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:bypass-diode
  note: When interconnects fully block current, the bypass diode conducts continuously and ages early.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h7
    h: 14013caaf10f
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h5
    h: 5f9cbfc08864
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:solder-bond-defect
  note: Poor soldering during manufacturing; it also raises power dissipation and causes local heating.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h4
    h: 3710145a6f87
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:manufacturing-defect
  note: Misplaced ribbons, an over-deformed ribbon kink, too little spacing between cells, and the lamination
    process.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h4
    h: 3710145a6f87
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:transport-damage
  note: Mechanical stress during transportation.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h4
    h: 3710145a6f87
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c6
  rel: caused_by
  target: stressor:thermal-cycling
  note: Thermomechanical stress in operation fatigues the interconnections.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h4
    h: 3710145a6f87
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:wind-load
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h4
    h: 3710145a6f87
  review: drafted
- claim_id: c8
  rel: caused_by
  target: stressor:hail
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h4
    h: 3710145a6f87
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c9
  rel: caused_by
  target: fm:severe-metallization-corrosion
  note: Corrosion of the cell metallization fatigues the interconnects; it often shows as light yellow
    to dark discoloration of the electrical parts.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h7
    h: 14013caaf10f
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h4
    h: 3710145a6f87
  review: drafted
- claim_id: c10
  rel: caused_by
  target: stressor:moisture-exposure
  note: A defective or detached junction box can let humidity in, which increases corrosion and weakens
    the interconnects.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h7
    h: 14013caaf10f
  review: drafted
- claim_id: c11
  rel: caused_by
  target: stressor:partial-shading
  note: Hotspots from partial shading add thermomechanical stress and fatigue to the interconnects.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h7
    h: 14013caaf10f
  review: drafted
- claim_id: c12
  rel: presents_as
  target: symptom:hotspot-ir-image
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: drafted
- claim_id: c13
  rel: presents_as
  target: symptom:el-dark-regions
  note: The darker regions appear at the failed interconnects.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c14
  rel: presents_as
  target: symptom:series-resistance-increase
  note: 'Stage 1: only a few interconnects are disconnected.'
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h5
    h: 5f9cbfc08864
  review: drafted
- claim_id: c15
  rel: presents_as
  target: symptom:fill-factor-reduction
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h5
    h: 5f9cbfc08864
  review: drafted
- claim_id: c16
  rel: presents_as
  target: symptom:iv-curve-distortion
  note: The knee of the IV curve becomes more rounded.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: drafted
- claim_id: c17
  rel: presents_as
  target: symptom:substring-loss
  note: Once failures block current, the bypass diode activates and the cell string is bypassed.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h5
    h: 5f9cbfc08864
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c18
  rel: presents_as
  target: symptom:burn-marks
  note: Appears in advanced stages.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h7
    h: 14013caaf10f
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h5
    h: 5f9cbfc08864
  review: drafted
- claim_id: c19
  rel: leads_to
  target: fm:glass-breakage
  note: Appears in advanced stages.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h7
    h: 14013caaf10f
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h5
    h: 5f9cbfc08864
  review: drafted
- claim_id: c20
  rel: leads_to
  target: fm:bypass-diode-failure
  note: Continuous bypass operation ages the diode early. An open-circuited diode then forces current
    through the failed string.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h7
    h: 14013caaf10f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c21
  rel: leads_to
  target: fm:arc-fault
  note: Arcing can occur if the bypass diode does not work correctly; fire is possible.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h7
    h: 14013caaf10f
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h5
    h: 5f9cbfc08864
  review: drafted
- claim_id: c22
  rel: detected_by
  target: method:el-imaging
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h2
    h: cc879c2d8fb5
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=33.r2
    h: dad17d1f52d0
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c23
  rel: detected_by
  target: method:ir-thermography
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h2
    h: cc879c2d8fb5
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=33.r2
    h: dad17d1f52d0
  review: drafted
- claim_id: c24
  rel: detected_by
  target: method:iv-curve-tracing
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h2
    h: cc879c2d8fb5
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: drafted
- claim_id: c25
  rel: detected_by
  target: method:visual-inspection
  note: Hard to see with the naked eye; visible mainly through burn marks or glass breakage in advanced
    stages.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h2
    h: cc879c2d8fb5
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=33.r2
    h: dad17d1f52d0
  review: drafted
- claim_id: c26
  rel: detected_by
  target: method:uv-fluorescence
  note: UV imaging can detect ribbon breakages.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: drafted
- claim_id: c27
  rel: detected_by
  target: method:signal-transmission
  note: A low-cost method.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=33.r2
    h: dad17d1f52d0
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c28
  rel: mitigated_by
  target: mit:module-replacement
  note: Advised when the failure is electrically active, in advanced stages, or when burn marks are visible.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h2
    h: cc879c2d8fb5
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: drafted
- claim_id: c29
  rel: mitigated_by
  target: mit:close-monitoring
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c30
  rel: mitigated_by
  target: mit:mechanical-stress-reduction
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h2
    h: cc879c2d8fb5
  review: drafted
- claim_id: c31
  rel: mitigated_by
  target: mit:thermal-stress-reduction
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h2
    h: cc879c2d8fb5
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c32
  attr: typical_power_loss
  value:
    nominal: 0.1
    unit: unit:PERCENT
  conditions: Per interconnection cut in cells with 4 busbars (Colvin et al.); series resistance rises
    by about 1%
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h5
    h: 5f9cbfc08864
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c33 (same source; check the conditions)
- claim_id: c33
  attr: typical_power_loss
  value:
    nominal: 1
    unit: unit:PERCENT
  conditions: Per interconnection cut in cells with 3 busbars, which have less redundancy (Annigoni et
    al.)
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h5
    h: 5f9cbfc08864
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c32 (same source; check the conditions)
---
Cell interconnection failure is a broken or high-resistance joint in the busbars or string ribbons that link the cells in a module. It usually starts with poor soldering or other manufacturing faults, or with transport stress, and gets worse with thermal stress, wind load, hail and corrosion. In early stages series resistance goes up, so fill factor drops and the IV curve knee becomes rounder. When the current is fully blocked, the bypass diode takes over the cell string. You can rarely see it with the naked eye. Use IR thermography to find hotspots, EL imaging to find dark areas at the failed joints, and IV curves to find the loss. Advanced stages can cause burn marks, glass breakage, early bypass diode failure, electric arcs and even fire. Monitor affected modules closely. Replace a module when the failure is electrically active or burn marks are visible.

<!-- review notes
- sentence 1: support check: partial - Busbars and string ribbons are described, and broken or resistive interconnections are mentioned, but no explicit definition as a broken/high-resistance joint.
-->
