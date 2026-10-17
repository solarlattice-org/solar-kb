---
id: fm:glass-breakage
type: FailureMode
name: Glass Breakage
category: Modules
claims:
- claim_id: c1
  rel: affects
  target: comp:module-glass
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r1
    h: 9a033fb55157
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.1.1
    h: 767c056a514a
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:solar-cell
  note: Shattering of tempered glass usually breaks the cells as well.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r5
    h: 21e9fd14fbde
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:cell-interconnect-ribbon
  note: Moisture entering through broken glass speeds up corrosion of cell interconnections.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h5
    h: 086a578b6c8a
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:manufacturing-defect
  note: Incorrect lamination raises mechanical stress on module materials.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  - src: src:pv-root-cause-glass-breakage
    loc: fig=3
    h: 87440da9cb8a
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c5
  rel: caused_by
  target: stressor:installation-error
  note: Improper clamping of frameless modules, overtightened screws and poor clamp design.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  - src: src:pv-root-cause-glass-breakage
    loc: fig=4
    h: 0692124bccf0
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c6
  rel: caused_by
  target: stressor:transport-damage
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:mechanical-stress
  note: Excessive stress during installation or extreme stress on the module frame.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.1.1
    h: 767c056a514a
  review: drafted
- claim_id: c8
  rel: caused_by
  target: stressor:hail
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.1.1
    h: 767c056a514a
  - src: src:pv-root-cause-glass-breakage
    loc: sec=front
    h: fbd89f70605e
  review: drafted
- claim_id: c9
  rel: caused_by
  target: stressor:object-impact
  note: Stones, other objects, and pebbles thrown up during grass cutting.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  review: drafted
- claim_id: c10
  rel: caused_by
  target: stressor:vandalism
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  review: drafted
- claim_id: c11
  rel: caused_by
  target: stressor:animal-activity
  note: For example, goats climbing on modules or birds dropping objects.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  review: drafted
- claim_id: c12
  rel: caused_by
  target: stressor:snow-load
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  review: drafted
- claim_id: c13
  rel: caused_by
  target: stressor:high-wind
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  review: drafted
- claim_id: c14
  rel: caused_by
  target: stressor:sand-abrasion
  note: Sandstorms can abrade and weaken the front glass in arid climates.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  review: drafted
  review_note: 'support check: partial - Sandstorm abrasion weakening the glass is stated, but the passage
    ties arid climates generally, which is fine; however it says weakening rather than directly causing
    breakage.'
- claim_id: c15
  rel: caused_by
  target: stressor:high-temperature
  note: Burn marks and hotspots create temperature gradients in the glass, and non-tempered glass is most
    at risk.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  - src: src:pv-root-cause-glass-breakage
    loc: fig=6
    h: 6c6b569f5cdd
  review: drafted
- claim_id: c16
  rel: caused_by
  target: fm:cell-interconnection-failure
  note: Hotspots and burn marks from interconnection defects cause local thermal stress.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h6
    h: da22d4046811
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  review: drafted
- claim_id: c17
  rel: caused_by
  target: fm:junction-box-failure
  note: Resistive heating in a failing junction box adds to the risk.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h6
    h: da22d4046811
  review: drafted
- claim_id: c18
  rel: caused_by
  target: stressor:mounting-structure-defect
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h4
    h: 82763b8d0653
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h6
    h: da22d4046811
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c19
  rel: presents_as
  target: symptom:cracked-glass
  note: Tempered or heat-treated float glass shatters into small pieces, while annealed glass breaks into
    large pieces.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r1
    h: 9a033fb55157
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c20
  rel: presents_as
  target: symptom:hotspot-ir-image
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h7
    h: 9a7ad0612a0a
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r5
    h: 21e9fd14fbde
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.1.1
    h: 767c056a514a
  review: drafted
  review_note: 'support check: partial - Glass breakage causes hot spots and IR detects temperature anomalies,
    but an IR image hotspot symptom is not explicitly stated.'
- claim_id: c21
  rel: presents_as
  target: symptom:ground-fault
  note: May be intermittent, with lower insulation or short circuits on rainy days.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h5
    h: 086a578b6c8a
  review: drafted
- claim_id: c22
  rel: presents_as
  target: symptom:string-current-low
  note: A module whose glass is broken over its full area lowers current and power for the whole string.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r5
    h: 21e9fd14fbde
  review: drafted
- claim_id: c23
  rel: presents_as
  target: symptom:gradual-performance-decline
  note: Caused by cell and circuit corrosion as water vapour and oxygen get in.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r5
    h: 21e9fd14fbde
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h5
    h: 086a578b6c8a
  review: drafted
- claim_id: c24
  rel: leads_to
  target: fm:insulation-loss
  note: Most pronounced in wet conditions. It can stop the whole plant.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=front
    h: fbd89f70605e
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h3
    h: 6dfd57c14260
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h5
    h: 086a578b6c8a
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r5
    h: 21e9fd14fbde
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h6
    h: da22d4046811
  review: drafted
- claim_id: c25
  rel: leads_to
  target: fm:cell-cracks
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h5
    h: 086a578b6c8a
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h6
    h: da22d4046811
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r5
    h: 21e9fd14fbde
  review: drafted
- claim_id: c26
  rel: leads_to
  target: fm:module-hotspot
  note: Could eventually lead to fire.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h5
    h: 086a578b6c8a
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r5
    h: 21e9fd14fbde
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h6
    h: da22d4046811
  review: drafted
- claim_id: c27
  rel: detected_by
  target: method:visual-inspection
  note: The simplest and most efficient way to detect it.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h7
    h: 9a7ad0612a0a
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r2
    h: 5fdd7c7be8f2
  - src: src:pv-root-cause-glass-breakage
    loc: sec=front
    h: fbd89f70605e
  review: drafted
- claim_id: c28
  rel: detected_by
  target: method:ir-thermography
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h7
    h: 9a7ad0612a0a
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r2
    h: 5fdd7c7be8f2
  review: drafted
- claim_id: c29
  rel: detected_by
  target: method:el-imaging
  note: Shows cell cracks caused by the breakage.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h7
    h: 9a7ad0612a0a
  - src: src:pv-root-cause-glass-breakage
    loc: sec=front
    h: fbd89f70605e
  - src: src:pv-root-cause-glass-breakage
    loc: fig=7
    h: c4fd984891aa
  review: drafted
- claim_id: c30
  rel: detected_by
  target: method:uv-fluorescence
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h7
    h: 9a7ad0612a0a
  review: drafted
- claim_id: c31
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=front
    h: fbd89f70605e
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h2
    h: 226b4cbee592
  review: drafted
- claim_id: c32
  rel: detected_by
  target: method:performance-monitoring
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h7
    h: 9a7ad0612a0a
  - src: src:pv-root-cause-glass-breakage
    loc: sec=front
    h: fbd89f70605e
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c33
  rel: mitigated_by
  target: mit:module-replacement
  note: Needed especially when there is a safety or insulation risk.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h7
    h: 9a7ad0612a0a
  - src: src:pv-root-cause-glass-breakage
    loc: sec=front
    h: fbd89f70605e
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h2
    h: 226b4cbee592
  review: drafted
- claim_id: c34
  rel: mitigated_by
  target: mit:glass-resealing
  note: Only a temporary fix for minor cracks.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h7
    h: 9a7ad0612a0a
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c35
  rel: mitigated_by
  target: mit:root-cause-investigation
  note: Check for clamp stress, hail, handling, or thermal damage.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=front
    h: fbd89f70605e
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h2
    h: 226b4cbee592
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c36
  attr: typical_power_loss
  value:
    min: 1
    max: 2
    unit: unit:PERCENT
  conditions: Loss from glass breakage events in temperate climates, per the Herz et al. study
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h5
    h: 086a578b6c8a
  review: drafted
---
Glass breakage means the module's front glass is cracked, either locally or across the whole module. It is a common, high-severity module failure that affects both safety and output. Common causes include hail or other impacts, wrong clamping or overtightened screws, transport and handling, lamination defects, and thermal stress from hotspots or burn marks. Tempered glass shatters into small pieces and annealed glass breaks into large pieces. The cells underneath are often cracked and can form hotspots. Broken glass lets moisture in, so insulation faults and ground faults can appear, often intermittently on rainy days. Interconnections then corrode over time. Visual inspection is the quickest way to find it. Use infrared thermography for hotspots, electroluminescence for cracked cells, and insulation testing for safety risk. Replace modules with broken glass, especially when safety or insulation is at risk. Resealing only helps temporarily for minor cracks. Also look into the root cause, such as clamp stress or hail.

<!-- review notes
- sentence 3: support check: partial - Glass type breakage patterns are stated, and tempered shattering breaks cells and raises hotspot risk, but 'often cracked' for all glass is a slight generalization.
- sentence 4: support check: partial - Moisture ingress, ground/insulation faults, intermittent rainy days and corrosion are stated, though the causal link of moisture directly to ground faults is somewhat inferred.
- sentence 5: support check: partial - Visual inspection simplest, IR for temperature anomalies, EL for cracks, insulation testing mentioned, but 'for safety risk' and IR-for-hotspots mapping are loosely matched.
-->
