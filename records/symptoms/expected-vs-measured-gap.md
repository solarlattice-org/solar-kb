---
id: symptom:expected-vs-measured-gap
type: Symptom
name: Persistent expected-vs-measured gap
aliases:
- Expected vs Real
- Actual vs Expected
- Expected vs. Actual Energy
claims:
- claim_id: c1
  rel: observed_as
  target: meas:performance-index-below-unity
  note: Measured energy divided by expected or modeled energy (EER, Performance Index, actual vs expected)
    stays below one over time.
  cite:
  - src: src:alsoenergy-kb-rescheduling-a-legacy-site-performance-yield-report-in-locusnoc
    loc: sec=front
    h: 003faad8cb7c
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=9.r9
    h: f818c5cb7d7e
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - Passages define Performance Index as measured/modeled energy,
    but never say a persistent value below unity is the signature.'
- claim_id: c2
  rel: observed_as
  target: meas:operating-voltage-above-iv-vmp
  note: Inverter operating voltage stays above IV-derived array Vmp and operating power is below IV-derived
    Pmp.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  rel: observed_as
  target: meas:air-mass-correlated-residual
  note: 'Spectral case: residual after irradiance and temperature correction tracks air mass, season,
    atmospheric water and aerosols; can be under- or overperformance.'
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h4
    h: eb8006cfb637
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h7
    h: d83138ae3933
  review: drafted
- claim_id: c4
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring, summer 2025, at a 100 MW California
    PV plant (approximate figure).
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - The 1.2% summer 2025 average energy loss at a 100 MW California
    plant is stated, but the passage says ''about'' and doesn''t call it a typical power loss; the approximate
    qualifier is covered.'
---
Over time, the plant produces a different amount than its expected or modeled energy. The difference shows up as a low ratio of measured to expected energy, or a low performance index, in monitoring reports. Before blaming the plant, first rule out weather, availability, clipping, curtailment, soiling, degradation and instrument problems. If the gap remains while the plant runs normally, the expected value itself may be wrong. A flawed PAN file is one cause. Find the exact PAN file used, then compare it with data sheets, independent test data and third-party files. If the gap appears mostly in hot periods, check whether the inverter DC voltage is stuck at its minimum. If the operating voltage stays above the Vmp measured from an IV curve, this points to inverter voltage floor losses. If the leftover gap follows air mass, season, atmospheric water or aerosols, spectral effect losses are likely. In this case the plant can look like it underperforms or overperforms. Use spectral correction only when it makes the residuals more regular and matches measured or modeled atmospheric conditions. Do not use it to explain away any unexplained gap.

<!-- review notes
- sentence 1: support check: partial - A persistent gap between expected and measured performance and the EER/performance index ratios are described, but nothing says the gap appears as a low ratio in monitoring reports.
- sentence 5: support check: partial - The correlation with air mass, season, water and aerosols and the under- or overperformance appearance are stated, but 'likely' is stronger than 'often correlated'.
-->
