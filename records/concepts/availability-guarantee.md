---
id: concept:availability-guarantee
type: Concept
name: Availability guarantee
aliases:
- liquidated damages
- performance guarantee
- Guaranteed Plant Availability
- GAV
- Minimum Guaranteed Availability
- Minimum Guaranteed Contractual Availability
category: Market
concept_kind: finance
claims:
- claim_id: c1
  rel: part_of
  target: concept:om-contract
  note: The O&M service provider gives the availability guarantee as part of the O&M contract.
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h35
    h: 5b31b4569f26
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=10.5.1
    h: a644ef13b2dc
  - src: src:solarpower-europe-om-guidelines
    loc: sec=10.5.1
    h: 6b3fb1a2164f
  review: drafted
- claim_id: c2
  rel: related_to
  target: metric:availability
  note: The guarantee is checked against contractual availability, which is calculated per inverter on
    an annual basis.
  cite:
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=11.5
    h: 0b08574c4ed8
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=10.5.1
    h: a644ef13b2dc
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h35
    h: 5b31b4569f26
  review: drafted
- claim_id: c3
  rel: related_to
  target: metric:energy-based-availability
  note: Energy-based availability is often used in the availability guarantee chapter of an O&M contract.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=10.5.3
    h: 84ef0f2bedff
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h35
    h: 5b31b4569f26
  review: drafted
- claim_id: c4
  rel: related_to
  target: metric:performance-ratio
  note: Best practice is to use a guaranteed performance ratio and a guaranteed availability together
    in O&M contracts.
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h35
    h: 5b31b4569f26
  - src: src:trn-oandm-nrel-best-practices-for-om-of-photovoltaic-and-ess
    loc: sec=h138
    h: aaba3e07db26
  review: drafted
- claim_id: c5
  rel: related_to
  target: std:solarpower-europe-om-guidelines
  note: Section 11.5 of these guidelines covers availability guarantees.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=11.5
    h: 10f2d9c59257
  - src: src:solarpower-europe-om-guidelines
    loc: sec=10.5.1
    h: 6b3fb1a2164f
  review: drafted
- claim_id: c6
  rel: related_to
  target: org:sandia
  note: Sandia published a best-practice report on writing availability guarantee language for PV O&M
    agreements.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h215
    h: 83b8e8c7c265
  review: drafted
- claim_id: c7
  attr: degradation_rate
  value:
    nominal: 0.5
    unit: unit:PERCENT-PER-YR
  conditions: Assumed module degradation from the previous year in an example table of expected performance
    ratio and availability for a commercial system performance guarantee
  cite:
  - src: src:trn-oandm-nrel-best-practices-for-om-of-photovoltaic-and-ess
    loc: sec=h138
    h: aaba3e07db26
  - src: src:trn-oandm-nrel-best-practices-for-om-of-photovoltaic-and-ess
    loc: tbl=25.r3
    h: fd73ee0c1fe7
  review: drafted
---
An availability guarantee is a promise in an O&M contract that the PV plant will be available for at least a minimum share of the time, or of the energy it could produce. After the guaranteed performance ratio, guaranteed plant availability is the most common guarantee in solar O&M contracts, and best practice is to use both together. SolarPower Europe recommends a minimum guaranteed contractual availability of 98% over a year, measured at least at the inverter level. Where full-time staff must be on site, as in Mexico, 99% can be offered. The IEA PVPS guidance says most guidelines set guaranteed plant availability at 99% or higher, because the grid side is outside the operator's control. Contractual availability excludes downtime the O&M provider is not responsible for, such as force majeure, grid operator curtailment and grid instability. Failure time starts only when the provider receives the error message. Availability can be measured by time, using inverter data above an irradiance threshold, or by energy. The energy-based method counts the lost energy, so an outage in strong sun weighs more. If measured availability falls below the guarantee, the provider repays the lost revenue as liquidated damages. If it exceeds the guarantee, a bonus scheme splits the extra revenue between owner and provider. Yearly liquidated damages should be capped at 100% of the annual O&M fee. Reaching the cap usually gives the right to terminate the contract.

<!-- review notes
- sentence 4: support check: partial - The 99% or higher recommendation and the grid being beyond operator control are in the passages, but the passages do not say the grid is the reason for the 99% level, and the IEA PVPS attribution is not stated.
- sentence 7: support check: partial - The bonus split is stated, but the LD condition is garbled as 'Minimum Guaranteed Availability is less than measured', which is the reverse of the statement's below-guarantee trigger. The surrounding text implies compensation for lower-than-guaranteed availability.
-->
