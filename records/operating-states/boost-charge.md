---
id: state:boost-charge
type: OperatingState
name: Boost charge
aliases:
- absorption phase
- boost charging
- Fast charge
- Boost
category: Storage
claims:
- claim_id: c1
  rel: subclass_of
  target: state:battery-charging
  note: Boost charge is one of the charging processes battery management selects for the constant voltage
    phase.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h20
    h: f3711be6fb20
  - src: src:sma-doc-260329
    loc: sec=2.2
    h: e012c72d98e3
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
Boost charge is a battery charging process in which the Sunny Island applies a high charging voltage so the battery reaches roughly 85% to 90% of its usable capacity quickly. It is the most common Sunny Island charging process. Battery management picks it, or a full or equalization charge, when charging moves into the constant voltage phase. During this constant voltage (absorption) phase the charging voltage stays fixed and the charging current falls steadily. With flooded lead-acid batteries, boost charge is meant to make the battery gas so the electrolyte is mixed and balanced again. Because it charges at a high voltage over a short time, it also keeps a generator heavily loaded. The parameter BatChrgOp shows Boost (1) while this process is active. The change into boost charge is logged as event 9320 or shown as display entry E204. Set the boost charging voltage (ChrgVtgBoost) and the absorption time (AptTmBoost) to match the battery maker's recommendations. The default cell voltage is 2.40 V and the default absorption time for flooded batteries is 90 min. A multifunction relay set to AptPhs switches while the battery charge is in the absorption phase.

<!-- review notes
- sentence 3: support check: partial - Passage says constant voltage and decreasing current, but not explicitly that this is the boost charge's phase, nor 'steadily'; mostly fine, though linking absorption to boost is via the AptTmBoost/u13.
- sentence 4: support check: partial - Gassing and compensating electrolytes for FLA, and high generator workload are stated; 'mixed and balanced' is a paraphrase of compensating, and generator workload claim is stated, but 'keeps a generator heavily loaded' is fine; minor interpretive detail.
- sentence 5: support check: partial - BatChrgOp Boost (1) and event 9320 are supported, and E204 is a state change entry for boost charge, but 'while active' and 'or' mapping are mostly fine; the display entry is described as state change, supported.
-->
