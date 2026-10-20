---
id: meas:stress-test-power-loss
type: Measurement
name: Power loss after stress test
aliases:
- power degradation
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: Bifacial glass/glass PERC modules with EVA after combined-accelerated stress testing with
    -1200 V bias, flash tested from the front at STC
  note: Reported as almost 10% relative degradation, attributed to PID-p on the rear with a smaller LID
    contribution.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
  review_note: 'possible conflict with c2 (same source; check the conditions); reviewer: the compiler-flagged
    conflict is a different scenario or source, not disagreement'
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 50
    unit: unit:PERCENT
  conditions: Same combined-accelerated stress test of bifacial PERC glass/glass EVA modules at -1200
    V, flash tested from the rear at STC
  note: Loss looks much larger when the rear is illuminated during measurement.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.3.1
    h: 3a65ff4976bc
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'possible conflict with c1 (same source; check the conditions); reviewer: the compiler-flagged
    conflict is a different scenario or source, not disagreement'
- claim_id: c3
  attr: typical_power_loss
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: One module design that survived a 96 h PID stress test at 60°C, 85% RH and -600 V
  note: The 5% figure is also the pass/fail criterion. Modules losing more than that in this test failed
    by PID outdoors.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=7.5
    h: 9b7c70ce3171
  review: disputed
  conflicts_with:
  - meas:stress-test-power-loss#c2
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions);
    possible conflict with c8 (same source; check the conditions); possible conflict with c10 (same source;
    check the conditions)
- claim_id: c4
  attr: typical_power_loss
  value:
    max: 1.5
    unit: unit:PERCENT
  conditions: Complete module shipping stacks after transport simulation per ASTM D4169/4728
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=7.1.2
    h: 965925e2642f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'possible conflict with c3 (same source; check the conditions); possible conflict with
    c7 (same source; check the conditions); possible conflict with c8 (same source; check the conditions);
    possible conflict with c10 (same source; check the conditions); reviewer: the compiler-flagged conflict
    is a different scenario or source, not disagreement'
- claim_id: c5
  attr: typical_power_loss
  value:
    max: 2.8
    unit: unit:PERCENT
  conditions: Modules after transport simulation followed by thermal cycling and dynamic wind load tests
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=7.1.2
    h: 965925e2642f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'possible conflict with c3 (same source; check the conditions); possible conflict with
    c7 (same source; check the conditions); possible conflict with c8 (same source; check the conditions);
    possible conflict with c10 (same source; check the conditions); reviewer: the compiler-flagged conflict
    is a different scenario or source, not disagreement'
- claim_id: c6
  attr: typical_power_loss
  value:
    max: 5
    unit: unit:PERCENT
  conditions: Seven of eight modules of one type after 2000 h damp heat at 85°C/85% RH
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=7.6.1
    h: e99729bd0589
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Seven of eight modules showed less than 5% degradation after
    2000 h damp heat, but the passage doesn''t give ''up to 5%'' as a maximum exactly; roughly consistent
    though ''less than 5%'' vs ''up to 5%'' is close; the figure also hints -7% for one module.; possible
    conflict with c8 (same source; check the conditions); reviewer: the compiler-flagged conflict is a
    different scenario or source, not disagreement'
- claim_id: c7
  attr: typical_power_loss
  value:
    nominal: 4
    unit: unit:PERCENT
  conditions: One module after 2000 h damp heat at 85°C/85% RH
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=7.6.1
    h: e99729bd0589
  review: disputed
  conflicts_with:
  - meas:stress-test-power-loss#c2
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c8 (same source; check the conditions); possible conflict with c10 (same source;
    check the conditions)
- claim_id: c8
  attr: typical_power_loss
  value:
    nominal: 28
    unit: unit:PERCENT
  conditions: Same module after extending damp heat to 3000 h at 85°C/85% RH
  note: Considered overstress. EL showed the outer cell parts completely dark from moisture-driven cell
    corrosion.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=7.6.1
    h: e99729bd0589
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'possible conflict with c3 (same source; check the conditions); possible conflict with
    c4 (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c6 (same source; check the conditions); possible conflict with c7 (same source;
    check the conditions); possible conflict with c9 (same source; check the conditions); possible conflict
    with c10 (same source; check the conditions); reviewer: the compiler-flagged conflict is a different
    scenario or source, not disagreement'
- claim_id: c9
  attr: typical_power_loss
  value:
    max: 5
    unit: unit:PERCENT
  conditions: Three of seven crystalline modules from different makers after 800 temperature cycles
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=7.6.1
    h: e99729bd0589
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'possible conflict with c8 (same source; check the conditions); reviewer: the compiler-flagged
    conflict is a different scenario or source, not disagreement'
- claim_id: c10
  attr: typical_power_loss
  value:
    nominal: 3
    unit: unit:PERCENT
  conditions: Baseline (bias) loss from glass corrosion after mechanical load followed by 200 humidity
    freeze cycles
  note: On top of this baseline, loss rises with the number of cracked cells.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'possible conflict with c3 (same source; check the conditions); possible conflict with
    c4 (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c7 (same source; check the conditions); possible conflict with c8 (same source;
    check the conditions); reviewer: the compiler-flagged conflict is a different scenario or source,
    not disagreement'
---
This signature is a drop in module maximum power, usually measured by flash testing at standard test conditions before and after an accelerated stress test. In PID lab tests the module's rated system voltage is applied to its shorted leads while the module surfaces are grounded, either in a damp heat chamber or with foil or other conductive electrodes. Modules that lose more than the pass/fail limit in the 60°C, 85% RH PID test have also failed by potential induced degradation outdoors. In bifacial PERC modules, the PID-p loss is much larger when the module is flash tested from the rear than from the front. With longer stress, power can partly recover. Leakage current during the test is only a weak indicator of how much power is lost, so measure power directly. After damp heat or thermal cycling tests, EL images taken with the power measurement can show dark cell edges from corrosion or dark areas from disconnected busbars. Modules with more cracked cells, or with dendritic crack patterns, show more power loss after humidity freeze sequences.

<!-- review notes
- sentence 1: support check: partial - Passages show drops in power measured by flash/IV before and after stress, but 'usually' and 'maximum power' before/after are not explicitly stated generally.
- sentence 5: support check: partial - Leakage current is called a weak indicator of degradation extent, but the advice to measure power directly is not stated.
- sentence 6: support check: partial - EL images show dark outer cell parts after damp heat and dark busbar areas after thermal cycling, but 'taken with power measurement' is only loosely implied; cell edges 'dark' matches, so mostly supported.
-->
