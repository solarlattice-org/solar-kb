---
id: concept:expected-energy-model
type: Concept
name: Expected energy model
aliases:
- modeled energy
- PV performance model
- expected production
- Expected AC Energy
- PV model
- Expected Yield
- Modeled AC Energy
category: Monitoring
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: metric:expected-energy-ratio
  note: The energy ratio divides measured energy by expected energy and should be 1.0 for a system operating
    normally.
  cite:
  - src: src:alsoenergy-kb-definitions-data-names-kpis-etc
    loc: sec=front
    h: 95bd390c335f
  - src: src:alsoenergy-kb-rescheduling-a-legacy-site-performance-yield-report-in-locusnoc
    loc: sec=front
    h: 003faad8cb7c
  review: drafted
- claim_id: c2
  rel: related_to
  target: metric:insolation-adjusted-expected-energy-ratio
  note: IEER uses expected AC energy (Ee) and adjusts it by the ratio of measured to expected insolation.
  cite:
  - src: src:alsoenergy-kb-ieer
    loc: sec=front
    h: c83c6d979313
  - src: src:alsoenergy-kb-rescheduling-a-legacy-site-performance-yield-report-in-locusnoc
    loc: sec=front
    h: 003faad8cb7c
  review: drafted
- claim_id: c3
  rel: related_to
  target: metric:performance-index
  note: Performance index is measured energy divided by modeled energy.
  cite:
  - src: src:alsoenergy-kb-rescheduling-a-legacy-site-performance-yield-report-in-locusnoc
    loc: sec=front
    h: 003faad8cb7c
  review: drafted
  review_note: 'support check: partial - Performance Index is Measured/Modeled energy per passage, but
    the link to the expected energy model is only via ''modeled energy may refer to expected energy'';
    the waterfall article even states it inversely.'
- claim_id: c4
  rel: related_to
  target: concept:energy-loss-waterfall
  note: The waterfall connects estimated energy to expected energy, then expected energy to measured energy.
  cite:
  - src: src:alsoenergy-kb-energy-loss-waterfall
    loc: sec=front
    h: b18a92c492b3
  review: drafted
  review_note: 'support check: partial - Waterfall shows Estimated→Expected and Expected→Measured, but
    the relation to the expected energy model is implicit.'
- claim_id: c5
  rel: related_to
  target: concept:plane-of-array-irradiance
  note: The model's first step is to work out the effective POA irradiance.
  cite:
  - src: src:alsoenergy-kb-understanding-the-powertrack-pv-model
    loc: sec=front
    h: 1c0c0061a1d8
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=front
    h: 53994d8c99ff
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c6
  rel: related_to
  target: concept:irradiance-transposition
  note: Transposition is needed when the sensor is not mounted in the same orientation as the array.
  cite:
  - src: src:alsoenergy-kb-understanding-the-powertrack-pv-model
    loc: sec=front
    h: 1c0c0061a1d8
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=front
    h: 53994d8c99ff
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: related_to
  target: concept:clear-sky-model
  cite:
  - src: src:alsoenergy-kb-definitions-data-names-kpis-etc
    loc: sec=front
    h: 95bd390c335f
  - src: src:eq-equip-das-alsoenergy-alsoenergy-performance-modeling-r9-a
    loc: tbl=1.r3
    h: b785dd8cf306
  review: drafted
  review_note: 'support check: partial - Passages define the clear-sky model and mention blue-sky expected
    output in the PV system model, but do not clearly state a relation to the expected energy model.'
- claim_id: c8
  rel: related_to
  target: concept:typical-meteorological-year
  note: In the IEER formula, the long-term expected energy and expected insolation are based on TMY data.
  cite:
  - src: src:alsoenergy-kb-ieer
    loc: sec=front
    h: c83c6d979313
  - src: src:alsoenergy-kb-ieer
    loc: sec=h3
    h: 36da990101d6
  review: drafted
- claim_id: c9
  rel: related_to
  target: tool:alsoenergy-powertrack
  cite:
  - src: src:alsoenergy-kb-understanding-the-powertrack-pv-model
    loc: sec=front
    h: 1c0c0061a1d8
  - src: src:man-alsoenergy-pv-model-powertrack-pv-model-losses
    loc: sec=h1
    h: efbe446c42da
  review: drafted
- claim_id: c10
  rel: related_to
  target: tool:pvsyst
  note: A shading map generated in PVsyst can be uploaded, and the inter-row shading uses the same parameters
    as the PVsyst Sheds model.
  cite:
  - src: src:alsoenergy-kb-understanding-the-powertrack-pv-model
    loc: sec=front
    h: 1c0c0061a1d8
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=front
    h: 53994d8c99ff
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c11
  rel: related_to
  target: method:energy-ratio-analysis
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=13.r4
    h: 729bb0c18bac
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=13.r5
    h: cd94e1ad1a36
  review: drafted
- claim_id: c12
  attr: degradation_rate
  value:
    nominal: 0.5
    unit: unit:PERCENT-PER-YR
  conditions: Commonly used default PV system degradation value in the PowerTrack expected energy model;
    annual compound percentage is the default mode
  cite:
  - src: src:alsoenergy-kb-definitions-data-names-kpis-etc
    loc: sec=front
    h: 95bd390c335f
  review: drafted
---
An expected energy model works out how much energy or power a PV system should produce under the weather actually measured on site, such as irradiance and module temperature. The model first finds the effective plane-of-array irradiance, applies shading corrections, and then calculates the DC power available from the modules. Next it applies DC-side losses (age, derate, wiring, LID and mismatch), then inverter conversion losses and clipping, and finally a scaling factor for losses it does not model explicitly, such as AC wiring and transformer losses. Expected energy includes the design losses built into the model, such as shading and inverter efficiency, but it leaves out soiling, snow, curtailment and downtime, so those losses show up as gaps against measured energy. Expected energy is not the same as estimated energy: estimates are monthly budget values based on long-term averages and do not depend on measurements. Dividing measured energy by expected energy gives the energy ratio or performance index, which should be close to one for a healthy system. A simpler option is a regression equation in irradiance and temperature, fitted to measured data and used for commissioning and long-term O&M baselines. Results are only as accurate as the tuning of the model and the quality of the irradiance and temperature data feeding it.

<!-- review notes
- sentence 4: support check: partial - Inclusion/exclusion of losses is stated, and the waterfall detects snow, soiling etc. between expected and measured, but 'show up as gaps' is only loosely stated.
- sentence 6: support check: partial - Energy ratio = produced/expected and should be 1.0, but the waterfall article defines performance index inversely, and EPI is defined as yield/expected; the passages are not fully consistent for 'performance index'.
- sentence 7: support check: partial - Regression equation in irradiance and temperature is stated and applicable for O&M baselines, but 'simpler option' and commissioning use are only partly stated; fitted to measured data is supported.
- sentence 7: review: partial - The SunSpec passage supports a regression equation in temperature and irradiance, developed from measured values and used for commissioning and long-term O&M baselines, but nothing calls it a 'simpler option'.
-->
