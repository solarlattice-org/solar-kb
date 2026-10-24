---
id: concept:arc-flash-incident-energy
type: Concept
name: Arc flash incident energy
aliases:
- incident energy
- arc flash boundary
- cal/cm2
- PPE category
- IE
category: Safety
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: hazard:ac-arc-flash
  note: Incident energy calculations for AC arc flash are well established and backed by industry tests.
  cite:
  - src: src:trn-safety-epri-dc-arc-flash-on-photovoltaic-equipment
    loc: sec=h12
    h: 6e12ea069aee
  - src: src:trn-safety-epri-dc-arc-flash-on-photovoltaic-equipment
    loc: sec=h18
    h: ddfdc2bab6b6
  - src: src:ref-standards-nfpa-06165704-optimized-ioc-iasm-2012
    loc: sec=h5
    h: 086b216ff4ec
  review: drafted
- claim_id: c2
  rel: related_to
  target: hazard:dc-arc-flash
  note: For DC systems such as PV and battery storage, incident energy calculation methods are not backed
    by standardized methods or broad testing.
  cite:
  - src: src:trn-safety-epri-dc-arc-flash-on-photovoltaic-equipment
    loc: sec=h12
    h: 6e12ea069aee
  - src: src:trn-safety-epri-dc-arc-flash-on-photovoltaic-equipment
    loc: sec=h18
    h: ddfdc2bab6b6
  - src: src:trn-safety-epri-dc-arc-flash-on-photovoltaic-equipment
    loc: sec=h28
    h: 826e6b628063
  - src: src:eq-equip-bess-powin-powin-stack750-dc-arc-flash-study-rev-c
    loc: sec=4.4
    h: 2ab51dd1ee3f
  review: drafted
- claim_id: c3
  rel: related_to
  target: std:ieee-1584
  note: IEEE 1584 provides the main industry equations for AC incident energy and arc flash boundary calculations.
  cite:
  - src: src:trn-safety-epri-dc-arc-flash-on-photovoltaic-equipment
    loc: sec=h18
    h: ddfdc2bab6b6
  - src: src:ref-standards-nfpa-06165704-optimized-ioc-iasm-2012
    loc: sec=h5
    h: 086b216ff4ec
  - src: src:std-standards-nfpa-nfpa-70e-2018
    loc: tbl=12.r3
    h: 1e0de072cfdb
  - src: src:book-practical-solution-guide-to-arc-flash-hazards
    loc: sec=4.7
    h: 06bbb568a238
  review: drafted
- claim_id: c4
  rel: related_to
  target: tool:arc-rated-clothing
  note: Arc-rated clothing is selected according to the incident energy at the task working distance.
  cite:
  - src: src:std-standards-nfpa-nfpa-70e-2018
    loc: sec=h58
    h: 883631174feb
  - src: src:book-practical-solution-guide-to-arc-flash-hazards-2nd-ed
    loc: sec=h84
    h: 62413b97e6dc
  - src: src:book-practical-solution-guide-to-arc-flash-hazards-2nd-ed
    loc: tbl=15.r1
    h: 019ca35cfa11
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c5
  rel: related_to
  target: tool:personal-protective-equipment
  cite:
  - src: src:trn-safety-epri-dc-arc-flash-on-photovoltaic-equipment
    loc: sec=h18
    h: ddfdc2bab6b6
  - src: src:eq-equip-bess-powin-powin-stack750-dc-arc-flash-study-rev-c
    loc: sec=4.4
    h: 2ab51dd1ee3f
  review: drafted
- claim_id: c6
  rel: related_to
  target: proc:arc-flash-hazard-assessment
  cite:
  - src: src:std-standards-nfpa-nfpa-70e-2018
    loc: sec=h58
    h: 883631174feb
  - src: src:book-practical-solution-guide-to-arc-flash-hazards
    loc: sec=4.7
    h: 06bbb568a238
  - src: src:book-practical-solution-guide-to-arc-flash-hazards
    loc: sec=4.9
    h: f5108ad95cd4
  review: drafted
- claim_id: c7
  rel: related_to
  target: mit:arc-flash-labeling
  note: Labels carry available incident energy with working distance, or the PPE category, plus the arc
    flash boundary.
  cite:
  - src: src:std-standards-nfpa-nfpa-70e-2018
    loc: sec=h58
    h: 883631174feb
  - src: src:eq-equip-bess-powin-powin-stack750-dc-arc-flash-study-rev-c
    loc: sec=4.4
    h: 2ab51dd1ee3f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: related_to
  target: concept:overcurrent-protection
  note: The protective device clearing time at the arcing current largely determines incident energy.
  cite:
  - src: src:ref-standards-nfpa-06165704-optimized-ioc-iasm-2012
    loc: sec=h5
    h: 086b216ff4ec
  - src: src:std-standards-nfpa-nfpa-70e-2018
    loc: sec=h58
    h: 883631174feb
  review: drafted
- claim_id: c9
  rel: related_to
  target: prod:powin-stack750
  note: A DC arc flash study calculated worst-case incident energy for this battery system.
  cite:
  - src: src:eq-equip-bess-powin-powin-stack750-dc-arc-flash-study-rev-c
    loc: sec=4.4
    h: 2ab51dd1ee3f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
Incident energy is the heat energy a worker could receive at a given working distance from an arc flash, and it decides what level of PPE the worker must wear and how far the arc flash boundary sits. The clearing time of the upstream protective device is a key factor; clearing in the instantaneous range can keep incident energy below 8 cal/cm2 for many industrial conditions. Under NFPA 70E the arc flash boundary is the distance where incident energy falls to 1.2 cal/cm2, so higher incident energy pushes the boundary farther out. For DC equipment such as PV inverters and combiners, calculation methods have little test backing; EPRI field tests found that measured incident energy rose linearly with PV array size. In battery storage, a DC arc flash study found worst-case incident energy of 22.746 cal/cm2 at 18 inches on an unfused stack, which corresponds to PPE category 4. The equipment label shows the available incident energy or the PPE category, and the analysis must be reviewed at least every 5 years or whenever the system changes.

<!-- review notes
- sentence 1: support check: partial - IE dictating PPE level and boundary is stated, and working distance is mentioned, but the definition as heat energy a worker receives is not explicit, and boundary is defined by 1.2 cal/cm2 rather than directly decided.
- sentence 6: support check: partial - Label contents and the 5-year review and update on system changes are stated, but the review applies to incident energy analysis and label data, and the label option includes other items; 'at least every 5 years' is fine though the label may show other options.
-->
