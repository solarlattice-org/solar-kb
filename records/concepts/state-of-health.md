---
id: concept:state-of-health
type: Concept
name: State of health
aliases:
- SoH
- SOH
category: Storage
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:state-of-charge
  note: Battery manuals cover SOC and SOH together as paired battery management values.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=5.r3
    h: 24a4f6262fc2
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=13.4
    h: 839cbe18cf85
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:battery-storage
  note: SOH refers to the battery or energy storage device and reports its remaining life.
  cite:
  - src: src:eq-equip-inverters-power-electronics-software-powersupervisor-en
    loc: tbl=5.r2
    h: 169ad1fcfb27
  - src: src:eq-equip-das-alsoenergy-hardware-cut-sheets-phoenix-pwr-supp-1314669-en-sg-power-supplies-lores
    loc: sec=h185
    h: 93089d1426c9
  review: drafted
- claim_id: c3
  rel: related_to
  target: symptom:low-battery-health
  note: An SMA battery error is reported when current battery capacity (SOH) falls below 70%.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h914
    h: cef6dae20c1d
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  rel: related_to
  target: meas:battery-soh-reading-low
  cite:
  - src: src:sma-doc-278742
    loc: sec=h914
    h: cef6dae20c1d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: related_to
  target: method:battery-capacity-test
  note: A more accurate SOH needs a capacity measurement, e.g. per DIN EN 60896, by qualified persons
    with special equipment.
  cite:
  - src: src:sma-doc-260329
    loc: sec=1.3
    h: 625cc005a741
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:lead-acid-battery
  note: Sunny Island SOH learning only works with cycled operation of a lead-acid battery plus recurring
    idle phases.
  cite:
  - src: src:sma-doc-260329
    loc: sec=1.3
    h: 625cc005a741
  review: drafted
---
State of health (SOH) describes how much of its original capability a battery still has, comparing its present condition with its condition when new. It is usually given as a percentage: the battery's current usable capacity divided by its nominal capacity. Battery management uses SOH to report how much life the storage device has left and to give early warning of failures. On a Sunny Island, SOH starts at 100% after commissioning, based on the nominal capacity that was set. The value is then refined during operation, but only with cycled lead-acid operation and regular idle periods. A loss of a few percent per year or per 100 cycles is normal aging. A drop of several tens of percent in the first months points to a possible fault, and an SOH that stays at 100% means the system cannot learn it. The inverter's SOH estimate is only accurate to about plus or minus 15 percent, so an accurate value needs a proper battery capacity test with special measuring equipment. Some SMA devices report a battery error when SOH falls below 70%. SOH is normally shown next to state of charge (SOC) in battery menus.

<!-- review notes
- sentence 7: support check: partial - The 70% battery error is stated and SOC/SOH are paired in a section heading, but 'normally shown next to SOC in battery menus' and 'some SMA devices' are only loosely supported.
- sentence 7: review: partial - The battery error below 70% SOH is stated, but the passages only pair SOC and SOH in a section heading and do not say SOH is normally shown next to SOC in battery menus.
-->
