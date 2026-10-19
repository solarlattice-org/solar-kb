---
id: method:performance-monitoring
type: DetectionMethod
name: Performance monitoring
aliases:
- Monitoring tools
claims:
- claim_id: c1
  rel: produces
  target: meas:dc-voltage-pinned-at-minimum
  note: Voltage-floor screening looks for intervals where inverter DC voltage sits at or near its minimum
    operating threshold while output supported by irradiance is lower than expected.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: drafted
  review_note: 'support check: partial - Passages support screening for DC voltage near the minimum threshold
    with lower-than-expected output, but not the specific signals (high-temperature periods, normal POAI,
    model IDs).'
- claim_id: c2
  rel: produces
  target: meas:operating-voltage-above-iv-vmp
  note: Inverter operating voltage from SCADA is compared with array Vmp from in-situ IV sweeps or a temperature-corrected
    model. Operating power below the IV-derived Pmp supports a voltage-floor event.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: drafted
  review_note: 'support check: partial - Passage supports comparing operating voltage to IV-derived Vmp
    and power below Pmp indicating voltage floor, but not the module temperature lowering Vmp or specific
    signals.'
- claim_id: c3
  rel: produces
  target: meas:low-normalized-row-current
  note: For tracker twist, the affected rows show lower irradiance-normalized current than neighboring
    rows. The shortfall depends on time of day and shows up at low sun angles, during backtracking transitions
    and in windy intervals.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h4
    h: 47d9eb5061f6
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  review: drafted
- claim_id: c4
  rel: produces
  target: meas:performance-ratio-decline
  note: For dust soiling, performance ratio trends and irradiance-normalized output are reviewed over
    dry accumulation periods together with rain and cleaning records.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=front
    h: 931a735f2be9
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h2
    h: 5d4993c87d37
  review: drafted
  review_note: 'support check: partial - Passages say to compare performance ratio trends, rain and cleaning
    records, and normalized output over dry accumulation periods, but do not describe the gradual fall
    and recovery after rain/cleaning pattern explicitly.'
- claim_id: c5
  rel: produces
  target: meas:production-loss-alarm
  note: Monitoring tools can flag a performance loss when a junction box failure creates a short-circuit
    or open-circuit condition.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: drafted
  review_note: 'support check: partial - Passage says monitoring may detect performance loss from short/open-circuit
    junction box failures, but not the string current to zero or voltage step down signals.'
---
Performance monitoring uses plant data from the monitoring system or SCADA to spot faults. It does this by finding electrical signatures, comparing current behavior with history or with a simulated system, and comparing components or subsystems with each other. Detection can rely on statistical tests, machine learning or programmed rules, and these approaches can be combined, for example by comparing the performance of neighboring arrays. The monitoring system should use open standards, have auditable measurement procedures, support calibration and backup, and collect enough data to report performance under the common industry standards. Monitoring can flag performance losses from junction box failures that create short or open circuits. It can also find inverter voltage floor losses, where DC voltage stays pinned near the inverter minimum while output is lower than irradiance would support. Irradiance-normalized string output helps find tracker twist. Compare rows in the morning, around solar noon and in the afternoon, because a twisted row can look fine at one position and lose output at another. Performance ratio trends, together with rain and cleaning records, help measure dust soiling. Early-life production trends, compared with nameplate values, help find light induced degradation. Before blaming a specific cause, filter out outages, curtailment, clipping, soiling and sensor faults. Do not rely on a single dirty irradiance sensor, because sensor drift or local obstruction can look like soiling. Monitoring only points to a likely cause. Confirm it in the field, for example with visual and infrared inspection of junction boxes or angle surveys of tracker rows, because several mechanical faults can produce similar production signatures.

<!-- review notes
- sentence 6: support check: partial - Dust soiling part is supported, and LID detection compares early-life production trends against nameplate, but the LID claim is slightly simplified (also against technology-specific expectations, flash tests).
-->
