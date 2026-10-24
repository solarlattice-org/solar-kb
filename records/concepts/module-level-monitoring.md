---
id: concept:module-level-monitoring
type: Concept
name: Module-level monitoring
aliases:
- panel-level monitoring
category: Monitoring
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: comp:power-optimizer
  note: Optimizer voltage appears in the same list of module-level monitored quantities as module current,
    voltage, power and energy.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: tbl=6.r2
    h: 06b15d4c30ad
  review: drafted
  review_note: 'support check: partial - The list includes optimizer voltage alongside module quantities,
    but nothing in the passage states a relation between module-level monitoring and power optimizers
    beyond that listing.'
---
The quantities recorded at this level include module current, module voltage, module power and module energy. In systems with power optimizers, the optimizer voltage can also be reported for each module.

<!-- review notes
- sentence 2: support check: partial - Optimizer voltage is listed, but the passage doesn't say it is reported per module or tie it to systems with power optimizers.
-->
