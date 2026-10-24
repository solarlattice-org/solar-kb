---
id: concept:accelerated-life-testing
type: Concept
name: Accelerated life testing
aliases:
- ALT
- accelerated stress testing
- accelerated testing
- accelerated ageing tests
category: Reliability
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: std:iec-61215
  note: Most PV module stress tests are based on the IEC 61215 type approval standard; extended IEC 61215
    testing multiplies its test durations or cycles.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h30
    h: 0a52a379598e
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.8
    h: 32807ea8b436
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.5
    h: 1cb1597d3ea1
  review: drafted
- claim_id: c2
  rel: related_to
  target: std:iec-61730
  note: Climate-specific accelerated ageing programmes adapted existing procedures including the IEC 61730
    module safety requirements.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.8
    h: 32807ea8b436
  review: drafted
- claim_id: c3
  rel: related_to
  target: std:iec-61701
  note: Salt mist corrosion testing was among the standard procedures adapted for climate-specific accelerated
    ageing.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.8
    h: 32807ea8b436
  review: drafted
- claim_id: c4
  rel: related_to
  target: stressor:thermal-cycling
  note: Temperature cycling is a common applied stress; more frequent cycling reproduced cell cracks and
    cell connector breakage.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h30
    h: 0a52a379598e
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.8
    h: 32807ea8b436
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.4.3
    h: d2cc5aae4e97
  review: drafted
- claim_id: c5
  rel: related_to
  target: stressor:mechanical-stress
  note: Static and cyclic dynamic mechanical loading are applied to bring out interconnect, cell, solder
    bond and glass failures.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h30
    h: 0a52a379598e
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.5
    h: 1cb1597d3ea1
  review: drafted
- claim_id: c6
  rel: related_to
  target: stressor:hail
  note: Impacts such as hail, stones and projectiles are among the applied stressors.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h30
    h: 0a52a379598e
  review: drafted
- claim_id: c7
  rel: related_to
  target: stressor:moisture-exposure
  note: Humidity and damp heat testing examine resistance to corrosion, water vapour intrusion, hydrolysis
    and encapsulant delamination.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h30
    h: 0a52a379598e
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.1
    h: bdc8440255cc
  review: drafted
- claim_id: c8
  rel: related_to
  target: fm:cell-cracks
  note: Cell cracking was reproduced in climate-specific and combined accelerated stress tests.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.8
    h: 32807ea8b436
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.9
    h: 63d23e8c062b
  review: drafted
- claim_id: c9
  rel: related_to
  target: fm:backsheet-cracking
  note: Observed in Combined-Accelerated Stress Testing.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.9
    h: 63d23e8c062b
  review: drafted
- claim_id: c10
  rel: related_to
  target: fm:delamination
  note: Delamination is induced by damp heat and by alternating mechanical and environmental stresses.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.9
    h: 63d23e8c062b
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.5
    h: 1cb1597d3ea1
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.1
    h: bdc8440255cc
  review: drafted
  review_note: 'support check: partial - Damp heat is said to examine resistance to encapsulant delamination
    and mechanical/environmental alternation is to precipitate delamination, but ''induced by damp heat''
    is only loosely stated.'
- claim_id: c11
  rel: related_to
  target: fm:light-induced-degradation
  note: Various light-induced degradation modes were observed in Combined-Accelerated Stress Testing.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=3.3.9
    h: 63d23e8c062b
  review: drafted
---
Accelerated life testing exposes PV modules to the same stresses they meet in the field, but at higher levels than they see outdoors. The aim is to make degradation happen faster than it would in real-world conditions. Typical stresses include high and low temperature, temperature cycling, sunlight, humidity, mechanical load, impacts such as hail, electrical discharge, corrosive fluids, and system voltage. Stresses can be applied one at a time, in sequence, or combined. The Combined-Accelerated Stress Test (C-AST) applies humidity, temperature, light, rain, wind and snow loads, and voltage together to find weaknesses in new module designs. Most tests are based on IEC 61215. Some run its tests for longer or for more cycles (extended IEC 61215 testing), and others keep going until the module fails (test to failure). Damp heat testing most often runs at 85°C and 85% relative humidity. It checks how well a module resists corrosion, water vapour getting in, hydrolysis, and encapsulant delamination. An acceleration factor tells you how much faster degradation runs under test. It only holds for one degradation mechanism, in one material, under one exposure condition. Results can be used to rank modules against each other, but they cannot be turned directly into an expected service life. Materials may not degrade in proportion to the higher stress, so a test may not trigger the same mechanisms as field exposure. Researchers are working to link indoor test results to outdoor degradation in different climates, using physics-based and statistical models.
