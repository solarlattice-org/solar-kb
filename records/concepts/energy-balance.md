---
id: concept:energy-balance
type: Concept
name: Energy balance at the grid connection point
aliases:
- consumption calculation
- load = PV + import - export
category: Monitoring
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: comp:energy-meter
  note: A measurement source such as an energy meter has to be present at the grid-connection point. Meter
    placement decides whether the balance comes out right.
  cite:
  - src: src:sma-doc-240154
    loc: sec=h217
    h: caf6c20f13c6
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  - src: src:sma-doc-259463
    loc: sec=h36
    h: 335e0ec8708d
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: related_to
  target: concept:point-of-interconnection
  note: The balance uses drawn power, fed-in power and reactive power measured at the point of interconnection.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: tbl=38
    h: 173265fd66de
  - src: src:sma-doc-275857
    loc: tbl=10
    h: b44bc0da7931
  - src: src:sma-doc-259761
    loc: sec=h501
    h: bc1116db50bf
  review: drafted
  review_note: 'support check: partial - Passages list drawn, fed-in and reactive power at the grid connection
    point, but do not describe an ''energy balance'' using them.'
- claim_id: c3
  rel: explains
  target: symptom:production-mirrors-consumption
  note: If PV is connected on the grid side of the meter, the meter only ever sees power drawn. The calculated
    consumption then follows PV production.
  cite:
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  review: drafted
- claim_id: c4
  rel: explains
  target: symptom:night-grid-feed-in
  note: If the meter, a CT or a current-measurement lead is installed the wrong way round, the sign of
    grid power flips, so the system shows feed-in at night.
  cite:
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  review: drafted
  review_note: 'support check: partial - Incorrect orientation of meter, CT or leads is given as possible
    reasons for night feed-in, but the ''sign flips'' mechanism isn''t explicitly stated.'
- claim_id: c5
  rel: related_to
  target: fm:energy-meter-installation-error
  cite:
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: related_to
  target: func:self-consumption-optimization
  note: Power control at the grid-connection point tries to use PV energy on site, or store it, before
    feeding it in, and to supply loads from PV or the battery before drawing from the grid.
  cite:
  - src: src:sma-doc-259463
    loc: sec=4.3.1
    h: e352f2fb4386
  - src: src:sma-doc-259463
    loc: sec=h36
    h: 335e0ec8708d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: related_to
  target: func:export-limitation
  note: Limited Export works with a meter at the grid-connection point. Inverter output rises or falls
    by the amount of self-consumption.
  cite:
  - src: src:sma-doc-278879
    loc: sec=5.2.7
    h: 05e66d8a958b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: related_to
  target: func:zero-export
  cite:
  - src: src:eq-equip-inverters-sma-data-manager-m-manual-edmm-10-be-en-17
    loc: sec=h75
    h: 3946a1e40165
  review: drafted
- claim_id: c9
  rel: related_to
  target: metric:self-consumption-rate
  cite:
  - src: src:sma-doc-246498
    loc: tbl=41.r1
    h: 4187ba7a2f23
  review: drafted
  review_note: 'support check: partial - Self-consumption rate is defined as ratio to total yield, but
    no link to grid-connection energy balance is stated.'
- claim_id: c10
  rel: related_to
  target: metric:self-sufficiency-rate
  cite:
  - src: src:sma-doc-246498
    loc: tbl=41.r1
    h: 4187ba7a2f23
  review: drafted
  review_note: 'support check: partial - Self-sufficiency quota is defined, but no relation to the grid-connection
    energy balance is stated.; review: partial - The table defines the self-sufficiency quota next to
    grid feed-in and self-consumption totals, but it never ties the metric to the energy balance at the
    grid-connection point.'
- claim_id: c11
  rel: related_to
  target: func:consumption-metering
  cite:
  - src: src:sma-doc-262631
    loc: tbl=15.r2
    h: 3ba43d08569d
  - src: src:sma-doc-262660
    loc: tbl=15.r2
    h: 3ba43d08569d
  review: drafted
  review_note: 'support check: partial - Passages mention current consumption and an Energy Balance page,
    but not consumption metering at the grid connection point.'
---
Energy balance means adding up the power flows at the grid-connection point (PV production, grid feed-in and grid draw) to work out how much energy the site's loads actually consume. When PV is connected on the load side of the meter, consumption is PV production minus feed-in. For example, 50kW produced with 40kW fed in gives 10kW of load. To make this work, a measurement source such as an energy meter must be fitted at the grid-connection point, positioned so that household loads can use PV energy before it reaches the feed-in point. If PV is wired on the grid side of the meter, the calculation adds PV on top of grid draw and overstates consumption. Monitoring then shows production mirroring consumption. Feed-in that appears at night usually means the meter, a CT or a current-measurement lead is installed the wrong way round. Check CT orientation, CT ratio, and that grid power changes when you switch the inverter on and off. Three-phase meters can add up import and export phase by phase, or by the direction of total power for billing. The two methods give different import and export totals for the same period.

<!-- review notes
- sentence 1: support check: partial - Examples compute load from PV and grid power flows, but there is no explicit definition of energy balance as such.
- sentence 5: support check: partial - Orientation causes are listed and checks of CT orientation, ratio and switching inverter are given, but 'usually' and the ratio check being for night feed-in are not directly stated.
- sentence 1: review: partial - The SMA examples work out load consumption from PV production, feed-in and grid draw at the meter, but no passage defines 'energy balance' as that calculation.
-->
