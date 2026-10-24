---
id: concept:depth-of-discharge
type: Concept
name: Depth of discharge
aliases:
- DoD
category: Storage
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:state-of-charge
  note: State of charge and depth of discharge add up to 100 percent.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=2.4
    h: bf405ed38474
  review: drafted
- claim_id: c2
  rel: explains
  target: concept:cycle-life
  note: Battery longevity depends mainly on DoD, cycle count, time at each state of charge and temperature.
    Shallower average daily DoD usually gives longer battery life.
  cite:
  - src: src:trn-oandm-nrel-best-practices-for-om-of-photovoltaic-and-ess
    loc: sec=6.1.2.2
    h: ac0d1e3c273d
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h57
    h: bbcce193db6f
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=2.4
    h: bf405ed38474
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c3
  rel: related_to
  target: comp:charge-controller
  note: The controller's low-voltage disconnect set point sets the maximum battery DoD at a given discharge
    rate.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h58
    h: 2aefb8692fb9
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:lead-acid-battery
  note: Limiting the allowable DoD protects lead-acid batteries from freezing. A lead-acid LVD of 1.85
    to 1.91 VPC corresponds to a DoD of 70 to 80%.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=2.4
    h: bf405ed38474
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h58
    h: 2aefb8692fb9
  review: drafted
  review_note: 'review: partial - The passages support both the freezing protection and the 1.85-1.91
    VPC to 70-80% DoD figure, but the note drops the source''s limit that this holds only at discharge
    rates of C/20 and lower.'
- claim_id: c5
  rel: related_to
  target: concept:usable-energy-capacity
  note: The allowable DoD sets how much of the nominal capacity can be used.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h57
    h: bbcce193db6f
  - src: src:se-academy-home-hub-technical-essentials-na-technical-06-home-hub-advanced-battery-concepts
    loc: sec=h21
    h: 58f7fdd29624
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: related_to
  target: func:backup-reserve
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-06-home-hub-advanced-battery-concepts
    loc: sec=h21
    h: 58f7fdd29624
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - The u3 figure shows depth of discharge diagram with backup reserve
    and minimum state of energy, but no explicit relation is stated.'
---
Depth of discharge (DoD) is the percentage of a battery's capacity that has been taken out, measured against the fully charged state. DoD and state of charge always add up to 100 percent. For example, a battery discharged once a day down to 65% of its capacity has a DoD of 35%. The allowable DoD is the deepest discharge permitted in operation. For deep-cycle batteries it is usually held to no more than 75 to 80%, and it must also be limited to keep lead-acid batteries from freezing in very cold conditions. Charge controllers and battery-based inverters enforce the DoD limit with a low-voltage disconnect set point. For a typical lead-acid cell, an LVD of 1.85 to 1.91 volts per cell corresponds to a DoD of 70 to 80% at discharge rates of C/20 and lower. Battery life depends mainly on DoD, cycle count, time spent at each state of charge, and temperature. The link between DoD and life is non-linear, and a shallower daily DoD usually means a longer life. Together with battery capacity and daily load, the allowable DoD sets the days of autonomy for off-grid designs. For example, a 400 Ah bank used to 75% DoD gives 300 Ah of usable capacity. Monitoring systems and set points should keep the battery above its minimum state of charge. Some products, such as the SolarEdge Home Battery, claim full DoD with no 5% manufacturer energy reserve, and also offer a backup reserve setting.

<!-- review notes
- sentence 7: support check: partial - Monitoring/set points avoiding minimum SOC and the SolarEdge no 5% reserve claim are stated, but the 'offers a backup reserve setting' is only implied by the diagram.
-->
