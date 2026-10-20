---
id: stressor:uneven-module-aging
type: Stressor
name: Uneven module aging
aliases:
- module-to-module spread
- unevenness of the module population
claims:
- claim_id: c1
  attr: degradation_rate
  value:
    nominal: 0.1
    unit: unit:PERCENT-PER-YR
  conditions: A modeling allowance that some independent engineers add on top of the module degradation
    rate to cover mismatch when modules degrade at different rates. The source says it is not a universal
    rule.
  quote: Some independent engineers add about 0.1% per year to the module degradation rate when evaluating
    system degradation.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  review: drafted
---
Uneven module aging means that modules in the same plant lose power at different rates over time, instead of all at once at the same rate. Because the plant is an electrical network, weaker modules can hold down the current of the strings or substrings around them. This creates mismatch. It drives the failure mode System Degradation vs Module Degradation: the system loses energy faster than the nameplate module degradation rate suggests. The average module may still be within its warranty while the system shows a larger energy decline. Some spread is present from the start, because even identical parts such as cells, ribbons and bypass diodes vary in initial quality.

<!-- review notes
- sentence 1: support check: partial - Passage says modules age at different rates, but 'instead of all at once' is odd phrasing and not stated; core of differing rates is supported.
- sentence 5: support check: partial - Passage says equal parts like ribbons, cells, bypass diodes vary in initial quality, but doesn't link this to uneven aging spread or say 'from the start' in that sense.
-->
