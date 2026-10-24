---
id: concept:anti-islanding-detection-methods
type: Concept
name: Anti-islanding detection methods
aliases:
- active frequency shift
- Sandia frequency shift
- impedance measurement
- passive islanding detection
- islanding detection
- island detection
- frequency shift
- active anti-islanding
category: Grid
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: func:anti-islanding
  note: Detection methods are the mechanisms inverters use to carry out the anti-islanding function.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.3.5.8
    h: 0943b61c4b74
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-125-150-gridservices-techinfo
    loc: sec=2.1
    h: 498d60cb2f86
  - src: src:eq-equip-bess-tesla-megapack-2-design-and-installation-manual
    loc: sec=5.4.5.1
    h: 90742956f36a
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:islanding
  note: Unintentional islands can form when the load in the disconnected section roughly matches the PV
    or storage feed-in power.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.3.5.8
    h: 0943b61c4b74
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc-up-us-be-en-14
    loc: sec=14.2.2.5
    h: 39500d616e75
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-125-150-gridservices-techinfo
    loc: sec=2.1
    h: 498d60cb2f86
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c3
  rel: related_to
  target: std:ieee-1547
  note: IEEE 1547 sets the island detection requirements but does not specify the detection mechanism,
    so vendor schemes vary and are often proprietary.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.3.5.8
    h: 0943b61c4b74
  review: drafted
- claim_id: c4
  rel: related_to
  target: std:ul-1741
  note: UL 1741 listing includes an unintentional islanding test of the inverter.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.3.5.8
    h: 0943b61c4b74
  - src: src:chint-cps-25-350kw-anti-islanding-method-app-note-may-2026
    loc: sec=5
    h: ea5c57c87656
  review: drafted
- claim_id: c5
  rel: related_to
  target: org:sandia
  note: 'Several common active methods are named after Sandia: Frequency Shift, Voltage Shift and Impedance
    Shift. A Sandia report also defines the method groups used in utility questionnaires.'
  cite:
  - src: src:chint-cps-25-350kw-anti-islanding-method-app-note-may-2026
    loc: sec=5
    h: ea5c57c87656
  - src: src:eq-equip-bess-tesla-megapack-2-design-and-installation-manual
    loc: sec=5.4.5.1
    h: 90742956f36a
  review: drafted
  review_note: 'support check: partial - Passages show Sandia Frequency Shift and the Sandia report groups,
    but Sandia Voltage Shift and Impedance Shift appear only as named options in a questionnaire, not
    as common methods.'
- claim_id: c6
  rel: related_to
  target: func:frequency-trip
  note: In the frequency-shift method, positive feedback pushes the frequency until it reaches the low
    or high frequency trip limit, and the inverter then disconnects.
  cite:
  - src: src:chint-cps-25-350kw-anti-islanding-method-app-note-may-2026
    loc: sec=5
    h: ea5c57c87656
  review: drafted
- claim_id: c7
  rel: related_to
  target: func:low-voltage-ride-through
  note: Ride-through means low voltage can no longer be used to detect an island, which may make an unintentional
    island more likely.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.3.5.8
    h: 0943b61c4b74
  review: drafted
- claim_id: c8
  rel: related_to
  target: mit:direct-transfer-trip
  note: A communications-based alternative when inverter anti-islanding is missing or not sufficient.
    It is often expensive because it needs protection-grade communication channels.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=4.3.5.8
    h: 0943b61c4b74
  review: drafted
- claim_id: c9
  rel: related_to
  target: prod:tesla-megapack-2
  note: Uses active Sandia Frequency Shift anti-islanding and trips within 2 seconds of the island forming.
  cite:
  - src: src:eq-equip-bess-tesla-megapack-2-design-and-installation-manual
    loc: sec=5.4.5.1
    h: 90742956f36a
  review: drafted
  review_note: 'support check: partial - The passage says Megapack uses active Sandia Frequency Shift
    and trips within 2 s, but it doesn''t name the Megapack 2 model specifically.'
- claim_id: c10
  rel: related_to
  target: prod:tesla-megapack-2-xl
  note: Uses active Sandia Frequency Shift anti-islanding.
  cite:
  - src: src:tesla-megapack-2-xl-design-and-installation-manual
    loc: sec=5.4.5.1
    h: 90742956f36a
  review: drafted
  review_note: 'support check: partial - The passage covers Megapack generally with active SFS, without
    naming the 2 XL model specifically.'
- claim_id: c11
  rel: related_to
  target: prod:tesla-powerpack
  note: Uses active Sandia Frequency Shift anti-islanding.
  cite:
  - src: src:eq-equip-bess-tesla-tesla-powerpack2-site-design-manual
    loc: sec=h72
    h: c4eb27777801
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - The passage gives active SFS for ''the inverter'' without naming
    Powerpack 2.'
- claim_id: c12
  rel: related_to
  target: prod:sma-sbse-us-50
  note: Its active anti-islanding method is frequency shift.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: tbl=57.r11
    h: 2954afd669b0
  review: drafted
- claim_id: c13
  rel: related_to
  target: prod:sma-sunny-central-up-us
  note: Can be ordered with passive islanding detection based on rate of frequency change. This function
    is not UL-certified.
  cite:
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc-up-us-be-en-14
    loc: sec=14.2.2.5
    h: 39500d616e75
  review: drafted
  review_note: 'support check: partial - The passage supports optional passive detection based on rate
    of frequency change and no UL certification, but it doesn''t name Sunny Central UP-US.'
- claim_id: c14
  rel: related_to
  target: prod:chint-sca-50-100k-t
  note: Uses the Group 2A islanding detection method with a stepped perturbation. Other CPS three-phase
    models use Group 1 with a continuous perturbation.
  cite:
  - src: src:chint-cps-25-350kw-anti-islanding-method-app-note-may-2026
    loc: sec=5
    h: ea5c57c87656
  - src: src:chint-cps-25-350kw-anti-islanding-method-app-note-may-2026
    loc: sec=11
    h: b8f15559c62d
  review: drafted
- claim_id: c15
  rel: related_to
  target: prod:chint-sch-200-250k-t
  note: Uses the Group 2A islanding detection method with a stepped perturbation.
  cite:
  - src: src:chint-cps-25-350kw-anti-islanding-method-app-note-may-2026
    loc: sec=5
    h: ea5c57c87656
  - src: src:chint-cps-25-350kw-anti-islanding-method-app-note-may-2026
    loc: sec=11
    h: b8f15559c62d
  review: drafted
---
Anti-islanding detection methods are how an inverter senses that the utility is gone, so it can stop feeding a section of grid that has been cut off. The risk is highest when the load in the cut-off section roughly matches the power the PV or battery system is feeding in at that moment. Active methods, such as Sandia Frequency Shift, apply a small, continuous disturbance to the inverter output. While the grid is present, the disturbance has no effect on it. In one vendor's version, the inverter adds a little reactive power, which acts as a phase shift. Positive feedback then pushes the frequency up or down until a frequency trip limit is reached, but only if the grid is absent. Passive methods leave the grid alone and only watch it. For example, they trip when the frequency changes by a set amount within a set time. IEEE 1547 and UL 1741 require islanding detection and test for it, but they do not say how detection must work, so vendor schemes vary and can interfere with each other. Ride-through functions mean low voltage can no longer be used to detect an island. Direct transfer trip is a communications-based fallback when inverter detection is not enough.

<!-- review notes
- sentence 2: support check: partial - Passages say islanding can occur when the load roughly equals feed-in power, but they don't say the risk is 'highest' then.
- sentence 3: support check: partial - Passages say the active method has no impact on an intact grid, but the 'continuous disturbance' is only stated for Group 1 (Group 2A is stepped) and 'small' is only given for CPS's reactive injection.
-->
