---
id: concept:power-vs-energy
type: Concept
name: Power vs energy
aliases:
- kW vs kWh
- Energy vs. Power
- Power vs. Capacity
category: Storage
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:demand-charge
  note: Demand is an average rate of energy use over an interval, given in kW. The peak demand value sets
    the demand charge on the utility bill.
  cite:
  - src: src:eq-equip-meters-shark-shark-200-shark-200-data-logging-power-and-energy-meter-user-manual-e149701
    loc: sec=h18
    h: 49058d2525cb
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:usable-energy-capacity
  note: A battery's capacity is an energy quantity, while its power rating is the most it can deliver
    at any instant. Capacity is further split into total energy and usable energy.
  cite:
  - src: src:se-academy-solaredge-home-battery-certification-na-technical-01-brush-up-on-solar-batteries-25-minutes
    loc: sec=h10
    h: 542359092ded
  - src: src:se-academy-solaredge-home-battery-certification-na-technical-01-brush-up-on-solar-batteries-25-minutes
    loc: sec=h2
    h: 8b053f2708dd
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:depth-of-discharge
  note: Usable energy is shown as the depth of discharge, with a reserve held back from the total energy.
  cite:
  - src: src:se-academy-solaredge-home-battery-certification-na-technical-01-brush-up-on-solar-batteries-25-minutes
    loc: sec=h10
    h: 542359092ded
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:nameplate-rating
  note: Plant size is usually given as maximum power capacity in kW or MW, not as energy.
  cite:
  - src: src:trn-training-very-basics-of-pv-lesson-1
    loc: sec=h14
    h: '6313e1495776'
  review: drafted
  review_note: 'support check: partial - Plant size is stated as maximum power capacity in MW, but kW
    and ''not as energy'' are not explicitly stated, and nameplate rating isn''t named.'
---
Power is the rate at which an electric circuit transfers electrical energy. Its unit is the watt, which equals one joule per second, and 1,000 watts is one kilowatt (kW). Energy is power added up over a period of time. It is usually measured in kilowatt-hours (kWh), and one kWh equals a steady load of one kilowatt running for one hour. A meter shows power as an instantaneous reading of the watts flowing right now, though many digital meters calculate it over about one second. Energy, by contrast, always covers a defined span of time. For example, a 4,000 watt load running for one hour uses four kWh. The same load running for 15 minutes uses one kWh. In solar, kW usually describes the size or output of a system, and a plant is rated by its maximum power output. kWh describes how much energy a home or device uses, and electricity is billed by the kWh. A battery has two separate ratings. Its power rating is the most it can deliver at any instant, and its capacity is the energy it can store. Capacity is then split into total energy and usable energy, which depends on depth of discharge and reserve. Demand is also given in kW, but it is not instantaneous power. It is the average rate of energy use over an interval, and the peak demand sets the demand charge on the utility bill.

<!-- review notes
- sentence 6: support check: partial - Power rating and capacity and total vs usable energy with depth of discharge and reserve are shown, but the slide text says capacity is 'power stored' and doesn't state capacity is split or that usable depends on them explicitly.
-->
