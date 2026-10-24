---
id: mit:ac-voltage-rise-limit
type: Mitigation
name: AC conductor voltage rise limiting
aliases:
- limit voltage rise to <1%
- center-tap feed
- conductor upsizing for voltage drop
- low lead resistance to AC terminals
- center-feed the branch circuit
- Center-feeding
claims:
- claim_id: c1
  attr: voltage_drop
  value:
    nominal: 0.19
    unit: unit:PERCENT
  conditions: Copper conductors, 4 parallel sets of 700 kcmil phase conductors, 30 m run in PVC conduit
    (SGI 500XT external transformer app note table)
  cite:
  - src: src:yaskawa-sgi-500xt-external-transformer-app-note
    loc: tbl=7
    h: b94bf08718f7
  - src: src:yaskawa-sgi-500xt-external-transformer-app-note
    loc: tbl=7.r2
    h: 4ea6e2b5d5af
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions)
- claim_id: c2
  attr: voltage_drop
  value:
    nominal: 0.24
    unit: unit:PERCENT
  conditions: Copper conductors, 4 parallel sets of 700 kcmil phase conductors, 30 m run in aluminum conduit
  cite:
  - src: src:yaskawa-sgi-500xt-external-transformer-app-note
    loc: tbl=7
    h: b94bf08718f7
  - src: src:yaskawa-sgi-500xt-external-transformer-app-note
    loc: tbl=7.r2
    h: 4ea6e2b5d5af
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions)
- claim_id: c3
  attr: voltage_drop
  value:
    nominal: 0.23
    unit: unit:PERCENT
  conditions: Aluminum conductors, 5 parallel sets of 700 kcmil phase conductors, 30 m run in PVC conduit
  cite:
  - src: src:yaskawa-sgi-500xt-external-transformer-app-note
    loc: tbl=8
    h: 19bec35af480
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions)
- claim_id: c4
  attr: voltage_drop
  value:
    nominal: 0.32
    unit: unit:PERCENT
  conditions: Aluminum conductors, 6 parallel sets of 500 kcmil phase conductors, 30 m run in aluminum
    conduit
  cite:
  - src: src:yaskawa-sgi-500xt-external-transformer-app-note
    loc: tbl=8
    h: 19bec35af480
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c3 (same source; check the conditions)
---
This action means sizing the AC conductors and laying out the branch circuits so the voltage rise between the inverter and the grid connection stays small. It prevents nuisance overvoltage trips caused by an undersized AC conductor. Grid-tied inverters must stop exporting when the voltage at their terminals goes above the allowed limit. Resistance in the system wiring adds to the grid voltage, so it can push an inverter over that limit. The main factors are conductor size and the distance to the point of common coupling. Too much wire resistance between the inverter and the grid can cause a repeated cycle: the inverter disconnects, reconnects after the set delay, and trips again as the voltage climbs back up. For microinverter systems, Enphase recommends keeping the total rise below 2% across all wire sections. Keeping the rise in the trunk cable below 1% is good practice. Conductor length tables give the maximum run for each wire size at a 1% rise. Center-feeding splits a branch into two sub-branches behind a single overcurrent device. In one example, the rise to the last microinverter fell from 1.32% with an end-fed circuit to 0.52% with center-feeding. Keeping the resistance of the leads to the AC terminals low also helps grid monitoring work properly. Lower conductor resistance cuts power loss and heat at the terminals and improves production. Limits: standard feeder voltage-rise guidelines may not be enough for fully populated microinverter branches. Wiring changes do not fix overvoltage that comes from high resistance in the distribution grid itself.

<!-- review notes
- sentence 7: support check: partial - Standard guidelines possibly being insufficient for fully populated branches is stated, but the passages do not say wiring changes can't fix grid-resistance overvoltage; they only name grid resistance as a separate cause.
- sentence 7: review: partial - The passages say standard guidelines may not be enough for fully populated branches, but none says wiring changes cannot fix overvoltage caused by distribution-grid resistance.
-->
