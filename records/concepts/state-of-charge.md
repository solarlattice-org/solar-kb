---
id: concept:state-of-charge
type: Concept
name: State of charge
aliases:
- SoC
- SOC
category: Storage
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:soc-estimation
  note: SOC is found by ampere-hour counting with full-charge detection, plus recalibration from battery
    voltage.
  cite:
  - src: src:sma-doc-260329
    loc: sec=1.2
    h: 0872223561b6
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h327
    h: 2e9d5ed84e19
  - src: src:sma-kb-battery-state-of-charge-soc-for-li-ion-batteries-and-how-it-works-in-sma-sunny-isla
    loc: sec=h1
    h: a8ba0e902184
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:charge-controller
  note: Most PV systems with battery storage need a charge controller to regulate battery state of charge.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: fig=65
    h: 0335ef930464
  review: drafted
- claim_id: c3
  rel: related_to
  target: state:float-charge
  note: Float charge ends when SOC drops below 70% of available charging capacity; reaching 100% by float
    charge takes several days.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h17
    h: 668e52e11175
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h640
    h: 1238d4052c9b
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:battery-charging-stages
  note: SOC is reset to 90%, 95% or 100% after boost, full or equalization charge respectively, under
    default settings.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h327
    h: 2e9d5ed84e19
  - src: src:sma-doc-260329
    loc: sec=2.2
    h: e012c72d98e3
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:lead-acid-battery
  note: With lead-acid batteries the Sunny Island needs several cycles to calculate SOC correctly and
    shows 50% after commissioning.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h350
    h: 636148d74283
  - src: src:sma-doc-259761
    loc: tbl=41.r2
    h: d1b331fd7578
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:lithium-ion-battery
  note: A lithium-ion BMS reports SOC to the inverter and adjusts charge limits using SOC.
  cite:
  - src: src:sma-doc-275666
    loc: sec=4.1
    h: 71239ba9a2d6
  - src: src:sma-kb-battery-state-of-charge-soc-for-li-ion-batteries-and-how-it-works-in-sma-sunny-isla
    loc: sec=h1
    h: a8ba0e902184
  review: drafted
- claim_id: c7
  rel: related_to
  target: func:backup-reserve
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-06-home-hub-advanced-battery-concepts
    loc: sec=h21
    h: 58f7fdd29624
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=131.r5
    h: eb5e7bb9c3fc
  review: drafted
  review_note: 'support check: partial - Backup reserve percentages and a state-of-charge maintenance
    range appear, but no explicit relation between SOC and backup reserve is stated.'
- claim_id: c8
  rel: related_to
  target: concept:depth-of-discharge
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-06-home-hub-advanced-battery-concepts
    loc: sec=h21
    h: 58f7fdd29624
  review: drafted
  review_note: 'support check: partial - Depth of discharge is shown with percentage figures, but SOC
    itself and its relation are not explicitly stated.'
---
State of charge is the amount of charge that can still be drawn from a battery, given as a percent of its nominal capacity, where 100% means full and 0% means empty. For example, if 25 Ah is taken from a 100 Ah battery, its state of charge is 75%. Inverters such as the Sunny Island work out state of charge by counting ampere-hours in and out of the battery, then correct it using full-charge detection and battery voltage. After a boost, full or equalization charge, the calculated value is reset, and an estimated error value shows how accurate the current reading is. Lithium-ion batteries that have their own battery management system send their state of charge to the inverter, and the BMS uses it to adjust charge limits. If the battery is not brought to full charge from time to time, cells can drift apart and the displayed value can stop matching the real state of charge, so periodic calibration matters. Example conservation ranges are 60% to 65% for lead-acid and 25% to 30% for lithium-ion, and backup reserve and depth of discharge settings are also expressed against state of charge. A charge controller regulates battery state of charge in most PV systems with battery storage.

<!-- review notes
- sentence 5: support check: partial - BMS-equipped batteries send SoC to the inverter, and the BMS adapts limits depending on SOC, but the passage does not say the BMS uses the sent SoC in that way beyond this.
- sentence 6: support check: partial - Passage supports approaching the upper limit periodically to stop cells drifting and to resync the displayed SOC, but it is about lithium-ion batteries and doesn't say the display stops matching otherwise.
- sentence 7: support check: partial - Conservation ranges are stated, but backup reserve and DoD being expressed against SOC is only loosely implied.
-->
