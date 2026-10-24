---
id: concept:islanding
type: Concept
name: Islanding
aliases:
- unintentional island
- intentional island
- island
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: func:anti-islanding
  note: PV inverters carry island detection (anti-islanding) schemes to prevent unintentional islands.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.3.5.8
    h: 0943b61c4b74
  - src: src:ref-reference-sandia-islanding-risk
    loc: sec=h10
    h: 5d1ecbddde3c
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:anti-islanding-detection-methods
  note: Loss-of-mains detection is grouped into passive, active and communications-based methods.
  cite:
  - src: src:ref-reference-sandia-islanding-risk
    loc: sec=h10
    h: 5d1ecbddde3c
  review: drafted
- claim_id: c3
  rel: related_to
  target: std:iec-62116
  note: Requires detection of an unintentional island and cessation of energization within 2 s.
  cite:
  - src: src:ref-reference-sandia-islanding-risk
    loc: sec=h10
    h: 5d1ecbddde3c
  review: drafted
- claim_id: c4
  rel: related_to
  target: std:ul-1741
  note: Islanding detection capability of compliant inverters is certified using an RLC test circuit.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.3.5.8
    h: 0943b61c4b74
  - src: src:ref-reference-sandia-islanding-risk
    loc: sec=h10
    h: 5d1ecbddde3c
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:cease-to-energize
  cite:
  - src: src:std-standards-ieee-ieee1547
    loc: sec=4.4.1
    h: e9bda8b61b00
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=8.1.1
    h: cca227a468ff
  - src: src:ref-reference-sandia-islanding-risk
    loc: sec=h10
    h: 5d1ecbddde3c
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:area-eps
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=8.2.1
    h: b6740cdf0da7
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=8.1.1
    h: cca227a468ff
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:automatic-reclosing
  note: Auto-reclose times longer than 2 s may be considered to coordinate with islanding detection.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=8.2.1
    h: b6740cdf0da7
  review: drafted
- claim_id: c8
  rel: related_to
  target: func:low-voltage-ride-through
  note: Ride-through means low voltage can no longer serve for island detection, raising unintentional-island
    likelihood.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.3.5.8
    h: 0943b61c4b74
  - src: src:ref-reference-sandia-islanding-risk
    loc: sec=h12
    h: 90c8cb694971
  review: drafted
- claim_id: c9
  rel: related_to
  target: hazard:backfeed
  note: An island can endanger utility workers and connected equipment.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=2.5.7
    h: 5d2888f1abf9
  - src: src:ref-reference-sandia-islanding-risk
    loc: sec=h10
    h: 5d1ecbddde3c
  review: drafted
- claim_id: c10
  rel: related_to
  target: state:island-operation
  note: Storage controllers offer commands to intentionally transition into an off-grid islanded state.
  cite:
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=60.r1
    h: 74e27c525f08
  - src: src:eq-equip-bess-tesla-powerpack-system-controls-and-communication-manual
    loc: tbl=55
    h: e1c96dfb6113
  review: drafted
  review_note: 'support check: partial - u14 and u21 show commands for an intentional transition to an
    off-grid state and islanding modes, but they do not name storage controllers or explicitly describe
    an islanded state concept.'
---
Islanding is when a generator such as PV keeps powering load through utility lines after it has been cut off from the utility source. An island that was planned ahead to keep service running is an intentional island. One that was not planned is an unintentional island, and these are normally prohibited because they can damage equipment, lower power quality and endanger utility workers. A sustained unintentional island can form only if PV output and local load match closely in both real and reactive power when the upstream switch opens. If they do not match, voltage or frequency quickly drifts out of range and the inverter can detect the loss of mains. Detection methods can be passive, active (for example impedance detection or positive frequency feedback), or communications-based, such as direct transfer trip. Most commercial inverters combine impedance detection with positive feedback. Sandia suggests a sustained island is not physically possible when the total PV nameplate rating in the potential island is below 2/3 of the minimum daytime feeder load. Ride-through functions such as low-voltage ride-through make islands more likely to form, because low voltage can no longer be used to detect an island. Inverter islanding detection is designed to find balanced islands, not faults, so it should not be relied on as fault protection.

<!-- review notes
- sentence 2: support check: partial - u32 supports the preplanned versus unintentional distinction, the typical prohibition, and the equipment and worker hazards, and u19 supports the power-quality concern, but no passage says the prohibition is because of power quality.
- sentence 5: support check: partial - u15 gives the 2/3 fraction of minimum daylight feeder load for DG/PV nameplate, but it does not attribute it to Sandia, and it is described as a conservative statement.
-->
