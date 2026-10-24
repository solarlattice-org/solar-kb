---
id: prod:enphase-iq-battery
type: Product
name: Enphase IQ Battery
aliases:
- Encharge
- IQ Battery 10C
- IQ Battery 5P
- IQ Battery 10T
- IQ Battery 10
- IQ Battery 3
category: Storage
make: enphase
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:enphase
  cite:
  - src: src:kb-enphase-what-are-the-generator-modes-in-the-enphase-app
    loc: sec=front
    h: fac698aa11d5
  - src: src:kb-enphase-how-does-my-enphase-energy-system-work
    loc: sec=front
    h: ac87a8ce03f9
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:battery-storage
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  - src: src:enphase-enphase-nec-2017-2020-2023-code-compliance
    loc: sec=h3
    h: cae8b3425bad
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: arch:ac-coupled-storage
  note: Described as an all-in-one AC-coupled storage system.
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=4.r4
    h: 137418b51b89
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: tbl=3.r4
    h: 1847fea2e46c
  - src: src:enphase-enphase-nec-2017-2020-2023-code-compliance
    loc: sec=h3
    h: cae8b3425bad
  review: drafted
- claim_id: c4
  rel: implements
  target: func:grid-forming
  note: Includes embedded grid-forming multimode microinverters.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  - src: src:enphase-enphase-nec-2017-2020-2023-code-compliance
    loc: sec=h3
    h: cae8b3425bad
  review: drafted
- claim_id: c5
  rel: implements
  target: func:backup-power
  note: Multiple units can be connected to increase home backup; capacity can be added incrementally.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:enphase-iq-gateway
  note: The gateway communicates with IQ Batteries; the battery LED flashes yellow while establishing
    communication with the gateway.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  - src: src:enphase-enphase-troubleshooting-energy-systems-with-iq-battery-5p
    loc: tbl=8
    h: 842c902f0053
  review: drafted
- claim_id: c7
  rel: compatible_with
  target: prod:enphase-iq-system-controller
  note: System controller allows the batteries to form an intentional island; IQ System Controller 3 supports
    IQ Battery 5P oversubscription.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  - src: src:enphase-enphase-troubleshooting-energy-systems-with-iq-battery-5p
    loc: sec=h9
    h: a1f63938aa25
  review: drafted
- claim_id: c8
  rel: compatible_with
  target: prod:enphase-iq-combiner
  note: Communication Kit installed in the IQ Combiner enables wireless communication with the battery.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c9
  rel: compatible_with
  target: prod:enphase-iq8
  conditions: PV solar + storage configurations of the Enphase Energy System
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c10
  rel: requires
  target: role:installer
  note: Commissioning or servicing requires Enphase IQ Battery Installer and Design certifications held
    by at least one person in the company.
  cite:
  - src: src:enphase-enphase-storage-3-3t-10-10t-troubleshooting-guide
    loc: sec=h46
    h: 1df83baa9c83
  review: drafted
- claim_id: c11
  attr: warranty_term
  value:
    nominal: 5
    unit: unit:YR
  conditions: Limited warranty extension offered for IQ Battery
  cite:
  - src: src:kb-enphase-how-do-i-transfer-ownership-of-an-enphase-system
    loc: sec=front
    h: ec67e8feb541
  review: drafted
  review_note: 'support check: partial - Evidence only lists a 5-Year Limited Warranty Extension in model
    names; it doesn''t state a warranty term for the battery explicitly.'
---
The Enphase IQ Battery, formerly called Encharge, is an all-in-one AC-coupled storage family with built-in grid-forming multimode microinverters. The family includes the IQ Battery 10C, the IQ Battery 5P and the IQ Battery 3/3T/10/10T. You can connect several batteries to extend home backup, and you can add capacity a step at a time. If the gateway loses contact with the system controller or the battery for more than one hour, the unit falls back to grid-tied operation. Lost AC voltage at the battery or too little sunlight can also stop it from charging or discharging. The LED shows the battery state: solid blue or green means idle, slow flashing blue means discharging, slow flashing green means charging, and rapid flashing yellow means starting up or connecting to the gateway. Only certified installers may commission or service these systems. At least one person in the company must hold the IQ Battery Installer certification and one the IQ Battery Design certification. The IQ Battery CT goes on battery L2 only, and its embossed arrow must point toward the IQ System Controller lugs.
