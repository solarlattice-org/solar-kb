---
id: fm:encapsulant-discoloration
type: FailureMode
name: Discoloration
aliases:
- EVA discolouration
- yellowing
- browning
- Discolouration of encapsulant
claims:
- claim_id: c1
  rel: affects
  target: comp:encapsulant
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.1
    h: 2cb68650cddf
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:backsheet
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:yellow-brown-discoloration
  note: Light yellow to dark brown colour over or between cells, along busbars or interconnects, or on
    the backsheet; often patchy, with clear frames around cell edges in glass/backsheet modules.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  review: drafted
- claim_id: c4
  rel: presents_as
  target: symptom:encapsulant-photobleaching
  note: Oxygen bleaches the chromophores, leaving a clear ring around the edge of a cell or along a cell
    crack.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.1
    h: 2cb68650cddf
  review: drafted
- claim_id: c5
  rel: presents_as
  target: symptom:gradual-performance-decline
  note: Module current and power fall only after the discoloration is already visible.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.1
    h: 2cb68650cddf
  review: drafted
- claim_id: c6
  rel: presents_as
  target: symptom:substring-loss
  note: Only when the discoloration is very severe and confined to a single cell.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.1
    h: 2cb68650cddf
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  review: drafted
- claim_id: c8
  rel: detected_by
  target: method:iv-curve-tracing
  note: Listed as a secondary detection method.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  review: drafted
- claim_id: c9
  rel: detected_by
  target: method:ir-thermography
  note: Listed as a secondary detection method.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  review: drafted
- claim_id: c10
  rel: caused_by
  target: stressor:uv-exposure
  note: Heat and UV acting on EVA; photo-oxidation produces discoloration.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.1
    h: 2cb68650cddf
  - src: src:iea-pvps-t13-16-2021
    loc: tbl=12.r2
    h: 2a0a2a40eb18
  review: drafted
- claim_id: c11
  rel: caused_by
  target: stressor:high-temperature
  note: Thermo-oxidation causes discoloration. A single dark cell suggests that cell ran hotter than its
    neighbours.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: tbl=12.r1
    h: f90c82d02f74
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.1
    h: 2cb68650cddf
  review: drafted
- claim_id: c12
  rel: caused_by
  target: stressor:low-quality-material
  note: Additives that are poorly chosen or at the wrong concentration, or UV absorber that is used up
    over time.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.1
    h: 2cb68650cddf
  review: drafted
- claim_id: c13
  rel: caused_by
  target: stressor:manufacturing-defect
  note: Lamination that is inadequate or incomplete.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  review: drafted
- claim_id: c14
  rel: leads_to
  target: fm:backsheet-cracking
  note: Discoloration of UV-sensitive backsheets can lead to loss of elasticity and to cracking under
    thermomechanical stress.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  review: drafted
- claim_id: c15
  rel: leads_to
  target: fm:severe-metallization-corrosion
  note: The sources report a correlation with acetic acid generation and accompanying corrosion, not a
    direct cause.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.1
    h: 2cb68650cddf
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:stabilized-encapsulant
  note: Better EVA stabilisation with UV absorbers and thermal stabilizers has largely solved the problem.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  review: drafted
- claim_id: c17
  attr: degradation_rate
  value:
    nominal: 0.5
    unit: unit:PERCENT-PER-YR
  conditions: Typical mean yearly degradation from yellowing
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h58
    h: '98e749035673'
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h24
    h: 017575ddabf4
  review: drafted
- claim_id: c18
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
  review: drafted
- claim_id: c19
  attr: degradation_rate
  value:
    max: 0.5
    unit: unit:PERCENT-PER-YR
  conditions: Expected share of EVA discoloration in the roughly 0.8%/a degradation commonly seen for
    Si modules
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.1
    h: 2cb68650cddf
  review: drafted
- claim_id: c20
  attr: typical_power_loss
  value:
    nominal: 10
    unit: unit:PERCENT
  conditions: Approximate total loss of module performance when discoloration is severe
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.1
    h: 2cb68650cddf
  review: drafted
  review_note: 'support check: partial - Passage says ~10% total loss appears with severe discolouration,
    but ''typical power loss'' framing is stronger than the source''s approximate statement.'
---
Discoloration happens when the polymer encapsulant, usually EVA, or the backsheet breaks down and turns light yellow to dark brown. The colour is often patchy: in glass/backsheet modules it tends to sit in the middle of cells with clear frames at the edges, while in glass/glass modules it is mostly even. Clear rings around cell edges or along cracks are photobleaching, and they should not be confused with snail tracks. Heat and UV light acting on poorly stabilised encapsulant or poorly laminated modules are the main drivers. Confirm it by visual inspection, then check the electrical impact with IV curve tracing and infrared thermography. It starts as a cosmetic issue and causes slow current and power loss, typically about 0.5 percent per year and up to 1 percent per year in hot, humid or moderate climates. Watch closely when one cell is much darker than its neighbours, because severe local discoloration can switch on a bypass diode. A discoloured UV-sensitive backsheet can later crack.

<!-- review notes
- sentence 3: support check: partial - Photobleaching rings and warning not to mistake snail tracks for photobleaching are stated, but 'clear rings are photobleaching' and the confusion warning are only loosely paired.
- sentence 4: support check: partial - Heat, UV and inadequate additives/lamination are stated causes, but 'main drivers' ranking is not explicitly stated.
- sentence 5: support check: partial - VI as detection with IV and IRT secondary is listed, but the sequenced workflow to check electrical impact is not stated.
-->
