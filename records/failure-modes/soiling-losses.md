---
id: fm:soiling-losses
type: FailureMode
name: Soiling Losses
category: Soiling
claims:
- claim_id: c1
  rel: affects
  target: comp:module-glass
  note: Deposits cause optical losses by lowering the transmittance of the glazing.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=4.2.2
    h: 389a887eb5f2
  review: drafted
- claim_id: c2
  rel: presents_as
  target: symptom:gradual-performance-decline
  note: The soiling ratio falls while deposits build up and recovers after rain or other cleaning events.
  cite:
  - src: src:alsoenergy-kb-pv-model-losses
    loc: sec=front
    h: 10001d881d82
  - src: src:iea-pvps-t13-21-2022
    loc: sec=3.1
    h: 1bd67b0ecb1e
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:isc-reduction
  note: Uniform soiling lowers short-circuit current roughly in step with power output.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=3.1
    h: 1bd67b0ecb1e
  review: drafted
- claim_id: c4
  rel: presents_as
  target: symptom:substring-loss
  note: When dirt collects unevenly, for example along the bottom row of cells, the bypass diode can open
    a soiled cell string. Power is lost but short-circuit current does not change.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=3.1
    h: 1bd67b0ecb1e
  review: drafted
  review_note: 'support check: partial - Bypass diode opening a soiled string gives power loss without
    Isc change, but the passage mentions bottom-row accumulation only from partial cleaning, not exactly
    this framing; mostly supported.'
- claim_id: c5
  rel: presents_as
  target: symptom:iv-curve-distortion
  note: Non-uniform soiling changes the shape of the IV curve and lowers Isc and maximum power by different
    amounts.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=3.1
    h: 1bd67b0ecb1e
  - src: src:iea-pvps-t13-25-2022
    loc: fig=95
    h: 64f5d28c60e3
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:soiling-station
  note: IEC 61724-1 calls for an on-site soiling station to reach monitoring class A.
  cite:
  - src: src:pv-root-cause-soiling-losses
    loc: sec=h7
    h: 22baf3f6fdbf
  - src: src:pv-root-cause-soiling-losses
    loc: sec=front
    h: 8b3204cccd40
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:clean-dirty-reference
  note: The soiling ratio is often approximated from the short-circuit current of a soiled device compared
    with a clean reference device.
  cite:
  - src: src:pv-root-cause-soiling-losses
    loc: sec=front
    h: 8b3204cccd40
  - src: src:iea-pvps-t13-21-2022
    loc: sec=3.1
    h: 1bd67b0ecb1e
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c8
  rel: detected_by
  target: method:optical-soiling-sensor
  note: Commercial sensors use LED optics or image-processing cameras.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: tbl=5.r2
    h: 2e85ddcb867f
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c9
  rel: detected_by
  target: method:performance-ratio-trend
  cite:
  - src: src:pv-root-cause-soiling-losses
    loc: sec=front
    h: 8b3204cccd40
  review: drafted
- claim_id: c10
  rel: detected_by
  target: method:energy-ratio-analysis
  note: Pattern matching on the energy ratio usually needs 5 or more days of data. Spans shorter than
    4 days are not detected.
  cite:
  - src: src:alsoenergy-kb-pv-model-losses
    loc: sec=front
    h: 10001d881d82
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c11
  rel: detected_by
  target: method:weather-normalized-comparison
  cite:
  - src: src:pv-root-cause-soiling-losses
    loc: sec=front
    h: 8b3204cccd40
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c12
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:pv-root-cause-soiling-losses
    loc: sec=front
    h: 8b3204cccd40
  review: drafted
- claim_id: c13
  rel: detected_by
  target: method:iv-curve-tracing
  note: Shows how clean, uniformly soiled and unevenly soiled modules differ.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=3.1
    h: 1bd67b0ecb1e
  - src: src:iea-pvps-t13-25-2022
    loc: fig=95
    h: 64f5d28c60e3
  review: drafted
  review_note: 'support check: partial - Passages show IV curves of clean, uniform and non-uniform soiling,
    but IV curve tracing isn''t stated as a detection method for soiling.'
- claim_id: c14
  rel: mitigated_by
  target: mit:anti-soiling-coating
  note: Described as one of the most widely used mitigation methods.
  cite:
  - src: src:pv-root-cause-soiling-losses
    loc: sec=h7
    h: 22baf3f6fdbf
  - src: src:pv-root-cause-soiling-losses
    loc: sec=front
    h: 8b3204cccd40
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c15
  rel: mitigated_by
  target: mit:cleaning-schedule-optimization
  note: Base the schedule on the measured soiling rate and the cost of cleaning.
  cite:
  - src: src:pv-root-cause-soiling-losses
    loc: sec=front
    h: 8b3204cccd40
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:tilt-optimization
  cite:
  - src: src:pv-root-cause-soiling-losses
    loc: sec=front
    h: 8b3204cccd40
  review: drafted
---
Soiling losses happen when dust, dirt and other particles build up on the module glass. Less light gets through to the cells, so yield goes down. Production usually drops slowly during dry spells and comes back after rain or cleaning. The loss can vary a lot from one site to another. Uneven dirt, such as a band along the bottom row of cells, can trigger a bypass diode. This costs power even when short-circuit current hardly changes, so Isc readings alone can make the loss look smaller than it is. To confirm soiling, use a soiling station or clean and dirty reference sensors, and track performance ratio or weather-normalized output over several days. Visual inspection and IV curve tracing help show where the dirt is and how it changes the module's electrical behaviour. To reduce the loss, set cleaning schedules from the measured soiling rate and the cost of cleaning, and consider anti-soiling coatings or a different module tilt.

<!-- review notes
- sentence 3: support check: partial - Bypass-diode power loss without Isc change and Isc underestimation are stated, but the specific band along bottom row of cells as trigger is only loosely tied.
- sentence 4: support check: partial - Methods are listed, but 'over several days' is only from energy-ratio detection, not a general confirmation recommendation.
- sentence 5: support check: partial - Visual inspection is a listed method and IV curves show soiling effects, but passages don't state they show where dirt is or are used as detection.
-->
