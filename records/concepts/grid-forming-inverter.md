---
id: concept:grid-forming-inverter
type: Concept
name: Grid-forming inverter
aliases:
- grid-forming
- voltage source mode
- Grid-Forming mode
- Grid-Forming (Islanding) Mode
category: Grid
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:grid-following-inverter
  note: Grid-following operation needs an external voltage and frequency source and faults when it is
    lost. Grid-forming operation acts as a standalone voltage-frequency source. It reaches power commands
    more slowly but responds much faster to voltage and frequency changes.
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.1.2
    h: fc2b174a8b7d
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=2.4.2
    h: 46138d6d5564
  review: drafted
- claim_id: c2
  rel: related_to
  target: func:grid-forming
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.1.2
    h: fc2b174a8b7d
  - src: src:kb-enphase-does-the-grid-forming-feature-work-for-both-240-v-and-208-v-ac-grid-interconnec
    loc: sec=h1
    h: fadcdb955784
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=2.4.2
    h: 46138d6d5564
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c3
  rel: related_to
  target: func:inertial-response
  scope:
    products:
    - prod:tesla-megapack-platform
  note: Grid-forming can be enabled while on-grid to add virtual inertia.
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=2.4.2
    h: 46138d6d5564
  review: drafted
- claim_id: c4
  rel: related_to
  target: state:island-operation
  note: Grid-forming can be used off-grid (islanded) and for backup when the grid is absent.
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=2.4.2
    h: 46138d6d5564
  - src: src:eq-equip-bess-tesla-tesla-powerpack2-site-design-manual
    loc: sec=h52
    h: 91e513559c55
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=4.4.3
    h: 5b712bf9cb1a
  review: drafted
- claim_id: c5
  rel: related_to
  target: arch:off-grid-system
  cite:
  - src: src:eq-equip-bess-tesla-megapack-2-design-and-installation-manual
    loc: fig=100
    h: dbd1a8796635
  - src: src:tesla-megapack-2-xl-design-and-installation-manual
    loc: fig=106
    h: 1913bff08668
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=4.5.1
    h: c7f644ba07e5
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=4.4.3
    h: 5b712bf9cb1a
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: related_to
  target: func:frequency-watt
  scope:
    products:
    - prod:solis-s6-eh2p-l-us
    applications:
    - backup
    - off-grid
  note: When the hybrid inverter is grid-forming, it shifts frequency to curtail AC-coupled PV on its
    Smart Port once DC PV has been curtailed to zero.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=4.4.3
    h: 5b712bf9cb1a
  review: drafted
- claim_id: c7
  rel: related_to
  target: arch:ac-coupled-storage
  scope:
    products:
    - prod:solis-s6-eh2p-l-us
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=4.4.3
    h: 5b712bf9cb1a
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: related_to
  target: prod:enphase-iq8
  note: Only IQ8 variants for 240 V AC interconnection support grid forming; IQ8 H-208 does not.
  cite:
  - src: src:kb-enphase-does-the-grid-forming-feature-work-for-both-240-v-and-208-v-ac-grid-interconnec
    loc: sec=h1
    h: fadcdb955784
  review: drafted
- claim_id: c9
  rel: related_to
  target: prod:tesla-megapack-platform
  note: Grid forming is only available on systems designed for it and must be enabled by Tesla at commissioning.
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.1.2
    h: fc2b174a8b7d
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=2.4.2
    h: 46138d6d5564
  review: drafted
- claim_id: c10
  rel: related_to
  target: func:black-start
  note: Grid-forming systems can operate on grids that have no conventional generation and no other inverter
    sources.
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.1.2
    h: fc2b174a8b7d
  review: drafted
  review_note: 'support check: partial - u2 supports operation on grids without conventional generation
    or other inverter sources, but black start is never mentioned.; review: partial - The note about running
    on grids with no conventional generation and no other inverter sources is stated, but the passage
    never mentions black start.'
---
A grid-forming inverter acts as its own voltage and frequency source, so it can run without any other source setting the grid. A grid-following inverter is different: it needs an outside voltage and frequency reference and faults when that reference is lost. In grid-forming mode the inverter still follows real and reactive power commands, but it also tracks voltage and frequency setpoints. It reacts within a fraction of a cycle to hold them at its AC terminals. Because the mode resists sudden changes, it reaches power commands more slowly than grid-following mode. In exchange, it responds much faster to voltage and frequency disturbances. The industry uses two main approaches, machine-based and droop-based. Grid forming can be used off-grid, as backup during an outage, or on-grid to add virtual inertia. In a hybrid system that is grid-forming on PV alone, loads must stay below the available PV power. Otherwise the inverter trips on overload, and repeated trips can require a manual hard reset. Support depends on the product. Enphase supports grid forming only on 240 V IQ8 variants, not on the IQ8 H-208 or IQ8 Commercial systems.

<!-- review notes
- sentence 5: support check: partial - Two approaches and on/off-grid with virtual inertia are stated, but backup during an outage appears only for the Solis product, though u15 does support backup generally.
- sentence 7: review: partial - The 240 V-only support and the lack of grid forming on IQ8 H-208 are stated, but the Commercial passage only says IQ8 Commercial would be grid-tied only 'upon release Spring 2023', and the sentence drops that time limit.
-->
