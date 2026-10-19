---
id: symptom:isc-reduction
type: Symptom
name: Reduced short-circuit current
aliases:
- Isc
claims:
- claim_id: c1
  rel: observed_as
  target: meas:low-string-isc
  note: In a string short-circuit test, measured string Isc is compared with the expected value and with
    identical strings under stable irradiance; the standard expects identical strings to agree typically
    within 5 % of the average. The test is meant to detect faults, not to rate performance.
  cite:
  - src: src:iec-62446-1
    loc: sec=6.5.2.1
    h: d4e5d5d644a3
  - src: src:iec-62446-1
    loc: sec=6.5.2.2
    h: e78cd394ec93
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:iv-low-isc
  note: Shown in IV traces for metallization corrosion, LID, PID-p and cracks that isolate part of a cell.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h6
    h: 0189f40b9ccf
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
  review_note: 'support check: partial - Corrosion, LID and PID-p lowering Isc are stated, but cracks
    lowering Isc is not stated in the IV context here (only EL-based mention elsewhere); the IV-trace
    attribution for cracks is missing.'
- claim_id: c3
  rel: observed_as
  target: meas:fill-factor-reduction
  note: Occurs together with lower Isc in metallization corrosion (higher series resistance) and in LID.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h6
    h: 0189f40b9ccf
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:low-voc
  note: LID and PID-p lower Voc along with Isc, while cracks and soiling mainly lower current.
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h6
    h: 0189f40b9ccf
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
  review_note: 'support check: partial - LID and PID-p lowering Voc with Isc is stated, but the claim
    that cracks and soiling mainly lower current is not supported for Voc comparison in these passages.'
- claim_id: c5
  rel: observed_as
  target: meas:soiled-vs-clean-isc-ratio
  note: Soiling stations take the soiling ratio from the temperature-compensated Isc of a regularly cleaned
    device and a soiled one. Data are usually filtered to clear-sky midday hours.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=3.2.2
    h: 7b13bcc8687f
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h41
    h: 27f364fa3c19
  - src: src:iea-pvps-t13-21-2022
    loc: tbl=5.r2
    h: 2e85ddcb867f
  review: drafted
- claim_id: c6
  rel: observed_as
  target: meas:el-crack-pattern
  note: Microcracks that cannot be seen by eye show up in EL images and can isolate cell regions, which
    lowers Isc.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h56
    h: 8d42c4699ab3
  review: drafted
- claim_id: c7
  rel: observed_as
  target: meas:el-patchwork-pattern
  note: Growing non-uniformity in EL can point to ongoing LID. PID also shows patchwork patterns.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
  review_note: 'support check: partial - Patchwork EL non-uniformity for LID is stated, but PID patchwork
    is mentioned only for IRT patterns, not EL.'
- claim_id: c8
  attr: typical_power_loss
  value:
    max: 30
    unit: unit:PERCENT
  conditions: Light induced degradation (light soaking effect), module power
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h3
    h: 950db263c013
  review: disputed
  review_note: 'support check: partial - Passage says LID could entail losses up to 30% in module power
    performance, but not specifically as Isc reduction or typical value; ''up to'' is a bound.'
  conflicts_with:
  - symptom:isc-reduction#c12
- claim_id: c9
  attr: typical_power_loss
  value:
    min: 1
    max: 3
    unit: unit:PERCENT
  conditions: LID (boron-oxygen) in c-Si modules, first days of sun exposure
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: disputed
  conflicts_with:
  - symptom:isc-reduction#c11
  - symptom:isc-reduction#c12
  - symptom:isc-reduction#c13
- claim_id: c10
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: LeTID, mainly PERC modules, over years at elevated temperature; adds to the LID loss
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: disputed
  conflicts_with:
  - symptom:isc-reduction#c11
  - symptom:isc-reduction#c12
- claim_id: c11
  attr: typical_power_loss
  value:
    min: 20
    unit: unit:PERCENT
  conditions: PID yield losses observed within 1 year
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: disputed
  conflicts_with:
  - symptom:isc-reduction#c9
  - symptom:isc-reduction#c10
  - symptom:isc-reduction#c13
- claim_id: c12
  attr: typical_power_loss
  value:
    nominal: 35
    unit: unit:PERCENT
  conditions: Simulated module with one cracked cell at 45 % inactive area, which activates the substring
    bypass diode
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  review: disputed
  conflicts_with:
  - symptom:isc-reduction#c8
  - symptom:isc-reduction#c9
  - symptom:isc-reduction#c10
  review_note: possible conflict with c13 (same source; check the conditions)
- claim_id: c13
  attr: typical_power_loss
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: Simulated module with one cracked cell at 15 % inactive area
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  review: disputed
  conflicts_with:
  - symptom:isc-reduction#c9
  - symptom:isc-reduction#c11
  review_note: possible conflict with c12 (same source; check the conditions)
- claim_id: c14
  attr: degradation_rate
  value:
    max: 3
    unit: unit:PERCENT-PER-YR
  conditions: Cell cracks, global rate in all climate zones except cold and snowy ones
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions)
- claim_id: c15
  attr: degradation_rate
  value:
    nominal: 8
    unit: unit:PERCENT-PER-YR
  conditions: Cell cracks, affected part, cold and snowy climate zones
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions)
---
Reduced short-circuit current shows up when a string's Isc is measured with a short-circuit test. Compare it with the expected value and with identical strings under stable irradiance. On an IV trace, look at the other parameters too. Metallization corrosion lowers Isc and fill factor because series resistance rises, while LID lowers Isc, fill factor and Voc together. PID-p causes a significant drop in Isc, Voc and power. PID-s mainly reduces fill factor and affects Isc only when it is far advanced. Cell cracks reduce current because isolated cell areas stop contributing. EL imaging shows microcracks that cannot be seen by eye. Most cracks do not isolate cell parts and cause little power loss. A large inactive area can reverse-bias the cell or switch on the bypass diode. Soiling also lowers Isc. Soiling stations measure it by comparing a regularly cleaned reference device with a soiled one, using temperature-corrected Isc. Uneven soiling can cost more power than the change in Isc suggests, so record power as well as Isc. First check whether the module surface is soiled or the cells are visibly corroded. Then use IV tracing, EL and thermography to tell cracks, corrosion, LID and PID apart.

<!-- review notes
- sentence 6: support check: partial - Measurement method with clean reference and temperature-compensated Isc is stated, but the passages do not explicitly state that soiling lowers Isc, only implicitly via the soiling ratio.
- sentence 8: support check: partial - Visual inspection for corrosion then IV, EL, thermography is supported, but checking soiled surface first and using these to tell cracks, corrosion, LID and PID apart is only partly stated.
-->
