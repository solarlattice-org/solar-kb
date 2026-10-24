---
id: concept:overcurrent-protection
type: Concept
name: Overcurrent protection
aliases:
- OCPD
- overcurrent protective device
- overcurrent protection device
category: Design
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:ampacity
  note: An OCPD is not needed where conductors have enough ampacity for the highest available current;
    the OCPD rating normally should not exceed conductor ampacity.
  cite:
  - src: src:std-standards-nec-2017-nec2017-690
    loc: sec=h15
    h: 3ddeddb2f95f
  - src: src:std-standards-nec-2020-nec-2020-690
    loc: sec=h54
    h: 01989f804c87
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h22
    h: a0abbaeecc7e
  - src: src:ref-reference-short-circuit-calcs-bussman-sht-ckt-calcs-book
    loc: sec=h6
    h: 0ace453bcb69
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:busbar-rule
  note: Busbar rating checks add 125% of the source output current to the rating of the OCPD protecting
    the busbar.
  cite:
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h130
    h: 32024b578c3c
  - src: src:std-standards-nec-2020-nec-2020-705
    loc: sec=h25
    h: c63742cb1b49
  - src: src:std-standards-nec-2017-nec2017-705
    loc: sec=h9
    h: 6de44b94103f
  - src: src:std-standards-nec-2014-nec2014-705
    loc: sec=h11
    h: e729ef3b6f0f
  - src: src:ref-standards-nec-2014-solar-pv-systems-2014nec
    loc: sec=h49
    h: 0f64065acf47
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:continuous-load
  note: As a general rule, fuse or breaker ampere rating is selected at 125% of the continuous load current.
  cite:
  - src: src:ref-reference-short-circuit-calcs-bussman-sht-ckt-calcs-book
    loc: sec=h6
    h: 0ace453bcb69
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-electrical-plan-review-cooper-bussman
    loc: sec=h6
    h: 0ace453bcb69
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:arc-flash-incident-energy
  note: The protective device's clearing time at the expected arcing current is a key determinant of incident
    energy.
  cite:
  - src: src:ref-standards-nfpa-06165704-optimized-ioc-iasm-2012
    loc: sec=h5
    h: 086b216ff4ec
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:protection-coordination
  note: Upstream and downstream OCPDs may need to be selectively coordinated; zone-selective interlocking
    lets the lower-tier device clear the fault first.
  cite:
  - src: src:std-standards-states-state-ny-nyc-electrical-amendments-nyc-nec-amendments-2011
    loc: sec=h74
    h: 1a0128d8c989
  - src: src:ref-standards-nfpa-06634249-advances-in-ocpd-zsi-iast-2014
    loc: sec=h6
    h: 23fbcd0d8d68
  - src: src:eq-equip-relays-reclosers-bus-ele-tech-lib-selective-coordination-2008-spd
    loc: sec=h86
    h: 26b219c15da4
  review: drafted
- claim_id: c6
  rel: related_to
  target: func:ground-fault-protection
  note: With the improved PV ground-fault protection, a single OCPD in either the positive or the negative
    conductor gives adequate overcurrent protection.
  cite:
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h27
    h: 4230f59325bd
  - src: src:std-standards-nec-2020-nec-2020-690
    loc: sec=h58
    h: 165f8191a30b
  - src: src:std-standards-nec-2017-nec-2017-690-solar
    loc: sec=h8
    h: f17153ed396e
  review: drafted
- claim_id: c7
  rel: related_to
  target: req:nfpa-70-2017-690-9-c
  cite:
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h27
    h: 4230f59325bd
  - src: src:std-standards-nec-2017-nec2017-690
    loc: sec=h15
    h: 3ddeddb2f95f
  - src: src:std-standards-nec-2017-nec-2017-690-solar
    loc: sec=h8
    h: f17153ed396e
  review: drafted
- claim_id: c8
  rel: related_to
  target: comp:string-fuse
  note: String OCPDs must be fitted and correctly specified where used.
  cite:
  - src: src:iec-62446-1
    loc: sec=h169
    h: 6309d78dae0a
  review: drafted
  review_note: 'support check: partial - u4 says string OCPDs must be fitted and correctly specified,
    but it is an IEC TS 62548 inspection checklist item rather than an explicit link to overcurrent protection
    in general.'
- claim_id: c9
  rel: related_to
  target: comp:ac-circuit-breaker
  cite:
  - src: src:ref-reference-short-circuit-calcs-bussman-sht-ckt-calcs-book
    loc: sec=h6
    h: 0ace453bcb69
  - src: src:ref-standards-mv-committee-application-docs-overall-mv-design-electrical-plan-review-cooper-bussman
    loc: sec=h6
    h: 0ace453bcb69
  review: drafted
  review_note: 'support check: partial - The passages cover fuse and circuit breaker ratings generally
    and mention inverse-time breakers, but they never address an AC circuit breaker as a PV component.'
- claim_id: c10
  rel: related_to
  target: mit:full-rated-breaker
  note: An assembly listed for continuous operation at 100% of its rating may be used at 100% of its rating.
  cite:
  - src: src:std-standards-nec-2017-nec2017-690
    loc: sec=h15
    h: 3ddeddb2f95f
  - src: src:std-standards-nec-2017-nec-2017-690-solar
    loc: sec=h8
    h: f17153ed396e
  review: drafted
- claim_id: c11
  rel: related_to
  target: hazard:backfeed
  note: Inverters, parallel strings and storage can feed fault current back into PV circuits.
  cite:
  - src: src:iec-62446-1
    loc: sec=h169
    h: 6309d78dae0a
  - src: src:std-standards-nec-2017-nec2017-690
    loc: sec=h15
    h: 3ddeddb2f95f
  review: drafted
- claim_id: c12
  rel: related_to
  target: func:power-control-system
  cite:
  - src: src:std-standards-nec-2020-nec-2020-705
    loc: sec=h34
    h: 3594f824a3b8
  review: drafted
---
Overcurrent protection means using fuses or circuit breakers, called OCPDs, to protect conductors and equipment from excess current. In PV systems, the dc circuits and the inverter output conductors and equipment must be protected against overcurrent. An OCPD is not required when the conductors have enough ampacity for the highest current available to them. PV modules and inverter outputs can supply only limited current. Protection is needed where they connect to stronger sources such as parallel strings, batteries or the utility, and the device usually goes at that stronger-source end. OCPDs in PV dc circuits must be listed for PV use, because dc faults are much harder to interrupt than ac faults. Devices marked only for ac should not be used in dc circuits. As a general rule, an OCPD is sized at 125% of the continuous load current, and its rating normally should not exceed the ampacity of the conductors it protects. Where single OCPDs protect source or output circuits, they must all be in the same polarity. Combined with the required ground-fault protection, one device in either conductor gives adequate protection. On interconnections, the rating of the OCPD that protects a busbar is part of the 120% busbar rule. A backfed breaker must be suitable for backfeed and carry a label warning not to relocate it. How fast an OCPD clears a fault strongly affects arc flash incident energy. Upstream and downstream devices may need to be selectively coordinated.

<!-- review notes
- sentence 1: support check: partial - The passages define OCPD and discuss fuses and circuit breakers protecting conductors and equipment against overcurrent, but they give no explicit definition tying them together.
-->
