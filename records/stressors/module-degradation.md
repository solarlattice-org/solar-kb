---
id: stressor:module-degradation
type: Stressor
name: Module degradation
aliases:
- Degradation
claims:
- claim_id: c1
  attr: degradation_rate
  value:
    nominal: 0.1
    unit: unit:PERCENT-PER-YR
  conditions: Allowance some independent engineers add on top of the module degradation rate when they
    estimate system degradation, to cover mismatch from modules aging at different rates
  note: The source calls this a modeling allowance, not a universal rule. Site measurements, module technology,
    warranty terms and IV or string data should take precedence when available.
  quote: Some independent engineers add about 0.1% per year to the module degradation rate when evaluating
    system degradation.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
Module degradation is the gradual loss of power in an individual PV module over time. Every module degrades to some degree during its operating life. Common causes are hotspots, potential induced degradation, cell cracks, delamination, bubbles, and yellowing or browning of the EVA layer. High levels of water vapour and acetic acid inside the module speed up nearly all degradation modes. The choice of encapsulant and backsheet affects how fast this happens. In a real plant, modules age at different rates. The weaker modules limit the current of the strings or substrings around them, so the whole system can lose more energy than the average module degradation rate suggests. Degraded modules can also push the array maximum power point voltage below the inverter's minimum DC input voltage. This is most likely in hot weather and leads to inverter voltage floor losses. Degradation happens slowly and does not show up in short-term data. Checking whether it exceeds the warranty needs at least two years of data. To limit the impact, model degradation at the system level, allow for spread between modules, and update long-term energy assumptions using field, IV and string-level measurements.

<!-- review notes
- sentence 7: support check: partial - Mitigation of system-level modeling, module spread and field-data updates is stated, but IV and string-level data are mentioned only for modeling inputs, not explicitly for updating long-term assumptions.
-->
