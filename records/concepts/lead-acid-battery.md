---
id: concept:lead-acid-battery
type: Concept
name: Lead-acid battery
aliases:
- FLA
- VRLA
- AGM
- gel battery
- flooded lead-acid
- Flooded lead-acid battery
- Vented (flooded) lead acid
- Valve Regulated Lead Acid
- Sealed Lead-Acid Battery
- SLA
- AGM Battery
- Gel batteries
category: Storage
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:lithium-ion-battery
  note: SMA battery inverters offer lead-acid (FLA, VRLA) or lithium-ion as alternative battery type settings.
  cite:
  - src: src:sma-doc-259761
    loc: tbl=84.r6
    h: c6683e875c06
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=85
    h: 7520405a2919
  - src: src:sma-doc-278742
    loc: tbl=87.r3
    h: bcd98df7f444
  - src: src:sma-doc-259761
    loc: tbl=45
    h: 5e488f822451
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:nickel-cadmium-battery
  note: Listed alongside FLA and VRLA as a selectable battery type.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=40
    h: daa5da0df125
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=158.r25
    h: ebcc391e8d61
  review: drafted
- claim_id: c3
  rel: related_to
  target: prod:sma-sunny-island
  note: Supports FLA and VRLA lead-acid batteries with integrated battery management.
  cite:
  - src: src:sma-doc-259761
    loc: tbl=84.r6
    h: c6683e875c06
  - src: src:sma-doc-278742
    loc: tbl=87.r3
    h: bcd98df7f444
  - src: src:sma-doc-278303
    loc: sec=h8
    h: 8e08e205856e
  review: drafted
- claim_id: c4
  rel: related_to
  target: prod:sma-sunny-home-manager
  note: Offers optimized discharge of lead-acid batteries using load profile and PV yield forecast.
  cite:
  - src: src:sma-doc-246498
    loc: tbl=15.r1
    h: 133e20e3743a
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:state-of-charge
  note: Extended low state of charge causes sulfation; deep discharge area for lead-acid is defined separately
    from lithium-ion.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h154
    h: bbb8a4584c8e
  - src: src:sma-doc-278303
    loc: sec=h8
    h: 8e08e205856e
  - src: src:sma-doc-259761
    loc: tbl=45
    h: 5e488f822451
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:battery-charging-stages
  note: Charging parameters must be matched to the manufacturer's recommendations; charge regulation voltage
    differs by lead-acid type.
  cite:
  - src: src:sma-doc-278303
    loc: sec=h8
    h: 8e08e205856e
  - src: src:sma-doc-278742
    loc: sec=7.6.2
    h: bcc826ed8451
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: tbl=7.r2
    h: 0cfbb82f90bc
  review: drafted
- claim_id: c7
  rel: related_to
  target: fm:battery-sulfation
  note: Crystallized sulfation permanently reduces capacity and efficiency and can swell or break the
    battery jar.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h154
    h: bbb8a4584c8e
  review: drafted
- claim_id: c8
  rel: related_to
  target: hazard:battery-vented-gas
  note: Hydrogen and oxygen are generated whenever lead-acid batteries are charged.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h641
    h: 869a64288aba
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h617
    h: 8784572c2a3d
  review: drafted
- claim_id: c9
  rel: related_to
  target: hazard:battery-electrolyte
  note: Electrolyte is a mixture of water and sulfuric acid.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h641
    h: 869a64288aba
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h617
    h: 8784572c2a3d
  review: drafted
- claim_id: c10
  rel: related_to
  target: mit:battery-watering
  note: Watering applies to flooded lead-acid batteries only, at manufacturer intervals.
  cite:
  - src: src:trn-oandm-nrel-best-practices-for-om-of-photovoltaic-and-ess
    loc: tbl=33.r11
    h: 7ad1c3db5aa5
  review: drafted
---
A lead-acid battery is a storage battery used with battery inverters such as the Sunny Island, where it is selected as either flooded (FLA) or valve-regulated (VRLA) type instead of lithium-ion. A flooded lead-acid battery has a liquid electrolyte, while a VRLA battery has its electrolyte immobilized either in a gel or in an absorbent glass mat (AGM). The electrolyte is water mixed with sulfuric acid, and charging always produces hydrogen and oxygen gas. In sealed types this gas recombines into water inside the battery, so they rarely need topping up with water. AGM batteries usually handle high currents well but hold up poorly to repeated deep discharge, while some gel batteries are built to tolerate very deep discharge cycling. Flooded batteries need periodic watering at the interval the manufacturer specifies. If the battery sits at a low state of charge for a long time, sulfation sets in. It can be reversed only by periodic full charges, and once it crystallizes it permanently cuts capacity and can crack the battery jar. The inverter's battery management handles careful charging, deep discharge prevention and state-of-charge estimation, but its parameters must be set to the battery manufacturer's recommendations. Spent lead-acid batteries have a well-established recycling industry, because lead is toxic and regulated and the batteries are used widely in other industries.

<!-- review notes
- sentence 6: support check: partial - Passage says low SOC failure is avoided by periodic full charge and amorphous sulfation is recoverable, but 'reversed only by periodic full charges' slightly overstates; the passage says avoided, not reversed.
-->
