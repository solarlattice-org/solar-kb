---
id: symptom:yellow-brown-discoloration
type: Symptom
name: Yellow to brown discoloration
aliases:
- yellowing
- browning
- EVA browning
- Browned EVA
- discolouration
claims:
- claim_id: c1
  rel: observed_as
  target: meas:iv-low-isc
  note: Encapsulant yellowing absorbs light in front of the cells; short-circuit current is the module
    parameter affected.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.1
    h: 725c270e5e04
  review: drafted
  review_note: 'support check: partial - Passage says yellowing affects short-circuit current and gives
    ~10% Jsc loss over a decade, but does not mention IV-curve observation or irradiance-normalized string
    current/neighbour comparison signals.'
- claim_id: c2
  rel: observed_as
  target: meas:ir-hotspot
  note: Discolouration behind or around the junction box from resistive heating; the heat shows as a hot
    spot in an IR camera.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - Passage links resistive heating in the junction box to discolouration
    behind/around it and IR-detectable heat, but is about junction box interconnection failure, not yellow-brown
    discoloration generally.'
- claim_id: c3
  rel: observed_as
  target: meas:visible-burn-marks
  note: Burn marks may appear with discolouration near the junction box, or with metallization discolouration/corrosion.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h37
    h: abafe13c83d7
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h65
    h: 932bed75d53f
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h34
    h: 57cc697f982e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: observed_as
  target: meas:el-dark-cell-edges
  note: Seen when metallization discolouration comes with corrosion caused by moisture diffusing in from
    the cell edges.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h65
    h: 932bed75d53f
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h34
    h: 57cc697f982e
  review: drafted
- claim_id: c5
  attr: degradation_rate
  value:
    nominal: 0.5
    unit: unit:PERCENT-PER-YR
  conditions: Typical mean yearly degradation from encapsulant yellowing
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.1
    h: 725c270e5e04
  review: drafted
- claim_id: c6
  attr: degradation_rate
  value:
    max: 1
    unit: unit:PERCENT-PER-YR
  conditions: Yellowing in hot and humid or moderate climates
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.1
    h: 725c270e5e04
  review: drafted
- claim_id: c7
  attr: degradation_rate
  value:
    max: 10
    unit: unit:PERCENT-PER-YR
  conditions: Mirror-enhanced PV modules installed in desert environments
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.1
    h: 725c270e5e04
  review: drafted
- claim_id: c8
  attr: current_drop
  value:
    nominal: 10
    unit: unit:PERCENT
  conditions: Short-circuit current loss over the first decade of exposure, for modules prone to yellowing
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.1
    h: 725c270e5e04
  review: drafted
---
Yellow to brown discoloration ranges from light yellow to dark brown. It can show in the encapsulant over or between cells, along busbars and interconnects, or on either side of the backsheet. In glass/backsheet modules the browning usually sits in the middle of each cell, with a clear frame around the cell edges and along cracks. This clear frame comes from photobleaching and should not be mistaken for snail tracks. If the browning is even across the module, encapsulant discoloration is the likely cause. It reduces short-circuit current, so look for a slow loss of current in IV curves or monitoring data. If one cell is much darker than its neighbours, that cell ran hotter, possibly because it sits above the junction box. Check the junction box for a hot spot with an IR camera. Yellowed, browned or bubbled potting inside the junction box, or burn marks behind it, point to a junction box interconnection failure caused by heat or arcing. This can start a fire, so treat it as a safety issue. If the yellow, brown or black color is on the gridlines, solder bonds or ribbons rather than the encapsulant, suspect metallization corrosion. EL images may show dark cell edges, and white or colored powdery deposits may be present. Discoloration of the backsheet can come before backsheet cracking. During a visual inspection, check discolored backsheets for cracks and chalking.

<!-- review notes
- sentence 3: support check: partial - Passages say uniform discolouration is typical for glass/glass and that yellowing reduces Jsc, but do not state that even browning implies encapsulant cause or the diagnostic advice about slow current loss.
- sentence 7: support check: partial - Discolouration is stated as a precursor to backsheet cracking, but the passages say nothing about checking for cracks and chalking during visual inspection (chalking is tied to strong chalking, not specifically advised).
-->
