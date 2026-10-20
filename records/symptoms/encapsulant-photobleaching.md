---
id: symptom:encapsulant-photobleaching
type: Symptom
name: Encapsulant photobleaching
aliases:
- photo-bleaching
- photobleaching effect
claims:
- claim_id: c1
  rel: observed_as
  target: meas:clear-encapsulant-ring
  note: 'Visual signature: oxygen diffusion leaves a ring or frame of transparent EVA around the cell
    perimeter or a cell crack, while the cell center stays yellow to brown. Mostly seen in glass/backsheet
    modules.'
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  review: drafted
  review_note: 'support check: partial - Passages state photobleaching creates a ring of transparent EVA
    around cell perimeter or crack and clear frames in glass/backsheet modules with central discoloration,
    but ''yellow to brown'' center is only loosely stated and ''mostly seen'' is roughly supported by
    ''typically''.'
- claim_id: c2
  rel: observed_as
  target: meas:clear-line-along-crack
  note: Bleaching that follows cell cracks makes otherwise invisible micro-cracks visible to the eye inside
    browned EVA. Do not confuse it with snail tracks, which are discolored silver gridlines.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r1
    h: 790734be7823
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h7
    h: 8b69da4daaac
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=10.r1
    h: a9e2b0882976
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=10
    h: f95eb9235f8d
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:el-crack-pattern
  note: The underlying cell cracks are easy to confirm with electroluminescence or UV fluorescence imaging.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r1
    h: 790734be7823
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  review: drafted
  review_note: 'support check: partial - Passages say cell cracks are easily detected by EL or UV fluorescence,
    but do not describe photobleaching appearing as a crack pattern in EL images.'
---
Photobleaching works against encapsulant yellowing: the encapsulant stays clear along cell cracks and around cell borders, while the rest of the encapsulant turns yellow or brown. Oxygen in the encapsulant drives the effect, so a discolored glass/backsheet module typically shows a transparent ring or frame around each cell or crack, with browning in the cell centers. In glass/backsheet modules, these clearer patterns usually line up with cell cracks, so photobleaching is a visible clue to cracks that the eye would otherwise miss. It points to two failure modes: encapsulant discoloration (the browning itself) and cell cracks (the lines where bleaching follows the cracks). Do not confuse it with snail tracks: a snail track is discolored silver paste on the gridlines, while photobleaching is clear encapsulant along the crack. In lab tests, colored compounds that form under heat and humidity break down under light, which is why this kind of yellowing does not appear in modules exposed to sun, heat and humidity together in the field.

<!-- review notes
- sentence 3: support check: partial - Passages say clearer patterns generally correlate with cell cracks in glass/backsheet modules and that photobleaching makes micro-cracks visible, though 'usually' and 'clue' are slightly stronger framing.
- sentence 4: support check: partial - Passages link photobleaching to both encapsulant discoloration and cell cracks, but do not state that it 'points to two failure modes' as such.
- sentence 6: support check: partial - Passage states chromophores formed under temperature and humidity decompose under irradiation and that this does not occur in real life, but it concerns PO encapsulant/PO backsheet incompatibility specifically, and the statement generalizes it to this kind of yellowing.
-->
