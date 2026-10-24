---
id: concept:tracker-stow
type: Concept
name: Tracker stow
aliases:
- wind stow
- snow stow
- hail stow
- stow position
- night stow
- overnight stow mode
- global stow
- defensive hail stow
category: Trackers
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: comp:single-axis-tracker
  note: Stow is a protective operating position of single-axis trackers.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h4
    h: 65b80c7f6952
  - src: src:eq-equip-trackers-valmont-kt084677mn-user-manual
    loc: sec=12.1
    h: 5a0513d92837
  - src: src:iea-pvps-t13-33-2025
    loc: fig=41
    h: 58b7f1d33f83
  review: drafted
- claim_id: c2
  rel: explains
  target: fm:tracker-wind-stow-losses
  note: Off-angle stow position reduces irradiance capture until rows return to tracking.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h4
    h: 65b80c7f6952
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h2
    h: 3c102c6647a1
  review: drafted
- claim_id: c3
  rel: related_to
  target: meas:stow-event-output-dip
  note: Stow periods appear as intermittent, weather-correlated output dips under otherwise good irradiance.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h4
    h: 65b80c7f6952
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  rel: related_to
  target: mit:tracker-stow-strategy
  cite:
  - src: src:iea-pvps-t13-33-2025
    loc: sec=3.5
    h: 7040eca2cd0a
  review: drafted
- claim_id: c5
  rel: related_to
  target: stressor:high-wind
  note: Wind stow is triggered when measured wind exceeds the controller threshold.
  cite:
  - src: src:eq-equip-trackers-terrasmart-terratrak-client-documents-90032-000-terratrak-tt2-o-m-manual-101220
    loc: sec=4.3
    h: e637a3569cea
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h4
    h: 65b80c7f6952
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h7
    h: 47f98047fafd
  review: drafted
- claim_id: c6
  rel: related_to
  target: stressor:hail
  note: Defensive hail stow; IEA PVPS suggests hail stow take precedence over other stow modes where the
    manufacturer allows.
  cite:
  - src: src:eq-equip-trackers-ati-array-tech-ati-duratrack-hz-v3-operations-maintenance-guide-rev-b-3-20201101
    loc: sec=5.5.1
    h: e82d2c772296
  - src: src:iea-pvps-t13-33-2025
    loc: sec=3.5
    h: 7040eca2cd0a
  review: drafted
- claim_id: c7
  rel: related_to
  target: stressor:snow-load
  note: Snow sensors or snow modes can trigger stow.
  cite:
  - src: src:eq-equip-trackers-terrasmart-terratrak-client-documents-90032-000-terratrak-tt2-o-m-manual-101220
    loc: sec=4.3
    h: e637a3569cea
  - src: src:eq-equip-trackers-valmont-kt084677mn-user-manual
    loc: sec=12.1
    h: 5a0513d92837
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: related_to
  target: tool:anemometer
  note: Multiple anemometers recommended because storm gusts are small and unevenly distributed.
  cite:
  - src: src:iea-pvps-t13-33-2025
    loc: sec=3.5
    h: 7040eca2cd0a
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c9
  rel: related_to
  target: concept:p50-p90
  note: Actual stow hours should be reconciled against energy model assumptions.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h2
    h: 3c102c6647a1
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h7
    h: 47f98047fafd
  review: drafted
- claim_id: c10
  rel: related_to
  target: concept:scada
  note: SCADA can override or command stow.
  cite:
  - src: src:eq-equip-trackers-terrasmart-terratrak-client-documents-90032-000-terratrak-tt2-o-m-manual-101220
    loc: sec=4.3
    h: e637a3569cea
  - src: src:eq-equip-trackers-ati-array-tech-ati-duratrack-hz-v3-operations-maintenance-guide-rev-b-3-20201101
    loc: sec=5.5.1
    h: e82d2c772296
  review: drafted
- claim_id: c11
  rel: related_to
  target: prod:terrasmart-terratrak
  cite:
  - src: src:eq-equip-trackers-terrasmart-terratrak-client-documents-90032-000-terratrak-tt2-o-m-manual-101220
    loc: sec=4.3
    h: e637a3569cea
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - The passage describes a tracker''s stow details but never names
    TerraSmart TerraTrak.'
- claim_id: c12
  rel: related_to
  target: prod:array-technologies-duratrack-hz-v3
  cite:
  - src: src:eq-equip-trackers-ati-array-tech-ati-duratrack-hz-v3-operations-maintenance-guide-rev-b-3-20201101
    loc: sec=5.5.1
    h: e82d2c772296
  - src: src:eq-equip-trackers-ati-array-tech-ati-duratrack-hz-v3-operations-maintenance-guide-rev-b-3-20201101
    loc: sec=6.4.4
    h: 46811bfa5a26
  - src: src:eq-equip-trackers-ati-array-tech-ati-duratrack-hz-v3-operations-maintenance-guide-rev-b-3-20201101
    loc: sec=6.4.5
    h: 1801a38bc1f1
  review: drafted
- claim_id: c13
  rel: related_to
  target: prod:game-change-genius
  cite:
  - src: src:eq-equip-trackers-game-change-genius-a2-gcs-modbus-register-structure
    loc: tbl=1.r121
    h: 944395a21a32
  - src: src:eq-equip-trackers-game-change-genius-a2-gcs-modbus-register-structure
    loc: tbl=1.r117
    h: 6d9e8f8b9902
  review: drafted
  review_note: 'support check: partial - Modbus Enable Stow registers are given but the passages do not
    name GameChange Genius.'
- claim_id: c14
  rel: related_to
  target: prod:valmont-trj-ai
  cite:
  - src: src:eq-equip-trackers-valmont-kt084677mn-user-manual
    loc: sec=12.1
    h: 5a0513d92837
  review: drafted
---
Tracker stow means moving a tracker to a safety position so that weather does not put critical loads on its parts and shorten their life. On a TerraTrak tracker with a plus or minus 60 degree range of motion, stow is triggered by the weather station wind speed, overnight stow at end of day, SCADA overrides, lost signal from the network controller, or snow and flood sensors. Operators can also command a global stow. On the DuraTrack HZ v3 they pick a preset angle of -52, 0 or +52 degrees to prepare for hail or severe weather. On GameChange trackers stow is enabled through Modbus registers that hold the stow angle. Night stow angles are set per site, and the vendor documents disagree. One Array source recommends 10 to 15 degrees, another recommends 0 to 10 degrees, and both say never to stow at or near the travel limits. Wind stow protects the structure from torsional divergence, resonance and fatigue. Do not lower stow thresholds to recover energy unless the tracker supplier and the structural engineer approve the change. The off-angle stow position cuts irradiance capture, so frequent gust-driven stow shows up as intermittent output dips. These are easily misfiled as availability or weather variance, and actual stow hours should be compared with the energy model assumptions. For hail, IEA PVPS describes defensive hail stow as a proven way to reduce damage. Where the manufacturer allows it, hail stow should override other stow modes, and sites should have several anemometers for good wind data.

<!-- review notes
- sentence 2: support check: partial - Triggers match the list, but the passage doesn't name the product as TerraTrak.
- sentence 3: support check: partial - Presets and Modbus enable-stow registers with stow angle are stated, but the passages don't name DuraTrack HZ v3 or GameChange for these.
- sentence 4: support check: partial - The 10-15 and 0-10 recommendations and the never-stow-near-limits advice are present, but the 'never near limits' advice appears only in the first source, not both, and 'per site' is not stated.
- sentence 4: review: partial - Both recommendations (10-15 and 0-10 degrees) are present, but only the first source warns against stowing at or near the limits, and 'set per site' is not stated.
-->
