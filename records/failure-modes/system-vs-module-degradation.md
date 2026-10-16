---
id: fm:system-vs-module-degradation
type: FailureMode
name: System Degradation vs Module Degradation
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:module-degradation
  note: Individual modules lose power over time; system loss follows from this but is not always the same
    number.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h4
    h: 3675d15ba302
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
  review_note: 'support check: partial - Passage says system and module degradation differ and mismatch
    arises from uneven aging, but doesn''t state system degradation is caused by module degradation in
    general.'
- claim_id: c2
  rel: caused_by
  target: stressor:uneven-module-aging
  note: Modules aging at different rates creates electrical mismatch, because weaker modules limit current
    in the strings or substrings around them.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h2
    h: 14c4627b4866
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h5
    h: 994460afbabc
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h4
    h: 3675d15ba302
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  rel: presents_as
  target: symptom:gradual-performance-decline
  note: The system energy decline can be larger than the average module loss, even while the average module
    is still within warranty.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h5
    h: 994460afbabc
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: detected_by
  target: method:normalized-output-trend
  note: Long-term normalized plant output helps separate average module degradation from degradation driven
    by mismatch.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h2
    h: 14c4627b4866
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=front
    h: ff0c8c5f07cc
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c5
  rel: detected_by
  target: method:string-inverter-trend
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h2
    h: 14c4627b4866
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=front
    h: ff0c8c5f07cc
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c6
  rel: detected_by
  target: method:iv-curve-tracing
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h2
    h: 14c4627b4866
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=front
    h: ff0c8c5f07cc
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:flash-test
  note: The source refers generally to module test results used to establish average module degradation.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h2
    h: 14c4627b4866
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=front
    h: ff0c8c5f07cc
  review: drafted
  review_note: 'support check: partial - Passages mention generic ''module test results'', not flash testing
    specifically, though the note acknowledges this generality.'
- claim_id: c8
  rel: mitigated_by
  target: mit:system-level-degradation-model
  note: The performance model should include system-level degradation, not just module-level degradation.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h2
    h: 14c4627b4866
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=front
    h: ff0c8c5f07cc
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:forecast-update
  note: Use field measurements, module technology, warranty terms and IV or string data to update long-term
    energy assumptions.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h2
    h: 14c4627b4866
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=front
    h: ff0c8c5f07cc
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  review: drafted
- claim_id: c10
  attr: degradation_rate
  value:
    nominal: 0.1
    unit: unit:PERCENT-PER-YR
  conditions: Modeling allowance that some independent engineers add on top of the module degradation
    rate to account for mismatch from uneven module aging; not a universal rule.
  quote: Some independent engineers add about 0.1% per year to the module degradation rate when evaluating
    system degradation.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
Module degradation is the power an individual module loses over time. System degradation is the energy the whole PV plant loses over time, and the two are not always equal. Modules in the field age at different rates. The weaker ones limit the current of the strings or substrings around them, so the extra mismatch makes the system lose more than the average module does. In practice the plant can show a larger drop in energy even while the average module is still within its warranty. To confirm it, compare long-term normalized plant output and string or inverter trends with IV curve data and module test results. This separates average module degradation from degradation caused by mismatch. Model degradation at the system level and include the spread between modules, not only the module warranty rate.
