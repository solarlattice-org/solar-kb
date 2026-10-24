---
id: concept:energy-loss-waterfall
type: Concept
name: Energy loss waterfall
aliases:
- loss waterfall
- loss tree
- loss factors
- Performance Waterfall
- pv energy losses waterfall
- VI Performance Waterfall
category: Monitoring
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: tool:alsoenergy-powertrack
  note: The Energy Loss Waterfall is a visual analysis tool under the PowerTrack Analysis tab.
  cite:
  - src: src:alsoenergy-kb-9-energy-loss-waterfall
    loc: sec=front
    h: 3eaf52f980fb
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: sec=7.3
    h: cf46db96b935
  review: drafted
- claim_id: c2
  rel: related_to
  target: metric:clipping-loss
  note: Clipping is one of the loss categories; PowerTrack separates it from Inverter Limit loss at 96%
    of rated output.
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=10.r2
    h: 0372516e81ca
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h2
    h: c6fba6569d7a
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h12
    h: 66cfaabb55b0
  - src: src:man-alsoenergy-pv-model-powertrack-pv-model-losses
    loc: sec=h4
    h: 922439f95406
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:shading-loss
  cite:
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h2
    h: c6fba6569d7a
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=10.r6
    h: c69a93783ca9
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h8
    h: 30e070dc9187
  review: drafted
- claim_id: c4
  rel: related_to
  target: fm:soiling-losses
  cite:
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h2
    h: c6fba6569d7a
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h10
    h: 0e53afbc7459
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=10.r8
    h: d0ec4e1591d7
  review: drafted
- claim_id: c5
  rel: related_to
  target: fm:snow-accumulation-losses
  cite:
  - src: src:alsoenergy-kb-9-energy-loss-waterfall
    loc: sec=front
    h: 3eaf52f980fb
  - src: src:alsoenergy-kb-energy-loss-waterfall
    loc: sec=front
    h: b18a92c492b3
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h2
    h: c6fba6569d7a
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:curtailment
  cite:
  - src: src:alsoenergy-kb-energy-loss-waterfall
    loc: sec=front
    h: b18a92c492b3
  review: drafted
- claim_id: c7
  rel: related_to
  target: metric:availability
  note: Downtime loss covers periods with no production while the model predicts output and no significant
    snow is present.
  cite:
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h6
    h: c07210b8eb97
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=10.r4
    h: 6df027c801f8
  review: drafted
  review_note: 'support check: partial - Downtime loss definition matches the note, but availability as
    a metric is not mentioned; downtime loss is only implicitly related.'
- claim_id: c8
  rel: related_to
  target: metric:degradation-rate
  cite:
  - src: src:alsoenergy-kb-energy-loss-waterfall
    loc: sec=front
    h: b18a92c492b3
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=10.r1
    h: 217652298bc9
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h11
    h: 84a06d8db5ac
  review: drafted
- claim_id: c9
  rel: related_to
  target: concept:expected-energy-model
  note: Expected energy comes from the PV performance model driven by measured weather data.
  cite:
  - src: src:alsoenergy-kb-energy-loss-waterfall
    loc: sec=front
    h: b18a92c492b3
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: sec=7.3
    h: cf46db96b935
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c10
  rel: related_to
  target: metric:performance-index
  cite:
  - src: src:alsoenergy-kb-energy-loss-waterfall
    loc: sec=front
    h: b18a92c492b3
  review: drafted
- claim_id: c11
  rel: related_to
  target: tool:pvsyst
  note: Predicted (non-weather-adjusted) values can refer to PVsyst or 8760 estimates.
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: sec=7.3
    h: cf46db96b935
  review: drafted
- claim_id: c12
  rel: related_to
  target: org:locus-energy
  note: Locus Energy offers the Virtual Irradiance (VI) Performance Waterfall.
  cite:
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h2
    h: c6fba6569d7a
  review: drafted
- claim_id: c13
  attr: degradation_rate
  value:
    nominal: 0.5
    unit: unit:PERCENT-PER-YR
  conditions: Degradation the VI Performance Waterfall assumes by default; only deviations from this rate
    appear in its Degradation bucket
  cite:
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h11
    h: 84a06d8db5ac
  review: drafted
---
An energy loss waterfall is a chart that breaks PV production losses into categories and shows them against actual production and baseline estimates, so you can see quickly where performance is falling short. On the left side it steps from estimated energy, meaning the budget or pro forma, to expected energy, meaning modeled ideal output. In between are an insolation adjustment, degradation and other modeling differences. On the right side it steps from expected energy down to measured energy, using detected losses such as snow, soiling, curtailment and downtime, plus an 'other' bar for unexplained losses and uncertainty. Model-based versions can also show clipping, shading, partial capacity or string outage, and degradation losses, estimated daily by comparing modeled and measured data. The results are only as accurate as the PV model and the irradiance and module temperature data feeding it, so a well-tuned model and good sensors are essential. Losses such as shading, thermal, clipping and inverter efficiency can be part of both the estimated and the expected energy. In that case they do not appear as differences on the estimate-to-expected side of the waterfall. Comparing losses against configured or contractual loss allowances helps owners explain underperformance and check whether site agreements are being met.

<!-- review notes
- sentence 7: support check: partial - Passages support explaining underperformance and compliance with contractual agreements, and contractual comparison, but the exact framing of checking against allowances is somewhat inferred.
-->
