---
id: concept:pv-module-end-of-life
type: Concept
name: PV module end of life
aliases:
- second-life PV
- module recycling
- end-of-life
- EoL
category: Lifecycle
concept_kind: technology
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 0
    max: 20
    nominal: 10
    unit: unit:PERCENT
  conditions: Wear-out failures (delamination, cell part isolation from cracks, laminate discoloration)
    in a fleet of 272 modules from 3 manufacturers after more than 15 years of operation; nominal is the
    reported mean
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=3
    h: ac0f157068c8
  review: drafted
- claim_id: c2
  rel: related_to
  target: metric:degradation-rate
  note: Degradation models combined with a defined end-of-life condition are used to predict service life
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h16
    h: 7be6ed35aa2e
  - src: src:iea-pvps-t13-16-2021
    loc: tbl=4.r9
    h: 05c512752e58
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h21
    h: e37f3264b2ee
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:bathtub-curve
  note: Wear-out failures at the end of working life follow infant and midlife failures
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=3
    h: ac0f157068c8
  review: drafted
- claim_id: c4
  rel: related_to
  target: std:iec-61215
  note: Type approval pass/fail criteria are minimum quality checks and cannot be read as end-of-life
    conditions
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h22
    h: acd307545bb5
  - src: src:iea-pvps-t13-01-2014
    loc: sec=3
    h: ac0f157068c8
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c5
  rel: related_to
  target: concept:accelerated-life-testing
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h16
    h: 7be6ed35aa2e
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h22
    h: acd307545bb5
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: related_to
  target: metric:levelized-cost-of-energy
  note: How end of life is defined affects calculated service life, yield and LCOE
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h16
    h: 7be6ed35aa2e
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h22
    h: acd307545bb5
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:repowering
  note: Economic end of life can come when swapping in newer, more efficient modules pays off; refurbishing
    can extend system life
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=2.2.2
    h: 85205e88bb23
  - src: src:trn-oandm-nrel-best-practices-for-om-of-photovoltaic-and-ess
    loc: sec=6.10
    h: e476192cb28d
  review: drafted
- claim_id: c8
  rel: related_to
  target: concept:standard-test-conditions
  note: Warranty-based end of life is often tied to losing a share of initial STC power
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: tbl=6.r7
    h: 23ed16e02dec
  review: drafted
- claim_id: c9
  rel: related_to
  target: concept:power-purchase-agreement
  note: Extending the performance contract or PPA is one option at the end of the performance period
  cite:
  - src: src:trn-oandm-nrel-best-practices-for-om-of-photovoltaic-and-ess
    loc: sec=6.10
    h: e476192cb28d
  review: drafted
---
PV module end of life is the point where a module is no longer considered fit for use, and no single definition works in every situation. Functional end of life is reached when a critical property, usually module power, drops below a chosen level; strictly it means no output or no electrical safety, but in practice a much higher threshold is used, often linked to warranty terms. Wear-out failures end a module's working life when a safety problem appears or power falls below a set level, typically between 80% and 70% of the initial rating. Economic end of life can come at any degradation stage, for example when electricity prices or contracts change or when replacing modules with more efficient ones becomes attractive. Service life prediction models gradual degradation driven by environmental and operational stressors; sudden events like hail or fire are left out of these models. Passing IEC 61215 type approval tests does not prove a module will last a given number of years, because those tests target early failures and product defects. At the end of the performance period, owners can refurbish and extend the system, extend the PPA, sell the system, or remove it and restore the site. Commercial recycling has shown that 84% to 90% of a module's weight can be recycled, and decommissioning plans may include money set aside for recycling or disposal.

<!-- review notes
- sentence 1: support check: partial - Passages say no generally applicable definition exists and that EoL is context-dependent, but they don't define it as 'no longer fit for use'.
- sentence 8: support check: partial - The 84-90% by weight recycling figure is stated, but decommissioning plans are said to include financial mechanisms for recycling or disposal, not explicitly money set aside.
- sentence 1: review: partial - The passages say no definition of end of life applies in every situation, but they never define it as the point where a module is 'no longer considered fit for use'.
-->
