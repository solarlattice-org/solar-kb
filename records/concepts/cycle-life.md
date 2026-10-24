---
id: concept:cycle-life
type: Concept
name: Cycle life
aliases:
- full cycles
- end-of-life capacity
- cycle count
- Cycle stability
category: Storage
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:depth-of-discharge
  note: Manufacturers often state cycle life as a function of depth of discharge.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h153
    h: c702807d918b
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:lead-acid-battery
  note: Lead-acid batteries typically last 1,000 or 2,000 cycles. Long periods at low state of charge
    cause irreversible damage.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h153
    h: c702807d918b
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:lithium-ion-battery
  note: Research on new material systems such as lithium-ion targets 10,000 cycles.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h153
    h: c702807d918b
  review: drafted
- claim_id: c4
  rel: related_to
  target: method:battery-capacity-test
  note: A charge/discharge test measures actual capacity, but battery operation must stop while the test
    runs.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h153
    h: c702807d918b
  review: drafted
  review_note: 'support check: partial - The passage says a charge/discharge test measures actual capacity
    and interrupts operation, and it offers an alternative measure of cycle life. It does not directly
    tie that test to cycle life as the statement does.'
- claim_id: c5
  rel: related_to
  target: concept:state-of-charge
  note: Time spent at a low state of charge damages lead-acid batteries.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h153
    h: c702807d918b
  review: drafted
- claim_id: c6
  rel: related_to
  target: comp:battery-storage
  note: Battery system specifications usually state the capacity required at end of life, not the capacity
    when new.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h153
    h: c702807d918b
  review: drafted
---
Cycle life, which SMA documents call cycle stability, describes how long a battery will last. It is the number of times the battery can be charged and discharged before its available capacity drops below a set value given by the manufacturer. Batteries lose capacity and efficiency with age and with the energy that passes in and out of them. The loss starts even before the battery is installed. Manufacturers often give cycle life as a function of depth of discharge. Lead-acid batteries typically reach 1,000 or 2,000 cycles, and research on newer chemistries such as lithium-ion aims for 10,000 cycles. End of life depends on how the battery is used. Where reliability matters, a cell at 80% capacity after 1,000 cycles would likely be replaced. In less demanding uses, it might keep running to around 2,000 cycles and 60% capacity. Cycle life can also be based on internal resistance: the number of cycles before resistance rises by a set factor, such as 1.3 times the initial value. This avoids taking the battery out of service for a capacity test. Battery systems are usually specified by the capacity they must still have at end of life, not their capacity when new. This matters when sizing storage and judging when to replace it.

<!-- review notes
- sentence 1: support check: partial - The SMA text defines cycle stability as the number of charge/discharge cycles before capacity falls below a manufacturer-specified value. Nothing in the passages equates cycle stability with the term cycle life.
- sentence 5: support check: partial - The resistance-based definition with the 1.3 times example is stated. The passage does not say that this avoids taking the battery out of service, though it is implied by the contrast with the capacity test.
- sentence 6: support check: partial - Specifying end-of-life capacity is stated. The claim that this matters for sizing and for judging replacement is not stated.
-->
