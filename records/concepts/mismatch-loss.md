---
id: concept:mismatch-loss
type: Concept
name: Mismatch loss
aliases:
- module mismatch
- string mismatch
- electrical mismatching
- Mismatch
category: Modules
concept_kind: electrical
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 2
    unit: unit:PERCENT
  conditions: Loss in system power from module-to-module performance inconsistencies, as stated in an
    IEA PVPS overview of typical losses
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.1.2
    h: d33eadee0e8d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 0.97
    max: 0.99
    nominal: 0.98
    unit: unit:UNITLESS
  conditions: 'Mismatch loss factor (multiplier) observed in the field: typical 0.98, low 0.97, high 0.99'
  note: Value is a derate factor, not a percentage loss.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: tbl=9.r3
    h: 35590d5a8092
  review: drafted
- claim_id: c3
  attr: degradation_rate
  value:
    nominal: 0.1
    unit: unit:PERCENT-PER-YR
  conditions: Approximate allowance some independent engineers add to the module degradation rate to cover
    mismatch from modules degrading at different rates; a modeling allowance, not a universal rule
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  review: drafted
- claim_id: c4
  rel: part_of
  target: metric:array-capture-loss
  note: Electrical mismatching is listed among the causes of capture losses.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.1.2
    h: d33eadee0e8d
  review: drafted
- claim_id: c5
  rel: explains
  target: fm:system-vs-module-degradation
  note: Uneven module degradation creates extra mismatch, so system degradation can exceed module nameplate
    degradation.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=front
    h: ff0c8c5f07cc
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h2
    h: 14c4627b4866
  review: drafted
- claim_id: c6
  rel: related_to
  target: arch:module-level-power-electronics
  note: Module-level MPPT with optimisers reduces mismatch losses.
  cite:
  - src: src:trn-training-industry-reports-and-guides-spe-floating-pv-report-02-mr-74f6db82ca
    loc: sec=h54
    h: 7e355a751003
  review: drafted
- claim_id: c7
  rel: related_to
  target: comp:bypass-diode
  note: Low-power modules or substrings can be bypassed, losing all their power.
  cite:
  - src: src:trn-training-industry-reports-and-guides-spe-floating-pv-report-02-mr-74f6db82ca
    loc: sec=h54
    h: 7e355a751003
  review: drafted
- claim_id: c8
  rel: related_to
  target: arch:floating-pv
  note: Relative module movement on water changes tilt and azimuth within a string and increases mismatch.
  cite:
  - src: src:trn-training-industry-reports-and-guides-spe-floating-pv-report-02-mr-74f6db82ca
    loc: sec=h54
    h: 7e355a751003
  review: drafted
- claim_id: c9
  rel: related_to
  target: fm:bypass-diode-failure
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=front
    h: 44eaacc73841
  review: drafted
  review_note: 'support check: partial - Bypass diode failure entry is tagged ''module mismatch'' and
    mentions upstream mismatch drivers, but the relation to mismatch loss is only loosely implied.'
---
Mismatch loss is power lost because the modules in a string do not all have the same current-voltage characteristics, so their small differences in performance cost power. Because of this, the maximum output of the whole array is always lower than the sum of each module's maximum output. A slightly weaker module limits the string current and pulls the stronger modules away from their best operating point. Very weak modules or substrings get bypassed, and all of their power is lost. Mismatch is one of the capture losses. Yield models usually apply a module mismatch factor of about 0.98. Modules can become mismatched when they degrade at different rates, so system degradation can be higher than the degradation of the modules themselves. Floating PV and bifacial modules tend to have more mismatch, partly because modules moving with the waves change tilt and azimuth within a string. Power optimisers and other module-level power electronics reduce mismatch by tracking the maximum power point of each module. In the field, mismatch can be found with string-current comparisons on combiner monitoring, or with module-level mismatch reports. In those reports, mismatch beyond plus or minus 6 percent, or a sudden increase, calls for investigation.

<!-- review notes
- sentence 3: support check: partial - Passages say slightly lower modules limit string current, forcing lower operating point for others, and weak modules/substrings are bypassed losing all power; 'best operating point' is paraphrase, fine, but is from floating PV context only.
- sentence 4: support check: partial - Capture loss and 0.98 factor are stated, but 'yield models usually apply' is not explicitly stated; the sources show a 0.98 typical value.
- sentence 4: review: partial - IEA lists electrical mismatching as a capture loss, and two tables give 0.98 as the typical mismatch factor, but no passage says yield models usually apply it (the IEA table is of factors observed in the field).
-->
