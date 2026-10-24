---
id: concept:usable-energy-capacity
type: Concept
name: Usable energy capacity
aliases:
- usable energy
- total vs usable energy
- nameplate energy capacity
- usable battery capacity
- usable capacity
category: Storage
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:depth-of-discharge
  note: Training material labels usable energy as the depth of discharge portion of total energy.
  cite:
  - src: src:se-academy-solaredge-home-battery-certification-na-technical-01-brush-up-on-solar-batteries-25-minutes
    loc: sec=h10
    h: 542359092ded
  - src: src:se-academy-home-hub-technical-essentials-na-technical-06-home-hub-advanced-battery-concepts
    loc: sec=h21
    h: 58f7fdd29624
  review: drafted
- claim_id: c2
  rel: related_to
  target: func:backup-reserve
  note: Total battery energy is split into usable energy and a reserve; a backup reserve setting holds
    back part of the energy.
  cite:
  - src: src:se-academy-solaredge-home-battery-certification-na-technical-01-brush-up-on-solar-batteries-25-minutes
    loc: sec=h10
    h: 542359092ded
  - src: src:se-academy-home-hub-technical-essentials-na-technical-06-home-hub-advanced-battery-concepts
    loc: sec=h21
    h: 58f7fdd29624
  review: drafted
  review_note: 'support check: partial - Slide shows usable energy and reserve split of total, and a Backup
    Reserve in the depth-of-discharge diagram, but doesn''t explicitly state a backup reserve setting
    holds back energy from usable energy.'
- claim_id: c3
  rel: related_to
  target: concept:state-of-health
  note: SOH is reported as the ratio of currently usable capacity to nominal or rated capacity, in percent.
  cite:
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=88.r11
    h: d833df8e1e41
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=177.r23
    h: b07b6d40acaa
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:self-consumption
  note: Usable battery capacity is an input when estimating the self-consumption quota; more usable energy
    raises self-consumption in the SMA example.
  cite:
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: sec=h14
    h: f98cd5c3ad07
  - src: src:sma-doc-259463
    loc: sec=h17
    h: 09f6a5e9232e
  review: drafted
- claim_id: c5
  rel: related_to
  target: comp:battery-storage
  cite:
  - src: src:se-academy-solaredge-home-battery-certification-na-technical-01-brush-up-on-solar-batteries-25-minutes
    loc: sec=h10
    h: 542359092ded
  - src: src:sma-doc-260329
    loc: sec=1.1
    h: 7630c9d1dfa8
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: fig=55
    h: 69258e8757c9
  review: drafted
---
Usable energy capacity is the part of a battery's total stored energy that the system can actually draw on. The rest is held back as a reserve. Training material equates usable energy with depth of discharge. A backup reserve and a minimum state of energy set how much charge stays unused in daily cycling. For the SolarEdge Home Battery, the material shows 90% as usable and an example backup reserve of 20%. SolarEdge says the battery offers full depth of discharge, without the 5% manufacturer reserve that other batteries keep. In an SMA planning example, a battery with 10000 Wh total capacity has 50% used by the Sunny Island for storing PV energy, which gives 5000 Wh of usable capacity. A new battery's usable capacity matches its nominal capacity for a ten-hour discharge (C10). It falls as the battery ages, and state of health is reported as the ratio of currently usable capacity to nominal capacity. Usable capacity also depends on temperature: it drops noticeably at 20°C and below, and SMA battery management reduces it by 1% per °C starting at 20°C. Usable energy matters for system design because more of it raises self-consumption. In the SMA example, the self-consumption quota rises from 30% to typically 65%.

<!-- review notes
- sentence 2: support check: partial - Usable energy is labeled depth of discharge, and backup reserve and minimum state of energy appear in the diagram, but the claim that they set unused charge is only implied.
- sentence 3: support check: partial - The 90% usable, 20% backup reserve and full-depth-of-discharge/5% reserve note are present, but 'example' is not stated and the 20% is labeled 'actual'.
-->
