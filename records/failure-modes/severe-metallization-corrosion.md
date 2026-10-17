---
id: fm:severe-metallization-corrosion
type: FailureMode
name: Severe Metallization Corrosion
category: Modules
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:moisture-exposure
  note: Water and oxygen getting into the module start the corrosion process.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=front
    h: 05a21582ed7b
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h2
    h: f411297a4a32
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h3
    h: '924544636200'
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h4
    h: de0a5bfe7306
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:acetic-acid-release
  note: Acetic acid forms when the encapsulant, usually EVA, hydrolyses in the presence of heat and water.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h6
    h: ab4b4f0e5fd4
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h4
    h: de0a5bfe7306
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:high-temperature
  note: Heat drives encapsulant hydrolysis. How sensitive the encapsulant is to heat is a key factor.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h4
    h: de0a5bfe7306
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:uv-exposure
  note: UV stress was considered a possible factor that helps acetic acid form.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h4
    h: de0a5bfe7306
  review: drafted
- claim_id: c5
  rel: caused_by
  target: fm:delamination
  note: Delamination lets water move into the module layers and often sets off encapsulant degradation.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h6
    h: ab4b4f0e5fd4
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h4
    h: de0a5bfe7306
  review: drafted
- claim_id: c6
  rel: caused_by
  target: fm:encapsulant-discoloration
  note: Degraded encapsulant shows yellowing before it promotes corrosion through acetic acid release.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h6
    h: ab4b4f0e5fd4
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c7
  rel: caused_by
  target: fm:glass-breakage
  note: Broken glass lets water in and speeds up corrosion.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h6
    h: ab4b4f0e5fd4
  review: drafted
- claim_id: c8
  rel: caused_by
  target: fm:potential-induced-degradation
  note: PID can raise corrosion levels through its own mechanisms.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h6
    h: ab4b4f0e5fd4
  review: drafted
- claim_id: c9
  rel: affects
  target: comp:solar-cell
  note: The corrosion attacks the cell busbars and metal grid.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h4
    h: de0a5bfe7306
  review: drafted
- claim_id: c10
  rel: affects
  target: comp:cell-interconnect-ribbon
  note: Ribbons are attacked, and corrosion weakens the cell interconnections.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h6
    h: ab4b4f0e5fd4
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h4
    h: de0a5bfe7306
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:series-resistance-increase
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=front
    h: 05a21582ed7b
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h2
    h: f411297a4a32
  review: drafted
- claim_id: c12
  rel: presents_as
  target: symptom:fill-factor-reduction
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c13
  rel: presents_as
  target: symptom:isc-reduction
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  review: drafted
- claim_id: c14
  rel: presents_as
  target: symptom:visible-corrosion
  note: Corrosion is easy to see during visual inspection.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=front
    h: 05a21582ed7b
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h2
    h: f411297a4a32
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c15
  rel: detected_by
  target: method:visual-inspection
  note: Look for corrosion and damage to the encapsulation.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=front
    h: 05a21582ed7b
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h2
    h: f411297a4a32
  review: drafted
- claim_id: c16
  rel: detected_by
  target: method:el-imaging
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=front
    h: 05a21582ed7b
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h2
    h: f411297a4a32
  review: drafted
- claim_id: c17
  rel: detected_by
  target: method:iv-curve-tracing
  note: The IV curve shows a lower fill factor because series resistance rises, plus a lower Isc.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=front
    h: 05a21582ed7b
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h2
    h: f411297a4a32
  review: drafted
- claim_id: c18
  rel: detected_by
  target: method:ir-thermography
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=front
    h: 05a21582ed7b
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h2
    h: f411297a4a32
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c19
  rel: leads_to
  target: fm:module-hotspot
  note: Corrosion is often uneven across the module, which creates mismatch and possible hotspots.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h6
    h: ab4b4f0e5fd4
  review: drafted
- claim_id: c20
  rel: leads_to
  target: fm:bypass-diode-failure
  note: Mismatch can switch on bypass diodes, and running longer than intended speeds up their ageing.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h6
    h: ab4b4f0e5fd4
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c21
  rel: leads_to
  target: fm:cell-interconnection-failure
  note: Weakened interconnections can fail from fatigue, with brown marks.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h6
    h: ab4b4f0e5fd4
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c22
  rel: mitigated_by
  target: mit:module-replacement
  note: Applies to severely corroded modules.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=front
    h: 05a21582ed7b
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h2
    h: f411297a4a32
  review: drafted
- claim_id: c23
  rel: mitigated_by
  target: mit:root-cause-investigation
  note: Find out why water is getting in.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=front
    h: 05a21582ed7b
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h2
    h: f411297a4a32
  review: drafted
- claim_id: c24
  rel: mitigated_by
  target: mit:moisture-resistant-design
  note: Favour module designs that limit moisture exposure.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=front
    h: 05a21582ed7b
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h2
    h: f411297a4a32
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c25
  rel: mitigated_by
  target: mit:proper-installation
  note: Favour installation practices that limit moisture exposure.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=front
    h: 05a21582ed7b
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h2
    h: f411297a4a32
  review: drafted
- claim_id: c26
  attr: typical_power_loss
  value:
    max: 80
    unit: unit:PERCENT
  conditions: Worst-case drop in module maximum power from corrosion caused by water ingress, seen in
    damp-heat tests
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h3
    h: '924544636200'
  review: drafted
  review_note: 'support check: partial - 80% is stated as a worst-case drop in damp-heat tests, not a
    typical value.'
---
Severe metallization corrosion is the chemical attack of a cell's busbars and interconnect ribbons after water and oxygen get into the module. Heat and moisture break down the encapsulant, usually EVA, which releases acetic acid that corrodes the metal. Delamination, a poor backsheet, broken glass and PID can all speed this up. Some corrosion is normal over a module's life, but advanced corrosion can sharply cut module power. Damp-heat tests found losses of up to 80% in the worst case. Corrosion is usually easy to spot visually. Electroluminescence images also show it. On an IV curve it shows as a lower fill factor from higher series resistance, along with a lower short-circuit current. Thermography also helps confirm the electrical impact. Because corrosion is often uneven, it can cause mismatch and hotspots, overwork bypass diodes and weaken cell interconnections. Replace severely corroded modules, find out where the water is getting in, and choose module designs and installation practices that limit moisture exposure.

<!-- review notes
- sentence 1: support check: partial - Passages say corrosion starts with water/oxygen ingress and attacks busbars and ribbons, but 'chemical attack' framing is roughly implied via acetic acid; mostly supported.
-->
